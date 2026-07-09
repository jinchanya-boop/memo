let GAS_URL = localStorage.getItem('gasUrl') || 'https://script.google.com/macros/s/AKfycbw-UaYyMHfZlklHhctqLInRSnEYCO_btfyQyMe0WYqaCT1XpjYoyZMKlthkFTF61PxS/exec';
const SECRET_TOKEN = 'SaaSchool_Secret_2026!';


function normalizeDateField(val) {
  if (!val) return '';
  const s = String(val).trim();
  if (/^\d{4}-\d{2}-\d{2}$/.test(s)) return s;
  const d = new Date(s);
  if (!isNaN(d.getTime())) {
    return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
  }
  return s;
}

// Generic sync function to fetch data for a specific module
async function syncFromSheets(actionStr, lsKey) {
  if (!GAS_URL) return null;
  return new Promise((resolve) => {
    const cbName = 'gasCallback_' + Date.now() + Math.floor(Math.random() * 1000);
    const timeout = setTimeout(() => {
      delete window[cbName];
      const el = document.getElementById('gas-jsonp-' + cbName);
      if (el) el.remove();
      resolve(null);
    }, 20000);
    
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
    script.src = GAS_URL + '?action=' + actionStr + '&callback=' + cbName + '&token=' + SECRET_TOKEN;
    script.onerror = () => { clearTimeout(timeout); resolve(null); };
    document.head.appendChild(script);
  });
}

// Sync all modules
async function syncAllModules() {
  await Promise.all([
    syncFromSheets('getAll', 'memoData'),
    syncFromSheets('getOrders', 'orderData'),
    syncFromSheets('getBooks', 'bookData')
  ]);
}

// Push to sheet generic
async function pushToSheets(actionStr, record) {
  if (!GAS_URL) return record;
  try {
    const startConfig = JSON.parse(localStorage.getItem('startConfig') || '{}');
    const res = await fetch(GAS_URL, { method:'POST', body: JSON.stringify({ action: actionStr, record, startConfig, token: SECRET_TOKEN }), headers:{'Content-Type':'text/plain'} });
    const json = await res.json();
    if(json.status === 'ok' && json.record) return json.record;
  } catch(e) {
    console.warn("Failed to push to sheets", e);
  }
  return record;
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
