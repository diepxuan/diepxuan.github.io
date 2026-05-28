# THÔNG TIN MYSQL DATABASE CHO DỰ ÁN VAN-BAN

## ✅ VERIFICATION STATUS (Checked: 2026-02-23)
- **✅ Server**: `mysql.diepxuan.corp:3306` - MariaDB 10.11.11
- **✅ User `vbpl`**: TỒN TẠI và có thể kết nối
- **✅ Database `vbpl`**: TỒN TẠI và sẵn sàng sử dụng
- **✅ Permissions**: User `vbpl` có **ALL PRIVILEGES** trên database `vbpl`
- **✅ Connection test**: Đã test thành công với CREATE/INSERT/SELECT/DROP

## 📊 THÔNG TIN KẾT NỐI MYSQL

### 1. **Multiple User Accounts**

#### **Option A: Laravel User (Existing)**
- **Username**: `laravel`
- **Password**: `<redacted - set via local env>`
- **Database**: `laravel` (existing Laravel application database)
- **Purpose**: General Laravel application access
- **Status**: Not verified (based on Portal .env file)

#### **Option B: VBPL User (Van-Ban Specific) - ✅ VERIFIED**
- **Username**: `vbpl`
- **Password**: `<redacted - set via local env>`
- **Database**: `vbpl` (existing and verified)
- **Purpose**: Dedicated access for van-ban/pháp điển project
- **Permissions**: ALL PRIVILEGES on `vbpl` database
- **Server**: MariaDB 10.11.11-MariaDB-0+deb12u1

### 2. **Connection strings**

#### **Using Laravel user:**
```bash
# Standard connection
mysql -h mysql.diepxuan.corp -P 3306 -u laravel -p laravel

# Alternative (specify database later)
mysql -h mysql.diepxuan.corp -u laravel -p

# With explicit password (not recommended for scripts)
mysql -h mysql.diepxuan.corp -u laravel -p laravel
```

#### **Using VBPL user (✅ VERIFIED):**
```bash
# Standard connection với database vbpl
mysql -h mysql.diepxuan.corp -P 3306 -u vbpl -p vbpl

# Hoặc connect rồi chọn database
mysql -h mysql.diepxuan.corp -u vbpl -p
# Sau đó trong mysql shell: USE vbpl;

# Test connection (verified working)
mysql -h mysql.diepxuan.corp -u vbpl -p -e "SELECT 'VBPL Connected' AS status;"

# Kiểm tra databases accessible
mysql -h mysql.diepxuan.corp -u vbpl -p -e "SHOW DATABASES;"

# Kiểm tra tables trong database vbpl (hiện tại empty)
mysql -h mysql.diepxuan.corp -u vbpl -p -e "USE vbpl; SHOW TABLES;"
```

### 3. **Host Information**
#### **Primary Host**: `mysql.diepxuan.corp`
- **Type**: Internal corporate MySQL server
- **Location**: Corporate data center/internal network
- **Purpose**: Primary database server for Laravel applications
- **Access**: Internal network access required

#### **Network Configuration**
- **DNS**: `mysql.diepxuan.corp` resolves to internal IP
- **Firewall**: Port 3306 open for internal connections
- **Authentication**: MySQL native authentication

#### **Host Verification**
```bash
# Check DNS resolution
host mysql.diepxuan.corp
nslookup mysql.diepxuan.corp
dig mysql.diepxuan.corp

# Check network connectivity
ping mysql.diepxuan.corp
traceroute mysql.diepxuan.corp

# Check port accessibility
nc -zv mysql.diepxuan.corp 3306
telnet mysql.diepxuan.corp 3306
```

### 3. **Environment variables**
```env
DB_CONNECTION=mysql
DB_HOST=mysql.diepxuan.corp
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=laravel
DB_PASSWORD=<set-in-local-env>
```

## 🗄️ CẤU TRÚC DATABASE

### 1. **Database hiện tại**
- **Tên database**: `laravel` (Laravel application database)
- **Mục đích**: Chứa dữ liệu cho ứng dụng Portal

### 2. **Các tables quan trọng**
```sql
-- Kiểm tra các tables trong database
SHOW TABLES FROM laravel;

-- Xem cấu trúc của các tables chính
DESCRIBE users;
DESCRIBE migrations;
DESCRIBE failed_jobs;
DESCRIBE password_reset_tokens;
DESCRIBE personal_access_tokens;
```

## 🔗 KẾT NỐI TỪ ỨNG DỤNG

### 1. **Environment Variables**

#### **For Laravel user (existing):**
```env
DB_CONNECTION=mysql
DB_HOST=mysql.diepxuan.corp
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=laravel
DB_PASSWORD=<set-in-local-env>
```

