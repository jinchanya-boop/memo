import sys

css_content = """
<style>
  :root {
    --pink-50: #fdf2f8; --pink-100: #fce7f3; --pink-200: #fbcfe8;
    --pink-300: #f9a8d4; --pink-400: #f472b6; --pink-500: #ec4899; --pink-600: #db2777;
    --blue-50: #eff6ff; --blue-100: #dbeafe; --blue-200: #bfdbfe;
    --blue-300: #93c5fd; --blue-400: #60a5fa; --blue-500: #3b82f6; --blue-600: #2563eb;
    --purple-100: #ede9fe; --purple-400: #a78bfa; --purple-600: #7c3aed;
    --rose-100: #ffe4e6; --emerald-100: #d1fae5; --emerald-600: #059669;
    --amber-100: #fef3c7; --amber-600: #d97706;
    --gray-50: #f9fafb; --gray-100: #f3f4f6; --gray-200: #e5e7eb; --gray-300: #d1d5db;
    --gray-400: #9ca3af; --gray-500: #6b7280; --gray-600: #4b5563;
    --gray-700: #374151; --gray-800: #1f2937; --gray-900: #111827;
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
    --shadow: 0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.06);
    --shadow-lg: 0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05);
    --shadow-xl: 0 20px 25px rgba(0,0,0,0.1), 0 10px 10px rgba(0,0,0,0.04);
    --radius: 12px; --radius-lg: 16px; --radius-xl: 20px;
  }
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  body {
    font-family: 'Sarabun', sans-serif;
    background: linear-gradient(135deg, #fdf2f8 0%, #eff6ff 50%, #fce7f3 100%);
    min-height: 100vh; color: var(--gray-800); font-size: 15px; line-height: 1.6;
  }

  /* ─── NAV ─── */
  .navbar {
    background: rgba(255,255,255,0.85); backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(236,72,153,0.12);
    position: sticky; top: 0; z-index: 100; padding: 0 24px;
  }
  .nav-inner {
    max-width: 1200px; margin: 0 auto;
    display: flex; align-items: center; justify-content: space-between; height: 64px;
  }
  .nav-brand { display: flex; align-items: center; gap: 10px; cursor: pointer; transition: transform 0.2s;}
  .nav-brand:hover { transform: scale(1.02); }
  .nav-icon {
    width: 40px; height: 40px;
    background: linear-gradient(135deg, var(--pink-400), var(--blue-400));
    border-radius: 10px; display: flex; align-items: center; justify-content: center;
    font-size: 20px; box-shadow: 0 4px 12px rgba(236,72,153,0.3);
  }
  .nav-title { font-family: 'Kanit', sans-serif; font-weight: 600; font-size: 16px; color: var(--gray-800); }
  .nav-sub { font-size: 12px; color: var(--gray-500); }
  .nav-tabs { display: flex; gap: 4px; }
  .nav-tab {
    padding: 8px 16px; border-radius: 8px; border: none; cursor: pointer;
    font-family: 'Sarabun', sans-serif; font-size: 14px; font-weight: 500;
    transition: all 0.2s; background: transparent; color: var(--gray-600);
  }
  .nav-tab:hover { background: var(--pink-50); color: var(--pink-600); }
  .nav-tab.active { background: linear-gradient(135deg, var(--pink-500), var(--blue-500)); color: white; box-shadow: 0 2px 8px rgba(236,72,153,0.3); }

  /* ─── LAYOUT ─── */
  .view-container { display: none; animation: fadeIn 0.3s ease; }
  .view-container.active { display: block; }
  .page { display: none; animation: fadeIn 0.3s ease; }
  .page.active { display: block; }
  @keyframes fadeIn { from { opacity:0; transform: translateY(8px); } to { opacity:1; transform:none; } }
  .container { max-width: 1200px; margin: 0 auto; padding: 32px 24px; }

  /* ─── HERO ─── */
  .hero { text-align: center; padding: 48px 24px 32px; position: relative; }
  .hero-badge {
    display: inline-flex; align-items: center; gap: 6px;
    background: var(--pink-100); color: var(--pink-600);
    padding: 6px 14px; border-radius: 999px; font-size: 13px; font-weight: 600; margin-bottom: 16px;
  }
  .hero-title {
    font-family: 'Kanit', sans-serif; font-weight: 700; font-size: 32px;
    background: linear-gradient(135deg, var(--pink-600), var(--blue-600));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 8px;
  }
  .hero-sub { color: var(--gray-500); font-size: 15px; }

  /* ─── HOME MENU CARDS ─── */
  .home-menu-grid {
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1000px; margin: 0 auto; padding: 20px 0;
  }
  .home-menu-card {
    background: rgba(255,255,255,0.9); backdrop-filter: blur(12px);
    border-radius: var(--radius-xl); border: 1px solid rgba(255,255,255,0.8);
    box-shadow: var(--shadow-lg); padding: 32px 24px; text-align: center;
    transition: all 0.3s cubic-bezier(0.34,1.56,0.64,1); cursor: pointer;
    display: flex; flex-direction: column; align-items: center; height: 100%;
  }
  .home-menu-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: var(--shadow-xl);
    border-color: var(--pink-300);
  }
  .home-menu-icon {
    font-size: 48px; margin-bottom: 20px;
    width: 80px; height: 80px; border-radius: 20px;
    display: flex; align-items: center; justify-content: center;
  }
  .home-menu-title {
    font-family: 'Kanit', sans-serif; font-weight: 700; font-size: 20px;
    color: var(--gray-800); margin-bottom: 12px;
  }
  .home-menu-desc {
    font-size: 14px; color: var(--gray-500); margin-bottom: 24px; flex-grow: 1;
  }

  /* ─── CARD ─── */
  .card {
    background: rgba(255,255,255,0.9); backdrop-filter: blur(12px);
    border-radius: var(--radius-xl); border: 1px solid rgba(255,255,255,0.8);
    box-shadow: var(--shadow-lg); padding: 28px; transition: transform 0.2s, box-shadow 0.2s;
  }
  .card:hover { transform: translateY(-1px); box-shadow: var(--shadow-xl); }
  .card-title {
    font-family: 'Kanit', sans-serif; font-weight: 600; font-size: 17px;
    color: var(--gray-800); margin-bottom: 20px;
    display: flex; align-items: center; gap: 8px;
    padding-bottom: 12px; border-bottom: 2px solid var(--pink-100);
  }

  /* ─── FORM ─── */
  .form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
  .form-full { grid-column: 1 / -1; }
  .form-group { display: flex; flex-direction: column; gap: 6px; }
  .form-label { font-size: 13px; font-weight: 600; color: var(--gray-700); }
  .form-label .req { color: var(--pink-500); margin-left: 2px; }
  .form-input, .form-select, .form-textarea {
    padding: 11px 14px; border-radius: 10px; border: 1.5px solid var(--gray-200);
    background: white; font-family: 'Sarabun', sans-serif; font-size: 14px;
    color: var(--gray-800); transition: all 0.2s; outline: none; width: 100%;
  }
  .form-input:focus, .form-select:focus, .form-textarea:focus {
    border-color: var(--pink-400); box-shadow: 0 0 0 3px rgba(236,72,153,0.1);
  }
  .form-textarea { resize: vertical; min-height: 80px; }

  /* ─── BUTTONS ─── */
  .btn {
    display: inline-flex; align-items: center; gap: 8px;
    padding: 11px 22px; border-radius: 10px; border: none; cursor: pointer;
    font-family: 'Sarabun', sans-serif; font-size: 14px; font-weight: 600;
    transition: all 0.2s; white-space: nowrap;
  }
  .btn-primary { background: linear-gradient(135deg, var(--pink-500), var(--blue-500)); color: white; box-shadow: 0 4px 14px rgba(236,72,153,0.35); }
  .btn-primary:hover { transform: translateY(-1px); box-shadow: 0 6px 20px rgba(236,72,153,0.45); }
  .btn-secondary { background: white; color: var(--gray-700); border: 1.5px solid var(--gray-200); box-shadow: var(--shadow-sm); }
  .btn-secondary:hover { border-color: var(--pink-300); color: var(--pink-600); }
  .btn-success { background: linear-gradient(135deg, #10b981, #059669); color: white; box-shadow: 0 4px 14px rgba(16,185,129,0.3); }
  .btn-info { background: linear-gradient(135deg, var(--blue-400), var(--blue-600)); color: white; box-shadow: 0 4px 14px rgba(59,130,246,0.3); }
  .btn-home { background: linear-gradient(135deg, var(--gray-700), var(--gray-900)); color: white; }
  .btn-sm { padding: 7px 14px; font-size: 13px; border-radius: 8px; }
  .btn-lg { padding: 14px 28px; font-size: 16px; border-radius: 12px; }
  .btn-row { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 24px; }

  /* ─── STATS ─── */
  .stats-row { display: grid !important; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 28px; }
  .stat-card {
    background: rgba(255,255,255,0.9); backdrop-filter: blur(12px);
    border-radius: var(--radius-lg); padding: 20px;
    border: 1px solid rgba(255,255,255,0.8); box-shadow: var(--shadow-md);
    display: flex; align-items: center; gap: 14px;
  }
  .stat-icon { width: 46px; height: 46px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; }
  .stat-icon.pink { background: var(--pink-100); }
  .stat-icon.blue { background: var(--blue-100); }
  .stat-icon.purple { background: var(--purple-100); }
  .stat-icon.emerald { background: var(--emerald-100); }
  .stat-num { font-family: 'Kanit', sans-serif; font-size: 26px; font-weight: 700; color: var(--gray-800); line-height: 1; }
  .stat-label { font-size: 12px; color: var(--gray-500); margin-top: 2px; }

  /* ─── TABLE ─── */
  .table-wrap { overflow-x: auto; border-radius: 12px; }
  table { width: 100%; border-collapse: collapse; font-size: 14px; }
  thead tr { background: linear-gradient(135deg, var(--pink-50), var(--blue-50)); }
  thead th { padding: 12px 14px; text-align: left; font-weight: 600; color: var(--gray-700); font-size: 13px; border-bottom: 2px solid var(--gray-200); }
  tbody tr { border-bottom: 1px solid var(--gray-100); transition: background 0.15s; }
  tbody tr:hover { background: var(--pink-50); }
  tbody td { padding: 12px 14px; color: var(--gray-700); }
  .empty-state { text-align: center; padding: 48px; color: var(--gray-400); }

  /* ─── COMPONENTS ─── */
  .badge { display: inline-flex; align-items: center; gap: 4px; padding: 4px 10px; border-radius: 999px; font-size: 12px; font-weight: 600; }
  .badge-วช { background: var(--blue-100); color: var(--blue-600); }
  .badge-บค { background: var(--pink-100); color: var(--pink-600); }
  .badge-งบ { background: var(--amber-100); color: var(--amber-600); }
  .badge-บท { background: var(--emerald-100); color: var(--emerald-600); }
  .badge-order { background: var(--purple-100); color: var(--purple-600); }
  .badge-book { background: var(--emerald-100); color: var(--emerald-600); }

  .bg-orb { position: fixed; border-radius: 50%; filter: blur(80px); pointer-events: none; z-index: -1; }
  .bg-orb-1 { width: 400px; height: 400px; background: rgba(236,72,153,0.08); top: -100px; right: -100px; }
  .bg-orb-2 { width: 350px; height: 350px; background: rgba(59,130,246,0.08); bottom: -80px; left: -80px; }

  /* ─── OVERLAYS ─── */
  .loading-overlay, .overlay {
    position: fixed; inset: 0; z-index: 300; background: rgba(255,255,255,0.85); backdrop-filter: blur(8px);
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    opacity: 0; pointer-events: none; transition: opacity 0.2s;
  }
  .loading-overlay.show, .overlay.show { opacity: 1; pointer-events: all; }
  .spinner { width: 52px; height: 52px; border-radius: 50%; border: 4px solid var(--gray-200); border-top-color: var(--pink-500); animation: spin 0.8s linear infinite; margin-bottom: 16px; }
  @keyframes spin { to { transform: rotate(360deg); } }

  .popup { background: white; border-radius: var(--radius-xl); padding: 40px 36px; max-width: 440px; width: 90%; text-align: center; box-shadow: var(--shadow-xl); transform: scale(0.85) translateY(20px); transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1); }
  .overlay.show .popup { transform: none; }

  .toast-area { position: fixed; top: 80px; right: 24px; z-index: 400; display: flex; flex-direction: column; gap: 8px; }
  .toast { background: white; border-radius: 12px; padding: 14px 18px; box-shadow: var(--shadow-xl); min-width: 260px; display: flex; align-items: center; gap: 12px; transform: translateX(120%); transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1); border-left: 4px solid var(--pink-500); }
  .toast.show { transform: none; }
  .toast.success { border-left-color: var(--emerald-600); }
  .toast.error { border-left-color: #ef4444; }

  @media (max-width: 767px) {
    .home-menu-grid { grid-template-columns: 1fr; }
    .form-grid { grid-template-columns: 1fr; }
    .stats-row { grid-template-columns: 1fr 1fr !important; }
  }
  
  /* RESULT INFO GRID */
  .result-hero { text-align: center; padding: 40px 24px; background: linear-gradient(135deg, rgba(236,72,153,0.06), rgba(59,130,246,0.06)); border-radius: var(--radius-xl); margin-bottom: 24px; }
  .result-num { font-family: 'Kanit', sans-serif; font-size: 52px; font-weight: 800; background: linear-gradient(135deg, var(--pink-500), var(--blue-600)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1; margin: 16px 0 8px; }
  .info-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin: 20px 0; }
  .info-row { background: var(--gray-50); border-radius: 10px; padding: 12px 16px; }
  .info-row-label { font-size: 12px; color: var(--gray-500); font-weight: 600; margin-bottom: 2px; }
  .info-row-val { font-size: 14px; color: var(--gray-800); font-weight: 500; }
</style>
"""

