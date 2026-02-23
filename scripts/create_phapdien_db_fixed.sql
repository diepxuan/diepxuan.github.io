-- TẠO TABLES CHO HỆ THỐNG PHÁP ĐIỂN ĐIỆN TỬ TRONG DATABASE VBPL

USE vbpl;

-- Disable foreign key checks
SET FOREIGN_KEY_CHECKS = 0;

-- Drop tables cũ nếu tồn tại
DROP TABLE IF EXISTS mapc_hierarchy;
DROP TABLE IF EXISTS dieu_khoan;
DROP TABLE IF EXISTS de_muc;
DROP TABLE IF EXISTS chu_de;
DROP TABLE IF EXISTS system_metadata;
DROP VIEW IF EXISTS vw_dieu_khoan_full;
DROP VIEW IF EXISTS vw_mapc_hierarchy;

-- Enable foreign key checks
SET FOREIGN_KEY_CHECKS = 1;

-- Bảng chủ đề (45 chủ đề)
CREATE TABLE chu_de (
    id VARCHAR(36) PRIMARY KEY,
    value VARCHAR(36) NOT NULL UNIQUE,
    text NVARCHAR(500) NOT NULL,
    stt VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_stt (stt),
    INDEX idx_text (text(100))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Bảng đề mục (271 đề mục)
CREATE TABLE de_muc (
    id VARCHAR(36) PRIMARY KEY,
    value VARCHAR(36) NOT NULL UNIQUE,
    text NVARCHAR(500) NOT NULL,
    chu_de_id VARCHAR(36) NOT NULL,
    stt VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_chu_de_id (chu_de_id),
    INDEX idx_stt (stt),
    INDEX idx_text (text(100)),
    FOREIGN KEY (chu_de_id) REFERENCES chu_de(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Bảng điều khoản pháp luật (76,303 điều khoản)
CREATE TABLE dieu_khoan (
    id VARCHAR(36) PRIMARY KEY,
    chi_muc VARCHAR(50),
    mapc VARCHAR(50) NOT NULL,
    ten NVARCHAR(2000) NOT NULL,
    chu_de_id VARCHAR(36) NOT NULL,
    de_muc_id VARCHAR(36) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_mapc (mapc),
    INDEX idx_chu_de_id (chu_de_id),
    INDEX idx_de_muc_id (de_muc_id),
    INDEX idx_chi_muc (chi_muc),
    INDEX idx_ten (ten(200)),
    FULLTEXT idx_fulltext_ten (ten),
    FOREIGN KEY (chu_de_id) REFERENCES chu_de(id) ON DELETE CASCADE,
    FOREIGN KEY (de_muc_id) REFERENCES de_muc(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Bảng phân cấp MAPC (để phân tích cấu trúc phân cấp)
CREATE TABLE mapc_hierarchy (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mapc VARCHAR(50) NOT NULL,
    level1 VARCHAR(2),
    level2 VARCHAR(3),
    level3 VARCHAR(3),
    level4 VARCHAR(3),
    level5 VARCHAR(3),
    level6 VARCHAR(3),
    level7 VARCHAR(3),
    level8 VARCHAR(3),
    level9 VARCHAR(3),
    level10 VARCHAR(3),
    dieu_khoan_id VARCHAR(36) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE INDEX idx_mapc (mapc),
    INDEX idx_dieu_khoan_id (dieu_khoan_id),
    INDEX idx_level1 (level1),
    INDEX idx_level2 (level2),
    INDEX idx_level3 (level3),
    FOREIGN KEY (dieu_khoan_id) REFERENCES dieu_khoan(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Bảng metadata cho hệ thống
CREATE TABLE system_metadata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    key_name VARCHAR(100) NOT NULL UNIQUE,
    value TEXT,
    description NVARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_key_name (key_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insert metadata
INSERT INTO system_metadata (key_name, value, description) VALUES
('system_name', 'PhapDienDienTu', 'Tên hệ thống'),
('source', 'Bộ Pháp điển Điện tử - Bộ Tư pháp', 'Nguồn dữ liệu'),
('total_chu_de', '45', 'Tổng số chủ đề'),
('total_de_muc', '271', 'Tổng số đề mục'),
('total_dieu_khoan', '76303', 'Tổng số điều khoản'),
('import_date', NOW(), 'Ngày import dữ liệu'),
('version', '1.0', 'Phiên bản database');

-- Tạo view để dễ query
CREATE VIEW vw_dieu_khoan_full AS
SELECT 
    dk.id,
    dk.chi_muc,
    dk.mapc,
    dk.ten,
    cd.text AS chu_de,
    dm.text AS de_muc,
    cd.stt AS chu_de_stt,
    dm.stt AS de_muc_stt,
    dk.created_at
FROM dieu_khoan dk
JOIN chu_de cd ON dk.chu_de_id = cd.id
JOIN de_muc dm ON dk.de_muc_id = dm.id;

-- Tạo view cho phân cấp MAPC
CREATE VIEW vw_mapc_hierarchy AS
SELECT 
    mh.*,
    dk.ten,
    dk.chi_muc,
    cd.text AS chu_de,
    dm.text AS de_muc
FROM mapc_hierarchy mh
JOIN dieu_khoan dk ON mh.dieu_khoan_id = dk.id
JOIN chu_de cd ON dk.chu_de_id = cd.id
JOIN de_muc dm ON dk.de_muc_id = dm.id;

-- Hiển thị thông tin database
SELECT 'Tables created successfully in vbpl database' AS message;
SELECT DATABASE() AS current_database;
SELECT COUNT(*) AS table_count FROM information_schema.tables WHERE table_schema = 'vbpl' AND table_name IN ('chu_de', 'de_muc', 'dieu_khoan', 'mapc_hierarchy', 'system_metadata');