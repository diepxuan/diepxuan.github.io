#!/usr/bin/env python3
"""OCR pipeline for Vietnamese legal PDFs.

Default behaviour remains compatible with the old Tesseract pipeline:

    python3 scripts/ocr_pdf.py input.pdf output.txt [dpi]

New PaddleOCR modes are available through flags:

    python3 scripts/ocr_pdf.py input.pdf output.txt --engine auto
    python3 scripts/ocr_pdf.py input.pdf output.txt --engine mobile
    python3 scripts/ocr_pdf.py input.pdf output.txt --engine server

PaddleOCR is intentionally executed in a child process. Some PaddlePaddle CPU
wheels can terminate the interpreter with SIGILL on older CPUs; keeping it in a
worker lets this script fall back to Tesseract cleanly when `--engine auto` is
used.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
from typing import Any


MIN_PDF_SIZE_MB = 0.1
MIN_PAGE_SIZE_BYTES = 1000
BLANK_WARNING_AVG_BYTES = 5000


PADDLE_MODEL_PRESETS = {
    # PaddleOCR 3.7 PP-OCRv6 models are tiny/small/medium, not the older
    # mobile/server naming. Keep the product-facing names as aliases.
    "mobile": {
        "det": "PP-OCRv6_tiny_det",
        "rec": "PP-OCRv6_tiny_rec",
    },
    "balanced": {
        "det": "PP-OCRv6_small_det",
        "rec": "PP-OCRv6_small_rec",
    },
    "server": {
        "det": "PP-OCRv6_medium_det",
        "rec": "PP-OCRv6_medium_rec",
    },
}


def get_pdf_size_mb(filepath: str | Path) -> float:
    """Return PDF size in MB."""
    return os.path.getsize(filepath) / (1024 * 1024)


def convert_pdf_to_images(input_pdf: str | Path, tmpdir: str | Path, dpi: int) -> list[Path]:
    """Convert PDF pages to PNG files with pdftoppm."""
    base = Path(tmpdir) / "page"
    print(f"Converting PDF pages to images at {dpi} DPI...")
    cmd = ["pdftoppm", "-r", str(dpi), "-png", str(input_pdf), str(base)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"pdftoppm failed: {result.stderr.strip()}")

    pages = sorted(Path(tmpdir).glob("page-*.png"))
    print(f"Generated {len(pages)} pages")
    if not pages:
        raise RuntimeError("No pages generated from PDF")

    total_size = sum(p.stat().st_size for p in pages)
    avg_size = total_size / len(pages)
    print(f"Average page size: {avg_size / 1024:.1f} KB")
    if avg_size < BLANK_WARNING_AVG_BYTES:
        print(
            "WARNING: Pages are very small "
            f"({avg_size / 1024:.1f} KB avg). PDF may have missing/blank content."
        )
    return pages


def ocr_pages_tesseract(pages: list[Path], tmpdir: str | Path, lang: str) -> list[str]:
    """OCR already-converted pages with Tesseract."""
    text_parts: list[str] = []
    for i, page_path in enumerate(pages, 1):
        txt_base = Path(tmpdir) / f"page_{i}"
        if page_path.stat().st_size < MIN_PAGE_SIZE_BYTES:
            print(f"Page {i}: SKIPPED (blank/small: {page_path.stat().st_size} bytes)")
            continue

        print(f"Tesseract OCR page {i}/{len(pages)}...")
        result = subprocess.run(
            ["tesseract", str(page_path), str(txt_base), "-l", lang],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"WARNING: tesseract page {i} failed: {result.stderr.strip()}")
            continue

        txt_file = Path(f"{txt_base}.txt")
        if txt_file.exists():
            text_parts.append(txt_file.read_text(encoding="utf-8"))
    return text_parts


def flatten_paddle_result(value: Any) -> list[str]:
    """Best-effort text extraction across PaddleOCR 2.x/3.x result shapes."""
    texts: list[str] = []

    if value is None:
        return texts

    if isinstance(value, str):
        return [value]

    if isinstance(value, dict):
        for key in ("rec_texts", "texts", "text"):
            item = value.get(key)
            if isinstance(item, list):
                texts.extend(str(x) for x in item if str(x).strip())
            elif isinstance(item, str) and item.strip():
                texts.append(item)
        # PaddleX Result objects often expose a JSON-like dict containing nested
        # result fields. Walk recursively after handling common keys.
        for item in value.values():
            if isinstance(item, (dict, list, tuple)):
                texts.extend(flatten_paddle_result(item))
        return texts

    if isinstance(value, (list, tuple)):
        # PaddleOCR 2.x classic shape: [[box, (text, score)], ...]
        if len(value) == 2 and isinstance(value[1], tuple) and value[1]:
            candidate = value[1][0]
            if isinstance(candidate, str) and candidate.strip():
                return [candidate]
        for item in value:
            texts.extend(flatten_paddle_result(item))
        return texts

    for attr in ("json", "dict", "res"):
        if hasattr(value, attr):
            try:
                texts.extend(flatten_paddle_result(getattr(value, attr)))
            except Exception:
                pass

    return texts


def paddle_worker(payload_path: Path) -> int:
    """Run PaddleOCR in a child process and write JSON output."""
    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    preset_name = payload["preset"]
    preset = PADDLE_MODEL_PRESETS[preset_name]
    pages = [Path(p) for p in payload["pages"]]
    output_json = Path(payload["output_json"])
    lang = payload["lang"]

    from paddleocr import PaddleOCR  # Import inside worker to isolate SIGILL.

    ocr = PaddleOCR(
        lang=lang,
        ocr_version="PP-OCRv6",
        text_detection_model_name=preset["det"],
        text_recognition_model_name=preset["rec"],
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
    )

    page_results: list[dict[str, Any]] = []
    for i, page in enumerate(pages, 1):
        if page.stat().st_size < MIN_PAGE_SIZE_BYTES:
            page_results.append({"page": i, "text": "", "skipped": True})
            continue
        print(f"PaddleOCR {preset_name} page {i}/{len(pages)}...", flush=True)
        result = ocr.predict(input=str(page))
        lines = flatten_paddle_result(result)
        page_results.append({"page": i, "text": "\n".join(lines), "skipped": False})

    output_json.write_text(json.dumps(page_results, ensure_ascii=False), encoding="utf-8")
    return 0


def explain_worker_failure(returncode: int, stderr: str) -> str:
    """Return a concise, actionable PaddleOCR failure message."""
    if returncode < 0:
        sig = signal.Signals(-returncode).name
        return f"PaddleOCR worker killed by {sig}. {stderr.strip()}"
    if returncode == 132:
        return (
            "PaddleOCR worker exited with SIGILL/Illegal instruction. "
            "The installed PaddlePaddle wheel likely requires newer CPU "
            "instructions (typically AVX2/FMA)."
        )
    return f"PaddleOCR worker failed with exit code {returncode}. {stderr.strip()}"


def ocr_pages_paddle(
    pages: list[Path],
    tmpdir: str | Path,
    preset: str,
    lang: str,
) -> list[str]:
    """OCR pages with PaddleOCR in a subprocess."""
    output_json = Path(tmpdir) / "paddle_output.json"
    payload_path = Path(tmpdir) / "paddle_payload.json"
    payload = {
        "preset": preset,
        "lang": lang,
        "pages": [str(p) for p in pages],
        "output_json": str(output_json),
    }
    payload_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

    cmd = [sys.executable, __file__, "--_paddle-worker", str(payload_path)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.returncode != 0:
        raise RuntimeError(explain_worker_failure(result.returncode, result.stderr))

    data = json.loads(output_json.read_text(encoding="utf-8"))
    return [item.get("text", "") for item in data if item.get("text")]


def route_engine(engine: str, doc_type: str, priority: str) -> str:
    """Map a high-level engine request to a concrete engine."""
    if engine in {"tesseract", "mobile", "server"}:
        return engine
    if engine != "auto":
        raise ValueError(f"Unknown engine: {engine}")
    if priority == "high" or doc_type in {"luat", "nghi-dinh-lon", "stub-revisit"}:
        return "server"
    return "mobile"


def ocr_pdf(
    input_pdf: str | Path,
    output_txt: str | Path,
    dpi: int = 150,
    engine: str = "tesseract",
    doc_type: str = "default",
    priority: str = "normal",
    tesseract_lang: str = "vie",
    paddle_lang: str = "vi",
    no_fallback: bool = False,
) -> bool:
    """OCR a PDF file using Tesseract or PaddleOCR."""
    input_pdf = Path(input_pdf)
    output_txt = Path(output_txt)
    size_mb = get_pdf_size_mb(input_pdf)
    print(f"PDF size: {size_mb:.1f} MB")

    if size_mb < MIN_PDF_SIZE_MB:
        print(
            f"WARNING: PDF {input_pdf} is very small ({size_mb:.3f} MB), "
            "likely corrupted or missing content"
        )
        output_txt.write_text(
            f"[ERROR: PDF too small ({size_mb:.3f} MB), content may be missing]\n",
            encoding="utf-8",
        )
        return False

    selected_engine = route_engine(engine, doc_type, priority)
    print(f"OCR engine: {selected_engine} (requested={engine}, doc_type={doc_type}, priority={priority})")

    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            pages = convert_pdf_to_images(input_pdf, tmpdir, dpi)
        except RuntimeError as exc:
            print(f"ERROR: {exc}")
            return False

        text_parts: list[str]
        if selected_engine == "tesseract":
            text_parts = ocr_pages_tesseract(pages, tmpdir, tesseract_lang)
        else:
            preset = "mobile" if selected_engine == "mobile" else "server"
            try:
                text_parts = ocr_pages_paddle(pages, tmpdir, preset, paddle_lang)
            except Exception as exc:
                print(f"WARNING: PaddleOCR failed: {exc}")
                if no_fallback:
                    return False
                print("Falling back to Tesseract...")
                text_parts = ocr_pages_tesseract(pages, tmpdir, tesseract_lang)

        output_txt.write_text("\n".join(text_parts), encoding="utf-8")
        print(f"OCR complete: {len(text_parts)} pages processed")
        return bool(text_parts)


def probe_paddle() -> int:
    """Smoke-test PaddleOCR initialization without processing a PDF."""
    with tempfile.TemporaryDirectory() as tmpdir:
        payload = {
            "preset": "mobile",
            "lang": "vi",
            "pages": [],
            "output_json": str(Path(tmpdir) / "probe.json"),
        }
        payload_path = Path(tmpdir) / "payload.json"
        payload_path.write_text(json.dumps(payload), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, __file__, "--_paddle-worker", str(payload_path)],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("PaddleOCR probe: OK")
            return 0
        print("PaddleOCR probe: FAIL")
        print(explain_worker_failure(result.returncode, result.stderr))
        return result.returncode or 1


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="OCR Vietnamese legal PDFs")
    parser.add_argument("input_pdf", nargs="?", help="Input PDF path")
    parser.add_argument("output_txt", nargs="?", help="Output TXT path")
    parser.add_argument("dpi_pos", nargs="?", type=int, help="Backward-compatible DPI positional arg")
    parser.add_argument("--dpi", type=int, default=None, help="PDF rasterization DPI (default: 150)")
    parser.add_argument(
        "--engine",
        choices=["tesseract", "auto", "mobile", "server"],
        default="tesseract",
        help="OCR engine. Default keeps legacy behaviour: tesseract.",
    )
    parser.add_argument(
        "--doc-type",
        choices=["default", "luat", "nghi-dinh", "nghi-dinh-lon", "thong-tu", "stub-revisit"],
        default="default",
        help="Routing hint for --engine auto",
    )
    parser.add_argument(
        "--priority",
        choices=["low", "normal", "high"],
        default="normal",
        help="Routing hint for --engine auto",
    )
    parser.add_argument("--tesseract-lang", default="vie", help="Tesseract language code")
    parser.add_argument("--paddle-lang", default="vi", help="PaddleOCR language code")
    parser.add_argument("--no-fallback", action="store_true", help="Do not fall back to Tesseract")
    parser.add_argument("--probe-paddle", action="store_true", help="Smoke-test PaddleOCR runtime")
    parser.add_argument("--_paddle-worker", help=argparse.SUPPRESS)
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args._paddle_worker:
        return paddle_worker(Path(args._paddle_worker))
    if args.probe_paddle:
        return probe_paddle()
    if not args.input_pdf or not args.output_txt:
        print("Usage: ocr_pdf.py <input.pdf> <output.txt> [dpi] [--engine ...]")
        return 1
    dpi = args.dpi if args.dpi is not None else (args.dpi_pos or 150)
    success = ocr_pdf(
        args.input_pdf,
        args.output_txt,
        dpi=dpi,
        engine=args.engine,
        doc_type=args.doc_type,
        priority=args.priority,
        tesseract_lang=args.tesseract_lang,
        paddle_lang=args.paddle_lang,
        no_fallback=args.no_fallback,
    )
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
