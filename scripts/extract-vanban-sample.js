#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// Đường dẫn đến file jsonData.js
const jsonDataPath = path.join(__dirname, '..', 'van-ban', 'crawled', 'BoPhapDienDienTu', 'jsonData.js');

console.log('🔍 Extracting sample data from van-ban file...');
console.log(`📁 File: ${jsonDataPath}`);

// Đọc file với stream để xử lý file lớn
const readStream = fs.createReadStream(jsonDataPath, { encoding: 'utf8' });

let buffer = '';
let inVanBan = false;
let braceCount = 0;
let vanBanData = '';
let sampleCount = 0;
const maxSamples = 10;

readStream.on('data', (chunk) => {
  buffer += chunk;
  
  // Tìm biến jdVanBan
  if (!inVanBan && buffer.includes('var jdVanBan = [')) {
    inVanBan = true;
    const startIndex = buffer.indexOf('var jdVanBan = [');
    buffer = buffer.substring(startIndex);
    braceCount = 1; // Đã có 1 dấu [
  }
  
  if (inVanBan) {
    // Đếm dấu ngoặc để xác định khi nào kết thúc mảng
    for (const char of buffer) {
      if (char === '[') braceCount++;
      if (char === ']') braceCount--;
      
      vanBanData += char;
      
      if (braceCount === 0) {
        // Đã tìm thấy kết thúc mảng
        inVanBan = false;
        break;
      }
    }
    
    // Nếu đã có đủ dữ liệu mẫu, dừng lại
    if (sampleCount >= maxSamples && vanBanData.includes('},')) {
      // Tìm vị trí của mẫu thứ maxSamples
      const samples = vanBanData.match(/\{[^}]*\}/g);
      if (samples && samples.length >= maxSamples) {
        vanBanData = '[' + samples.slice(0, maxSamples).join(',') + ']';
        inVanBan = false;
        readStream.destroy(); // Dừng đọc stream
      }
    }
    
    buffer = '';
  }
});

readStream.on('close', () => {
  if (vanBanData) {
    try {
      // Clean up dữ liệu
      vanBanData = vanBanData.trim();
      if (!vanBanData.startsWith('[')) {
        vanBanData = '[' + vanBanData;
      }
      if (!vanBanData.endsWith(']')) {
        vanBanData = vanBanData + ']';
      }
      
      const parsedData = JSON.parse(vanBanData);
      console.log(`✅ Extracted ${parsedData.length} sample van-ban records`);
      
      // Lưu sample data
      const samplePath = path.join(__dirname, '..', 'van-ban', 'crawled', 'vanban-sample.json');
      fs.writeFileSync(samplePath, JSON.stringify(parsedData, null, 2), 'utf8');
      console.log(`💾 Saved sample to: ${samplePath}`);
      
      // Phân tích cấu trúc
      console.log('\n📊 VAN-BAN DATA STRUCTURE ANALYSIS:');
      if (parsedData.length > 0) {
        const sample = parsedData[0];
        console.log('\n📦 Sample record structure:');
        console.log(JSON.stringify(sample, null, 2));
        
        console.log('\n🔑 Fields analysis:');
        const fields = Object.keys(sample);
        console.log(`Total fields: ${fields.length}`);
        console.log('Field list:', fields.join(', '));
        
        console.log('\n📝 Field types and sample values:');
        fields.forEach(field => {
          const value = sample[field];
          const type = typeof value;
          const truncated = typeof value === 'string' ? 
            (value.length > 100 ? value.substring(0, 100) + '...' : value) :
            JSON.stringify(value).substring(0, 100);
          console.log(`  - ${field}: ${type} = ${truncated}`);
        });
        
        // Phân tích các trường quan trọng
        console.log('\n🎯 IMPORTANT FIELDS IDENTIFIED:');
        const importantFields = [
          'SoHieu', 'TrichYeu', 'NgayBanHanh', 'NgayCoHieuLuc', 'NgayHetHieuLuc',
          'CoQuanBanHanh', 'LoaiVanBan', 'NguoiKy', 'ChucVuNguoiKy', 'FileDinhKem',
          'ID', 'MaLoaiVanBan', 'MaCoQuan', 'MaLinhVuc', 'DeMuc'
        ];
        
        importantFields.forEach(field => {
          if (sample[field] !== undefined) {
            console.log(`  - ${field}: ${JSON.stringify(sample[field]).substring(0, 100)}`);
          }
        });
        
        // Kiểm tra quan hệ với đề mục
        if (sample.DeMuc) {
          console.log(`\n🔗 RELATIONSHIP WITH DeMuc: ${JSON.stringify(sample.DeMuc)}`);
        }
      }
      
      // Thống kê
      console.log('\n📈 STATISTICS:');
      console.log(`Total sample records: ${parsedData.length}`);
      
      // Đếm các trường phổ biến
      const fieldCounts = {};
      parsedData.forEach(record => {
        Object.keys(record).forEach(field => {
          fieldCounts[field] = (fieldCounts[field] || 0) + 1;
        });
      });
      
      console.log('\n📊 Field presence in samples:');
      Object.entries(fieldCounts)
        .sort((a, b) => b[1] - a[1])
        .forEach(([field, count]) => {
          const percentage = ((count / parsedData.length) * 100).toFixed(1);
          console.log(`  - ${field}: ${count}/${parsedData.length} (${percentage}%)`);
        });
        
    } catch (error) {
      console.error('❌ Error parsing van-ban data:', error.message);
      console.log('Raw data (first 500 chars):', vanBanData.substring(0, 500));
    }
  } else {
    console.log('❌ Could not extract jdVanBan data from file');
  }
});

readStream.on('error', (error) => {
  console.error('❌ Error reading file:', error.message);
});