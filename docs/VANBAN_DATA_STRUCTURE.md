# VANBAN DATA STRUCTURE DOCUMENTATION

## Tổng quan
Tài liệu này mô tả cấu trúc dữ liệu của hệ thống văn bản pháp luật (van-ban) được crawl từ Bộ Pháp Điện Điện Tử.

## File dữ liệu chính
- **Vị trí**: `/van-ban/crawled/BoPhapDienDienTu/jsonData.js` (24MB)
- **Định dạng**: JavaScript với các biến JSON
- **Kích thước**: ~24MB (chứa dữ liệu metadata và có thể cả nội dung văn bản)

## Cấu trúc dữ liệu đã phân tích

### 1. CHỦ ĐỀ (ChuDe)
**Biến**: `jdChuDe` - 45 items

**Cấu trúc**:
```json
{
  "Value": "c3b69131-2931-4f67-926e-b244e18e8081",
  "Text": "An ninh quốc gia",
  "STT": "1"
}
```

**Fields**:
- `Value` (UUID/VARCHAR): ID duy nhất của chủ đề
- `Text` (VARCHAR): Tên chủ đề
- `STT` (INT): Số thứ tự

**Danh sách chủ đề** (45 chủ đề):
1. An ninh quốc gia
2. Bảo hiểm
3. Bưu chính, viễn thông
4. Bổ trợ tư pháp
5. Cán bộ, công chức, viên chức
6. Chính sách xã hội
7. Công nghiệp
8. Dân số, gia đình, trẻ em, bình đẳng giới
9. Dân sự
10. Dân tộc
11. Đất đai
12. Doanh nghiệp, hợp tác xã
13. Giáo dục, đào tạo
14. Giao thông, vận tải
15. Hành chính tư pháp
16. Hình sự
17. Kế toán, kiểm toán
18. Khiếu nại, tố cáo
19. Khoa học, công nghệ
20. Lao động
21. Môi trường
22. Ngân hàng, tiền tệ
23. Ngoại giao, điều ước quốc tế
24. Nông nghiệp, nông thôn
25. Quốc phòng
26. Tài chính
27. Tài nguyên
28. Tài sản công, nợ công, dự trữ nhà nước
29. Thi đua, khen thưởng, các danh hiệu vinh dự nhà nước
30. Thi hành án
31. Thống kê
32. Thông tin, báo chí, xuất bản
33. Thuế, phí, lệ phí, các khoản thu khác
34. Thương mại, đầu tư, chứng khoán
35. Tổ chức bộ máy nhà nước
36. Tổ chức chính trị - xã hội, hội
37. Tố tụng và các phương thức giải quyết tranh chấp
38. Tôn giáo, tín ngưỡng
39. Trật tự, an toàn xã hội
40. Tương trợ tư pháp
41. Văn hóa, thể thao, du lịch
42. Văn thư lưu trữ
43. Xây dựng, nhà ở, đô thị
44. Xây dựng pháp luật và thi hành pháp luật
45. Y tế, dược

### 2. ĐỀ MỤC (DeMuc)
**Biến**: `jdDeMuc` - 306 items

**Cấu trúc**:
```json
{
  "Value": "049522e0-fec2-4d52-916d-dd103ba69627",
  "Text": "Công tác dân tộc",
  "ChuDe": "a6ee2d1a-2edc-4c30-bff5-81efbd765464",
  "STT": "1"
}
```

**Fields**:
- `Value` (UUID/VARCHAR): ID duy nhất của đề mục
- `Text` (VARCHAR): Tên đề mục
- `ChuDe` (UUID/VARCHAR): ID chủ đề (foreign key)
- `STT` (INT): Số thứ tự trong chủ đề

**Mối quan hệ**:
- Mỗi đề mục thuộc 1 chủ đề
- 45 chủ đề có 306 đề mục (trung bình ~6.8 đề mục/chủ đề)

**Ví dụ đề mục**:
- Công tác dân tộc (Chủ đề: Dân tộc)
- Đất đai (Chủ đề: Đất đai)
- An toàn thực phẩm (Chủ đề: Y tế, dược)
- Cấp bản sao từ sổ gốc, chứng thực bản sao từ bản chính, chứng thực chữ ký (Chủ đề: Hành chính tư pháp)
- Đo đạc và bản đồ (Chủ đề: Tài nguyên)

