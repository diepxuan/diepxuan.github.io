# THÔNG TIN DATABASE PHÁP ĐIỂN HOÀN CHỈNH

## Tổng quan

- **Tổng số entries trong file nguồn**: 76,303
- **Số chủ đề (chude)**: 45
- **Số đề mục (demuc)**: 306
- **Số điều khoản trong database**: 76303
- **Database file**: `sqlite/phapdien.db`
- **Parser sử dụng**: `advanced_parser.py`
- **Kích thước database**: 36.02 MB

## So sánh với database cũ

| Metric | Database cũ | Database mới | Ghi chú |
|--------|-------------|--------------|---------|
| Số entries | 18,649 | 76,303 | Tăng 409% |
| Số chủ đề | 45 | 45 | Không đổi |
| Số đề mục | 306 | 306 | Không đổi |
| Entry đặc biệt | ❌ Không có | ✅ Có đầy đủ | Entry sếp tìm |

## Entry đặc biệt đã được xác minh

- **ID**: AA4C41EB-CC02-4629-8077-3691D02E64F2
- **Tên**: Điều 14.4.NĐ.3.10. Điều kiện đối với doanh nghiệp cung cấp dịch vụ thông báo hàng hải[6]
- **Vị trí**: Entry thứ 18,650 trong danh sách
- **Trạng thái**: ✅ HỢP LỆ - đã được lưu vào database
- **Kiểm tra trong database**: FOUND

## Cấu trúc database

```sql
-- Table: chude
CREATE TABLE chude (
    id TEXT PRIMARY KEY,
    value TEXT,
    text TEXT,
    stt TEXT
);

-- Table: demuc
CREATE TABLE demuc (
    id TEXT PRIMARY KEY,
    value TEXT,
    text TEXT,
    stt TEXT
);

-- Table: dieukhoan
CREATE TABLE dieukhoan (
    id TEXT PRIMARY KEY,
    mapc TEXT,
    chimuc TEXT,
    ten TEXT,
    chude_id TEXT,
    demuc_id TEXT,
    FOREIGN KEY (chude_id) REFERENCES chude(id),
    FOREIGN KEY (demuc_id) REFERENCES demuc(id)
);
```
