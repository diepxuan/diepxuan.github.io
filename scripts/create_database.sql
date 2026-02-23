-- Tạo database phapdien_db nếu chưa tồn tại
CREATE DATABASE IF NOT EXISTS phapdien_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Cấp quyền cho user vbpl
GRANT ALL PRIVILEGES ON phapdien_db.* TO 'vbpl'@'%';
FLUSH PRIVILEGES;

-- Hiển thị thông tin
SELECT 'Database phapdien_db đã được tạo và cấp quyền' AS message;