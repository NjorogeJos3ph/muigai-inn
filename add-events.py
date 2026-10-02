with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

events_section = '''
  <!-- WHAT'S ON -->
  <section id="whatson" class="events-section">
    <div class="section-heading">
      <p class="eyebrow">WHAT'S ON</p>
      <h2>Kila kitu kinachoendelea.</h2>
      <p class="section-sub">Events, match days, live music — kila wiki hapa Muigai Inn.</p>
    </div>

    <div class="events-grid">

      <article class="event-card">
        <div class="event-date">
          <span class="event-day">FRI</span>
          <span class="event-time">8 PM</span>
        </div>
        <div class="event-body">
          <p class="event-tag">LIVE MUSIC</p>
          <h3>Live Band Friday</h3>
          <p>Local bands, cold beer, good vibes. Karibu uanze weekend yako hapa.</p>
        </div>
      </article>

      <article class="event-card">
        <div class="event-date">
          <span class="event-day">SUN</span>
          <span class="event-time">3 PM</span>
        </div>
        <div class="event-body">
          <p class="event-tag">MATCH DAY</p>
          <h3>Live Football Screen</h3>
          <p>Every big match on the big screen. Karibu uone game na mabeste.</p>
        </div>
      </article>

      <article class="event-card">
        <div class="event-date">
          <span class="event-day">TUE</span>
          <span class="event-time">9 PM</span>
        </div>
        <div class="event-body">
          <p class="event-tag">KARAOKE</p>
          <h3>Karaoke Night</h3>
          <p>Show us what you've got. Cold drinks, warm crowd, good music.</p>
        </div>
      </article>

    </div>

    <div class="events-cta">
      <a href="https://wa.me/254719438751?text=Habari%20Muigai%20Inn%20[SITE]%2C%20nataka%20kujua%20event%20zinazokuja" class="btn btn-secondary" target="_blank" rel="noopener">Uliza Events Zinazokuja</a>
    </div>
  </section>

'''

# Insert before the MENU section
html = html.replace('  <!-- MENU -->', events_section + '  <!-- MENU -->', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done. Events section added.')
