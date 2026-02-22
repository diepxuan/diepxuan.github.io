#!/usr/bin/env python3
"""
Tạo hệ thống single-page cho van-ban
Chỉ cần 1 file HTML chính, xử lý routing bằng JavaScript
"""

import os
import json
import sqlite3

def create_single_page_system():
    """Tạo hệ thống single-page với 1 file HTML chính"""
    base_dir = '/root/.openclaw/workspace/projects/github-io/van-ban'
    
    print("=== TẠO HỆ THỐNG SINGLE-PAGE ===")
    
    # 1. Tạo data.json từ database
    db_path = os.path.join(base_dir, 'phap-dien', 'sqlite', 'phapdien_complete.db')
    
    print("1. Đọc dữ liệu từ database...")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Lấy dữ liệu chủ đề
    cursor.execute('SELECT id, text, stt FROM chude ORDER BY stt')
    chude_list = []
    for chude_id, chude_text, stt in cursor.fetchall():
        # Lấy đề mục thuộc chủ đề này
        cursor.execute('''
            SELECT DISTINCT d.id, d.text, d.stt
            FROM demuc d
            JOIN dieukhoan dk ON d.id = dk.demuc_id
            WHERE dk.chude_id = ?
            ORDER BY d.stt
        ''', (chude_id,))
        
        demuc_items = []
        for demuc_id, demuc_text, demuc_stt in cursor.fetchall():
            # Lấy điều khoản thuộc đề mục này
            cursor.execute('''
                SELECT id, mapc, chimuc, ten
                FROM dieukhoan
                WHERE demuc_id = ?
                ORDER BY mapc
            ''', (demuc_id,))
            
            dieukhoan_items = []
            for dk_id, mapc, chimuc, ten in cursor.fetchall():
                dieukhoan_items.append({
                    'id': dk_id,
                    'mapc': mapc,
                    'chimuc': chimuc,
                    'ten': ten
                })
            
            demuc_items.append({
                'id': demuc_id,
                'text': demuc_text,
                'stt': demuc_stt,
                'dieukhoan': dieukhoan_items,
                'count': len(dieukhoan_items)
            })
        
        chude_list.append({
            'id': chude_id,
            'text': chude_text,
            'stt': stt,
            'demuc': demuc_items,
            'count': len(demuc_items)
        })
    
    conn.close()
    
    # 2. Tạo data.json
    data = {
        'chude': chude_list,
        'total_chude': len(chude_list),
        'total_demuc': sum(len(c['demuc']) for c in chude_list),
        'total_dieukhoan': sum(sum(d['count'] for d in c['demuc']) for c in chude_list)
    }
    
    data_file = os.path.join(base_dir, 'data.json')
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Đã tạo data.json: {len(chude_list)} chủ đề, {data['total_demuc']} đề mục, {data['total_dieukhoan']} điều khoản")
    
    # 3. Tạo index.html chính
    index_html = os.path.join(base_dir, 'index.html')
    
    html_content = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bộ Pháp điển Điện tử</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background: linear-gradient(135deg, #1a237e, #283593);
            color: white;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }
        
        .stat-card {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #1a237e;
            display: block;
        }
        
        .stat-label {
            color: #666;
            font-size: 0.9rem;
        }
        
        .breadcrumb {
            background: #f5f5f5;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .breadcrumb a {
            color: #1a237e;
            text-decoration: none;
        }
        
        .breadcrumb a:hover {
            text-decoration: underline;
        }
        
        .breadcrumb-separator {
            color: #999;
        }
        
        .content {
            min-height: 400px;
        }
        
        /* Chủ đề list */
        .chude-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1rem;
        }
        
        .chude-card {
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 1.5rem;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            color: inherit;
            display: block;
        }
        
        .chude-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            border-color: #1a237e;
        }
        
        .chude-title {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: #1a237e;
        }
        
        .chude-meta {
            font-size: 0.9rem;
            color: #666;
        }
        
        /* Đề mục list */
        .demuc-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1rem;
        }
        
        .demuc-card {
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 1.5rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .demuc-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            border-color: #1a237e;
        }
        
        .demuc-title {
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: #1a237e;
        }
        
        .demuc-meta {
            font-size: 0.9rem;
            color: #666;
        }
        
        /* Điều khoản list */
        .dieukhoan-list {
            background: white;
            border-radius: 8px;
            border: 1px solid #e0e0e0;
            overflow: hidden;
        }
        
        .dieukhoan-item {
            padding: 1.5rem;
            border-bottom: 1px solid #eee;
        }
        
        .dieukhoan-item:last-child {
            border-bottom: none;
        }
        
        .dieukhoan-title {
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: #333;
        }
        
        .dieukhoan-meta {
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 0.5rem;
        }
        
        .dieukhoan-id {
            font-family: monospace;
            font-size: 0.8rem;
            color: #999;
            background: #f5f5f5;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            display: inline-block;
        }
        
        .back-button {
            background: #f5f5f5;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.9rem;
            margin-bottom: 1rem;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .back-button:hover {
            background: #e0e0e0;
        }
        
        .loading {
            text-align: center;
            padding: 3rem;
            color: #666;
        }
        
        .error {
            background: #ffebee;
            color: #c62828;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        
        footer {
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #e0e0e0;
            text-align: center;
            color: #666;
            font-size: 0.9rem;
        }
        
        @media (max-width: 768px) {
            .chude-list,
            .demuc-list {
                grid-template-columns: 1fr;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            .stats {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>📚 Bộ Pháp điển Điện tử</h1>
        <div class="subtitle">Hệ thống pháp luật chính thức của Việt Nam - Bộ Tư pháp</div>
    </header>
    
    <div class="stats" id="stats">
        <!-- Stats sẽ được cập nhật bằng JavaScript -->
    </div>
    
    <div class="breadcrumb" id="breadcrumb">
        <a href="#" onclick="showHome()">Trang chủ</a>
    </div>
    
    <div class="content" id="content">
        <!-- Nội dung sẽ được cập nhật bằng JavaScript -->
        <div class="loading">Đang tải dữ liệu...</div>
    </div>
    
    <footer>
        <p>Dữ liệu được trích xuất từ Bộ Pháp điển Điện tử chính thức của Bộ Tư pháp Việt Nam</p>
        <p>Chỉ sử dụng cho mục đích tham khảo, nghiên cứu</p>
        <p>© 2026 - docs.diepxuan.com</p>
    </footer>
    
    <script>
        // Biến toàn cục
        let data = null;
        let currentState = {
            view: 'home', // 'home', 'chude', 'demuc'
            chudeId: null,
            demucId: null
        };
        
        // Tải dữ liệu
        async function loadData() {
            try {
                const response = await fetch('data.json');
                data = await response.json();
                renderHome();
                updateStats();
            } catch (error) {
                document.getElementById('content').innerHTML = `
                    <div class="error">
                        <h3>Lỗi tải dữ liệu</h3>
                        <p>Không thể tải dữ liệu từ server. Vui lòng thử lại sau.</p>
                        <button onclick="loadData()" class="back-button">Thử lại</button>
                    </div>
                `;
                console.error('Lỗi tải dữ liệu:', error);
            }
        }
        
        // Cập nhật thống kê
        function updateStats() {
            if (!data) return;
            
            document.getElementById('stats').innerHTML = `
                <div class="stat-card">
                    <span class="stat-number">${data.total_chude}</span>
                    <span class="stat-label">Chủ đề pháp luật</span>
                </div>
                <div class="stat-card">
                    <span class="stat-number">${data.total_demuc}</span>
                    <span class="stat-label">Đề mục chuyên sâu</span>
                </div>
                <div class="stat-card">
                    <span class="stat-number">${data.total_dieukhoan.toLocaleString()}</span>
                    <span class="stat-label">Điều khoản pháp luật</span>
                </div>
            `;
        }
        
        // Hiển thị trang chủ
        function showHome() {
            currentState = { view: 'home', chudeId: null, demucId: null };
            updateUrl();
            renderHome();
        }
        
        function renderHome() {
            if (!data) return;
            
            let html = '<h2>Danh sách Chủ đề Pháp luật</h2>';
            html += '<div class="chude-list">';
            
            data.chude.forEach(chude => {
                const demucCount = chude.demuc.length;
                const dieukhoanCount = chude.demuc.reduce((sum, d) => sum + d.count, 0);
                
                html += `
                    <div class="chude-card" onclick="showChude('${chude.id}')">
                        <div class="chude-title">${chude.text}</div>
                        <div class="chude-meta">
                            ${demucCount} đề mục • ${dieukhoanCount.toLocaleString()} điều khoản
                        </div>
                    </div>
                `;
            });
            
            html += '</div>';
            document.getElementById('content').innerHTML = html;
            updateBreadcrumb();
        }
        
        // Hiển thị chủ đề
        function showChude(chudeId) {
            const chude = data.chude.find(c => c.id === chudeId);
            if (!chude) return;
            
            currentState = { view: 'chude', chudeId: chudeId, demucId: null };
            updateUrl();
            
            let html = `<button class="back-button" onclick="showHome()">← Quay lại danh sách chủ đề</button>`;
            html += `<h2>${chude.text}</h2>`;
            html += `<p class="chude-meta">${chude.demuc.length} đề mục</p>`;
            html += '<div class="demuc-list">';
            
            chude.demuc.forEach(demuc => {
                html += `
                    <div class="demuc-card" onclick="showDemuc('${chude.id}', '${demuc.id}')">
                        <div class="demuc-title">${demuc.text}</div>
                        <div class="demuc-meta">${demuc.count.toLocaleString()} điều khoản</div>
                    </div>
                `;
            });
            
            html += '</div>';
            document.getElementById('content').innerHTML = html;
            updateBreadcrumb();
        }
        
        // Hiển thị đề mục
        function showDemuc(chudeId, demucId) {
            const chude = data.chude.find(c => c.id === chudeId);
            if (!chude) return;
            
            const demuc = chude.demuc.find(d => d.id === demucId);
            if (!demuc) return;
            
            currentState = { view: 'demuc', chudeId: chudeId, demucId: demucId };
            updateUrl();
            
            let html = `<button class="back-button" onclick="showChude('${chudeId}')">← Quay lại ${chude.text}</button>`;
            html += `<h2>${demuc.text}</h2>`;
            html += `<p class="demuc-meta">${demuc.count.toLocaleString()} điều khoản • Chủ đề: ${chude.text}</p>`;
            html += '<div class="die