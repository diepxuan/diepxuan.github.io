# PaddleOCR PP-OCRv6 CPU-only plan

## Mục tiêu

Thêm đường chạy OCR mới cho PDF văn bản pháp luật, dùng PaddleOCR PP-OCRv6 với hai mức chất lượng vận hành:

- `mobile`: nhanh, dùng cho batch crawl và văn bản ngắn.
- `server`: chính xác hơn, dùng cho văn bản lớn, stub cần bổ sung full text, hoặc retry khi audit fail.

Trong PaddleOCR 3.7, PP-OCRv6 không còn đặt tên model `mobile/server` như PP-OCRv5. Project vẫn giữ interface `mobile/server` cho dễ vận hành, nhưng map nội bộ như sau:

| Interface | PP-OCRv6 model |
|---|---|
| `mobile` | `PP-OCRv6_tiny_det` + `PP-OCRv6_tiny_rec` |
| `server` | `PP-OCRv6_medium_det` + `PP-OCRv6_medium_rec` |
| `auto` + normal | `mobile` |
| `auto` + high / `luat` / `nghi-dinh-lon` / `stub-revisit` | `server` |

## Files added/changed

- `scripts/ocr_pdf.py`: OCR dispatcher. Default remains Tesseract for backward compatibility.
- `requirements-paddleocr.txt`: optional PaddleOCR dependencies.
- `.gitignore`: ignore local `.venv*/` and Paddle cache folders.

## Usage

Legacy Tesseract path, unchanged:

```bash
python3 scripts/ocr_pdf.py input.pdf output.txt 150
```

Auto route:

```bash
python3 scripts/ocr_pdf.py input.pdf output.txt --engine auto --doc-type nghi-dinh --priority normal
```

Force mobile:

```bash
python3 scripts/ocr_pdf.py input.pdf output.txt --engine mobile
```

Force server:

```bash
python3 scripts/ocr_pdf.py input.pdf output.txt --engine server --no-fallback
```

Runtime probe:

```bash
python3 scripts/ocr_pdf.py --probe-paddle
```

## Current machine result

The current host CPU is `Intel Xeon E5-2650 v2` with `avx`, `sse4_1`, `sse4_2`, but no observed `avx2`/`fma` flags.

Test result:

- `paddlepaddle==2.6.2` imports successfully.
- `paddleocr==3.7.0` + `paddlex==3.7.2` can download PP-OCRv6 model files, but fails at initialization because PaddleOCR 3.7 calls `AnalysisConfig.set_optimization_level`, which is not available in PaddlePaddle 2.6.2.
- `paddlepaddle==3.0.0` was tested and failed with `Illegal instruction` on this CPU.

Conclusion: PP-OCRv6 native Paddle runtime is integrated but not enabled on this current CPU with official wheels. The dispatcher catches worker failure and falls back to Tesseract when `--engine auto` is used.

## Deployment requirement for real PP-OCRv6

Use one of these:

1. Host CPU with AVX2/FMA support, then install `requirements-paddleocr.txt` in a venv.
2. Build PaddlePaddle from source for this older CPU target.
3. Use a container/runner on newer hardware for OCR jobs, commit OCR output back to this repo.

## Recommended rollout

1. Keep default `tesseract` on this machine.
2. Use `--probe-paddle` as a preflight in any OCR worker.
3. When a compatible host is available, run PoC with:
   - `mobile`: batch thông tư/nghị định ngắn.
   - `server`: 242, 202 stub-revisit, NĐ lớn >= 50 trang, audit-fail retries.
4. Accept cutover only if OCR audit issues drop by at least 30% versus Tesseract.
