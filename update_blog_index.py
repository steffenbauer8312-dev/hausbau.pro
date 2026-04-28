#!/usr/bin/env python3
"""Update blog index to include both dachdecker and heating articles."""

DACHARTICLES = [
    {"id": "dachsanierung-kosten-2026", "title": "Dachsanierung Kosten 2026", "badge": "Kosten"},
    {"id": "flachdach-sanieren-oder-neu", "title": "Flachdach sanieren oder neu?", "badge": "Flachdach"},
    {"id": "dachausbau-kosten-2026", "title": "Dachausbau Kosten 2026", "badge": "Dachausbau"},
    {"id": "geg-dach-pflicht-2026", "title": "GEG Dach 2026 - Was ist Pflicht?", "badge": "GEG"},
    {"id": "gruendach-foerderung-2026", "title": "Gründach Förderung 2026", "badge": "Förderung"},
    {"id": "gaube-einbauen-kosten", "title": "Gaube einbauen Kosten 2026", "badge": "Gauben"},
    {"id": "dachreparatur-kosten-wann", "title": "Dachreparatur: Wann lohnt sie sich?", "badge": "Dachreparatur"},
    {"id": "dachsanierung-koeln-kosten", "title": "Dachsanierung Köln Kosten", "badge": "Regional"},
]

HEATINGARTICLES = [
    {"id": "waermepumpe-kosten-2026", "title": "Wärmepumpe Kosten 2026", "badge": "Kosten"},
    {"id": "waermepumpe-foerderung-2026", "title": "Wärmepumpe Förderung 2026", "badge": "Förderung"},
    {"id": "klimaanlage-einbauen-kosten", "title": "Klimaanlage einbauen Kosten 2026", "badge": "Kosten"},
    {"id": "bad-sanierung-kosten-2026", "title": "Bad Sanierung Kosten 2026", "badge": "Kosten"},
    {"id": "heizungsbauer-finden", "title": "Heizungsbauer finden", "badge": "Ratgeber"},
    {"id": "solarthermie-vs-photovoltaik", "title": "Solarthermie vs. Photovoltaik", "badge": "Energie"},
    {"id": "klimaanlage-wartung", "title": "Klimaanlage Wartung", "badge": "Wartung"},
    {"id": "sanitaer-installation-kosten", "title": "Sanitär Installation Kosten 2026", "badge": "Kosten"},
]

html = '''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blog - Ratgeber für Dach und Heizung</title>
  <meta name="description" content="Dachsanierung Kosten, Wärmepumpe Förderung, Klimaanlage Wartung - Ratgeber für Dach und Heizung in Deutschland.">
  <link rel="stylesheet" href="/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
  <header class="header">
    <div class="container header__inner">
      <a href="/" class="logo">hausbau<span class="logo-accent">.pro</span></a>
      <nav class="nav">
        <a href="/#so-funktionierts" class="nav__link">So funktioniert's</a>
        <a href="/#services" class="nav__link">Dach</a>
        <a href="/waermepumpe/" class="nav__link">Heizung</a>
        <a href="/blog/" class="nav__link">Blog</a>
        <a href="/#faq" class="nav__link">FAQ</a>
        <a href="/#angebot" class="btn btn--header">Kostenlos anfragen</a>
      </nav>
      <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </header>

  <section class="hero hero--small">
    <div class="container">
      <div class="hero__content">
        <h1>Ratgeber für Dach und Heizung</h1>
        <p class="hero__sub">Dachsanierung Kosten, Wärmepumpe Förderung, Klimaanlage Wartung - hier finden Sie Antworten auf die wichtigsten Fragen.</p>
      </div>
    </div>
  </section>

  <section class="section section--light">
    <div class="container">
      <h2 style="margin-bottom:1rem">Dachdecker & Zimmerei</h2>
      <div class="grid grid--3">
'''

for a in DACHARTICLES:
    html += f'''        <a href="/blog/{a["id"]}/" class="card card--link">
          <div class="card-badge" style="margin-top:0;margin-bottom:12px">{a["badge"]}</div>
          <h3>{a["title"]}</h3>
        </a>
'''

html += '''
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <h2 style="margin-bottom:1rem">Heizung & Sanitär</h2>
      <div class="grid grid--3">
'''

for a in HEATINGARTICLES:
    html += f'''        <a href="/blog/{a["id"]}/" class="card card--link">
          <div class="card-badge" style="margin-top:0;margin-bottom:12px">{a["badge"]}</div>
          <h3>{a["title"]}</h3>
        </a>
'''

html += '''
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <h2 style="margin-bottom:2rem">Mehr Wissen</h2>
      <div class="grid grid--3">
        <a href="/glossar/" class="card card--link"><h3>Dachdecker Glossar</h3><p>35 Fachbegriffe rund ums Dach.</p></a>
        <a href="/glossar/waermepumpe/" class="card card--link"><h3>Wärmepumpe</h3><p>Was ist das und wie funktioniert sie?</p></a>
        <a href="/dachdecker/koeln/" class="card card--link"><h3>Dachdecker Köln</h3><p>Geprüfte Dachdecker, NRW-Bank Förderung.</p></a>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand"><span class="logo">hausbau<span class="logo-accent">.pro</span></span><p>Kostenlose Vermittlung von geprüften Fachbetrieben in ganz Deutschland.</p></div>
      <div class="footer__links"><h4>Wissen</h4><a href="/glossar/">Glossar</a><a href="/blog/">Blog</a></div>
      <div class="footer__links"><h4>Heizung & Sanitär</h4><a href="/waermepumpe/">Wärmepumpe</a><a href="/heizungsbau/">Heizungsbau</a><a href="/sanitaer/">Sanitär</a></div>
    </div>
  </footer>
  <script src="/js/main.js"></script>
</body>
</html>'''

with open("blog/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated: blog/index.html")