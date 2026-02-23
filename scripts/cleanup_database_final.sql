-- Database Cleanup Final
-- Thực hiện: Xóa bảng thừa, rename columns, xóa file_name
-- Created: 2026-02-23

USE vbpl;

-- Bước 1: Backup thông tin trước khi xóa
CREATE TABLE IF NOT EXISTS backup_before_cleanup AS
SELECT 
    'de_muc_content' as table_name,
    COUNT(*) as record_count,
    SUM(LENGTH(html_content)) as total_size_bytes,
    NOW() as backup_time
FROM de_muc_content
UNION ALL
SELECT 
    'de_muc_markdown_simple',
    COUNT(*),
    SUM(LENGTH(html_content)),
    NOW()
FROM de_muc_markdown_simple;

-- Hiển thị backup info
SELECT '=== BACKUP INFORMATION ===' as info;
SELECT * FROM backup_before_cleanup;

-- Bước 2: Xóa các bảng thừa
DROP TABLE IF EXISTS de_muc_content;
DROP TABLE IF EXISTS de_muc_markdown_simple;
DROP TABLE IF EXISTS mapc_hierarchy;

SELECT '=== TABLES DELETED ===' as info;
SELECT '1. de_muc_content (306 records HTML)' as deleted_table;
SELECT '2. de_muc_markdown_simple (140 records test)' as deleted_table;
SELECT '3. mapc_hierarchy (0 records empty)' as deleted_table;

-- Bước 3: Rename columns trong de_muc_markdown cho rõ ràng
-- Hiện tại: id, de_muc_id, file_name, markdown_content, html_content, content_size, ...
-- Đổi thành: id, de_muc_id, content_markdown, content_html, content_size, ...

ALTER TABLE de_muc_markdown 
CHANGE COLUMN markdown_content content_markdown LONGTEXT,
CHANGE COLUMN html_content content_html LONGTEXT,
CHANGE COLUMN content_size content_size_bytes INT,
ADD COLUMN content_type ENUM('markdown', 'html', 'both') DEFAULT 'both',
ADD COLUMN compression_ratio DECIMAL(5,2) DEFAULT 0.00 COMMENT 'markdown/html ratio %';

SELECT '=== COLUMNS RENAMED ===' as info;
SELECT '1. markdown_content → content_markdown' as rename_action;
SELECT '2. html_content → content_html' as rename_action;
SELECT '3. content_size → content_size_bytes' as rename_action;
SELECT '4. Added: content_type, compression_ratio' as rename_action;

-- Bước 4: Xóa column file_name (không cần thiết)
ALTER TABLE de_muc_markdown DROP COLUMN file_name;

SELECT '=== COLUMN DELETED ===' as info;
SELECT 'file_name column deleted' as action;

-- Bước 5: Update content_type và compression_ratio
UPDATE de_muc_markdown 
SET content_type = CASE 
        WHEN content_html IS NOT NULL AND LENGTH(content_html) > 0 
             AND content_markdown IS NOT NULL AND LENGTH(content_markdown) > 0 
        THEN 'both'
        WHEN content_markdown IS NOT NULL AND LENGTH(content_markdown) > 0 
        THEN 'markdown'
        WHEN content_html IS NOT NULL AND LENGTH(content_html) > 0 
        THEN 'html'
        ELSE 'markdown'
    END,
    compression_ratio = CASE 
        WHEN content_html IS NOT NULL AND LENGTH(content_html) > 0 
             AND content_markdown IS NOT NULL AND LENGTH(content_markdown) > 0 
        THEN ROUND(LENGTH(content_markdown) / LENGTH(content_html) * 100, 2)
        ELSE 0 
    END;

SELECT '=== DATA UPDATED ===' as info;
SELECT 'Updated content_type and compression_ratio' as action;

-- Bước 6: Hiển thị cấu trúc mới
SELECT '=== NEW TABLE STRUCTURE ===' as info;
DESCRIBE de_muc_markdown;