#### **For VBPL user (van-ban specific) - ✅ VERIFIED:**
```env
DB_CONNECTION=mysql
DB_HOST=mysql.diepxuan.corp
DB_PORT=3306
DB_DATABASE=vbpl          # ✅ Database name: vbpl (verified)
DB_USERNAME=vbpl          # ✅ Username: vbpl (verified)
DB_PASSWORD=<set-in-local-env>  # ✅ Password (verified)
```

### 2. **Laravel configuration**
```php
// config/database.php
'mysql' => [
    'driver' => 'mysql',
    'url' => env('DATABASE_URL'),
    'host' => env('DB_HOST', '127.0.0.1'),
    'port' => env('DB_PORT', '3306'),
    'database' => env('DB_DATABASE', 'forge'),
    'username' => env('DB_USERNAME', 'forge'),
    'password' => env('DB_PASSWORD', ''),
    'unix_socket' => env('DB_SOCKET', ''),
    'charset' => 'utf8mb4',
    'collation' => 'utf8mb4_unicode_ci',
    'prefix' => '',
    'prefix_indexes' => true,
    'strict' => true,
    'engine' => null,
    'options' => extension_loaded('pdo_mysql') ? array_filter([
        PDO::MYSQL_ATTR_SSL_CA => env('MYSQL_ATTR_SSL_CA'),
    ]) : [],
],
```

### 2. **Connection test**
```php
// Test connection trong Laravel
try {
    DB::connection('mysql')->getPdo();
    echo "Connected successfully to MySQL database!";
} catch (\Exception $e) {
    die("Could not connect to the database. Error: " . $e->getMessage());
}
```

## 📋 QUẢN LÝ DATABASE

### 1. **Backup database**
```bash
# Backup toàn bộ database
mysqldump -h mysql.diepxuan.corp -u laravel -p laravel > laravel_backup_$(date +%Y%m%d).sql

# Backup chỉ cấu trúc
mysqldump -h mysql.diepxuan.corp -u laravel -p --no-data laravel > laravel_structure.sql

# Backup chỉ dữ liệu
mysqldump -h mysql.diepxuan.corp -u laravel -p --no-create-info laravel > laravel_data.sql
```

### 2. **Restore database**
```bash
# Restore từ backup
mysql -h mysql.diepxuan.corp -u laravel -p laravel < laravel_backup.sql
```

### 3. **Kiểm tra connection**

#### **Test Laravel user:**
```bash
# Test connection từ terminal
mysqladmin -h mysql.diepxuan.corp -u laravel -p ping

# Kiểm tra version
mysql -h mysql.diepxuan.corp -u laravel -p -e "SELECT VERSION();"
```

#### **Test VBPL user (✅ VERIFIED WORKING):**
```bash
# Test connection với VBPL user (verified)
mysqladmin -h mysql.diepxuan.corp -u vbpl -p ping

# Kiểm tra version và user (verified)
mysql -h mysql.diepxuan.corp -u vbpl -p -e "SELECT VERSION();"
# Kết quả: 10.11.11-MariaDB-0+deb12u1

mysql -h mysql.diepxuan.corp -u vbpl -p -e "SELECT USER();"
# Kết quả: vbpl@openclaw.diepxuan.corp

# Kiểm tra databases accessible (verified)
mysql -h mysql.diepxuan.corp -u vbpl -p -e "SHOW DATABASES;"
# Kết quả: information_schema, vbpl

# Test full functionality (verified)
mysql -h mysql.diepxuan.corp -u vbpl -p vbpl -e "
  CREATE TABLE IF NOT EXISTS test_connection (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    message VARCHAR(100)
  );
  INSERT INTO test_connection (message) VALUES ('VBPL connection verified');
  SELECT * FROM test_connection;
  DROP TABLE test_connection;
"
# Kết quả: id=1, message='VBPL connection verified'
```

## 🔐 BẢO MẬT

### 1. **User Permissions**

#### **Laravel user permissions:**
```sql
-- Kiểm tra permissions của laravel user
SHOW GRANTS FOR 'laravel'@'%';
```

#### **VBPL user status (✅ VERIFIED EXISTS):**
```sql
-- User đã tồn tại với password đã xác minh
-- Kiểm tra user (verified):
SELECT User, Host FROM mysql.user WHERE User = 'vbpl';
-- Kết quả: vbpl@%

-- Kiểm tra permissions (verified):
SHOW GRANTS FOR 'vbpl'@'%';
-- Kết quả: 
-- GRANT USAGE ON *.* TO `vbpl`@`%` IDENTIFIED BY PASSWORD '*27207571548F2E8C1F10AD97CCF07402441F9654'
-- GRANT ALL PRIVILEGES ON `vbpl`.* TO `vbpl`@`%`

-- Database đã tồn tại:
SHOW DATABASES LIKE 'vbpl';
-- Kết quả: vbpl
```

