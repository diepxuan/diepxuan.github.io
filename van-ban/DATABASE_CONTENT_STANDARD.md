# DATABASE CONTENT STANDARD - VAN-BAN PROJECT

## 🎯 QUY TẮC SỬ DỤNG NỘI DUNG

### **1. NGUYÊN TẮC CHÍNH**

**`dieu_khoan.ten` LÀ CHUẨN CHÍNH** cho nội dung điều khoản pháp luật.

**`de_muc.content_markdown` DÙNG ĐỂ HIỂN THỊ VÀ THAM KHẢO** - có thể có lỗi format hoặc thiếu sót.

### **2. HIỆN TRẠNG DỮ LIỆU**

#### **2.1. Trùng lặp có chủ đích**
- **94.74% nội dung trùng lặp** giữa `dieu_khoan.ten` và `de_muc.content_markdown`
- **5.26% không trùng** (các mục "Chương", "Phần", format differences)

#### **2.2. Lý do trùng lặp**
1. **Performance**: `de_muc.content_markdown` cho hiển thị toàn văn nhanh
2. **Search**: `dieu_khoan.ten` cho tìm kiếm/tra cứu chi tiết
3. **Redundancy**: Backup tự động, nếu một bên lỗi vẫn có bên kia

### **3. QUY TẮC SỬ DỤNG**

#### **3.1. KHI HIỂN THỊ TOÀN VĂN LUẬT**
```sql
-- Ưu tiên dùng de_muc.content_markdown cho hiển thị
SELECT content_markdown as toan_van_luat
FROM de_muc 
WHERE id = 'de_muc_id';
```

#### **3.2. KHI TRA CỨU/TÌM KIẾM ĐIỀU KHOẢN**
```sql
-- LUÔN dùng dieu_khoan.ten làm chuẩn
SELECT ten as noi_dung_chuan
FROM dieu_khoan
WHERE de_muc_id = 'de_muc_id' 
  AND ten LIKE '%từ_khóa%';
```

#### **3.3. KHI PHÁT HIỆN LỖI**
```sql
-- Nếu de_muc.content_markdown bị lỗi
-- Dùng dieu_khoan.ten làm nguồn chuẩn để sửa

-- 1. Lấy nội dung chuẩn từ dieu_khoan
SELECT GROUP_CONCAT(ten ORDER BY mapc SEPARATOR '\\n\\n') as noi_dung_chuan
FROM dieu_khoan
WHERE de_muc_id = 'de_muc_id';

-- 2. Update de_muc.content_markdown
UPDATE de_muc 
SET content_markdown = :noi_dung_chuan
WHERE id = 'de_muc_id';
```

### **4. QUY TRÌNH XỬ LÝ LỖI**

#### **4.1. Phát hiện lỗi**
```sql
-- Kiểm tra consistency
SELECT 
    dm.id,
    dm.text as de_muc_name,
    COUNT(dk.id) as so_dieu_khoan,
    SUM(CASE 
        WHEN dm.content_markdown LIKE CONCAT('%', LEFT(dk.ten, 50), '%') 
        THEN 1 ELSE 0 
    END) as trung_khop,
    ROUND(SUM(CASE 
        WHEN dm.content_markdown LIKE CONCAT('%', LEFT(dk.ten, 50), '%') 
        THEN 1 ELSE 0 
    END) / COUNT(dk.id) * 100, 2) as phan_tram_trung_khop
FROM de_muc dm
LEFT JOIN dieu_khoan dk ON dm.id = dk.de_muc_id
GROUP BY dm.id
HAVING phan_tram_trung_khop < 90;  -- Dưới 90% là có vấn đề
```

#### **4.2. Sửa lỗi**
1. **Xác định điều khoản bị lỗi**
2. **Lấy nội dung chuẩn từ `dieu_khoan.ten`**
3. **Sửa `de_muc.content_markdown`**
4. **Ghi log sửa chữa**

### **5. CẤU TRÚC DỮ LIỆU CHUẨN**

