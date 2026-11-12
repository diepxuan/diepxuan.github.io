# AUTOMATION_RESTORE_PLAN.md

Phương án khôi phục automation cho workspace github-io.
Trạng thái: **ĐANG CHỜ SẾP DUYỆT** — không có thay đổi hệ thống nào được thực hiện.

Ngày lập: 2026-11-12. Người lập: Bot.

---

## 1. Hiện trạng (đo tại thời điểm lập)

| Hạng mục | Giá trị |
|---|---|
| openclaw gateway | Đã gỡ package 2026-11-05, service `disabled` |
| File cấu hình `~/.openclaw/openclaw.json` | Còn nguyên (9.5KB) |
| Dữ liệu `~/.openclaw` | Còn nguyên (~8 GB: workspace, agents, memory, credentials) |
| Cron job `crawl-vanban` | Không còn chạy. Lần chạy OK cuối: 2026-09-15 13:18 |
| Hermes cron | `hermes cron list` → "No scheduled jobs" |
| systemd timer | Không có timer nào cho github-io |
| crontab root | Trống (chỉ ghi chú mặc định) |
| Node runtime | `/usr/bin/node` **không còn**; DSH chạy bằng `~/.nvm/versions/node/v26.13.0/bin/node` |
| DSH web service | `dsh-web.service` active, enabled, chạy OK |

**Kết luận**: không tồn tại bất kỳ scheduler nào đang gọi workspace này. Toàn bộ nội dung dừng từ 2026-09-15 là do thiếu automation, không phải do lỗi nội dung.

---

## 2. Nguyên nhân gốc (bằng chứng cũ)

Ghi nhận trong `memory/2026-11-05.md`:

1. `agents.list[github-io].model.primary = 9router/openclaw-free`.
2. Provider `9router` chỉ khai báo model `openclaw-coder`, `openclaw-data`; trong khi danh sách model thực tế của API **không có** cả 3 model `openclaw-*` (kiểm tra lại 2026-11-12: 114 model, **0 model tên `openclaw-*`**; có `llmcoder`).
3. Hệ quả: mọi run đều `FailoverError: The selected model was not found by the provider`.
4. Cron `crawl-vanban` ghi nhận `consecutive_errors = 1174`.

Đây là lỗi cấu hình, không phải lỗi nội dung. Sửa đúng một trường là hết.

---

## 3. Ba phương án

### Phương án A — Khôi phục OpenClaw (đường cũ)

Cài lại `openclaw`, sửa `ExecStart` cho đúng version, sửa `model.primary` sang model tồn tại.

```bash
export PATH=/root/.nvm/versions/node/v26.13.0/bin:$PATH
pnpm add -g openclaw@2026.10.10
sed -i 's#openclaw@2026\.6\.8#openclaw@2026.10.10#' ~/.config/systemd/user/openclaw-gateway.service
systemctl --user daemon-reload
systemctl --user enable --now openclaw-gateway.service
```

Sau đó sửa `~/.openclaw/openclaw.json`:

```json
"agents": { "list": [ { "id": "github-io", "model": { "primary": "9router/llmcoder" } } ] }
```

| Ưu điểm | Nhược điểm |
|---|---|
| Giữ nguyên toàn bộ hành vi cũ (HEARTBEAT.md, định nghĩa sub-agent, memory search) | Cài lại 353 package; unit file đang trỏ version sai là lỗi đã biết |
| Không phải viết lại quy trình heartbeat | Phụ thuộc package bên thứ ba đã bị gỡ vì sự cố |
| | Bot Telegram `8579372032` đang bị Hermes chiếm token — phải xử lý trước |
| | Rủi ro lặp lại sự cố 2026-11-05 (apt remove kéo theo node) |

Rủi ro: **cao**. Đã một lần gây sự cố hệ thống.

### Phương án B — Chuyển sang Hermes cron (khuyến nghị)

Hermes gateway đang chạy sẵn (PID 444, `gateway_state: running`, Telegram connected). Chỉ cần tạo job định kỳ.

```bash
hermes cron create "every 2h" \
  --name crawl-vanban \
  --workdir /data/github-io \
  --deliver local \
  "Đọc HEARTBEAT.md trong workspace và thực hiện đúng quy trình task crawl-vanban. Tuân thủ SOUL.md và OCR_QUALITY_GATE.md."
```

Cú pháp đã kiểm chứng tại 2026-11-12 bằng `hermes cron create --help`:

```text
usage: hermes cron create [-h] [--name NAME] [--deliver DELIVER]
                          [--repeat REPEAT] [--skill SKILLS] [--script SCRIPT]
                          [--no-agent] [--workdir WORKDIR]
                          schedule [prompt]
```

- `schedule`: `30m`, `every 2h`, hoặc cron expression `0 9 * * *`.
- `--workdir`: inject `AGENTS.md` của repo và dùng làm cwd — đúng nhu cầu.
- `--deliver local`: kết quả lưu local, không đẩy ra kênh chat.
- `--no-agent`: chế độ watchdog, chạy script không qua LLM (dùng khi chỉ cần kiểm tra trạng thái).