#### **Nếu cần recreate (cho development):**
```sql
-- Xóa và tạo lại (cẩn thận - sẽ mất dữ liệu)
DROP DATABASE IF EXISTS vbpl;
DROP USER IF EXISTS 'vbpl'@'%';

-- Tạo lại user và database
CREATE USER 'vbpl'@'%' IDENTIFIED BY '${VBPL_DB_PASSWORD}';
CREATE DATABASE vbpl CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
GRANT ALL PRIVILEGES ON vbpl.* TO 'vbpl'@'%';
FLUSH PRIVILEGES;
```

### 2. **SSL/TLS connection** (nếu có)
```env
# Thêm vào .env nếu server hỗ trợ SSL
MYSQL_ATTR_SSL_CA=/path/to/ca-cert.pem
```

## 📊 MONITORING

### 1. **Kiểm tra status**
```sql
-- Kiểm tra server status
SHOW STATUS;

-- Kiểm tra process list
SHOW PROCESSLIST;

-- Kiểm tra variables
SHOW VARIABLES LIKE '%version%';
SHOW VARIABLES LIKE '%max_connections%';
```

### 2. **Performance metrics**
```sql
-- Kiểm tra query performance
SHOW GLOBAL STATUS LIKE 'Questions';
SHOW GLOBAL STATUS LIKE 'Slow_queries';
SHOW GLOBAL STATUS LIKE 'Connections';
```

## 🚀 DEPLOYMENT NOTES

### 1. **User Options cho dự án van-ban**

#### **Option 1: Sử dụng VBPL user (✅ VERIFIED & RECOMMENDED)**
- **Username**: `vbpl` (✅ verified exists)
- **Password**: `<redacted - set via local env>` (✅ verified working)
- **Database**: `vbpl` (✅ verified exists, currently empty)
- **Permissions**: ALL PRIVILEGES (✅ verified)
- **Ưu điểm**: Dedicated user, better security isolation, ready to use
- **Status**: ✅ Hoàn toàn sẵn sàng cho dự án van-ban

#### **Option 2: Sử dụng Laravel user**
- **Username**: `laravel`
- **Password**: `<redacted - set via local env>`
- **Database**: `laravel` (existing - not verified)
- **Ưu điểm**: Đã có sẵn, không cần setup thêm
- **Status**: Chưa verified - dựa trên Portal .env file

### 2. **Current Status với VBPL user (✅ ALREADY SETUP)**
```sql
-- User và database ĐÃ TỒN TẠI và VERIFIED
-- Không cần setup thêm

-- Chỉ cần verify:
SHOW GRANTS FOR 'vbpl'@'%';
-- Kết quả: GRANT ALL PRIVILEGES ON `vbpl`.* TO `vbpl`@`%`

SHOW DATABASES LIKE 'vbpl';
-- Kết quả: vbpl

-- Database hiện tại empty, sẵn sàng cho schema van-ban
USE vbpl;
SHOW TABLES;
-- Kết quả: (empty - ready for your schema)
```

