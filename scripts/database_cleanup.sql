-- Database Cleanup Script
-- Tinh giản cấu trúc database vbpl
-- Created: 2026-02-23

USE vbpl;

-- Bước 1: Backup thông tin trước khi xóa
CREATE TABLE IF NOT EXISTS backup_deleted_tables AS
SELECT 
    'de_muc_content' as source_table,
    COUNT(*) as record_count,
    SUM(LENGTH(html_content)) as total_html_size,
    NOW() as backup_time
FROM de_muc_content
UNION ALL
SELECT 
    'de_muc_markdown_simple',
    COUNT(*),
    SUM(LENGTH(html_content)),
    NOW()
FROM de_muc_markdown_simple
UNION ALL
SELECT 
    'mapc_hierarchy',
    COUNT(*),
    0,
    NOW()
FROM mapc_hierarchy;

-- Hiển thị backup info
SELECT * FROM backup_deleted_tables;

-- Bước 2: Xóa foreign keys trước khi xóa bảng
-- (MySQL sẽ tự động xóa FK khi xóa bảng, nhưng tốt hơn nên xóa trước)

-- Bước 3: Xóa các bảng thừa
DROP TABLE IF EXISTS de_muc_content;
DROP TABLE IF EXISTS de_muc_markdown_simple;
DROP TABLE IF EXISTS mapc_hierarchy;

-- Bước 4: Tối ưu bảng de_muc_markdown
-- Option 1: Xóa cột html_content (nếu chỉ cần markdown)
-- ALTER TABLE de_muc_markdown DROP COLUMN html_content;

-- Option 2: Giữ cả hai nhưng rename cho rõ ràng
ALTER TABLE de_muc_markdown 
CHANGE COLUMN markdown_content content LONGTEXT,
CHANGE COLUMN html_content original_html LONGTEXT,
ADD COLUMN content_type ENUM('markdown', 'html') DEFAULT 'markdown',
ADD COLUMN compression_ratio DECIMAL(5,2) DEFAULT 0.00;

-- Update content_type và compression_ratio
UPDATE de_muc_markdown 
SET content_type = 'markdown',
    compression_ratio = CASE 
        WHEN LENGTH(original_html) > 0 
        THEN ROUND(LENGTH(content) / LENGTH(original_html) * 100, 2)
        ELSE 0 
    END;

-- Bước 5: Kiểm tra views còn hoạt động không
-- (Các views không phụ thuộc vào bảng đã xóa)

-- Bước 6: Tạo bảng tổng hợp mới (nếu cần)
CREATE TABLE IF NOT EXISTS vw_de_muc_summary AS
SELECT 
    dm.id as de_muc_id,
    dm.text as de_muc_name,
    dm.stt,
    dm.chu_de_id,
    cd.text as chu_de_name,
    dmm.file_name,
    dmm.content_type,
    LENGTH(dmm.content) as content_size,
    dmm.compression_ratio,
    dmm.created_at,
    dmm.updated_at
FROM de_muc dm
LEFT JOIN chu_de cd ON dm.chu_de_id = cd.id
LEFT JOIN de_muc_markdown dmm ON dm.id = dmm.de_muc_id
ORDER BY CAST(cd.stt AS UNSIGNED), CAST(dm.stt AS UNSIGNED);

-- Bước 7: Hiển thị cấu trúc mới
SHOW TABLES;

SELECT 
    TABLE_NAME,
    TABLE_ROWS as record_count
FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = 'vbpl'
ORDER BY TABLE_NAME;

-- Bước 8: Thống kê kích thước
SELECT 
    'chu_de' as table_name,
    COUNT(*) as records,
    'N/A' as avg_size
FROM chu_de
UNION ALL
SELECT 
    'de_muc',
    COUNT(*),
    'N/A'
FROM de_muc
UNION ALL
SELECT 
    'de_muc_markdown',
    COUNT(*),
    CONCAT(ROUND(AVG(LENGTH(content)) / 1024, 2), ' KB')
FROM de_muc_markdown
UNION ALL
SELECT 
    'dieu_khoan',
    COUNT(*),
    'N/A'
FROM dieu_khoan
UNION ALL
SELECT 
    'system_metadata',
    COUNT(*),
    'N/A'
FROM system_metadata;

-- Bước 9: Kiểm tra integrity
SELECT 
    'Total de_muc' as check_item,
    COUNT(*) as count
FROM de_muc
UNION ALL
SELECT 
    'de_muc with markdown',
    COUNT(DISTINCT dmm.de_muc_id)
FROM de_muc_markdown dmm
UNION ALL
SELECT 
    'Missing markdown',
    COUNT(*)
FROM de_muc dm
LEFT JOIN de_muc_markdown dmm ON dm.id = dmm.de_muc_id
WHERE dmm.de_muc_id IS NULL;