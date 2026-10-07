import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove duplicate trust bar (keep only first)
trust_block = '''<div class="trust-bar">
    <span>24 Hours</span><span class="sep">·</span>
    <span>Nyama Choma Daily</span><span class="sep">·</span>
    <span>Live Sports Screen</span><span class="sep">·</span>
    <span>Kenyatta Road, Juja</span>
  </div>'''

count = html.count(trust_block)
print(f'Trust bar found {count} times')

if count > 1:
    # Keep first, remove the rest
    first = html.find(trust_block)
    after_first = first + len(trust_block)
    html = html[:after_first] + html[after_first:].replace(trust_block, '')
    print('Removed duplicate trust bar(s)')

# 2. Add back-to-top button before </body>
if 'back-to-top' not in html:
    back_html = '''
<button type="button" class="back-to-top" id="backToTop" aria-label="Back to top">
  <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
</button>
'''
    html = html.replace('</body>', back_html + '\n</body>', 1)
    print('Added back-to-top button')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done.')