### 3. **Schema đề xuất cho van-ban (sử dụng database `vbpl`)**
```sql
-- Sử dụng database vbpl (✅ verified exists)
USE vbpl;

-- Table cho văn bản pháp luật
CREATE TABLE IF NOT EXISTS vanban (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ma_van_ban VARCHAR(100) UNIQUE,
    ten_van_ban TEXT,
    loai_van_ban VARCHAR(50),
    co_quan_ban_hanh VARCHAR(200),
    ngay_ban_hanh DATE,
    ngay_co_hieu_luc DATE,
    noi_dung LONGTEXT,
    trang_thai VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table cho điều khoản
CREATE TABLE IF NOT EXISTS dieukhoan (
    id INT PRIMARY KEY AUTO_INCREMENT,
    vanban_id INT,
    so_dieu VARCHAR(20),
    tieu_de TEXT,
    noi_dung LONGTEXT,
    FOREIGN KEY (vanban_id) REFERENCES vanban(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Index cho tìm kiếm
CREATE FULLTEXT INDEX IF NOT EXISTS idx_vanban_search ON vanban(ten_van_ban, noi_dung);
CREATE FULLTEXT INDEX IF NOT EXISTS idx_dieukhoan_search ON dieukhoan(tieu_de, noi_dung);

-- Table cho pháp điển (nếu cần)
CREATE TABLE IF NOT EXISTS phapdien_dieukhoan (
    id VARCHAR(36) PRIMARY KEY,
    dieukhoan_id VARCHAR(36) NOT NULL,
    ten TEXT,
    chimuc TEXT,
    mapc TEXT,
    html_content LONGTEXT,
    markdown_content LONGTEXT,
    raw_text LONGTEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table cho metadata pháp điển
CREATE TABLE IF NOT EXISTS phapdien_metadata (
    id INT PRIMARY KEY AUTO_INCREMENT,
    topic_name VARCHAR(200),
    subtopic_name VARCHAR(200),
    provision_count INT,
    content_coverage DECIMAL(5,2),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

## 📞 TROUBLESHOOTING

### 1. **Host Connection Issues**
#### **Lỗi: Cannot resolve host**
```
ERROR 2005 (HY000): Unknown MySQL server host 'mysql.diepxuan.corp' (0)
```
**Giải pháp**:
1. Kiểm tra DNS resolution:
   ```bash
   nslookup mysql.diepxuan.corp
   ping mysql.diepxuan.corp
   ```
2. Kiểm tra `/etc/hosts` file:
   ```bash
   cat /etc/hosts | grep mysql.diepxuan.corp
   ```
3. Add host entry nếu cần:
   ```bash
   echo "192.168.1.100 mysql.diepxuan.corp" >> /etc/hosts
   ```

#### **Lỗi: Connection refused**
```
ERROR 2002 (HY000): Can't connect to MySQL server on 'mysql.diepxuan.corp' (115)
```
**Giải pháp**:
1. Kiểm tra port accessibility:
   ```bash
   nc -zv mysql.diepxuan.corp 3306
   ```
2. Kiểm tra firewall rules:
   ```bash
   iptables -L | grep 3306
   ```
3. Kiểm tra MySQL service status:
   ```bash
   # Nếu có SSH access
   ssh user@mysql.diepxuan.corp "systemctl status mysql"
   ```

### 2. **Host-Specific Issues**
#### **Lỗi: Network unreachable**
```
ERROR 2003 (HY000): Can't connect to MySQL server on 'mysql.diepxuan.corp' (113)
```
**Giải pháp**:
1. Kiểm tra network connectivity:
   ```bash
   traceroute mysql.diepxuan.corp
   mtr mysql.diepxuan.corp
   ```
2. Kiểm tra corporate VPN/network access
3. Verify internal network routing

#### **Lỗi: Slow connection to host**
**Giải pháp**:
1. Kiểm tra network latency:
   ```bash
   ping -c 10 mysql.diepxuan.corp
   ```
2. Consider connection pooling
3. Use persistent connections trong application

### 3. **Lỗi authentication**
```
ERROR 1045 (28000): Access denied for user 'laravel'@'%' (using password: YES)
```
**Giải pháp**: Kiểm tra lại username/password, và user permissions.

### 4. **Lỗi database không tồn tại**
```
ERROR 1049 (42000): Unknown database 'laravel'
```
**Giải pháp**: Tạo database hoặc kiểm tra tên database.

### 5. **Host-Based Authentication Issues**
#### **Lỗi: Access from specific host denied**
```
ERROR 1130 (HY000): Host 'client-ip' is not allowed to connect to this MySQL server
```
**Giải pháp**:
1. Kiểm tra MySQL user permissions:
   ```sql
   SELECT Host, User FROM mysql.user WHERE User = 'laravel';
   ```
2. Update permissions nếu cần:
   ```sql
   GRANT ALL PRIVILEGES ON laravel.* TO 'laravel'@'%';
   FLUSH PRIVILEGES;
   ```

## 📚 TÀI LIỆU THAM KHẢO

### 1. **MySQL Documentation**
- [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)
- [MySQL Workbench](https://dev.mysql.com/doc/workbench/en/)

### 2. **Laravel Database**
- [Laravel Database: Getting Started](https://laravel.com/docs/database)
- [Laravel Migrations](https://laravel.com/docs/migrations)

### 3. **Security Best Practices**
- [MySQL Security Guidelines](https://dev.mysql.com/doc/refman/8.0/en/security-guidelines.html)
- [OWASP Database Security](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html)

---

**Lưu ý**: Thông tin này được lấy từ file `.env` của dự án Portal. Cần verify với hệ thống production trước khi sử dụng cho dự án van-ban.

**Ngày cập nhật**: 2026-02-23  
**Người cập nhật**: Bột (AI Assistant)  
**Nguồn**: `/root/.openclaw/workspace/portal/.env`