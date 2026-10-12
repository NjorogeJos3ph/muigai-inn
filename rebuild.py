import os

# ============ ITEMS.JS ============
items = '''const ITEMS = [
  { id: 'tusker', name: 'Tusker', cat: 'beer', price: 250, stock: 48 },
  { id: 'whitecap', name: 'White Cap', cat: 'beer', price: 250, stock: 36 },
  { id: 'pilsner', name: 'Pilsner', cat: 'beer', price: 250, stock: 24 },
  { id: 'guinness', name: 'Guinness', cat: 'beer', price: 300, stock: 12 },
  { id: 'balozi', name: 'Balozi', cat: 'beer', price: 220, stock: 24 },
  { id: 'smirnoffice', name: 'Smirnoff Ice', cat: 'beer', price: 300, stock: 18 },
  { id: 'tuskerlite', name: 'Tusker Lite', cat: 'beer', price: 250, stock: 12 },
  { id: 'summit', name: 'Summit', cat: 'beer', price: 220, stock: 24 },
  { id: 'becks', name: "Beck's", cat: 'beer', price: 350, stock: 6 },
  { id: 'heineken', name: 'Heineken', cat: 'beer', price: 350, stock: 8 },
  { id: 'jameson', name: 'Jameson', cat: 'spirits', price: 500, stock: 4 },
  { id: 'gilbeys', name: "Gilbey's", cat: 'spirits', price: 300, stock: 6 },
  { id: 'kenyacane', name: 'Kenya Cane', cat: 'spirits', price: 300, stock: 8 },
  { id: 'chrome', name: 'Chrome', cat: 'spirits', price: 350, stock: 5 },
  { id: 'bond7', name: 'Bond 7', cat: 'spirits', price: 300, stock: 6 },
  { id: 'jackdaniels', name: "Jack Daniel's", cat: 'spirits', price: 600, stock: 3 },
  { id: 'smirnoffvodka', name: 'Smirnoff Vodka', cat: 'spirits', price: 350, stock: 5 },
  { id: 'captainmorgan', name: 'Captain Morgan', cat: 'spirits', price: 400, stock: 4 },
  { id: 'grant', name: "Grant's", cat: 'spirits', price: 400, stock: 5 },
  { id: 'napoleon', name: 'Napoleon', cat: 'spirits', price: 350, stock: 4 },
  { id: 'coke', name: 'Coke', cat: 'soft', price: 100, stock: 36 },
  { id: 'cokezero', name: 'Coke Zero', cat: 'soft', price: 100, stock: 24 },
  { id: 'fanta', name: 'Fanta', cat: 'soft', price: 100, stock: 24 },
  { id: 'sprite', name: 'Sprite', cat: 'soft', price: 100, stock: 24 },
  { id: 'novida', name: 'Novida', cat: 'soft', price: 120, stock: 12 },
  { id: 'krest', name: 'Krest', cat: 'soft', price: 120, stock: 12 },
  { id: 'water', name: 'Water 500ml', cat: 'soft', price: 80, stock: 36 },
  { id: 'water1l', name: 'Water 1L', cat: 'soft', price: 130, stock: 24 },
  { id: 'nyamachoma', name: 'Nyama Choma 1kg', cat: 'nyama', price: 700, stock: 10 },
  { id: 'nyamahalf', name: 'Nyama 1/2kg', cat: 'nyama', price: 400, stock: 12 },
  { id: 'kukuchoma', name: 'Kuku Choma', cat: 'nyama', price: 600, stock: 8 },
  { id: 'kukuhalf', name: 'Kuku 1/2', cat: 'nyama', price: 350, stock: 10 },
  { id: 'mbuzi', name: 'Mbuzi Choma', cat: 'nyama', price: 800, stock: 6 },
  { id: 'beef', name: 'Beef Choma', cat: 'nyama', price: 700, stock: 8 },
  { id: 'liver', name: 'Liver', cat: 'nyama', price: 500, stock: 5 },
  { id: 'matumbo', name: 'Matumbo', cat: 'nyama', price: 450, stock: 6 },
  { id: 'chips', name: 'Chips', cat: 'food', price: 200, stock: 20 },
  { id: 'chipsmasala', name: 'Chips Masala', cat: 'food', price: 300, stock: 15 },
  { id: 'ugali', name: 'Ugali', cat: 'food', price: 80, stock: 30 },
  { id: 'sukuma', name: 'Sukuma', cat: 'food', price: 100, stock: 20 },
  { id: 'ugalisukuma', name: 'Ugali + Sukuma', cat: 'food', price: 150, stock: 25 },
  { id: 'fish', name: 'Fish', cat: 'food', price: 700, stock: 6 },
  { id: 'fishchips', name: 'Fish & Chips', cat: 'food', price: 800, stock: 5 },
  { id: 'kachumbari', name: 'Kachumbari', cat: 'food', price: 50, stock: 30 },
  { id: 'smokie', name: 'Smokie', cat: 'snacks', price: 50, stock: 24 },
  { id: 'sausage', name: 'Sausage', cat: 'snacks', price: 60, stock: 24 },
  { id: 'smokieschips', name: 'Smokie + Chips', cat: 'snacks', price: 250, stock: 15 },
  { id: 'crisps', name: 'Crisps', cat: 'snacks', price: 100, stock: 20 },
  { id: 'peanuts', name: 'Peanuts', cat: 'snacks', price: 80, stock: 18 },
  { id: 'bhajia', name: 'Bhajia', cat: 'snacks', price: 200, stock: 12 },
  { id: 'freshjuice', name: 'Fresh Juice', cat: 'juice', price: 200, stock: 12 },
  { id: 'mango', name: 'Mango Juice', cat: 'juice', price: 200, stock: 10 },
  { id: 'passion', name: 'Passion Juice', cat: 'juice', price: 200, stock: 10 },
  { id: 'smoothie', name: 'Smoothie', cat: 'juice', price: 300, stock: 8 }
];

const CATEGORIES = [
  { id: 'all', name: 'All' },
  { id: 'beer', name: 'Bia' },
  { id: 'spirits', name: 'Spirits' },
  { id: 'soft', name: 'Soft' },
  { id: 'nyama', name: 'Nyama' },
  { id: 'food', name: 'Food' },
  { id: 'snacks', name: 'Snacks' },
  { id: 'juice', name: 'Juice' }
];

const STORAGE_KEY = 'muigai-data';
'''

