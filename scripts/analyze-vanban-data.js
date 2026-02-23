#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// Đường dẫn đến file jsonData.js
const jsonDataPath = path.join(__dirname, '..', 'van-ban', 'crawled', 'BoPhapDienDienTu', 'jsonData.js');

console.log('📊 Phân tích cấu trúc dữ liệu van-ban...');
console.log(`📁 File: ${jsonDataPath}`);

// Đọc file
const content = fs.readFileSync(jsonDataPath, 'utf8');

// Tìm các biến JavaScript trong file
const variables = {
  jdChuDe: null,
  jdDeMuc: null,
  jdVanBan: null,
  jdCoQuan: null,
  jdLinhVuc: null,
  jdLoaiVanBan: null,
  jdNguoiKy: null
};

// Trích xuất từng biến từ file
const lines = content.split('\n');
let currentVar = null;
let currentData = '';

for (const line of lines) {
  // Tìm khai báo biến
  for (const varName in variables) {
    if (line.includes(`var ${varName} = `)) {
      if (currentVar) {
        // Lưu dữ liệu biến trước đó
        try {
          variables[currentVar] = JSON.parse(currentData);
        } catch (e) {
          console.log(`⚠️ Không parse được ${currentVar}: ${e.message}`);
        }
      }
      currentVar = varName;
      currentData = line.split('=')[1].trim();
      break;
    }
  }
  
  if (currentVar && !line.includes('var ') && !line.includes('];')) {
    currentData += line;
  }
  
  if (currentVar && line.includes('];')) {
    currentData += line;
    try {
      variables[currentVar] = JSON.parse(currentData);
    } catch (e) {
      console.log(`⚠️ Không parse được ${currentVar}: ${e.message}`);
    }
    currentVar = null;
    currentData = '';
  }
}

// Kiểm tra biến cuối cùng
if (currentVar && currentData) {
  try {
    variables[currentVar] = JSON.parse(currentData);
  } catch (e) {
    console.log(`⚠️ Không parse được ${currentVar}: ${e.message}`);
  }
}

// Phân tích từng biến
console.log('\n📈 THỐNG KÊ DỮ LIỆU:');
for (const [varName, data] of Object.entries(variables)) {
  if (data && Array.isArray(data)) {
    console.log(`\n📦 ${varName}:`);
    console.log(`   Số lượng: ${data.length} items`);
    
    if (data.length > 0) {
      console.log(`   Mẫu dữ liệu đầu tiên:`);
      console.log(JSON.stringify(data[0], null, 2));
      
      // Phân tích cấu trúc
      const sample = data[0];
      console.log(`   Cấu trúc fields: ${Object.keys(sample).join(', ')}`);
      
      // Thống kê kiểu dữ liệu
      const fieldTypes = {};
      for (const key in sample) {
        const value = sample[key];
        fieldTypes[key] = typeof value === 'string' ? 'string' : 
                         typeof value === 'number' ? 'number' :
                         typeof value === 'boolean' ? 'boolean' :
                         Array.isArray(value) ? 'array' : 'object';
      }
      console.log(`   Kiểu dữ liệu:`, fieldTypes);
    }
  } else if (data) {
    console.log(`\n📦 ${varName}:`);
    console.log(`   Kiểu: ${typeof data}`);
    console.log(`   Mẫu: ${JSON.stringify(data).substring(0, 200)}...`);
  } else {
    console.log(`\n📦 ${varName}: Không tìm thấy hoặc không parse được`);
  }
}

// Tạo báo cáo chi tiết
console.log('\n📋 BÁO CÁO CHI TIẾT:');

// 1. Chủ đề (ChuDe)
if (variables.jdChuDe) {
  console.log(`\n1. CHỦ ĐỀ (ChuDe): ${variables.jdChuDe.length} chủ đề`);
  console.log('   Danh sách 10 chủ đề đầu tiên:');
  variables.jdChuDe.slice(0, 10).forEach((item, index) => {
    console.log(`   ${index + 1}. ${item.Text} (${item.Value}) - STT: ${item.STT}`);
  });
}

// 2. Đề mục (DeMuc)
if (variables.jdDeMuc) {
  console.log(`\n2. ĐỀ MỤC (DeMuc): ${variables.jdDeMuc.length} đề mục`);
  console.log('   Mối quan hệ với Chủ đề:');
  const deMucByChuDe = {};
  variables.jdDeMuc.forEach(item => {
    if (!deMucByChuDe[item.ChuDe]) {
      deMucByChuDe[item.ChuDe] = 0;
    }
    deMucByChuDe[item.ChuDe]++;
  });
  console.log(`   - Có ${Object.keys(deMucByChuDe).length} chủ đề có đề mục`);
  
  // Tìm chủ đề tương ứng
  if (variables.jdChuDe) {
    const chuDeMap = {};
    variables.jdChuDe.forEach(item => {
      chuDeMap[item.Value] = item.Text;
    });
    
    console.log('   Ví dụ đề mục theo chủ đề:');
    const sampleDeMuc = variables.jdDeMuc.slice(0, 5);
    sampleDeMuc.forEach((item, index) => {
      const chuDeName = chuDeMap[item.ChuDe] || 'Không xác định';
      console.log(`   ${index + 1}. ${item.Text} (Chủ đề: ${chuDeName})`);
    });
  }
}

