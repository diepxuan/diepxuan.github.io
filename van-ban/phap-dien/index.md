---
layout: default
title: Bộ Pháp điển Điện tử
permalink: /van-ban/phap-dien/
---

# 📚 Bộ Pháp điển Điện tử

**Nguồn:** Bộ Tư pháp Việt Nam  
**Cập nhật:** {{ site.time | date: "%Y-%m-%d" }}  
**Phiên bản:** 1.0

## 📊 Tổng quan

Bộ Pháp điển Điện tử là hệ thống pháp luật chính thức của Việt Nam, được Bộ Tư pháp công bố. Hệ thống này bao gồm toàn bộ các văn bản pháp luật được hệ thống hóa theo cấu trúc phân cấp rõ ràng.

### Thống kê
- **45 Chủ đề** pháp luật
- **271 Đề mục** chuyên sâu  
- **76,303 Điều khoản** (chương, điều, khoản, điểm)
- **Cập nhật** theo quy định pháp luật

## 🔍 Tra cứu

### 1. Theo Chủ đề
Xem danh sách đầy đủ 45 chủ đề pháp luật:

👉 [Danh sách 45 Chủ đề](markdown/00-danh-sach-chu-de.md)

### 2. Theo Đề mục
Truy cập trực tiếp các đề mục quan trọng:

{% assign important_demuc = "Đất đai, Doanh nghiệp, Đầu tư, Thuế, Lao động, Hình sự, Dân sự, Hành chính, Tố tụng" | split: ", " %}
{% for demuc in important_demuc %}
- [{{ demuc }}](markdown/) - *Đang cập nhật*
{% endfor %}

👉 [Xem tất cả 271 Đề mục](markdown/README.md)

### 3. Tìm kiếm
Sử dụng chức năng tìm kiếm của GitHub/GitLab để tìm kiếm nhanh.

## 📁 Cấu trúc Dữ liệu

### Database Formats
Dữ liệu được lưu trữ dưới nhiều định dạng:

| Định dạng | Mục đích | Đường dẫn |
|-----------|----------|-----------|
| **SQLite** | Query nhanh, full-text search | `sqlite/phapdien.db` |
| **Markdown** | Hiển thị web, documentation | `markdown/*.md` |
| **JSON** | API, mobile apps | `database/json/*.json` |
| **Search Index** | Tìm kiếm keywords | `database/search/keywords.json` |

### Cấu trúc Phân cấp
```
Chủ đề (45)
  ├── Đề mục (271)
  │     ├── Chương (I, II, III...)
  │     │     ├── Điều (1, 2, 3...)
  │     │     │     ├── Khoản (1.1, 1.2...)
  │     │     │     │     └── Điểm (1.1.1, 1.1.2...)
```

## 🛠 Công cụ & Scripts

### Build Script
Toàn bộ dữ liệu được tự động build từ nguồn gốc:

```bash
cd scripts/
python3 build_database.py
```

### Các Script có sẵn
- `build_database.py` - Build toàn bộ database
- `phapdien_crawler.py` - Crawler gốc
- `extract_phapdien.py` - Trích xuất dữ liệu
- `analyze_structure.py` - Phân tích cấu trúc

## 📈 45 Chủ đề Pháp luật

1. **An ninh quốc gia**
2. **Bảo hiểm**
3. **Bổ trợ tư pháp**
4. **Bưu chính, viễn thông**
5. **Cán bộ, công chức, viên chức**
6. **Chính sách xã hội**
7. **Công nghiệp**
8. **Dân số, gia đình, trẻ em, bình đẳng giới**
9. **Dân sự**
10. **Doanh nghiệp, hợp tác xã**
11. **Giáo dục, đào tạo**
12. **Giao thông, vận tải**
13. **Hành chính tư pháp**
14. **Hình sự**
15. **Kế toán, kiểm toán**
16. **Khiếu nại, tố cáo**
17. **Khoa học, công nghệ**
18. **Lao động**
19. **Môi trường**
20. **Ngân hàng, tiền tệ**
21. **Ngoại giao, điều ước quốc tế**
22. **Nông nghiệp, nông thôn**
23. **Quốc phòng**
24. **Tài chính**
25. **Tài nguyên**
26. **Tài sản công, nợ công, dự trữ nhà nước**
27. **Thi hành án**
28. **Thống kê**
29. **Thông tin, báo chí, xuất bản**
30. **Thuế, phí, lệ phí, các khoản thu khác**
31. **Thương mại, đầu tư, chứng khoán**
32. **Tổ chức bộ máy nhà nước**
33. **Tổ chức chính trị - xã hội, hội**
34. **Tố tụng và các phương thức giải quyết tranh chấp**
35. **Tôn giáo, tín ngưỡng**
36. **Trật tự, an toàn xã hội**
37. **Tương trợ tư pháp**
38. **Văn hóa, thể thao, du lịch**
39. **Văn thư lưu trữ**
40. **Xây dựng pháp luật và thi hành pháp luật**
41. **Xây dựng, nhà ở, đô thị**
42. **Y tế, dược**

👉 [Xem đầy đủ với số đề mục](markdown/00-danh-sach-chu-de.md)

## 🚀 Sử dụng Dữ liệu

### 1. Query SQLite
```sql
-- Tìm các điều khoản về "đất đai"
SELECT * FROM dieukhoan 
WHERE ten LIKE '%đất đai%' 
LIMIT 10;

-- Đếm số điều khoản theo chủ đề
SELECT c.ten, COUNT(d.id) as so_dieu_khoan
FROM chude c
LEFT JOIN dieukhoan d ON c.id = d.chude_id
GROUP BY c.id
ORDER BY so_dieu_khoan DESC;
```

### 2. Đọc Markdown
Mỗi đề mục được xuất ra file Markdown riêng với cấu trúc phân cấp đầy đủ.

### 3. API JSON
```javascript
// Đọc danh sách chủ đề
fetch('/van-ban/phap-dien/database/json/chude.json')
  .then(response => response.json())
  .then(data => console.log(data));
```

## 📝 Quy trình Cập nhật

1. **Download** phiên bản mới từ Bộ Tư pháp
2. **Copy** file `jsonData.js` vào thư mục `json/`
3. **Chạy build script**:
   ```bash
   cd scripts/
   python3 build_database.py
   ```
4. **Commit & Push** thay đổi lên Git
5. **GitHub Pages** tự động deploy

## ⚖️ Lưu ý Pháp lý

- Dữ liệu được trích xuất từ **Bộ Pháp điển Điện tử chính thức**
- Chỉ sử dụng cho mục đích **tham khảo, nghiên cứu**
- **Không thay thế** văn bản pháp luật chính thức
- Luôn **kiểm tra** với nguồn chính thức khi áp dụng

## 📞 Liên hệ & Hỗ trợ

- **Vấn đề kỹ thuật**: Mở issue trên GitHub
- **Cập nhật dữ liệu**: Theo dõi Bộ Tư pháp
- **Đề xuất tính năng**: Gửi pull request

## 🔗 Liên kết

- [Bộ Pháp điển Điện tử](https://phapdien.moj.gov.vn/) - Nguồn chính thức
- [GitHub Repository](https://github.com/diepxuan/github-io) - Mã nguồn
- [Website chính](https://docs.diepxuan.com/) - Trang chủ

---

*Trang này được tạo tự động từ dữ liệu Pháp điển. Cập nhật lần cuối: {{ site.time | date: "%Y-%m-%d %H:%M" }}*