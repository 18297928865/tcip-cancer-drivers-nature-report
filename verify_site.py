import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

toc_targets = set(re.findall(r'href="#([a-zA-Z0-9_-]+)"', content))
defined_ids = set(re.findall(r'id="([a-zA-Z0-9_-]+)"', content))

missing = toc_targets - defined_ids
print("TOC targets:", len(toc_targets))
print("Defined IDs:", len(defined_ids))
print("Missing targets:", missing)

img_srcs = set(re.findall(r'src="([^"]+)"', content))
print("Images referenced:", len(img_srcs))
all_exist = True
for src in sorted(img_srcs):
    if not src.startswith('http') and src:
        exists = os.path.exists(src)
        print("Image:", src, "Exists:", exists)
        if not exists:
            all_exist = False

print("All local images exist:", all_exist)
