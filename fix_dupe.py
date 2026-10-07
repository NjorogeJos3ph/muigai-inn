with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []
prev_reserve = False
removed = 0

for line in lines:
    if 'Reserve Meza' in line and 'btn btn-secondary' in line:
        if prev_reserve:
            removed += 1
            continue
        prev_reserve = True
    else:
        prev_reserve = False
    out.append(line)

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(out)

print(f'Done. Removed {removed} duplicate Reserve Meza line(s).')
