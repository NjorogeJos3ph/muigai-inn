import re

# Read both files
pos = open('pos.html', 'r', encoding='utf-8').read()
dash = open('dashboard.html', 'r', encoding='utf-8').read()

# Find what key each is using
pos_match = re.search(r"CART_KEY\s*=\s*'([^']+)'", pos)
dash_match = re.search(r"getItem\('([^']+)'\)", dash)

print("POS key:", pos_match.group(1) if pos_match else "NOT FOUND")
print("Dashboard key:", dash_match.group(1) if dash_match else "NOT FOUND")

# Force both to v3
pos = re.sub(r"CART_KEY\s*=\s*'[^']+'", "CART_KEY = 'muigai-pos-v3'", pos)
dash = re.sub(r"getItem\('[^']+'\)", "getItem('muigai-pos-v3')", dash)
dash = re.sub(r"setItem\('[^']+'", "setItem('muigai-pos-v3'", dash)

open('pos.html', 'w', encoding='utf-8').write(pos)
open('dashboard.html', 'w', encoding='utf-8').write(dash)

print("\nBoth files now use: muigai-pos-v3")
print("Done.")
