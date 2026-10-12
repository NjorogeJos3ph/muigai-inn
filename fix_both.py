import re

print("=== FIXING pos.html ===\n")

with open('pos.html', 'r', encoding='utf-8') as f:
    pos = f.read()

# Show what we found
orphans = re.findall(r'/\*[^*]*ITEMS[^*]*\*/\s*\n\];', pos)
print(f"Found {len(orphans)} orphan ITEMS block(s) in pos.html")

# Remove all orphan ITEMS comment + following ];
pos = re.sub(r'/\*[^*]*ITEMS[^*]*\*/\s*\n\];\s*\n', '', pos)

# Ensure items.js is loaded
if 'src="items.js"' not in pos:
    print("Adding items.js script tag to pos.html")
    pos = pos.replace('<script>', '<script src="items.js"></script>\n<script>', 1)
else:
    print("items.js already loaded in pos.html")

with open('pos.html', 'w', encoding='utf-8') as f:
    f.write(pos)

print("pos.html fixed.\n")

print("=== FIXING dashboard.html ===\n")

with open('dashboard.html', 'r', encoding='utf-8') as f:
    dash = f.read()

# Find hardcoded ITEMS arrays
hardcoded = re.findall(r'const ITEMS = \[[\s\S]*?\];', dash)
print(f"Found {len(hardcoded)} hardcoded ITEMS array(s) in dashboard.html")

# Remove the hardcoded array
dash = re.sub(r'const ITEMS = \[[\s\S]*?\];\s*\n', '', dash, count=1)

# Ensure items.js is loaded before the main script
if 'src="items.js"' not in dash:
    print("Adding items.js script tag to dashboard.html")
    dash = dash.replace('<script>', '<script src="items.js"></script>\n<script>', 1)
else:
    print("items.js already loaded in dashboard.html")

# Bump storage key to force fresh data
dash = dash.replace("'muigai-pos'", "'muigai-pos-v2'")
pos_fixed = open('pos.html', 'r', encoding='utf-8').read()
if "'muigai-pos-v2'" in pos_fixed:
    print("Storage keys match: muigai-pos-v2")

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash)

print("dashboard.html fixed.\n")
print("=== DONE ===")
print("Now run: python -m http.server 8080")