with open("generate_html.py", "w", encoding="utf-8") as f:
    f.write(f'''
import os

css_content = """{css_content}"""

html_shell = """<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ระบบสารบรรณอิเล็กทรอนิกส์ โรงเรียนสา</title>
<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700;800&family=Kanit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
""" + css_content + """
</head>
<body>
<div class="bg-orb bg-orb-1"></div>
<div class="bg-orb bg-orb-2"></div>

<div class="loading-overlay" id="loadingOverlay">
  <div class="spinner"></div>
  <div class="loading-text" id="loadingText">กำลังประมวลผล...</div>
</div>

<div class="toast-area" id="toastArea"></div>

<!-- Success Popup -->
<div class="overlay" id="successOverlay">
  <div class="popup">
    <span class="popup-icon" style="font-size: 40px; margin-bottom: 10px; display: block;">🎉</span>
    <div class="popup-title">บันทึกสำเร็จ!</div>
    <div style="color:var(--gray-500);font-size:13px;margin-bottom:8px;">หมายเลขของคุณคือ</div>
    <div style="font-family:'Kanit',sans-serif;font-size:36px;font-weight:800;background:linear-gradient(135deg,var(--pink-500),var(--blue-600));-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:14px 0;" id="popupNum">—</div>
    <div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:20px;">
      <button class="btn btn-secondary" onclick="document.getElementById('successOverlay').classList.remove('show');">ปิด</button>
    </div>
  </div>
</div>

<!-- NAVBAR -->
<nav class="navbar">
  <div class="nav-inner">
    <div class="nav-brand" onclick="switchView('home')">
      <div class="nav-icon" style="padding:0;overflow:hidden;">
        <img src="https://img2.pic.in.th/pic/sa1.png" style="width:100%;height:100%;object-fit:cover;border-radius:10px;">
      </div>
      <div>
        <div class="nav-title">ระบบสารบรรณอิเล็กทรอนิกส์</div>
        <div class="nav-sub">โรงเรียนสา จ.น่าน</div>
      </div>
    </div>
    <div class="nav-tabs" id="navTabsContainer">
        <!-- Tabs will be injected dynamically -->
    </div>
  </div>
</nav>

<!-- ================= VIEWS ================= -->
<div id="view-home" class="view-container active">
  <div class="container">
    <div class="hero">
      <div class="hero-badge">🏛️ ระบบสารบรรณอิเล็กทรอนิกส์ โรงเรียนสา</div>
      <h1 class="hero-title">ระบบขอเลขที่เอกสารราชการออนไลน์</h1>
      <p class="hero-sub">เลือกประเภทเอกสารที่ต้องการทำรายการด้านล่าง</p>
    </div>
    
    <div class="home-menu-grid">
      <div class="home-menu-card" onclick="switchView('memo')">
        <div class="home-menu-icon" style="background:var(--pink-100);color:var(--pink-600);">📋</div>
        <div class="home-menu-title">ขอเลขที่บันทึกข้อความ</div>
        <div class="home-menu-desc">สำหรับออกเลขที่บันทึกข้อความภายในโรงเรียน</div>
        <button class="btn btn-primary">เข้าสู่ระบบ</button>
      </div>
      <div class="home-menu-card" onclick="switchView('order')">
        <div class="home-menu-icon" style="background:var(--purple-100);color:var(--purple-600);">📑</div>
        <div class="home-menu-title">ขอเลขที่คำสั่งโรงเรียนสา</div>
        <div class="home-menu-desc">สำหรับออกเลขที่คำสั่งของโรงเรียน</div>
        <button class="btn btn-primary" style="background:linear-gradient(135deg,var(--purple-400),var(--purple-600));">เข้าสู่ระบบ</button>
      </div>
      <div class="home-menu-card" onclick="switchView('book')">
        <div class="home-menu-icon" style="background:var(--emerald-100);color:var(--emerald-600);">📤</div>
        <div class="home-menu-title">ขอเลขหนังสือออกโรงเรียนสา</div>
        <div class="home-menu-desc">สำหรับออกเลขหนังสือราชการส่งออกภายนอก</div>
        <button class="btn btn-primary" style="background:linear-gradient(135deg,#10b981,#059669);">เข้าสู่ระบบ</button>
      </div>
    </div>
    
    <div style="text-align:center; margin-top: 40px;">
        <button class="btn btn-secondary btn-lg" onclick="switchView('dashboard')">📊 ดูแดชบอร์ดสรุปรวมทั้งหมด</button>
    </div>
  </div>
</div>

<!-- ================= MEMO VIEW ================= -->
<div id="view-memo" class="view-container">
  <div class="container">
    <div class="hero">
      <div class="hero-badge">📋 ระบบออกเลขที่บันทึกข้อความ</div>
      <h1 class="hero-title">ขอเลขที่บันทึกข้อความ</h1>
    </div>
    <div style="max-width:760px;margin:0 auto;">
      <div class="card">
        <div class="card-title"><span>📝</span> แบบฟอร์มขอเลขที่บันทึกข้อความ</div>
        <div class="form-grid">
          <div class="form-group"><label class="form-label">ชื่อ-สกุล <span class="req">*</span></label><input class="form-input" id="memo-name" type="text" placeholder="นาย/นาง/นางสาว ชื่อ นามสกุล"></div>
          <div class="form-group"><label class="form-label">ตำแหน่ง <span class="req">*</span></label><input class="form-input" id="memo-position" type="text" placeholder="เช่น ครู, ผู้ช่วยผู้อำนวยการ"></div>
          <div class="form-group">
            <label class="form-label">ฝ่าย <span class="req">*</span></label>
            <select class="form-select" id="memo-dept">
              <option value="">-- เลือกฝ่าย --</option>
              <option value="ฝ่ายวิชาการ">ฝ่ายวิชาการ</option>
              <option value="ฝ่ายบุคคล">ฝ่ายบุคคล</option>
              <option value="ฝ่ายงบประมาณ">ฝ่ายงบประมาณ</option>
              <option value="ฝ่ายบริหารทั่วไป">ฝ่ายบริหารทั่วไป</option>
            </select>
          </div>
          <div class="form-group"><label class="form-label">วันที่ <span class="req">*</span></label><input class="form-input" id="memo-date" type="date"></div>
          <div class="form-group form-full"><label class="form-label">เรื่อง <span class="req">*</span></label><input class="form-input" id="memo-subject" type="text" placeholder="เรื่องของบันทึกข้อความ"></div>
          <div class="form-group form-full"><label class="form-label">รายละเอียดเพิ่มเติม</label><textarea class="form-textarea" id="memo-desc" placeholder="รายละเอียดหรือหมายเหตุเพิ่มเติม (ถ้ามี)"></textarea></div>
        </div>
        <div class="btn-row">
          <button class="btn btn-primary btn-lg" onclick="appContext.memo.submit()">✨ ขอเลขที่บันทึกข้อความ</button>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ================= ORDER VIEW ================= -->
<div id="view-order" class="view-container">
  <div class="container">
    <div class="hero">
      <div class="hero-badge" style="background:var(--purple-100);color:var(--purple-600);">📑 ระบบคำสั่งโรงเรียน</div>
      <h1 class="hero-title" style="background:linear-gradient(135deg,var(--purple-400),var(--purple-600));-webkit-background-clip:text;">ขอเลขที่คำสั่งโรงเรียนสา</h1>
    </div>
    <div style="max-width:760px;margin:0 auto;">
      <div class="card">
        <div class="card-title"><span>📝</span> แบบฟอร์มขอเลขที่คำสั่ง</div>
        <div class="form-grid">
          <div class="form-group"><label class="form-label">ชื่อ-สกุลผู้ขอ <span class="req">*</span></label><input class="form-input" id="order-name" type="text" placeholder="ชื่อ-สกุล"></div>
          <div class="form-group"><label class="form-label">ตำแหน่ง <span class="req">*</span></label><input class="form-input" id="order-position" type="text" placeholder="ตำแหน่ง"></div>
          <div class="form-group"><label class="form-label">วันที่ <span class="req">*</span></label><input class="form-input" id="order-date" type="date"></div>
          <div class="form-group form-full"><label class="form-label">เรื่องคำสั่ง <span class="req">*</span></label><input class="form-input" id="order-subject" type="text" placeholder="เรื่องของคำสั่ง"></div>
          <div class="form-group form-full"><label class="form-label">รายละเอียดเพิ่มเติม</label><textarea class="form-textarea" id="order-desc" placeholder="หมายเหตุ (ถ้ามี)"></textarea></div>
        </div>
        <div class="btn-row">
          <button class="btn btn-primary btn-lg" style="background:linear-gradient(135deg,var(--purple-400),var(--purple-600));" onclick="appContext.order.submit()">✨ ขอเลขที่คำสั่ง</button>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ================= BOOK VIEW ================= -->
<div id="view-book" class="view-container">
  <div class="container">
    <div class="hero">
      <div class="hero-badge" style="background:var(--emerald-100);color:var(--emerald-600);">📤 ระบบหนังสือออก</div>
      <h1 class="hero-title" style="background:linear-gradient(135deg,#10b981,#059669);-webkit-background-clip:text;">ขอเลขหนังสือออกโรงเรียนสา</h1>
    </div>
    <div style="max-width:760px;margin:0 auto;">
      <div class="card">
        <div class="card-title"><span>📝</span> แบบฟอร์มขอเลขหนังสือออก</div>
        <div class="form-grid">
          <div class="form-group"><label class="form-label">ชื่อ-สกุลผู้ส่ง <span class="req">*</span></label><input class="form-input" id="book-name" type="text" placeholder="ชื่อ-สกุล"></div>
          <div class="form-group"><label class="form-label">ตำแหน่ง <span class="req">*</span></label><input class="form-input" id="book-position" type="text" placeholder="ตำแหน่ง"></div>
          <div class="form-group form-full"><label class="form-label">เรื่อง <span class="req">*</span></label><input class="form-input" id="book-subject" type="text" placeholder="เรื่อง"></div>
          <div class="form-group"><label class="form-label">เรียน (ผู้รับ) <span class="req">*</span></label><input class="form-input" id="book-destination" type="text" placeholder="ชื่อหรือหน่วยงานผู้รับ"></div>
          <div class="form-group"><label class="form-label">วันที่ <span class="req">*</span></label><input class="form-input" id="book-date" type="date"></div>
          <div class="form-group form-full"><label class="form-label">รายละเอียดเพิ่มเติม</label><textarea class="form-textarea" id="book-desc" placeholder="หมายเหตุ (ถ้ามี)"></textarea></div>
        </div>
        <div class="btn-row">
          <button class="btn btn-primary btn-lg" style="background:linear-gradient(135deg,#10b981,#059669);" onclick="appContext.book.submit()">✨ ขอเลขหนังสือออก</button>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ================= GLOBAL DASHBOARD ================= -->
<div id="view-dashboard" class="view-container">
  <div class="container">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 24px;">
        <h2 class="hero-title" style="font-size: 28px; margin:0;">📊 แดชบอร์ดสรุปรวม</h2>
        <button class="btn btn-info" onclick="generateReportPDF()">📄 สร้างรายงาน PDF (แก้ไขปัญหาระยะตัดคำแล้ว)</button>
    </div>
    <div class="stats-row" id="globalStats">
      <div class="stat-card"><div class="stat-icon pink">📋</div><div><div class="stat-num" id="stat-total-memos">0</div><div class="stat-label">บันทึกข้อความ</div></div></div>
      <div class="stat-card"><div class="stat-icon purple">📑</div><div><div class="stat-num" id="stat-total-orders">0</div><div class="stat-label">คำสั่งโรงเรียน</div></div></div>
      <div class="stat-card"><div class="stat-icon emerald">📤</div><div><div class="stat-num" id="stat-total-books">0</div><div class="stat-label">หนังสือออก</div></div></div>
      <div class="stat-card"><div class="stat-icon blue">📦</div><div><div class="stat-num" id="stat-total-all">0</div><div class="stat-label">รวมเอกสารทั้งหมด</div></div></div>
    </div>
    
    <div class="card">
        <div class="card-title">📝 รายการล่าสุด (ทุกประเภท)</div>
        <div class="table-wrap">
            <table>
                <thead>
                    <tr><th>ประเภท</th><th>เลขที่</th><th>เรื่อง</th><th>ผู้ขอ</th><th>วันที่</th></tr>
                </thead>
                <tbody id="globalRecentTableBody"></tbody>
            </table>
        </div>
    </div>
  </div>
</div>

<script src="js/api.js"></script>
<script src="js/app.js"></script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_shell)

js_api = """
let GAS_URL = localStorage.getItem('gasUrl') || 'https://script.google.com/macros/s/AKfycbye4PrDSh7fuUyDc6aHQMxF9kHa6zNnvuHOMHwB9k-pwBF0DJ6P42OUd_rh39AhMnzX/exec';

function normalizeDateField(val) {
  if (!val) return '';
  const s = String(val).trim();
  if (/^\\\\d{4}-\\\\d{2}-\\\\d{2}$/.test(s)) return s;
  const d = new Date(s);
  if (!isNaN(d.getTime())) {
    return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
  }
  return s;
}

async function syncFromSheets(actionStr, lsKey) {
  if (!GAS_URL) return null;
  return new Promise((resolve) => {
    const cbName = 'gasCallback_' + Date.now() + Math.floor(Math.random() * 1000);
    const timeout = setTimeout(() => {
      delete window[cbName];
      const el = document.getElementById('gas-jsonp-' + cbName);
      if (el) el.remove();
      resolve(null);
    }, 10000);
    
    window[cbName] = function(json) {
      clearTimeout(timeout);
      delete window[cbName];
      const el = document.getElementById('gas-jsonp-' + cbName);
      if (el) el.remove();
      try {
        if (json.status === 'ok' && Array.isArray(json.data)) {
          const normalized = json.data.map(r => ({ ...r, date: normalizeDateField(r.date), id: String(r.id) }));
          localStorage.setItem(lsKey, JSON.stringify(normalized));
          if (json.startConfig) localStorage.setItem('startConfig', JSON.stringify(json.startConfig));
          resolve(normalized);
        } else { resolve(null); }
      } catch(e) { resolve(null); }
    };
    const script = document.createElement('script');
    script.id = 'gas-jsonp-' + cbName;
    script.src = GAS_URL + '?action=' + actionStr + '&callback=' + cbName;
    script.onerror = () => { clearTimeout(timeout); resolve(null); };
    document.head.appendChild(script);
  });
}

async function pushToSheets(actionStr, record) {
  if (!GAS_URL) return;
  try {
    const startConfig = JSON.parse(localStorage.getItem('startConfig') || '{}');
    await fetch(GAS_URL, { method:'POST', mode:'no-cors', body: JSON.stringify({ action: actionStr, record, startConfig }), headers:{'Content-Type':'text/plain'} });
  } catch(e) {
    console.warn("Failed to push to sheets", e);
  }
}

function showLoading(msg='กำลังประมวลผล...') {
  document.getElementById('loadingText').textContent = msg;
  document.getElementById('loadingOverlay').classList.add('show');
}
function hideLoading() {
  document.getElementById('loadingOverlay').classList.remove('show');
}

function showToast(msg, type='info') {
  const area = document.getElementById('toastArea');
  if(!area) return;
  const t = document.createElement('div');
  const icons = { success:'✅', error:'❌', info:'ℹ️' };
  t.className = `toast ${type}`;
  t.innerHTML = `<span class="toast-icon">${icons[type]||'ℹ️'}</span><span class="toast-msg">${msg}</span>`;
  area.appendChild(t);
  requestAnimationFrame(() => requestAnimationFrame(() => t.classList.add('show')));
  setTimeout(() => { t.classList.remove('show'); setTimeout(() => t.remove(), 400); }, 3000);
}

function getThaiBE(dateStr) {
  const d = dateStr ? new Date(dateStr) : new Date();
  return d.getFullYear() + 543;
}

function formatThaiDate(dateStr) {
  const months = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม'];
  const d = new Date(dateStr);
  if (isNaN(d.getTime())) return dateStr;
  return `${d.getDate()} ${months[d.getMonth()]} ${d.getFullYear() + 543}`;
}
"""

if not os.path.exists('js'):
    os.makedirs('js')

with open("js/api.js", "w", encoding="utf-8") as f:
    f.write(js_api)

js_app = """
// State
const appContext = {
    currentView: 'home',
    data: {
        memo: [],
        order: [],
        book: []
    }
};

function loadAllData() {
    try { appContext.data.memo = JSON.parse(localStorage.getItem('memoData') || '[]'); } catch {}
    try { appContext.data.order = JSON.parse(localStorage.getItem('orderData') || '[]'); } catch {}
    try { appContext.data.book = JSON.parse(localStorage.getItem('bookData') || '[]'); } catch {}
}

function getStartConfig(key) {
    try {
        const all = JSON.parse(localStorage.getItem('startConfig') || '{}');
        return all[key] !== undefined ? parseInt(all[key]) : 0;
    } catch { return 0; }
}

function switchView(viewName) {
    document.querySelectorAll('.view-container').forEach(v => v.classList.remove('active'));
    document.getElementById('view-' + viewName).classList.add('active');
    appContext.currentView = viewName;
    
    // Update tabs
    const nav = document.getElementById('navTabsContainer');
    nav.innerHTML = '';
    
    if (viewName !== 'home') {
        nav.innerHTML += `<button class="nav-tab" onclick="switchView('home')">🏠 กลับหน้าหลัก</button>`;
    }
    
    if (viewName === 'dashboard') {
        loadAllData();
        updateDashboard();
    }
}

function updateDashboard() {
    const memos = appContext.data.memo.length;
    const orders = appContext.data.order.length;
    const books = appContext.data.book.length;
    
    document.getElementById('stat-total-memos').textContent = memos;
    document.getElementById('stat-total-orders').textContent = orders;
    document.getElementById('stat-total-books').textContent = books;
    document.getElementById('stat-total-all').textContent = memos + orders + books;
    
    // Combine and sort
    let all = [];
    appContext.data.memo.forEach(r => all.push({...r, type: 'บันทึกข้อความ', num: r.memoNum, badge: 'badge-วช'}));
    appContext.data.order.forEach(r => all.push({...r, type: 'คำสั่ง', num: r.orderNum, badge: 'badge-order'}));
    appContext.data.book.forEach(r => all.push({...r, type: 'หนังสือออก', num: r.bookNum, badge: 'badge-book'}));
    
    all.sort((a,b) => b.id - a.id);
    const tbody = document.getElementById('globalRecentTableBody');
    tbody.innerHTML = all.slice(0, 10).map(r => `
        <tr>
            <td><span class="badge ${r.badge}">${r.type}</span></td>
            <td><strong>${r.num}</strong></td>
            <td style="max-width: 250px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" title="${r.subject}">${r.subject}</td>
            <td>${r.name}</td>
            <td>${formatThaiDate(r.date)}</td>
        </tr>
    `).join('');
}

// Sub-modules
appContext.memo = {
    submit: async function() {
        const name = document.getElementById('memo-name').value;
        const position = document.getElementById('memo-position').value;
        const dept = document.getElementById('memo-dept').value;
        const date = document.getElementById('memo-date').value;
        const subject = document.getElementById('memo-subject').value;
        const desc = document.getElementById('memo-desc').value;
        
        if (!name || !position || !dept || !date || !subject) {
            showToast('กรุณากรอกข้อมูลให้ครบถ้วน', 'error'); return;
        }
        
        showLoading('กำลังออกเลขบันทึก...');
        
        const year = getThaiBE(date);
        const prefix = {'ฝ่ายวิชาการ':'วช', 'ฝ่ายบุคคล':'บค', 'ฝ่ายงบประมาณ':'งบ', 'ฝ่ายบริหารทั่วไป':'บท'}[dept];
        
        let maxNum = getStartConfig(dept + '_' + year);
        appContext.data.memo.forEach(r => {
            if (r.dept === dept && r.memoNum.includes('/' + year)) {
                const num = parseInt(r.memoNum.replace(prefix, '').split('/')[0]);
                if (num > maxNum) maxNum = num;
            }
        });
        
        const nextNum = maxNum + 1;
        const memoNum = `${prefix}${String(nextNum).padStart(3,'0')}/${year}`;
        const record = { id: Date.now(), memoNum, name, position, dept, subject, desc, date, timestamp: new Date().toLocaleString('th-TH') };
        
        appContext.data.memo.unshift(record);
        localStorage.setItem('memoData', JSON.stringify(appContext.data.memo));
        
        await pushToSheets('add', record);
        
        hideLoading();
        document.getElementById('popupNum').textContent = memoNum;
        document.getElementById('successOverlay').classList.add('show');
        
        ['memo-name','memo-position','memo-subject','memo-desc'].forEach(id => document.getElementById(id).value = '');
    }
};

appContext.order = {
    submit: async function() {
        const name = document.getElementById('order-name').value;
        const position = document.getElementById('order-position').value;
        const date = document.getElementById('order-date').value;
        const subject = document.getElementById('order-subject').value;
        const desc = document.getElementById('order-desc').value;
        
        if (!name || !position || !date || !subject) {
            showToast('กรุณากรอกข้อมูลให้ครบถ้วน', 'error'); return;
        }
        
        showLoading('กำลังออกเลขคำสั่ง...');
        
        const year = getThaiBE(date);
        let maxNum = getStartConfig('order_' + year);
        
        appContext.data.order.forEach(r => {
            if (r.orderNum.includes('/' + year)) {
                // คำสั่งโรงเรียนสา ที่ 001/2569
                const parts = r.orderNum.split(' ที่ ')[1].split('/');
                const num = parseInt(parts[0]);
                if (num > maxNum) maxNum = num;
            }
        });
        
        const nextNum = maxNum + 1;
        const orderNum = `คำสั่งโรงเรียนสา ที่ ${String(nextNum).padStart(3,'0')}/${year}`;
        const record = { id: Date.now(), orderNum, name, position, subject, desc, date, timestamp: new Date().toLocaleString('th-TH') };
        
        appContext.data.order.unshift(record);
        localStorage.setItem('orderData', JSON.stringify(appContext.data.order));
        
        await pushToSheets('addOrder', record);
        
        hideLoading();
        document.getElementById('popupNum').textContent = orderNum;
        document.getElementById('successOverlay').classList.add('show');
        
        ['order-name','order-position','order-subject','order-desc'].forEach(id => document.getElementById(id).value = '');
    }
};

appContext.book = {
    submit: async function() {
        const name = document.getElementById('book-name').value;
        const position = document.getElementById('book-position').value;
        const destination = document.getElementById('book-destination').value;
        const date = document.getElementById('book-date').value;
        const subject = document.getElementById('book-subject').value;
        const desc = document.getElementById('book-desc').value;
        
        if (!name || !position || !date || !subject || !destination) {
            showToast('กรุณากรอกข้อมูลให้ครบถ้วน', 'error'); return;
        }
        
        showLoading('กำลังออกเลขหนังสือ...');
        
        const year = getThaiBE(date);
        let maxNum = getStartConfig('book_' + year);
        
        appContext.data.book.forEach(r => {
            // ศธ 04269.31/001
            const parts = r.bookNum.split('/');
            if (parts.length > 1) {
                const num = parseInt(parts[1]);
                if (num > maxNum) maxNum = num;
            }
        });
        
        const nextNum = maxNum + 1;
        const bookNum = `ศธ 04269.31/${String(nextNum).padStart(3,'0')}`;
        const record = { id: Date.now(), bookNum, name, position, destination, subject, desc, date, timestamp: new Date().toLocaleString('th-TH') };
        
        appContext.data.book.unshift(record);
        localStorage.setItem('bookData', JSON.stringify(appContext.data.book));
        
        await pushToSheets('addBook', record);
        
        hideLoading();
        document.getElementById('popupNum').textContent = bookNum;
        document.getElementById('successOverlay').classList.add('show');
        
        ['book-name','book-position','book-destination','book-subject','book-desc'].forEach(id => document.getElementById(id).value = '');
    }
};

// Initial load
document.addEventListener('DOMContentLoaded', () => {
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('memo-date').value = today;
    document.getElementById('order-date').value = today;
    document.getElementById('book-date').value = today;
    
    showLoading('กำลังเชื่อมต่อฐานข้อมูล...');
    Promise.all([
        syncFromSheets('getAll', 'memoData'),
        syncFromSheets('getOrders', 'orderData'),
        syncFromSheets('getBooks', 'bookData')
    ]).then(() => {
        hideLoading();
        loadAllData();
    });
});

// Fix for PDF Text Wrapping requested by User
async function generateReportPDF() {
    showLoading('กำลังสร้างรายงาน PDF แบบไม่ตัดคำ...');
    
    // We will use jsPDF + html2canvas for robustness with Thai fonts
    // But we will ensure the subject column has word-wrap and no truncation
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF({ orientation:'portrait', unit:'mm', format:'a4' });
    
    let all = [];
    appContext.data.memo.forEach(r => all.push({...r, type: 'บันทึกข้อความ', num: r.memoNum}));
    appContext.data.order.forEach(r => all.push({...r, type: 'คำสั่ง', num: r.orderNum}));
    appContext.data.book.forEach(r => all.push({...r, type: 'หนังสือออก', num: r.bookNum}));
    all.sort((a,b) => b.id - a.id);
    
    if (all.length === 0) {
        hideLoading(); showToast('ไม่มีข้อมูล', 'error'); return;
    }
    
    // The key is to style the Subject TD to wrap properly and take 30% width
    const rowsHtml = all.map((r, i) => `
        <tr style="background:${i%2===0?'#f9f9ff':'white'};">
            <td style="padding:8px; font-size:12px; width:8%; text-align:center;">${i+1}</td>
            <td style="padding:8px; font-size:12px; width:15%; font-weight:bold;">${r.num}</td>
            <td style="padding:8px; font-size:12px; width:20%;">${r.name}</td>
            <td style="padding:8px; font-size:12px; width:15%; color:#6b7280;">${r.position}</td>
            <td style="padding:8px; font-size:12px; width:30%; word-wrap:break-word; white-space:normal; line-height:1.4;">${r.subject}</td>
            <td style="padding:8px; font-size:12px; width:12%; color:#6b7280;">${formatThaiDate(r.date)}</td>
        </tr>
    `).join('');
    
    const content = `
    <div style="width:794px; min-height:1123px; background:white; font-family:'Sarabun',sans-serif; padding:40px;">
        <h2 style="text-align:center; font-family:'Kanit',sans-serif; color:#ec4899; margin-bottom:20px;">รายงานรวมเอกสารทั้งหมด</h2>
        <table style="width:100%; border-collapse:collapse; table-layout:fixed;">
            <thead>
                <tr style="background:#ec4899; color:white;">
                    <th style="padding:8px; width:8%;">ลำดับ</th>
                    <th style="padding:8px; width:15%; text-align:left;">เลขที่</th>
                    <th style="padding:8px; width:20%; text-align:left;">ชื่อ-สกุล</th>
                    <th style="padding:8px; width:15%; text-align:left;">ตำแหน่ง</th>
                    <th style="padding:8px; width:30%; text-align:left;">เรื่อง</th>
                    <th style="padding:8px; width:12%; text-align:left;">วันที่</th>
                </tr>
            </thead>
            <tbody>
                ${rowsHtml}
            </tbody>
        </table>
    </div>
    `;
    
    const wrap = document.createElement('div');
    wrap.style.cssText = 'position:fixed; left:-9999px; top:0; width:794px; background:white; z-index:9999;';
    wrap.innerHTML = content; 
    document.body.appendChild(wrap);
    
    await new Promise(r => setTimeout(r, 500));
    
    const canvas = await html2canvas(wrap, { scale:2, useCORS:true, backgroundColor:'#ffffff' });
    document.body.removeChild(wrap);
    
    doc.addImage(canvas.toDataURL('image/jpeg', 0.95), 'JPEG', 0, 0, 210, 297);
    doc.save(`รายงานรวมเอกสาร_${new Date().getTime()}.pdf`);
    
    hideLoading();
    showToast('สร้าง PDF เรียบร้อย', 'success');
}
"""

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js_app)

print("HTML, JS, CSS structure generated successfully.")
'''
    )