| Ưu điểm | Nhược điểm |
|---|---|
| Không cài thêm package; dùng runtime đang chạy | Phải map lại logic HEARTBEAT.md sang prompt của Hermes |
| Không đụng tới node/systemd | Khác engine so với lịch sử commit trước đây |
| Tách khỏi lỗi model `openclaw-*` | Cần kiểm chứng skills/tools tương đương (spawn sub-agent, git, ocr) |
| Có sẵn cơ chế kanban dispatch (`dispatch_in_gateway: true`) | |

Rủi ro: **trung bình**, nhưng có thể kiểm chứng từng bước.

### Phương án C — Cron hệ thống gọi DSH headless (đơn giản nhất)

Dùng `crontab` gọi `dsh headless` mỗi 30 phút.

```bash
# crontab -e
*/30 * * * * cd /data/github-io && PATH=/root/.nvm/versions/node/v26.13.0/bin:$PATH /root/.npm-global/bin/dsh headless "Đọc HEARTBEAT.md và thực hiện task crawl-vanban theo đúng quy trình" >> /var/log/github-io-heartbeat.log 2>&1
```

| Ưu điểm | Nhược điểm |
|---|---|
| Đơn giản nhất, không phụ thuộc gateway nào | Không có state/session continuity giữa các lần chạy |
| Dễ debug (log thẳng ra file) | Không có cơ chế chống chạy chồng (overlap) |
| Không đụng cấu hình hiện có | Mỗi lần chạy là session mới, tốn context đọc lại quy trình |

Rủi ro: **thấp** về hệ thống, nhưng chất lượng vận hành thấp hơn.

---

## 4. So sánh

| Tiêu chí | A — OpenClaw | B — Hermes cron | C — DSH + crontab |
|---|---|---|---|
| Công sức triển khai | Cao | Trung bình | Thấp |
| Rủi ro hệ thống | Cao | Trung bình | Thấp |
| Continuity giữa các lần chạy | Có | Có | Không |
| Chống chạy chồng | Có | Có | Không |
| Khôi phục đúng hành vi cũ | Hoàn toàn | Gần đúng | Khác |
| Phụ thuộc mới | openclaw@2026.10.10 | Không | Không |

**Khuyến nghị: Phương án B**, có phương án C làm bước đệm.

---

## 5. Kế hoạch triển khai đề xuất (Phương án B)

### Bước 0 — Kiểm chứng trước khi đổi (không thay đổi hệ thống)

1. `hermes cron create --help` để lấy cú pháp chính xác.
2. Chạy thử một lượt **thủ công** `dsh headless` với prompt heartbeat, xem bot có thực hiện đúng quy trình không.
3. Xác nhận bot có quyền: tạo branch, commit, push, tạo PR (kiểm tra `gh auth status`).
4. Đo thời gian một lượt chạy để chọn interval phù hợp (30m có thể quá dày).

### Bước 1 — Pilot 1 task, interval dài

- Tạo job `crawl-vanban` với interval **2h** thay vì 30m.
- Theo dõi 3 lượt chạy liên tiếp.
- Điều kiện dừng khẩn: nếu 2 lượt liên tiếp fail → tự disable job, báo Sếp.

### Bước 2 — Nâng dần

- Nếu 3 lượt OK và PR active được cập nhật đúng: nâng lên 1h, rồi 30m.
- Không nâng nếu tỉ lệ lỗi > 20%.

### Bước 3 — Bổ sung guard

- Chống chạy chồng: kiểm tra lock file trước khi chạy.
- Giới hạn: mỗi lượt tối đa 1 văn bản crawl (tránh PR phình to).
- Tự động tạo PR mới nếu PR active đã merged/closed.

---

## 6. Việc cần Sếp quyết

1. Chọn phương án nào trong A / B / C.
2. Nếu chọn B: có đồng ý chạy thử thủ công 1 lượt trước khi tạo cron không.
3. Interval khởi điểm: 2h (đề xuất) hay giữ 30m như cũ.
4. Mức tự chủ: bot được tự push + tạo PR như trước, hay chỉ commit local để Sếp review.

---

## 7. Ghi chú kỹ thuật

- `9router` test tại 2026-11-12: endpoint `http://10.0.0.101:3000/v1/models` trả 114 model, không có model `openclaw-*`. Có `llmcoder`, `nvidia`, `llmfree`.
- Nếu sau này bật lại OpenClaw, phải sửa `model.primary` trước khi start, nếu không sẽ lặp lại đúng lỗi cũ.
- `/usr/bin/node` đã mất; mọi script dùng `#!/usr/bin/env node` chỉ chạy khi PATH có nvm. `dsh-web.service` đã xử lý đúng bằng cách `source /root/.nvm/nvm.sh`.
