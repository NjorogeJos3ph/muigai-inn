with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add data-day + next-up badge to each event card
html = html.replace(
    '<article class="event-card">\n        <div class="event-date">\n          <span class="event-day">FRI</span>',
    '<article class="event-card" data-day="5">\n        <div class="event-date">\n          <span class="event-day">FRI</span>',
    1
)
html = html.replace(
    '<article class="event-card">\n        <div class="event-date">\n          <span class="event-day">SUN</span>',
    '<article class="event-card" data-day="0">\n        <div class="event-date">\n          <span class="event-day">SUN</span>',
    1
)
html = html.replace(
    '<article class="event-card">\n        <div class="event-date">\n          <span class="event-day">TUE</span>',
    '<article class="event-card" data-day="2">\n        <div class="event-date">\n          <span class="event-day">TUE</span>',
    1
)

# Add "next-up-badge" inside each event-body
html = html.replace(
    '<p class="event-tag">LIVE MUSIC</p>',
    '<span class="next-up-badge">NEXT UP</span><p class="event-tag">LIVE MUSIC</p>',
    1
)
html = html.replace(
    '<p class="event-tag">MATCH DAY</p>',
    '<span class="next-up-badge">NEXT UP</span><p class="event-tag">MATCH DAY</p>',
    1
)
html = html.replace(
    '<p class="event-tag">KARAOKE</p>',
    '<span class="next-up-badge">NEXT UP</span><p class="event-tag">KARAOKE</p>',
    1
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done. Event cards tagged with day and badge.')
