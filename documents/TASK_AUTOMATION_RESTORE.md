# TASK_AUTOMATION_RESTORE.md

**Trạng thái**: CHỜ SẾP DUYỆT
**Loại**: Task thiết kế / quyết định kiến trúc
**Ngày tạo**: 2026-11-12
**Phương án chi tiết**: `documents/AUTOMATION_RESTORE_PLAN.md`

---

## 1. Mục tiêu

Khôi phục cơ chế chạy định kỳ (heartbeat) cho workspace github-io, đang chết hoàn toàn
từ 2026-09-15.

## 2. Hiện trạng

| Hạng mục | Giá trị |
|---|---|
| openclaw gateway | Đã gỡ package 2026-11-05, service `disabled` |
| Dữ liệu `~/.openclaw` | Còn nguyên ~8 GB (workspace, agents, memory, credentials) |
| Cron `crawl-vanban` | Không chạy. Lần OK cuối: 2026-09-15 13:18 |
| Hermes cron | `hermes cron list` → "No scheduled jobs" |
| systemd timer | Không có timer nào cho github-io |
| crontab root | Trống |
| Node runtime | `/usr/bin/node` mất; DSH dùng `~/.nvm/versions/node/v26.13.0/bin/node` |

**Hệ quả**: nội dung website dừng từ 2026-09-15. Không phải lỗi nội dung.

## 3. Nguyên nhân gốc (đã xác minh)

1. `agents.list[github-io].model.primary = 9router/openclaw-free`
2. Provider `9router` khai báo model `openclaw-coder`, `openclaw-data` — nhưng API thực tế
   **không có** cả 3 model `openclaw-*`.
3. Kiểm chứng lại 2026-11-12: endpoint `http://10.0.0.101:3000/v1/models` trả **114 model**,
   lọc `openclaw` → **0 kết quả**. Có `llmcoder`, `llmfree`, `llmfree-tier`.
4. Hệ quả: mọi run đều `FailoverError: The selected model was not found by the provider`.
5. Cron `crawl-vanban` ghi `consecutive_errors = 1174`.

Đây là lỗi cấu hình một trường, không phải lỗi nội dung.

## 4. Ba phương án

### Phương án A — Khôi phục OpenClaw

```bash
export PATH=/root/.nvm/versions/node/v26.13.0/bin:$PATH
pnpm add -g openclaw@2026.10.10
sed -i 's#openclaw@2026\.6\.8#openclaw@2026.10.10#' ~/.config/systemd/user/openclaw-gateway.service
systemctl --user daemon-reload
systemctl --user enable --now openclaw-gateway.service
```

Sau đó sửa `~/.openclaw/openclaw.json`:
```json
"model": { "primary": "9router/llmcoder" }
```

- Ưu: giữ nguyên hành vi cũ, không viết lại quy trình.
- Nhược: cài lại 353 package; phụ thuộc bên thứ ba đã bị gỡ vì sự cố; bot Telegram
  `8579372032` đang bị Hermes chiếm token.
- **Rủi ro: CAO** — đã một lần gây sự cố hệ thống (apt remove kéo theo nodejs).

### Phương án B — Hermes cron (KHUYẾN NGHỊ)

Hermes gateway đang chạy sẵn (PID 444, `gateway_state: running`, Telegram connected).

```bash
hermes cron create "every 2h" \
  --name crawl-vanban \
  --workdir /data/github-io \
  --deliver local \
  "Đọc HEARTBEAT.md trong workspace và thực hiện đúng quy trình task crawl-vanban. Tuân thủ SOUL.md và OCR_QUALITY_GATE.md."
```

Cú pháp đã kiểm chứng 2026-11-12 bằng `hermes cron create --help`:
```text
usage: hermes cron create [-h] [--name NAME] [--deliver DELIVER]
                          [--repeat REPEAT] [--skill SKILLS] [--script SCRIPT]
                          [--no-agent] [--workdir WORKDIR]
                          schedule [prompt]
```
- `schedule`: `30m`, `every 2h`, hoặc cron expression `0 9 * * *`
- `--workdir`: inject `AGENTS.md` và dùng làm cwd — đúng nhu cầu
- `--deliver local`: lưu local, không đẩy ra chat
- `--no-agent`: watchdog thuần script, không qua LLM

