# THÔNG TIN KẾT NỐI MYSQL - VAN-BAN PROJECT

## ✅ VERIFICATION STATUS (2026-02-23)
- **✅ User `vbpl`**: TỒN TẠI và có thể kết nối
- **✅ Database `vbpl`**: TỒN TẠI và user có ALL PRIVILEGES
- **✅ Connection**: Hoạt động hoàn toàn
- **✅ Server**: MariaDB 10.11.11

## 🔗 QUICK CONNECTION INFO

### Option 1: Laravel User (Existing)
```bash
# Connection command
mysql -h mysql.diepxuan.corp -P 3306 -u laravel -p laravel

# Password: d72a5c40fc31c537deb8917fa192873a
```

### Option 2: VBPL User (Van-Ban Specific) - **VERIFIED**
```bash
# Connection command với user vbpl và database vbpl
mysql -h mysql.diepxuan.corp -P 3306 -u vbpl -p'G]9E9S_TahIFVbq-' vbpl

# Hoặc connect rồi chọn database
mysql -h mysql.diepxuan.corp -u vbpl -p'G]9E9S_TahIFVbq-'
# Sau đó: USE vbpl;

# Test connection
mysql -h mysql.diepxuan.corp -u vbpl -p'G]9E9S_TahIFVbq-' -e "SELECT 'VBPL Connected' AS status;"
```

## 📋 ENVIRONMENT VARIABLES

### Laravel User (Existing)
```env
DB_CONNECTION=mysql
DB_HOST=mysql.diepxuan.corp
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=laravel
DB_PASSWORD=d72a5c40fc31c537deb8917fa192873a
```

### VBPL User (Van-Ban Specific) - **VERIFIED**
```env
DB_CONNECTION=mysql
DB_HOST=mysql.diepxuan.corp
DB_PORT=3306
DB_DATABASE=vbpl          # ✅ Database name: vbpl
DB_USERNAME=vbpl          # ✅ Username: vbpl
DB_PASSWORD=G]9E9S_TahIFVbq-  # ✅ Password verified
```

## 🌐 HOST INFORMATION

### **Primary Host**: `mysql.diepxuan.corp`
- **Type**: Internal corporate MySQL server
- **Port**: 3306 (default MySQL port)
- **Network**: Corporate internal network
- **Access**: Requires internal network access or VPN

### **DNS/Network Configuration**
```bash
# Test host resolution
nslookup mysql.diepxuan.corp
ping mysql.diepxuan.corp

# Test port accessibility
nc -zv mysql.diepxuan.corp 3306
telnet mysql.diepxuan.corp 3306
```

## 🚀 QUICK START

### 1. **Test connection**
```bash
mysql -h mysql.diepxuan.corp -u laravel -p -e "SELECT 'Connected successfully' AS status;"
```

### 2. **Check database**
```bash
mysql -h mysql.diepxuan.corp -u laravel -p -e "SHOW DATABASES;"
```

### 3. **Check tables**
```bash
mysql -h mysql.diepxuan.corp -u laravel -p laravel -e "SHOW TABLES;"
```

## 📊 DATABASE STATUS

- **Server**: `mysql.diepxuan.corp:3306`
- **Database**: `laravel` (existing Laravel app database)
- **User**: `laravel` với full access
- **Source**: Portal project `.env` file

## 🛠 USAGE FOR VAN-BAN

### Option 1: Use existing `laravel` database
- **Pros**: Đã có sẵn, không cần setup
- **Cons**: Chia sẻ với Portal app

### Option 2: Create new database
```sql
CREATE DATABASE vanban_db;
CREATE USER 'vanban_user'@'%' IDENTIFIED BY 'new_password';
GRANT ALL PRIVILEGES ON vanban_db.* TO 'vanban_user'@'%';
FLUSH PRIVILEGES;
```

## 📞 TROUBLESHOOTING

### Common issues:
1. **Connection refused**: Check firewall/network
2. **Access denied**: Verify username/password
3. **Unknown database**: Database might not exist

### Test steps:
```bash
# 1. Test network connectivity
ping mysql.diepxuan.corp

# 2. Test port accessibility
nc -zv mysql.diepxuan.corp 3306

# 3. Test MySQL service
mysqladmin -h mysql.diepxuan.corp -u laravel -p ping
```

---

**Full documentation**: Xem `docs/MYSQL_DATABASE_VANBAN.md`  
**Source**: Portal project `.env` file  
**Last updated**: 2026-02-23