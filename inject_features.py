import re

# Read current index.html and app.js
with open("index.html", "r", encoding="utf-8") as f:
    current_html = f.read()
    
with open("js/app.js", "r", encoding="utf-8") as f:
    current_js = f.read()

# Read index_backup.html
with open("index_backup.html", "r", encoding="utf-8") as f:
    backup_html = f.read()

# --- EXTRACT HTML BLOCKS ---
# Extract Batch View
batch_match = re.search(r'<div class="page" id="page-batch">(.+?)<!-- ================= BATCH SCRIPT ================= -->', backup_html, re.DOTALL)
if batch_match:
    batch_html = '<div id="view-batch" class="view-container">\n' + batch_match.group(1).strip() + '\n</div>\n'
else:
    batch_match = re.search(r'<div class="page" id="page-batch">(.*?)<div class="page"', backup_html, re.DOTALL)
    batch_html = '<div id="view-batch" class="view-container">\n' + batch_match.group(1).strip() + '\n</div>\n' if batch_match else ""

# Extract Settings View
settings_match = re.search(r'<div class="page" id="page-settings">(.*?)</div>\s*</div>\s*</div>\s*</div>', backup_html, re.DOTALL)
settings_html = '<div id="view-settings" class="view-container">\n' + settings_match.group(1).strip() + '\n</div>\n</div>\n</div>\n' if settings_match else ""

# Extract Admin Overlays
admin_login_match = re.search(r'<div class="overlay" id="adminLoginOverlay">.*?</div>\s*</div>', backup_html, re.DOTALL)
admin_login_html = admin_login_match.group(0) if admin_login_match else ""

change_pwd_match = re.search(r'<div class="overlay" id="changePwdOverlay">.*?</div>\s*</div>', backup_html, re.DOTALL)
change_pwd_html = change_pwd_match.group(0) if change_pwd_match else ""

# --- INJECT HTML ---
# Insert overlays before <nav>
if "adminLoginOverlay" not in current_html:
    current_html = current_html.replace('<!-- NAVBAR -->', admin_login_html + '\n\n' + change_pwd_html + '\n\n<!-- NAVBAR -->')

# Insert views before scripts
if "view-batch" not in current_html:
    current_html = current_html.replace('<script src="js/api.js">', batch_html + '\n\n' + settings_html + '\n\n<script src="js/api.js">')


# --- EXTRACT JS ---
# Extract Admin Auth and Settings functions
js_match = re.search(r'// ══════════════════════════════════════════\s*// GAS URL\s*// ══════════════════════════════════════════(.*?)// ══════════════════════════════════════════\s*// NAVIGATION', backup_html, re.DOTALL)
js_settings = js_match.group(1) if js_match else ""

# Extract Batch functions
batch_js_match = re.search(r'function generateBatch\(\) \{.*?(?=</script>)', backup_html, re.DOTALL)
if not batch_js_match:
    batch_js_match = re.search(r'// ══════════════════════════════════════════\s*// BATCH\s*// ══════════════════════════════════════════(.*?)// ══════════════════════════════════════════\s*// PDF', backup_html, re.DOTALL)
js_batch = batch_js_match.group(1) if batch_js_match else ""


# --- INJECT JS ---
if "saveGasUrl" not in current_js:
    current_js += "\n\n/* ================= SETTINGS & ADMIN ================= */\n" + js_settings

if "generateBatch" not in current_js:
    current_js += "\n\n/* ================= BATCH MEMO ================= */\n" + js_batch

# Replace page- name references to view- names
current_js = current_js.replace("markTabActive('settings')", "")
current_js = current_js.replace("markTabActive('batch')", "")
current_js = current_js.replace("showPage('form')", "switchView('home')")
current_js = current_js.replace("document.getElementById('page-settings').classList.add('active')", "switchView('settings')")
current_js = current_js.replace("document.querySelectorAll('.page').forEach(p => p.classList.remove('active'))", "")

# Fix Navigation Menu to include Settings and Batch
nav_update = """
    if (viewName !== 'home') {
        nav.innerHTML += `<button class="nav-tab" onclick="switchView('home')">🏠 กลับหน้าหลัก</button>`;
    }
    if (viewName === 'home') {
        nav.innerHTML += `<button class="nav-tab" onclick="switchView('batch')">⚡ ขอเลขแบบกลุ่ม (บันทึกข้อความ)</button>`;
        nav.innerHTML += `<button class="nav-tab" onclick="openAdminLogin()">⚙️ ตั้งค่า</button>`;
    }
"""
if "⚡ ขอเลขแบบกลุ่ม" not in current_js:
    current_js = re.sub(r'if \(viewName !== \'home\'\) \{\s*nav\.innerHTML \+= `<button class="nav-tab" onclick="switchView\(\'home\'\)">🏠 กลับหน้าหลัก</button>`;\s*\}', nav_update, current_js)

# Fix openAdminLogin logic
current_js = current_js.replace("""function openAdminLogin() {
  if (isAdminLoggedIn()) {
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    document.getElementById('page-settings').classList.add('active');
    markTabActive('settings'); initSettingsPage(); return;
  }""", """function openAdminLogin() {
  if (isAdminLoggedIn()) {
    switchView('settings');
    initSettingsPage(); return;
  }""")

current_js = current_js.replace("""  if (input === getAdminPwd()) {
    sessionStorage.setItem('adminAuth', 'true'); closeAdminLogin();
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    document.getElementById('page-settings').classList.add('active');
    markTabActive('settings'); initSettingsPage();
    showToast('เข้าสู่ระบบสำเร็จ', 'success');
  }""", """  if (input === getAdminPwd()) {
    sessionStorage.setItem('adminAuth', 'true'); closeAdminLogin();
    switchView('settings');
    initSettingsPage();
    showToast('เข้าสู่ระบบสำเร็จ', 'success');
  }""")


with open("index.html", "w", encoding="utf-8") as f:
    f.write(current_html)
    
with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(current_js)

print("Successfully injected missing features.")
