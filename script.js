document.addEventListener('DOMContentLoaded', () => {

  /* ===== REVEAL ON SCROLL ===== */
  const els = document.querySelectorAll('.known-card, .stat, .menu-block, .visit-detail, .event-card, .exp-card');
  els.forEach(el => el.classList.add('reveal'));
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  els.forEach(el => observer.observe(el));

  /* ===== CART ===== */
  const CART_KEY = 'muigai-cart';
  let cart = [];
  try { cart = JSON.parse(localStorage.getItem(CART_KEY) || '[]'); } catch (e) { cart = []; }

  const cartDrawer = document.getElementById('cartDrawer');
  const cartOverlay = document.getElementById('cartOverlay');
  const cartBadge = document.getElementById('cartBadge');
  const cartItemsEl = document.getElementById('cartItems');
  const cartBtn = document.getElementById('cartButton');
  const cartClose = document.getElementById('cartClose');
  const cartCheckout = document.getElementById('cartCheckout');
  const toast = document.getElementById('toast');

  function updateBadge() {
    if (!cartBadge) return;
    const total = cart.reduce((sum, item) => sum + (item.qty || 1), 0);
    cartBadge.textContent = total;
    cartBadge.style.display = total > 0 ? 'flex' : 'none';
  }

  function save() {
    try { localStorage.setItem(CART_KEY, JSON.stringify(cart)); } catch (e) {}
  }

  function renderCart() {
    if (!cartItemsEl) return;
    if (cart.length === 0) {
      cartItemsEl.innerHTML = '<p class="cart-empty">Bado hakuna kitu.</p>';
      return;
    }
    cartItemsEl.innerHTML = cart.map((item, i) => `
      <div class="cart-item">
        <div class="cart-item-info">
          <p class="cart-item-name">${item.name}${item.qty > 1 ? ' × ' + item.qty : ''}</p>
        </div>
        <button type="button" class="cart-remove" data-index="${i}" aria-label="Remove">×</button>
      </div>`).join('');
    cartItemsEl.querySelectorAll('.cart-remove').forEach(b => {
      b.addEventListener('click', () => {
        cart.splice(parseInt(b.dataset.index), 1);
        save(); renderCart(); updateBadge();
      });
    });
  }

  function openCart() {
    if (cartDrawer) cartDrawer.classList.add('open');
    if (cartOverlay) cartOverlay.classList.add('open');
    if (cartDrawer) cartDrawer.setAttribute('aria-hidden', 'false');
  }
  function closeCart() {
    if (cartDrawer) cartDrawer.classList.remove('open');
    if (cartOverlay) cartOverlay.classList.remove('open');
    if (cartDrawer) cartDrawer.setAttribute('aria-hidden', 'true');
  }
  function showToast(text) {
    if (!toast) return;
    toast.textContent = text;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 1800);
  }

  function addToCart(name) {
    const existing = cart.find(x => x.name === name);
    if (existing) { existing.qty = (existing.qty || 1) + 1; }
    else { cart.push({ name: name, qty: 1 }); }
    save(); updateBadge(); renderCart();
    showToast('Imeongezwa: ' + name);
  }

  if (cartBtn) cartBtn.addEventListener('click', openCart);
  if (cartClose) cartClose.addEventListener('click', closeCart);
  if (cartOverlay) cartOverlay.addEventListener('click', closeCart);

  if (cartCheckout) {
    cartCheckout.addEventListener('click', () => {
      if (cart.length === 0) return;
      const list = cart.map((item, i) => `${i+1}. ${item.name}${item.qty > 1 ? ' × ' + item.qty : ''}`).join('\n');
      const msg = `Habari Muigai Inn [SITE],\n\nOrder yangu:\n\n${list}\n\nTafadhali thibitisha bei na kama ziko.`;
      window.open(`https://wa.me/254719438751?text=${encodeURIComponent(msg)}`, '_blank');
    });
  }

  /* Attach + buttons on menu items */
  document.querySelectorAll('.menu-add').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      addToCart(btn.dataset.name || 'Item');
    });
  });

  updateBadge();
  renderCart();

  /* ===== EVENT DAY HIGHLIGHT ===== */
  const today = new Date().getDay();
  const eventCards = document.querySelectorAll('.event-card[data-day]');
  const eventDays = Array.from(eventCards).map(c => parseInt(c.dataset.day));

  let nextDay = null;
  let daysAway = null;
  for (let offset = 0; offset <= 7; offset++) {
    const check = (today + offset) % 7;
    if (eventDays.includes(check)) {
      nextDay = check;
      daysAway = offset;
      break;
    }
  }

  if (nextDay !== null) {
    eventCards.forEach(card => {
      if (parseInt(card.dataset.day) === nextDay) {
        card.classList.add('next-up');
        const badge = card.querySelector('.next-up-badge');
        if (badge) {
          if (daysAway === 0) badge.textContent = 'TONIGHT';
          else if (daysAway === 1) badge.textContent = 'TOMORROW';
          else badge.textContent = 'IN ' + daysAway + ' DAYS';
        }
      }
    });
  }
});