### 3. CÁC BIẾN KHÁC (Chưa parse được từ file 24MB)
Các biến sau có thể tồn tại trong file nhưng chưa được parse do kích thước file lớn:
- `jdVanBan`: Dữ liệu văn bản (có thể rất lớn)
- `jdCoQuan`: Danh sách cơ quan ban hành
- `jdLinhVuc`: Danh sách lĩnh vực
- `jdLoaiVanBan`: Danh sách loại văn bản
- `jdNguoiKy`: Danh sách người ký

## ĐỀ XUẤT SCHEMA DATABASE

### 1. Bảng `chu_de` (Chủ đề)
```sql
CREATE TABLE chu_de (
    id VARCHAR(36) PRIMARY KEY,           -- UUID từ field Value
    ten_chu_de VARCHAR(255) NOT NULL,     -- Từ field Text
    stt INT,                              -- Số thứ tự
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### 2. Bảng `de_muc` (Đề mục)
```sql
CREATE TABLE de_muc (
    id VARCHAR(36) PRIMARY KEY,           -- UUID từ field Value
    ten_de_muc VARCHAR(255) NOT NULL,     -- Từ field Text
    chu_de_id VARCHAR(36) NOT NULL,       -- FK đến chu_de.id
    stt INT,                              -- Số thứ tự trong chủ đề
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (chu_de_id) REFERENCES chu_de(id) ON DELETE CASCADE
);
```

### 3. Bảng `co_quan` (Cơ quan ban hành)
```sql
CREATE TABLE co_quan (
    ma_co_quan VARCHAR(50) PRIMARY KEY,   -- Mã cơ quan
    ten_co_quan VARCHAR(255) NOT NULL,    -- Tên cơ quan
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### 4. Bảng `loai_van_ban` (Loại văn bản)
```sql
CREATE TABLE loai_van_ban (
    ma_loai_van_ban VARCHAR(50) PRIMARY KEY,  -- Mã loại văn bản
    ten_loai_van_ban VARCHAR(255) NOT NULL,   -- Tên loại văn bản
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### 5. Bảng `van_ban` (Văn bản)
```sql
CREATE TABLE van_ban (
    id VARCHAR(50) PRIMARY KEY,           -- ID văn bản
    so_hieu VARCHAR(100),                 -- Số hiệu văn bản
    trich_yeu TEXT,                       -- Trích yếu
    ngay_ban_hanh DATE,                   -- Ngày ban hành
    ngay_co_hieu_luc DATE,                -- Ngày có hiệu lực
    ngay_het_hieu_luc DATE,               -- Ngày hết hiệu lực
    co_quan_ban_hanh_id VARCHAR(50),      -- FK đến co_quan
    loai_van_ban_id VARCHAR(50),          -- FK đến loai_van_ban
    nguoi_ky VARCHAR(255),                -- Người ký
    chuc_vu_nguoi_ky VARCHAR(255),        -- Chức vụ người ký
    file_path VARCHAR(500),               -- Đường dẫn file
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (co_quan_ban_hanh_id) REFERENCES co_quan(ma_co_quan),
    FOREIGN KEY (loai_van_ban_id) REFERENCES loai_van_ban(ma_loai_van_ban)
);
```

### 6. Bảng `van_ban_noi_dung` (Nội dung văn bản)
```sql
CREATE TABLE van_ban_noi_dung (
    id INT AUTO_INCREMENT PRIMARY KEY,
    van_ban_id VARCHAR(50) NOT NULL,      -- FK đến van_ban
    noi_dung LONGTEXT,                    -- Nội dung đầy đủ
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (van_ban_id) REFERENCES van_ban(id) ON DELETE CASCADE
);
```

### 7. Bảng `van_ban_de_muc` (Quan hệ nhiều-nhiều)
```sql
CREATE TABLE van_ban_de_muc (
    van_ban_id VARCHAR(50) NOT NULL,      -- FK đến van_ban
    de_muc_id VARCHAR(36) NOT NULL,       -- FK đến de_muc
    PRIMARY KEY (van_ban_id, de_muc_id),
    FOREIGN KEY (van_ban_id) REFERENCES van_ban(id) ON DELETE CASCADE,
    FOREIGN KEY (de_muc_id) REFERENCES de_muc(id) ON DELETE CASCADE
);
```

## KẾ HOẠCH IMPORT DỮ LIỆU

### Bước 1: Tạo database và tables
1. Kết nối đến MySQL server `mysql.diepxuan.corp:3306`
2. Tạo database `vbpl` (nếu chưa tồn tại)
3. Tạo tất cả tables theo schema trên

### Bước 2: Import dữ liệu metadata
1. **Chủ đề (chu_de)**: Import 45 records từ `jdChuDe`
2. **Đề mục (de_muc)**: Import 306 records từ `jdDeMuc`
3. **Cơ quan (co_quan)**: Cần extract từ `jdCoQuan` (nếu có)
4. **Loại văn bản (loai_van_ban)**: Cần extract từ `jdLoaiVanBan` (nếu có)

### Bước 3: Import dữ liệu văn bản
1. **Văn bản (van_ban)**: Extract từ `jdVanBan` (cần phân tích cấu trúc cụ thể)
2. **Nội dung văn bản (van_ban_noi_dung)**: Có thể lưu riêng do kích thước lớn
3. **Quan hệ văn bản - đề mục (van_ban_de_muc)**: Tạo mapping

### Bước 4: Tạo indexes cho performance
```sql
-- Indexes cho bảng van_ban
CREATE INDEX idx_van_ban_ngay_ban_hanh ON van_ban(ngay_ban_hanh);
CREATE INDEX idx_van_ban_co_quan ON van_ban(co_quan_ban_hanh_id);
CREATE INDEX idx_van_ban_loai ON van_ban(loai_van_ban_id);

-- Indexes cho bảng de_muc
CREATE INDEX idx_de_muc_chu_de ON de_muc(chu_de_id);

-- Indexes cho bảng van_ban_de_muc
CREATE INDEX idx_vbdm_de_muc ON van_ban_de_muc(de_muc_id);
```

## CÔNG CỤ VÀ SCRIPTS

### 1. Script phân tích dữ liệu
- **File**: `scripts/analyze-vanban-data.js`
- **Chức năng**: Phân tích cấu trúc file jsonData.js
- **Cách chạy**: `node scripts/analyze-vanban-data.js`

### 2. Script import dữ liệu (cần phát triển)
Cần tạo các scripts:
- `import-chu-de.js`: Import chủ đề
- `import-de-muc.js`: Import đề mục
- `import-van-ban.js`: Import văn bản
- `create-database.js`: Tạo database schema

### 3. Script extract dữ liệu từ file lớn
Do file jsonData.js 24MB quá lớn, cần script để:
- Đọc từng phần của file
- Parse JSON từng biến một
- Lưu thành các file JSON riêng biệt

## THÔNG TIN KẾT NỐI DATABASE

### MySQL Connection
- **Host**: `mysql.diepxuan.corp:3306`
- **Database**: `vbpl`
- **Username**: `vbpl`
- **Password**: `G]9E9S_TahIFVbq-`
- **Status**: ✅ Đã verify - user có ALL PRIVILEGES trên database

### Connection Test
```bash
mysql -h mysql.diepxuan.corp -u vbpl -p'G]9E9S_TahIFVbq-' vbpl
```

## LƯU Ý QUAN TRỌNG

1. **Kích thước dữ liệu**: File jsonData.js 24MB chứa nhiều dữ liệu, cần xử lý cẩn thận
2. **Encoding**: File sử dụng UTF-8 với BOM (﻿)
3. **UUID format**: Các ID sử dụng UUID format (36 ký tự)
4. **Quan hệ dữ liệu**: Đề mục liên kết với chủ đề qua field `ChuDe`
5. **Performance**: Cần indexes cho các truy vấn thường xuyên

## NEXT STEPS

1. **Phân tích sâu hơn**: Extract thông tin từ biến `jdVanBan` để hiểu cấu trúc văn bản
2. **Tạo database schema**: Tạo SQL script để tạo tables
3. **Viết import scripts**: Tạo scripts import từng loại dữ liệu
4. **Test import**: Import thử một phần dữ liệu để verify
5. **Tạo API/Interface**: Xây dựng interface để query và hiển thị dữ liệu

---

**Documentation created**: 2026-02-23  
**Data source**: Bộ Pháp Điện Điện Tử  
**File analyzed**: `BoPhapDienDienTu/jsonData.js` (24MB)  
**Total records**: 45 chủ đề + 306 đề mục