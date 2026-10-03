document.addEventListener('DOMContentLoaded', () => {

  // ===== REVEAL =====
  const els = document.querySelectorAll('.known-card, .stat, .menu-block, .visit-detail, .event-card');
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

  // ===== CART =====
  const CART_KEY = 'muigai-cart';
  let cart = JSON.parse(localStorage.getItem(CART_KEY) || '[]');
  const cartDrawer = document.getElementById('cartDrawer');
  const cartOverlay = document.getElementById('cartOverlay');
  const cartBadge = document.getElementById('cartBadge');
  const cartItemsEl = document.getElementById('cartItems');
  const cartBtn = document.getElementById('cartButton');
  const cartClose = document.getElementById('cartClose');
  const cartCheckout = document.getElementById('cartCheckout');
  const toast = document.getElementById('toast');

  function updateBadge() {
    cartBadge.textContent = cart.length;
    cartBadge.style.display = cart.length > 0 ? 'flex' : 'none';
  }
  function save() { localStorage.setItem(CART_KEY, JSON.stringify(cart)); }

  function renderCart() {
    if (cart.length === 0) {
      cartItemsEl.innerHTML = '<p class="cart-empty">Hakuna kitu bado.</p>';
      return;
    }
    cartItemsEl.innerHTML = cart.map((item, i) => `
      <div class="cart-item">
        <div class="cart-item-info">
          <p class="cart-item-name">${item.name}</p>
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
    cartDrawer.classList.add('open'); cartOverlay.classList.add('open');
    cartDrawer.setAttribute('aria-hidden','false');
  }
  function closeCart() {
    cartDrawer.classList.remove('open'); cartOverlay.classList.remove('open');
    cartDrawer.setAttribute('aria-hidden','true');
  }
  function showToast(text) {
    toast.textContent = text; toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 1800);
  }
  function addToCart(name) {
    const existing = cart.find(x => x.name === name);
    if (existing) { existing.qty++; }
    else { cart.push({ name, qty: 1 }); }
    save(); updateBadge(); renderCart(); showToast('Imeongezwa: ' + name);
  }

  cartBtn.addEventListener('click', openCart);
  cartClose.addEventListener('click', closeCart);
  cartOverlay.addEventListener('click', closeCart);

  cartCheckout.addEventListener('click', () => {
    if (cart.length === 0) return;
    const list = cart.map((item, i) => `${i+1}. ${item.name}${item.qty > 1 ? ' x' + item.qty : ''}`).join('\n');
    const msg = `Habari Muigai Inn [SITE],\n\nOrder yangu:\n\n${list}\n\nTafadhali thibitisha bei na kama ziko.`;
cd ~/muigai-inn

    window.open(`https://wa.me/254719438751?text=${encodeURIComponent(msg)}`, '_blank');
  });

  document.querySelectorAll('.menu-add').forEach(btn => {
    btn.addEventListener('click', () => addToCart(btn.dataset.name));
  });

  updateBadge(); renderCart();
// ===== EVENT DAY HIGHLIGHT =====
const today = new Date().getDay(); // 0=Sun ... 6=Sat
const eventCards = document.querySelectorAll('.event-card[data-day]');
const eventDays = Array.from(eventCards).map(c => parseInt(c.dataset.day));

// Find next upcoming event (including today)
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

// Mark that card as "next up"
if (nextDay !== null) {
  eventCards.forEach(card => {
    if (parseInt(card.dataset.day) === nextDay) {
      card.classList.add('next-up');

      // Update badge text based on timing
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
