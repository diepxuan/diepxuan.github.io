# docs.diepxuan.com

Kho nội dung Jekyll cho website tài liệu tại `https://docs.diepxuan.com`.

## Mục đích

Dự án dùng để quản lý và xuất bản:

- Bài viết kỹ thuật trong `_posts/`.
- Tài liệu nội bộ trong `documents/`.
- Hệ thống văn bản pháp luật trong `van-ban/`.
- Tài liệu vận hành agent và quy trình bảo trì nội dung.

## Cấu trúc thư mục chính

| Đường dẫn | Mục đích |
|---|---|
| `_posts/` | Bài viết Jekyll theo ngày. |
| `documents/` | Tài liệu nội bộ và trang chỉ mục tài liệu. |
| `van-ban/` | Nội dung văn bản pháp luật, phân nhóm theo lĩnh vực. |
| `docs/` | Tài liệu kỹ thuật phụ trợ cho dữ liệu, schema, vận hành. |
| `scripts/` | Script hỗ trợ crawl, sinh nội dung, kiểm tra dữ liệu. |
| `archive/` | Nơi lưu tài liệu cũ hoặc báo cáo đã hết hiệu lực nếu cần giữ lịch sử. |
| `memory/` | Memory local của agent, không dùng làm nội dung public. |

## Build và triển khai

- Jekyll build được thực hiện trên GitHub Actions/GitHub Pages.
- Workspace agent không bắt buộc chạy build local.
- Trạng thái build chính thức lấy từ GitHub Actions sau khi branch hoặc PR được đẩy lên GitHub.
- Trước khi commit vẫn cần kiểm tra Markdown, front matter và phạm vi diff.

## Quy tắc nội dung

- Nội dung website ưu tiên tiếng Việt.
- Không dùng biểu tượng cảm xúc trong tài liệu mới.
- Page/post cần front matter đầy đủ khi được render bởi Jekyll.
- Không commit credential, token, password hoặc file state local.
- Với văn bản pháp luật, ưu tiên nguồn chính thức `vanban.chinhphu.vn` và file PDF từ `datafiles.chinhphu.vn`.

## Quy trình thay đổi

1. Cập nhật từ `main`.
2. Tạo branch mới đúng phạm vi task.
3. Chỉ sửa các file thuộc scope.
4. Commit theo Conventional Commits.
5. Push branch và tạo PR để Sếp review.
6. Chỉ merge khi Sếp yêu cầu rõ.

## Tài liệu liên quan

- `AGENTS.md`: giao thức vận hành agent trong workspace.
- `SOUL.md`: nguyên tắc cốt lõi và kỷ luật làm việc.
- `HEARTBEAT.md`: mô tả các task tự động và backlog pháp luật.
- `REFACTOR_GUIDE.md`: hướng dẫn refactor từng file trong `van-ban/`.
- `documents/LEGISLATION_TRACKING.md`: backlog văn bản pháp luật mới.
- `docs/VANBAN_DATA_STRUCTURE.md`: cấu trúc dữ liệu văn bản pháp luật.

## Ghi chú bảo mật

- Không lưu thông tin đăng nhập trong repo.
- Các cấu hình nhạy cảm phải đi qua biến môi trường hoặc secret store.
- File local như `.heartbeat-state.json` và long-term memory của agent không được commit.

Cập nhật lần cuối: 2026-05-28
