# -*- coding: utf-8 -*-
import io, os

files = [
    r'C:\Users\steff\Videos\sanitär\dachfenster\dortmund\index.html',
    r'C:\Users\steff\Videos\sanitär\dachausbau\dortmund\index.html',
    r'C:\Users\steff\Videos\sanitär\dachausbau\hamburg\index.html',
    r'C:\Users\steff\Videos\sanitär\dachsanierung\dortmund\index.html',
    r'C:\Users\steff\Videos\sanitär\dachsanierung\muenchen\index.html',
    r'C:\Users\steff\Videos\sanitär\zimmermann\dortmund\index.html',
    r'C:\Users\steff\Videos\sanitär\zimmermann\koeln\index.html',
    r'C:\Users\steff\Videos\sanitär\zimmermann\muenchen\index.html',
    r'C:\Users\steff\Videos\sanitär\dachfenster\freiburg\index.html',
    r'C:\Users\steff\Videos\sanitär\flachdach\freiburg\index.html',
]

out_lines = []
for f in files:
    with io.open(f, 'r', encoding='utf-8', errors='replace') as fh:
        content = fh.read()
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        bad = [(c, ord(c)) for c in set(line) if ord(c) > 127 and c not in u'äöüßÄÖÜ€—–©·²★✓←' ]
        if bad:
            unique_bad = list(set(bad))
            name = os.path.basename(f)
            out_lines.append(name + ' line ' + str(i) + ': ' + str(unique_bad) + ' | ' + line.strip()[:80])

with io.open(r'C:\Users\steff\Videos\sanitär\char_lines.txt', 'w', encoding='utf-8') as out:
    out.write('\n'.join(out_lines))
print('Done')