with open('items.js', 'w', encoding='utf-8') as f:
    f.write(items)

print("Written: items.js")

# ============ POS.HTML ============
pos = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Muigai Inn — POS</title>
<style>
:root{--bg:#1C1207;--surface:#2A1A0C;--surface-2:#362210;--amber:#D4A24C;--amber-light:#E5B35C;--hot:#B8322A;--text:#F5E8CE;--muted:#B8A48C;--border:#3D2817;}
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent;}
body{background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;padding-bottom:120px;}
.header{padding:14px 16px 10px;background:var(--surface);border-bottom:2px solid var(--amber);position:sticky;top:0;z-index:20;}
.header h1{font-size:1rem;color:var(--amber);text-align:center;text-transform:uppercase;font-weight:800;letter-spacing:.1em;}
.header .date{text-align:center;font-size:.68rem;color:var(--muted);margin-top:2px;letter-spacing:.15em;text-transform:uppercase;}
.mode-toggle{display:flex;gap:8px;padding:10px 16px;max-width:780px;margin:0 auto;}
.mode-btn{flex:1;padding:16px;border:2px solid var(--border);background:transparent;color:var(--muted);font-family:inherit;font-size:.85rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;border-radius:12px;cursor:pointer;min-height:54px;}
.mode-btn.active{background:var(--amber);color:#1A0E05;border-color:var(--amber);}
.mode-btn.stock-active{background:var(--hot);color:#fff;border-color:var(--hot);}
.search-wrap{max-width:780px;margin:0 auto;padding:0 16px 12px;}
.search-input{width:100%;padding:16px 20px;background:var(--surface);border:2px solid var(--border);border-radius:12px;color:var(--text);font-size:1rem;font-family:inherit;min-height:54px;}
.search-input:focus{outline:none;border-color:var(--amber);}
.tabs-wrap{position:sticky;top:108px;z-index:15;background:var(--bg);border-bottom:1px solid var(--border);padding:8px 0;}
.tabs{display:flex;gap:8px;overflow-x:auto;padding:0 16px;}
.tabs::-webkit-scrollbar{display:none;}
.tab{flex-shrink:0;padding:12px 20px;background:transparent;border:2px solid var(--border);color:var(--muted);font-family:inherit;font-size:.82rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;border-radius:999px;cursor:pointer;min-height:46px;white-space:nowrap;}
.tab.active{background:var(--amber);color:#1A0E05;border-color:var(--amber);}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;padding:14px 16px;max-width:780px;margin:0 auto;}
@media(min-width:560px){.grid{grid-template-columns:repeat(3,1fr);}}
@media(min-width:800px){.grid{grid-template-columns:repeat(4,1fr);}}
.item-btn{background:var(--surface);border:2px solid var(--border);border-radius:14px;padding:18px 10px 14px;cursor:pointer;text-align:center;font-family:inherit;color:var(--text);min-height:110px;display:flex;flex-direction:column;justify-content:space-between;align-items:center;}
.item-btn:active{transform:scale(.94);border-color:var(--amber);}
.item-btn .name{font-size:.78rem;font-weight:700;text-transform:uppercase;color:var(--text);margin-bottom:8px;line-height:1.2;word-break:break-word;}
.item-btn .count{font-size:2rem;font-weight:900;color:var(--amber);line-height:1;font-family:'Arial Black',sans-serif;}
.item-btn.low .count{opacity:.85;}
.item-btn.low{border-color:rgba(184,50,42,.5);}
.item-btn.out{opacity:.6;}
.item-btn.out .count{color:var(--hot);}
.empty-state{text-align:center;padding:60px 20px;color:var(--muted);font-size:.9rem;}
.footer-bar{position:fixed;bottom:0;left:0;right:0;background:var(--surface);border-top:2px solid var(--amber);padding:12px 16px;z-index:25;}
.footer-inner{max-width:780px;margin:0 auto;display:flex;gap:10px;align-items:center;}
.undo-btn{flex:1;padding:16px;background:transparent;border:2px solid var(--border);color:var(--muted);font-family:inherit;font-size:.85rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;border-radius:12px;cursor:pointer;min-height:54px;}
.stat-mini{font-size:.7rem;color:var(--muted);letter-spacing:.12em;text-transform:uppercase;font-weight:700;}
.stat-mini strong{display:block;font-size:1.2rem;color:var(--amber);font-family:'Arial Black',sans-serif;margin-top:2px;}
.toast{position:fixed;bottom:100px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--amber);color:#1A0E05;padding:14px 26px;border-radius:999px;font-weight:800;font-size:.9rem;opacity:0;pointer-events:none;transition:all .22s;white-space:nowrap;z-index:100;}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0);}
.toast.stock{background:var(--hot);color:#fff;}
</style>
</head>
<body>
<div class="header"><h1>Muigai Inn — POS</h1><div class="date" id="today">Leo</div></div>
<div class="mode-toggle">
  <button type="button" class="mode-btn active" id="modeSell">SELL</button>
  <button type="button" class="mode-btn" id="modeStock">STOCK IN</button>
</div>
<div class="search-wrap"><input type="text" class="search-input" id="searchInput" placeholder="🔍 Search... (Tusker, Nyama)"></div>
<div class="tabs-wrap"><div class="tabs" id="tabs"></div></div>
<div class="grid" id="grid"></div>
<div class="footer-bar">
  <div class="footer-inner">
    <button type="button" class="undo-btn" id="undoBtn">↶ Undo</button>
    <div class="stat-mini">Sold<strong id="totalSold">0</strong></div>
    <div class="stat-mini">Stock<strong id="totalStock">0</strong></div>
  </div>
</div>
<div class="toast" id="toast">+1</div>

<script src="items.js"></script>
<script>
function getData(){
  try{return JSON.parse(localStorage.getItem(STORAGE_KEY)||'null')||fresh();}
  catch(e){return fresh();}
}
function fresh(){
  const d={stock:{},sold:{},added:{},history:[],mode:'sell',activeCat:'all',search:''};
  ITEMS.forEach(i=>{d.stock[i.id]=i.stock;d.sold[i.id]=0;d.added[i.id]=0;});
  return d;
}
function save(d){localStorage.setItem(STORAGE_KEY,JSON.stringify(d));}

let state=getData();

function renderTabs(){
  const el=document.getElementById('tabs');
  el.innerHTML=CATEGORIES.map(c=>`<button type="button" class="tab ${state.activeCat===c.id?'active':''}" data-cat="${c.id}">${c.name}</button>`).join('');
  el.querySelectorAll('.tab').forEach(t=>{
    t.addEventListener('click',()=>{state.activeCat=t.dataset.cat;state.search='';document.getElementById('searchInput').value='';save(state);render();});
  });
}
function renderGrid(){
  const grid=document.getElementById('grid');
  const q=state.search.trim().toLowerCase();
  let list=ITEMS.filter(i=>{
    if(q)return i.name.toLowerCase().includes(q);
    if(state.activeCat==='all')return true;
    return i.cat===state.activeCat;
  });
  if(list.length===0){grid.innerHTML='<div class="empty-state">Hakuna item.</div>';return;}
  grid.innerHTML=list.map(item=>{
    const stock=state.stock[item.id]||0;
    let cls='';
    if(stock===0)cls='out';else if(stock<=3)cls='low';
    return `<button type="button" class="item-btn ${cls}" data-id="${item.id}"><div class="name">${item.name}</div><div class="count">${stock}</div></button>`;
  }).join('');
  grid.querySelectorAll('.item-btn').forEach(b=>b.addEventListener('click',()=>handleTap(b.dataset.id)));
}
function renderFooter(){
  document.getElementById('totalSold').textContent=Object.values(state.sold).reduce((a,b)=>a+b,0);
  document.getElementById('totalStock').textContent=Object.values(state.added).reduce((a,b)=>a+b,0);
}
function render(){
  renderTabs();renderGrid();renderFooter();
  document.getElementById('today').textContent=new Date().toLocaleDateString('en-GB',{weekday:'long',day:'numeric',month:'short'});
}
function handleTap(id){
  const item=ITEMS.find(x=>x.id===id);
  if(!item)return;
  if(state.mode==='sell'){
    if((state.stock[id]||0)<=0){showToast('Hakuna '+item.name,true);return;}
    state.stock[id]--;state.sold[id]=(state.sold[id]||0)+1;
    state.history.push({type:'sell',id,time:Date.now()});
    showToast('-1 '+item.name);
  }else{
    state.stock[id]=(state.stock[id]||0)+1;state.added[id]=(state.added[id]||0)+1;
    state.history.push({type:'stock',id,time:Date.now()});
    showToast('+1 '+item.name,true);
  }
  save(state);render();
}
function showToast(t,isStock){
  const el=document.getElementById('toast');
  el.textContent=t;el.classList.toggle('stock',!!isStock);el.classList.add('show');
  clearTimeout(el._to);el._to=setTimeout(()=>el.classList.remove('show'),1000);
}
document.getElementById('modeSell').addEventListener('click',()=>{state.mode='sell';save(state);document.getElementById('modeSell').classList.add('active');document.getElementById('modeStock').classList.remove('active','stock-active');});
document.getElementById('modeStock').addEventListener('click',()=>{state.mode='stock';save(state);document.getElementById('modeSell').classList.remove('active');document.getElementById('modeStock').classList.add('active','stock-active');});
document.getElementById('undoBtn').addEventListener('click',()=>{
  const last=state.history.pop();
  if(!last)return;
  if(last.type==='sell'){state.stock[last.id]++;state.sold[last.id]--;}
  else{state.stock[last.id]--;state.added[last.id]--;}
  save(state);render();
});
document.getElementById('searchInput').addEventListener('input',e=>{state.search=e.target.value;render();});
if(state.mode==='stock'){document.getElementById('modeStock').classList.add('active','stock-active');document.getElementById('modeSell').classList.remove('active');}
render();
</script>
</body>
</html>
'''

with open('pos.html', 'w', encoding='utf-8') as f:
    f.write(pos)

print("Written: pos.html")

# ============ DASHBOARD.HTML ============
dash = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Muigai Inn — Dashboard</title>
<style>
:root{--bg:#1C1207;--surface:#2A1A0C;--surface-2:#362210;--amber:#D4A24C;--hot:#B8322A;--green:#2E8B57;--text:#F5E8CE;--muted:#B8A48C;--border:#3D2817;}
*{margin:0;padding:0;box-sizing:border-box;}
body{background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;padding-bottom:40px;}
.header{padding:22px 20px;background:var(--surface);border-bottom:2px solid var(--amber);}
.header h1{font-size:1rem;color:var(--amber);text-transform:uppercase;font-weight:800;text-align:center;letter-spacing:.1em;}
.header .sub{text-align:center;font-size:.72rem;color:var(--muted);margin-top:4px;letter-spacing:.15em;text-transform:uppercase;}
.container{max-width:720px;margin:0 auto;padding:20px;}
.card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:22px;margin-bottom:14px;}
.label{font-size:.65rem;letter-spacing:.22em;color:var(--amber);text-transform:uppercase;font-weight:800;margin-bottom:14px;}
.value{font-size:2.4rem;font-weight:900;color:var(--text);line-height:1;font-family:'Arial Black',sans-serif;}
.value.amber{color:var(--amber);}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
.list{list-style:none;}
.list li{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--border);font-size:.95rem;}
.list li:last-child{border-bottom:none;}
.list .num{font-weight:800;color:var(--amber);}
.alert{display:flex;align-items:center;gap:10px;padding:14px 16px;background:rgba(184,50,42,.1);border-left:3px solid var(--hot);border-radius:8px;margin-bottom:10px;font-size:.9rem;}
.alert .dot{width:8px;height:8px;border-radius:50%;background:var(--hot);flex-shrink:0;}
.alert.ok{background:rgba(46,139,87,.1);border-left-color:var(--green);}
.alert.ok .dot{background:var(--green);}
.empty{color:var(--muted);text-align:center;padding:40px 20px;font-size:.9rem;}
</style>
</head>
<body>
<div class="header"><h1>Muigai Inn — Dashboard</h1><div class="sub" id="today">Leo</div></div>
<div class="container" id="container"></div>

<script src="items.js"></script>
<script>
const state=JSON.parse(localStorage.getItem(STORAGE_KEY)||'null');
const c=document.getElementById('container');
const today=new Date().toLocaleDateString('en-GB',{weekday:'long',day:'numeric',month:'short'});
document.getElementById('today').textContent=today;

if(!state){
  c.innerHTML='<div class="card"><div class="empty">No data yet. Open POS first to log sales.</div></div>';
}else{
  let totalSales=0;
  ITEMS.forEach(i=>{totalSales+=(state.sold[i.id]||0)*i.price;});
  const itemsSold=Object.values(state.sold).reduce((a,b)=>a+b,0);
  const stockAdded=Object.values(state.added).reduce((a,b)=>a+b,0);

  let top=null,topCount=0;
  ITEMS.forEach(i=>{const s=state.sold[i.id]||0;if(s>topCount){topCount=s;top=i;}});

  let alerts='';let hasAlert=false;
  ITEMS.forEach(i=>{
    const s=state.stock[i.id]||0;
    if(s===0){alerts+=`<div class="alert"><span class="dot"></span>${i.name} — OUT of stock</div>`;hasAlert=true;}
    else if(s<=3){alerts+=`<div class="alert"><span class="dot"></span>${i.name} — only ${s} left</div>`;hasAlert=true;}
  });
  if(!hasAlert)alerts='<div class="alert ok"><span class="dot"></span>All items in stock</div>';

  const byItem=ITEMS.map(i=>{
    const sold=state.sold[i.id]||0;const stock=state.stock[i.id]||0;
    if(sold===0&&stock===i.stock)return '';
    return `<li><span>${i.name}</span><span class="num">${sold} sold · ${stock} left</span></li>`;
  }).filter(x=>x).join('');

  c.innerHTML=`
    <div class="card"><div class="label">Sales Leo · Today</div><div class="value amber">KES ${totalSales.toLocaleString()}</div></div>
    <div class="grid2">
      <div class="card"><div class="label">Items Sold</div><div class="value">${itemsSold}</div></div>
      <div class="card"><div class="label">Stock Added</div><div class="value">${stockAdded}</div></div>
    </div>
    <div class="card"><div class="label">Top Seller</div><div class="value">${top?top.name+' ('+topCount+')':'—'}</div></div>
    <div class="card"><div class="label">Stock Alerts</div>${alerts}</div>
    <div class="card"><div class="label">By Item</div><ul class="list">${byItem||'<li>No sales yet</li>'}</ul></div>
  `;
}
</script>
</body>
</html>
'''

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash)

print("Written: dashboard.html")

# ============ VERIFY ============
print("\n=== VERIFY ===")
for f in ['items.js','pos.html','dashboard.html']:
    if os.path.exists(f):
        size=os.path.getsize(f)
        content=open(f).read()
        has_key='muigai-data' in content
        has_items='items.js' in content if f!='items.js' else True
        print(f"{f}: {size} bytes | key: {has_key} | items.js: {has_items}")
print("\nAll files rebuilt. Ready to test.")
print("\nTest: python -m http.server 8080")
print("POS:       http://127.0.0.1:8080/pos.html")
print("Dashboard: http://127.0.0.1:8080/dashboard.html")
