#!/usr/bin/env python3
import pathlib, re, sys

root = pathlib.Path('/home/tz/.openclaw/workspace-dev')
review = root / 'review.html'
if not review.exists():
    print('review.html missing')
    sys.exit(1)

html = review.read_text(encoding='utf-8', errors='ignore')
links = re.findall(r'href="(\./dist/[^"]+/)"', html)
missing = []
for rel in links:
    p = root / rel[2:] / 'index.html'
    if not p.exists():
        missing.append(rel)

if missing:
    print('Broken review links detected:')
    for m in missing:
        print('-', m)
    sys.exit(2)

# Ensure each dist article has core assets
bad_assets = []
for d in sorted((root/'dist').iterdir()):
    if not d.is_dir():
        continue
    idx = d/'index.html'
    if not idx.exists():
        continue
    required = ['image_prompt.txt', 'image_alt.txt', 'sources.json', 'cover.svg']
    miss = [r for r in required if not (d/r).exists()]
    if miss:
        bad_assets.append((d.name, miss))

if bad_assets:
    print('Missing required assets:')
    for name, miss in bad_assets:
        print('-', name, '=>', ', '.join(miss))
    sys.exit(3)

print(f'OK: {len(links)} review links validated; assets complete.')
