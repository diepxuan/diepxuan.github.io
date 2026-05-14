---
layout: home
title: Trang chủ
description: Cổng tài liệu Điệp Xuân cho văn bản pháp luật, tài liệu nội bộ và ghi chú kỹ thuật.
---

<section class="hero">
  <span class="badge">docs.diepxuan.com</span>
  <h1>Cổng tài liệu tập trung cho vận hành và pháp luật</h1>
  <p>Tra cứu văn bản pháp luật, tài liệu công ty, ghi chú kỹ thuật và backlog luật mới trong một giao diện gọn, rõ, dễ mở rộng.</p>
  <div class="hero-actions">
    <a class="button button-primary" href="{{ '/van-ban/' | relative_url }}">Tra cứu văn bản pháp luật</a>
    <a class="button button-secondary" href="{{ '/documents/LEGISLATION_TRACKING' | relative_url }}">Xem luật mới đang theo dõi</a>
  </div>
</section>

<section class="grid grid-4" aria-label="Thống kê nhanh">
  <div class="stat"><strong>45</strong><span>Chủ đề pháp luật</span></div>
  <div class="stat"><strong>306</strong><span>Đề mục chuyên sâu</span></div>
  <div class="stat"><strong>76k+</strong><span>Điều khoản tham khảo</span></div>
  <div class="stat"><strong>GitHub</strong><span>Host bằng GitHub Pages</span></div>
</section>

<section style="margin-top: 2rem;" class="grid grid-2">
  <article class="card">
    <span class="badge">Pháp luật</span>
    <h2>Văn bản pháp luật</h2>
    <p>Danh mục văn bản được tổ chức theo chủ đề, đề mục và nội dung chi tiết. Phù hợp để tra cứu nhanh, đối chiếu nguồn và theo dõi phần còn thiếu cần cập nhật.</p>
    <a class="button button-secondary" style="color: var(--primary); border-color: var(--border);" href="{{ '/van-ban/' | relative_url }}">Mở danh mục pháp luật</a>
  </article>

  <article class="card">
    <span class="badge">Tracking</span>
    <h2>Theo dõi luật mới</h2>
    <p>Backlog các văn bản mới phát hiện từ nguồn chính thức, dùng cho heartbeat và các đợt cập nhật nội dung tiếp theo.</p>
    <a class="button button-secondary" style="color: var(--primary); border-color: var(--border);" href="{{ '/documents/LEGISLATION_TRACKING' | relative_url }}">Mở backlog luật mới</a>
  </article>

  <article class="card">
    <span class="badge">Nội bộ</span>
    <h2>Tài liệu công ty</h2>
    <p>Khu vực lưu tài liệu, báo cáo và file vận hành nội bộ được quản lý bằng Git để có lịch sử thay đổi rõ ràng.</p>
    <a class="button button-secondary" style="color: var(--primary); border-color: var(--border);" href="{{ '/documents/' | relative_url }}">Xem tài liệu</a>
  </article>

  <article class="card">
    <span class="badge">Kỹ thuật</span>
    <h2>Tin kỹ thuật</h2>
    <p>Ghi chú hệ thống, mạng, máy chủ, cập nhật Windows, MikroTik, Proxmox và các hướng dẫn kỹ thuật phục vụ vận hành.</p>
    <a class="button button-secondary" style="color: var(--primary); border-color: var(--border);" href="{{ '/news/' | relative_url }}">Xem tin kỹ thuật</a>
  </article>
</section>

<section style="margin-top: 2rem;" class="content-shell">
  <div class="content">
    <h2>Hướng phát triển</h2>
    <div class="grid grid-3">
      <div>
        <h3>Giao diện tài liệu</h3>
        <p>Layout đọc dài, bảng metadata, điều hướng nhanh và typography phù hợp văn bản pháp luật.</p>
      </div>
      <div>
        <h3>Tìm kiếm</h3>
        <p>Chuẩn bị nền cho search index theo tiêu đề, số hiệu, lĩnh vực và nội dung trích yếu.</p>
      </div>
      <div>
        <h3>Hỏi đáp pháp luật</h3>
        <p>Thiết kế không khóa đường mở rộng sang RAG/backend riêng, bắt buộc có trích dẫn nguồn khi triển khai.</p>
      </div>
    </div>
  </div>
</section>