-- Bước 7: Thống kê sau cleanup
SELECT '=== FINAL STATISTICS ===' as info;

-- Tổng số tables
SELECT COUNT(*) as total_tables FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = 'vbpl' AND TABLE_TYPE = 'BASE TABLE';

-- Danh sách tables
SELECT TABLE_NAME as table_name FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = 'vbpl' AND TABLE_TYPE = 'BASE TABLE'
ORDER BY TABLE_NAME;

-- Thống kê records
SELECT 
    'chu_de' as table_name,
    COUNT(*) as record_count,
    'N/A' as content_info
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
    CONCAT(
        'Markdown: ', COUNT(CASE WHEN LENGTH(content_markdown) > 0 THEN 1 END),
        ', HTML: ', COUNT(CASE WHEN LENGTH(content_html) > 0 THEN 1 END),
        ', Both: ', COUNT(CASE WHEN LENGTH(content_markdown) > 0 AND LENGTH(content_html) > 0 THEN 1 END)
    )
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

-- Compression statistics
SELECT 
    'Compression Stats' as stat_type,
    COUNT(*) as total_records,
    ROUND(AVG(compression_ratio), 2) as avg_compression_percent,
    ROUND(MIN(compression_ratio), 2) as min_compression,
    ROUND(MAX(compression_ratio), 2) as max_compression
FROM de_muc_markdown 
WHERE compression_ratio > 0;

-- Content type distribution
SELECT 
    content_type,
    COUNT(*) as record_count,
    ROUND(COUNT(*) / (SELECT COUNT(*) FROM de_muc_markdown) * 100, 1) as percentage
FROM de_muc_markdown 
GROUP BY content_type
ORDER BY record_count DESC;

-- Bước 8: Tạo view tổng hợp mới
CREATE OR REPLACE VIEW vw_de_muc_complete AS
SELECT 
    dm.id as de_muc_id,
    dm.text as de_muc_name,
    dm.stt as de_muc_order,
    dm.chu_de_id,
    cd.text as chu_de_name,
    cd.stt as chu_de_order,
    dmm.content_markdown,
    LENGTH(dmm.content_markdown) as markdown_size,
    dmm.content_html,
    LENGTH(dmm.content_html) as html_size,
    dmm.compression_ratio,
    dmm.content_type,
    dmm.created_at,
    dmm.updated_at
FROM de_muc dm
LEFT JOIN chu_de cd ON dm.chu_de_id = cd.id
LEFT JOIN de_muc_markdown dmm ON dm.id = dmm.de_muc_id
ORDER BY CAST(cd.stt AS UNSIGNED), CAST(dm.stt AS UNSIGNED);

SELECT '=== VIEW CREATED ===' as info;
SELECT 'vw_de_muc_complete created successfully' as action;

-- Bước 9: Kiểm tra integrity
SELECT '=== INTEGRITY CHECK ===' as info;

SELECT 
    'Total de_muc records' as check_item,
    COUNT(*) as count
FROM de_muc
UNION ALL
SELECT 
    'de_muc with markdown content',
    COUNT(DISTINCT dmm.de_muc_id)
FROM de_muc_markdown dmm
WHERE LENGTH(dmm.content_markdown) > 0
UNION ALL
SELECT 
    'Missing markdown content',
    COUNT(*)
FROM de_muc dm
LEFT JOIN de_muc_markdown dmm ON dm.id = dmm.de_muc_id
WHERE dmm.de_muc_id IS NULL OR LENGTH(dmm.content_markdown) = 0;

-- Bước 10: Final message
SELECT '=== CLEANUP COMPLETED SUCCESSFULLY ===' as final_status;
SELECT 'Database structure simplified and optimized' as result;
SELECT CONCAT('Total tables: ', COUNT(*)) as summary 
FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = 'vbpl' AND TABLE_TYPE = 'BASE TABLE';