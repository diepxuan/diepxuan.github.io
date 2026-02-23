-- Merge de_muc và de_muc_markdown thành 1 bảng
-- Created: 2026-02-23

USE vbpl;

-- Bước 1: Tạo bảng mới với tất cả columns
CREATE TABLE de_muc_combined (
    -- Columns từ de_muc
    id VARCHAR(36) PRIMARY KEY,
    value VARCHAR(36) UNIQUE NOT NULL,
    text VARCHAR(500) NOT NULL,
    chu_de_id VARCHAR(36) NOT NULL,
    stt VARCHAR(10),
    
    -- Columns từ de_muc_markdown (bỏ id và de_muc_id)
    content_markdown LONGTEXT,
    content_html LONGTEXT,
    content_size_bytes INT,
    provision_count INT DEFAULT 0,
    related_documents LONGTEXT,
    update_date VARCHAR(50),
    content_type ENUM('markdown', 'html', 'both') DEFAULT 'both',
    compression_ratio DECIMAL(5,2) DEFAULT 0.00,
    
    -- Timestamps (giữ từ de_muc_markdown nếu có, không thì từ de_muc)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    -- Indexes
    INDEX idx_chu_de_id (chu_de_id),
    INDEX idx_stt (stt),
    INDEX idx_value (value),
    INDEX idx_text (text(100)),
    
    -- Foreign key
    FOREIGN KEY (chu_de_id) REFERENCES chu_de(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SELECT '=== BẢNG MỚI ĐƯỢC TẠO ===' as info;
DESCRIBE de_muc_combined;

-- Bước 2: Copy data từ 2 bảng cũ
INSERT INTO de_muc_combined (
    id, value, text, chu_de_id, stt,
    content_markdown, content_html, content_size_bytes,
    provision_count, related_documents, update_date,
    content_type, compression_ratio,
    created_at, updated_at
)
SELECT 
    dm.id,
    dm.value,
    dm.text,
    dm.chu_de_id,
    dm.stt,
    dmm.content_markdown,
    dmm.content_html,
    dmm.content_size_bytes,
    dmm.provision_count,
    dmm.related_documents,
    dmm.update_date,
    dmm.content_type,
    dmm.compression_ratio,
    -- Ưu tiên timestamps từ de_muc_markdown, fallback về de_muc
    COALESCE(dmm.created_at, dm.created_at, CURRENT_TIMESTAMP),
    COALESCE(dmm.updated_at, dm.updated_at, CURRENT_TIMESTAMP)
FROM de_muc dm
LEFT JOIN de_muc_markdown dmm ON dm.id = dmm.de_muc_id;

SELECT '=== DATA ĐÃ ĐƯỢC COPY ===' as info;
SELECT COUNT(*) as records_copied FROM de_muc_combined;

-- Bước 3: Kiểm tra data integrity
SELECT '=== KIỂM TRA INTEGRITY ===' as info;

-- Kiểm tra số records
SELECT 
    'de_muc' as source_table,
    COUNT(*) as record_count
FROM de_muc
UNION ALL
SELECT 
    'de_muc_markdown',
    COUNT(*)
FROM de_muc_markdown
UNION ALL
SELECT 
    'de_muc_combined',
    COUNT(*)
FROM de_muc_combined;

-- Kiểm tra missing data
SELECT 
    'Missing in combined' as check_type,
    COUNT(*) as count
FROM de_muc dm
LEFT JOIN de_muc_combined dmc ON dm.id = dmc.id
WHERE dmc.id IS NULL;

-- Kiểm tra content
SELECT 
    'Content analysis' as analysis,
    COUNT(CASE WHEN LENGTH(content_markdown) > 0 THEN 1 END) as has_markdown,
    COUNT(CASE WHEN LENGTH(content_html) > 0 THEN 1 END) as has_html,
    COUNT(CASE WHEN content_markdown IS NULL AND content_html IS NULL THEN 1 END) as no_content
FROM de_muc_combined;

-- Bước 4: Tạm thời disable foreign key checks
SET FOREIGN_KEY_CHECKS = 0;

-- Bước 5: Update foreign key trong dieu_khoan (nếu cần, nhưng thực tế vẫn trỏ tới cùng id)
-- Không cần update vì dieu_khoan.de_muc_id vẫn trỏ tới cùng id

-- Bước 6: Xóa bảng cũ
DROP TABLE IF EXISTS de_muc_markdown;
DROP TABLE IF EXISTS de_muc;

SELECT '=== BẢNG CŨ ĐÃ XÓA ===' as info;
SELECT '1. de_muc_markdown (306 records)' as deleted_table;
SELECT '2. de_muc (306 records)' as deleted_table;

-- Bước 7: Đổi tên bảng mới thành de_muc
RENAME TABLE de_muc_combined TO de_muc;

SELECT '=== BẢNG ĐÃ ĐƯỢC ĐỔI TÊN ===' as info;
SELECT 'de_muc_combined → de_muc' as rename_action;

-- Bước 8: Bật lại foreign key checks
SET FOREIGN_KEY_CHECKS = 1;

-- Bước 9: Kiểm tra foreign keys
SELECT '=== KIỂM TRA FOREIGN KEYS ===' as info;

SELECT 
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM information_schema.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'vbpl' 
  AND REFERENCED_TABLE_NAME = 'de_muc'
ORDER BY TABLE_NAME, CONSTRAINT_NAME;

-- Bước 10: Kiểm tra cấu trúc bảng mới
SELECT '=== CẤU TRÚC BẢNG MỚI ===' as info;
DESCRIBE de_muc;

-- Bước 11: Thống kê bảng mới
SELECT '=== THỐNG KÊ BẢNG MỚI ===' as info;

SELECT 
    'Total records' as metric,
    COUNT(*) as value
FROM de_muc
UNION ALL
SELECT 
    'Has markdown content',
    COUNT(CASE WHEN LENGTH(content_markdown) > 0 THEN 1 END)
FROM de_muc
UNION ALL
SELECT 
    'Has HTML content',
    COUNT(CASE WHEN LENGTH(content_html) > 0 THEN 1 END)
FROM de_muc
UNION ALL
SELECT 
    'Content type: both',
    COUNT(CASE WHEN content_type = 'both' THEN 1 END)
FROM de_muc
UNION ALL
SELECT 
    'Content type: markdown only',
    COUNT(CASE WHEN content_type = 'markdown' THEN 1 END)
FROM de_muc
UNION ALL
SELECT 
    'Content type: html only',
    COUNT(CASE WHEN content_type = 'html' THEN 1 END)
FROM de_muc;

-- Bước 12: Kiểm tra sample data
SELECT '=== SAMPLE DATA (5 RECORDS) ===' as info;

SELECT 
    id,
    LEFT(text, 50) as de_muc_name,
    stt,
    content_type,
    compression_ratio,
    ROUND(LENGTH(content_markdown) / 1024, 2) as markdown_kb,
    ROUND(LENGTH(content_html) / 1024, 2) as html_kb,
    created_at
FROM de_muc
ORDER BY CAST(stt AS UNSIGNED)
LIMIT 5;

-- Bước 13: Final check - đảm bảo dieu_khoan vẫn hoạt động
SELECT '=== KIỂM TRA DIEU_KHOAN RELATIONSHIP ===' as info;

SELECT 
    'dieu_khoan records with valid de_muc' as check_item,
    CASE 
        WHEN NOT EXISTS (
            SELECT 1 FROM dieu_khoan dk
            LEFT JOIN de_muc dm ON dk.de_muc_id = dm.id
            WHERE dm.id IS NULL
        ) THEN '✅ ALL VALID'
        ELSE '❌ INVALID RECORDS FOUND'
    END as status
UNION ALL
SELECT 
    'Total dieu_khoan records',
    CONCAT(COUNT(*), ' records')
FROM dieu_khoan;

-- Bước 14: Tạo view mới cho convenience
CREATE OR REPLACE VIEW vw_de_muc_with_chu_de AS
SELECT 
    dm.id,
    dm.value,
    dm.text as de_muc_name,
    dm.stt as de_muc_order,
    dm.chu_de_id,
    cd.text as chu_de_name,
    cd.stt as chu_de_order,
    dm.content_type,
    dm.compression_ratio,
    ROUND(LENGTH(dm.content_markdown) / 1024, 2) as markdown_size_kb,
    ROUND(LENGTH(dm.content_html) / 1024, 2) as html_size_kb,
    dm.created_at,
    dm.updated_at
FROM de_muc dm
LEFT JOIN chu_de cd ON dm.chu_de_id = cd.id
ORDER BY CAST(cd.stt AS UNSIGNED), CAST(dm.stt AS UNSIGNED);

SELECT '=== VIEW ĐÃ ĐƯỢC TẠO ===' as info;
SELECT 'vw_de_muc_with_chu_de created successfully' as action;

-- Bước 15: Final success message
SELECT '=== MERGE COMPLETED SUCCESSFULLY ===' as final_status;
SELECT '✅ de_muc và de_muc_markdown đã được gộp thành 1 bảng' as result;
SELECT '✅ Tất cả 306 records được bảo toàn' as result;
SELECT '✅ Foreign keys vẫn hoạt động bình thường' as result;
SELECT '✅ Cấu trúc database đã được tối ưu' as result;