- Ưu: không cài package mới; dùng runtime đang chạy; tách khỏi lỗi model `openclaw-*`;
  có sẵn kanban dispatch (`dispatch_in_gateway: true`).
- Nhược: phải map lại HEARTBEAT.md sang prompt Hermes; cần kiểm chứng skills/tools
  tương đương (spawn sub-agent, git, ocr).
- **Rủi ro: TRUNG BÌNH**, kiểm chứng được từng bước.

### Phương án C — crontab + dsh headless

```bash
*/30 * * * * cd /data/github-io && PATH=/root/.nvm/versions/node/v26.13.0/bin:$PATH /root/.npm-global/bin/dsh headless "Đọc HEARTBEAT.md và thực hiện task crawl-vanban" >> /var/log/github-io-heartbeat.log 2>&1
```

- Ưu: đơn giản nhất, không phụ thuộc gateway, dễ debug.
- Nhược: không có continuity giữa các lần chạy; không chống chạy chồng.
- **Rủi ro: THẤP** về hệ thống, chất lượng vận hành thấp hơn.

## 5. So sánh

| Tiêu chí | A — OpenClaw | B — Hermes | C — dsh |
|---|---|---|---|
| Công sức | Cao | Trung bình | Thấp |
| Rủi ro hệ thống | Cao | Trung bình | Thấp |
| Continuity | Có | Có | Không |
| Chống chạy chồng | Có | Có | Không |
| Đúng hành vi cũ | Hoàn toàn | Gần đúng | Khác |
| Phụ thuộc mới | openclaw@2026.10.10 | Không | Không |

## 6. Kế hoạch triển khai đề xuất (nếu chọn B)

### Bước 0 — Kiểm chứng, chưa đổi hệ thống
1. `hermes cron create --help` lấy cú pháp chính xác (đã làm).
2. Chạy thử **thủ công** `dsh headless` với prompt heartbeat, xem bot có làm đúng quy trình.
3. Xác nhận quyền: tạo branch, commit, push, tạo PR (`gh auth status`).
4. Đo thời gian một lượt chạy để chọn interval.

### Bước 1 — Pilot interval dài
- Tạo job với interval **2h** thay vì 30m.
- Theo dõi 3 lượt liên tiếp.
- Điều kiện dừng: 2 lượt liên tiếp fail → tự disable, báo Sếp.

### Bước 2 — Nâng dần
- 3 lượt OK → nâng 1h, rồi 30m.
- Không nâng nếu tỉ lệ lỗi > 20%.

### Bước 3 — Bổ sung guard
- Lock file chống chạy chồng.
- Mỗi lượt tối đa 1 văn bản (tránh PR phình to).
- Tự tạo PR mới nếu PR active đã merged/closed.

## 7. Việc cần Sếp quyết

1. Chọn phương án **A / B / C**.
2. Nếu chọn B: có đồng ý chạy thử thủ công 1 lượt trước khi tạo cron không.
3. Interval khởi điểm: **2h (đề xuất)** hay giữ 30m.
4. Mức tự chủ: bot được tự push + tạo PR như trước, hay chỉ commit local để Sếp review.

## 8. Ghi chú kỹ thuật

- Nếu bật lại OpenClaw, **phải sửa `model.primary` trước khi start**, nếu không lặp lại đúng lỗi cũ.
- `/usr/bin/node` đã mất; mọi script `#!/usr/bin/env node` chỉ chạy khi PATH có nvm.
  `dsh-web.service` đã xử lý đúng bằng `source /root/.nvm/nvm.sh`.
- Không tự thực hiện thay đổi hệ thống nào cho tới khi Sếp duyệt.
