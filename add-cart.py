with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Header: add cart button
html = html.replace(
    '<a href="https://wa.me/254719438751?text=Habari%20Muigai%20Inn%20[SITE]%2C%20nataka%20kujua%20kama%20mko%20wazi" class="header-cta" target="_blank" rel="noopener">\n    <span class="dot"></span> Tuko Wazi\n  </a>',
    '''<button type="button" class="cart-button" id="cartButton" aria-label="Open cart">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1.5"/><circle cx="19" cy="21" r="1.5"/><path d="M2.5 3h2.5l2.5 13h11l2-9H6"/></svg>
    <span class="cart-badge" id="cartBadge">0</span>
  </button>''',
    1
)

# 2. Add "Add" buttons to menu items
menu_items = [
    'Bia Baridi', 'Whiskey & Spirits', 'Soda & Juice', 'Hot Drinks',
    'Nyama Choma', 'Kuku Choma', 'Fish & Chips', 'Ugali & Sukuma',
    'Chips Masala', 'Smokie & Chips', 'Soup of the Day', 'Snacks & Bites'
]
for item in menu_items:
    old = f'<li><span>{item}</span><em>Ask</em></li>'
    new = f'<li><span>{item}</span><em>Ask</em><button type="button" class="menu-add" data-name="{item}">+</button></li>'
    html = html.replace(old, new)

# 3. Cart drawer + toast before </body>
extras = '''
<aside class="cart-drawer" id="cartDrawer" aria-hidden="true">
  <div class="cart-header">
    <h3>Oda yako</h3>
    <button type="button" class="cart-close" id="cartClose" aria-label="Close">×</button>
  </div>
  <div class="cart-items" id="cartItems"><p class="cart-empty">Hakuna kitu bado.</p></div>
  <div class="cart-footer">
    <p class="cart-note">Bei zitathibitishwa kwa WhatsApp.</p>
    <button type="button" class="btn btn-primary cart-checkout" id="cartCheckout">Tuma Oda kwa WhatsApp</button>
  </div>
</aside>
<div class="cart-overlay" id="cartOverlay"></div>
<div class="toast" id="toast">Imeongezwa</div>
'''
html = html.replace('</body>', extras + '\n</body>', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done. Cart added to Muigai Inn.')
