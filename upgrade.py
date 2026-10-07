with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. TRUST BAR under hero (after </section> of hero, before ticker)
trust_bar = '''
  <div class="trust-bar">
    <span>24 Hours</span><span class="sep">·</span>
    <span>Nyama Choma Daily</span><span class="sep">·</span>
    <span>Live Sports Screen</span><span class="sep">·</span>
    <span>Kenyatta Road, Juja</span>
  </div>
'''
html = html.replace('  <!-- TICKER -->', trust_bar + '\n  <!-- TICKER -->', 1)

# 2. RESERVE A TABLE button in hero actions
html = html.replace(
    '<a href="#menu" class="btn btn-secondary">Ona Menu</a>',
    '<a href="#menu" class="btn btn-secondary">Ona Menu</a>\n        <a href="https://wa.me/254719438751?text=Habari%20Muigai%20Inn%20[SITE]%2C%20nataka%20kureserve%20meza" class="btn btn-secondary" target="_blank" rel="noopener">Reserve Meza</a>',
    1
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done. Trust bar + Reserve button added.')