#### **5.1. `dieu_khoan.ten` - CHUẨN CHÍNH**
```
Điều [số]. [Nội dung đầy đủ của điều khoản]
```
**Ví dụ:**
```
Điều 36.3.LQ.1. Thanh niên
(Điều 1 Luật số 57/2020/QH14 Luật Thanh niên ngày 16/06/2020 của Quốc hội, có hiệu lực thi hành kể từ ngày 01/01/2021)
Thanh niên là công dân Việt Nam từ đủ 16 tuổi đến 30 tuổi.
```

#### **5.2. `de_muc.content_markdown` - HIỂN THỊ**
```
# [Tên đề mục]

[Toàn văn luật với format markdown]

## Chương I
### Điều 1. [Nội dung]
### Điều 2. [Nội dung]
...
```

### **6. QUY TẮC PHÁT TRIỂN**

#### **6.1. Khi thêm mới**
1. **Thêm vào `dieu_khoan.ten` trước** (chuẩn chính)
2. **Sau đó update `de_muc.content_markdown`** (hiển thị)

#### **6.2. Khi sửa đổi**
1. **Sửa `dieu_khoan.ten` trước**
2. **Đồng bộ sang `de_muc.content_markdown`**

#### **6.3. Khi xóa**
1. **Xóa từ `dieu_khoan`**
2. **Update `de_muc.content_markdown`** (remove content tương ứng)

### **7. SCRIPT KIỂM TRA & ĐỒNG BỘ**

#### **7.1. Kiểm tra consistency**
```sql
-- check_consistency.sql
SELECT 
    'Consistency Report' as report_type,
    NOW() as check_time,
    COUNT(DISTINCT dm.id) as total_de_muc,
    SUM(CASE 
        WHEN dm.content_markdown IS NOT NULL AND LENGTH(dm.content_markdown) > 0 
        THEN 1 ELSE 0 
    END) as de_muc_with_content,
    COUNT(DISTINCT dk.de_muc_id) as de_muc_with_dieu_khoan,
    ROUND(AVG(
        CASE 
            WHEN dm.content_markdown LIKE CONCAT('%', LEFT(dk.ten, 50), '%') 
            THEN 1 ELSE 0 
        END
    ) * 100, 2) as avg_consistency_percent
FROM de_muc dm
LEFT JOIN dieu_khoan dk ON dm.id = dk.de_muc_id;
```

#### **7.2. Đồng bộ từ dieu_khoan sang de_muc**
```sql
-- sync_from_dieu_khoan.sql
UPDATE de_muc dm
JOIN (
    SELECT 
        de_muc_id,
        GROUP_CONCAT(ten ORDER BY mapc SEPARATOR '\\n\\n') as consolidated_content
    FROM dieu_khoan
    GROUP BY de_muc_id
) dk ON dm.id = dk.de_muc_id
SET dm.content_markdown = dk.consolidated_content
WHERE dm.content_markdown IS NULL 
   OR dm.content_markdown != dk.consolidated_content;
```

### **8. LƯU Ý QUAN TRỌNG**

1. **KHÔNG BAO GIỜ** sửa `dieu_khoan.ten` mà không có lý do chính đáng
2. **LUÔN KIỂM TRA** consistency trước khi deploy changes
3. **BACKUP** `dieu_khoan.ten` trước khi thực hiện bulk updates
4. **DOCUMENT** mọi thay đổi đối với `dieu_khoan.ten`

### **9. TÀI LIỆU THAM KHẢO**

1. **Database Schema**: `DESCRIBE dieu_khoan;`, `DESCRIBE de_muc;`
2. **Sample Data**: Xem ví dụ tại `examples/dieu_khoan_samples.sql`
3. **Consistency Reports**: `reports/consistency_YYYYMMDD.md`

---

**Document Version**: 1.0  
**Last Updated**: 2026-02-23  
**Author**: Bột - AI Assistant  
**Project**: Van-Ban (Pháp điển điện tử)  

**QUY TẮC BẮT BUỘC**:  
✅ `dieu_khoan.ten` LÀ CHUẨN CHÍNH  
✅ `de_muc.content_markdown` DÙNG ĐỂ HIỂN THỊ  
✅ NẾU CÓ LỖI, DÙNG `dieu_khoan.ten` LÀM CHUẨN SỬA