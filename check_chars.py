# -*- coding: utf-8 -*-
from __future__ import print_function
import os, re, io

ALLOWED = set([
    u'\xe4',u'\xf6',u'\xfc',u'\xdf',u'\xc4',u'\xd6',u'\xdc',
    u'—',u'–',u'€',u'\xa9',u'\xab',u'\xbb',u'\xb0',u'→',
])

bad_char = re.compile(r'[^\x00-\x7F]', re.UNICODE)

results = []
base = u'C:/Users/steff/Videos/sanitär'
for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith(u'.html'):
            continue
        path = os.path.join(root, f)
        try:
            with io.open(path, 'r', encoding='utf-8', errors='replace') as fh:
                content = fh.read()
        except Exception as e:
            continue
        problems = [(m, ord(m)) for m in set(bad_char.findall(content)) if m not in ALLOWED]
        if problems:
            rel = os.path.relpath(path, base)
            results.append((rel, problems))

with io.open(base + u'/char_check_results.txt', 'w', encoding='utf-8') as out:
    for rel, probs in sorted(results):
        out.write(rel + ': ' + str(probs) + u'\n')
print('Done, wrote', len(results), 'files with issues')