// 3. Văn bản (VanBan) - có thể rất lớn
if (variables.jdVanBan) {
  console.log(`\n3. VĂN BẢN (VanBan): ${variables.jdVanBan.length} văn bản`);
  console.log('   Cấu trúc mẫu:');
  const sampleVanBan = variables.jdVanBan[0];
  console.log(JSON.stringify(sampleVanBan, null, 2));
  
  // Phân tích các trường quan trọng
  const importantFields = ['SoHieu', 'TrichYeu', 'NgayBanHanh', 'CoQuanBanHanh', 'LoaiVanBan'];
  console.log('   Các trường quan trọng:');
  importantFields.forEach(field => {
    if (sampleVanBan[field]) {
      console.log(`   - ${field}: ${sampleVanBan[field]}`);
    }
  });
}

// 4. Cơ quan (CoQuan)
if (variables.jdCoQuan) {
  console.log(`\n4. CƠ QUAN (CoQuan): ${variables.jdCoQuan.length} cơ quan`);
  console.log('   Danh sách 10 cơ quan đầu tiên:');
  variables.jdCoQuan.slice(0, 10).forEach((item, index) => {
    console.log(`   ${index + 1}. ${item.TenCoQuan} (${item.MaCoQuan})`);
  });
}

// 5. Lĩnh vực (LinhVuc)
if (variables.jdLinhVuc) {
  console.log(`\n5. LĨNH VỰC (LinhVuc): ${variables.jdLinhVuc.length} lĩnh vực`);
  console.log('   Danh sách 10 lĩnh vực đầu tiên:');
  variables.jdLinhVuc.slice(0, 10).forEach((item, index) => {
    console.log(`   ${index + 1}. ${item.TenLinhVuc} (${item.MaLinhVuc})`);
  });
}

// 6. Loại văn bản (LoaiVanBan)
if (variables.jdLoaiVanBan) {
  console.log(`\n6. LOẠI VĂN BẢN (LoaiVanBan): ${variables.jdLoaiVanBan.length} loại`);
  console.log('   Danh sách tất cả loại văn bản:');
  variables.jdLoaiVanBan.forEach((item, index) => {
    console.log(`   ${index + 1}. ${item.TenLoaiVanBan} (${item.MaLoaiVanBan})`);
  });
}

// 7. Người ký (NguoiKy)
if (variables.jdNguoiKy) {
  console.log(`\n7. NGƯỜI KÝ (NguoiKy): ${variables.jdNguoiKy.length} người`);
  console.log('   Danh sách 10 người ký đầu tiên:');
  variables.jdNguoiKy.slice(0, 10).forEach((item, index) => {
    console.log(`   ${index + 1}. ${item.HoTen} (${item.ChucVu})`);
  });
}

// Tạo đề xuất schema database
console.log('\n🗄️ ĐỀ XUẤT SCHEMA DATABASE:');

console.log(`
1. Bảng chu_de (Chủ đề)
   - id (UUID/VARCHAR) - PK
   - ten_chu_de (VARCHAR)
   - stt (INT)

2. Bảng de_muc (Đề mục)
   - id (UUID/VARCHAR) - PK
   - ten_de_muc (VARCHAR)
   - chu_de_id (UUID/VARCHAR) - FK
   - stt (INT)

3. Bảng co_quan (Cơ quan)
   - ma_co_quan (VARCHAR) - PK
   - ten_co_quan (VARCHAR)

4. Bảng loai_van_ban (Loại văn bản)
   - ma_loai_van_ban (VARCHAR) - PK
   - ten_loai_van_ban (VARCHAR)

5. Bảng van_ban (Văn bản)
   - id (VARCHAR) - PK
   - so_hieu (VARCHAR)
   - trich_yeu (TEXT)
   - ngay_ban_hanh (DATE)
   - ngay_co_hieu_luc (DATE)
   - ngay_het_hieu_luc (DATE)
   - co_quan_ban_hanh_id (VARCHAR) - FK
   - loai_van_ban_id (VARCHAR) - FK
   - nguoi_ky (VARCHAR)
   - chuc_vu_nguoi_ky (VARCHAR)
   - file_path (VARCHAR)
   - de_muc_id (UUID/VARCHAR) - FK
   - created_at (TIMESTAMP)
   - updated_at (TIMESTAMP)

6. Bảng van_ban_noi_dung (Nội dung văn bản)
   - id (INT) - PK, AUTO_INCREMENT
   - van_ban_id (VARCHAR) - FK
   - noi_dung (LONGTEXT)
   - created_at (TIMESTAMP)

7. Bảng van_ban_de_muc (Quan hệ nhiều-nhiều giữa văn bản và đề mục)
   - van_ban_id (VARCHAR) - FK
   - de_muc_id (UUID/VARCHAR) - FK
   - PRIMARY KEY (van_ban_id, de_muc_id)
`);

console.log('\n✅ Phân tích hoàn thành!');