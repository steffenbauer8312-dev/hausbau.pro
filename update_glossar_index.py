#!/usr/bin/env python3
"""Update glossar index to include both dachdecker and heating terms."""

DACHTERMS = [
    {"id": "bitumenbahn", "title": "Bitumenbahn", "badge": "Material"},
    {"id": "fpo-bahn", "title": "FPO-Bahn", "badge": "Material"},
    {"id": "pib-bahn", "title": "PIB-Bahn", "badge": "Material"},
    {"id": "tonpfanne", "title": "Tonpfanne", "badge": "Material"},
    {"id": "biberschwanz", "title": "Biberschwanz", "badge": "Material"},
    {"id": "schiefer", "title": "Schiefer", "badge": "Material"},
    {"id": "dachkonstruktion", "title": "Dachkonstruktion", "badge": "Konstruktion"},
    {"id": "lattung", "title": "Lattung", "badge": "Konstruktion"},
    {"id": "dampfsperre", "title": "Dampfsperre", "badge": "Konstruktion"},
    {"id": "unterspannbahn", "title": "Unterspannbahn", "badge": "Konstruktion"},
    {"id": "dachformen-aufbauten", "title": "Dachformen & Aufbauten", "badge": "Formen"},
    {"id": "lichtkuppel", "title": "Lichtkuppel", "badge": "Aufbauten"},
    {"id": "neueindeckung", "title": "Neueindeckung", "badge": "Sanierung"},
    {"id": "sanierung-ausbau", "title": "Sanierung & Ausbau", "badge": "Sanierung"},
    {"id": "daemmung-energie", "title": "Dämmung & Energie", "badge": "Energie"},
    {"id": "gruendach", "title": "Gründach", "badge": "Energie"},
    {"id": "foerderung-baurecht", "title": "Förderung & Baurecht", "badge": "Förderung"},
    {"id": "denkmalschutz-dach", "title": "Denkmalschutz", "badge": "Förderung"},
]

HEATINGTERMS = [
    {"id": "waermepumpe", "title": "Wärmepumpe", "badge": "Heizung"},
    {"id": "luft-waermepumpe", "title": "Luft-Wärmepumpe", "badge": "Heizung"},
    {"id": "erdwaerme", "title": "Erdwärme", "badge": "Heizung"},
    {"id": "gasheizung", "title": "Gasheizung", "badge": "Heizung"},
    {"id": "brennwertheizung", "title": "Brennwertheizung", "badge": "Heizung"},
    {"id": "fussbodenheizung", "title": "Fußbodenheizung", "badge": "Heizung"},
    {"id": "heizkoerper", "title": "Heizkörper", "badge": "Heizung"},
    {"id": "thermostat", "title": "Thermostat", "badge": "Steuerung"},
    {"id": "heizungssanierung", "title": "Heizungssanierung", "badge": "Sanierung"},
    {"id": "rohrleitungen", "title": "Rohrleitungen", "badge": "Sanitär"},
    {"id": "abwasser", "title": "Abwasser", "badge": "Sanitär"},
    {"id": "trinkwasser", "title": "Trinkwasser", "badge": "Sanitär"},
    {"id": "durchlauferhitzer", "title": "Durchlauferhitzer", "badge": "Sanitär"},
    {"id": "badsanierung", "title": "Bad Sanierung", "badge": "Sanierung"},
    {"id": "klimaanlage", "title": "Klimaanlage", "badge": "Klima"},
    {"id": "solarthermie", "title": "Solarthermie", "badge": "Energie"},
]

html = '''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Glossar - Fachbegriffe für Dach und Heizung erklärt</title>
  <meta name="description" content="Dachdecker Glossar und Heizung & Sanitär Glossar: Fachbegriffe einfach erklärt - von Bitumenbahn bis Wärmepumpe.">
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
        <h1>Glossar - Fachbegriffe einfach erklärt</h1>
        <p class="hero__sub">Was ist eine Wärmepumpe? Was bedeutet GEG? Was ist der Unterschied zwischen Bitumenbahn und FPO? Hier finden Sie Fachbegriffe rund ums Dach und um Heizung - verständlich erklärt.</p>
      </div>
    </div>
  </section>

  <section class="section section--light">
    <div class="container">
      <h2 style="margin-bottom:1rem">Dachdecker & Zimmerei</h2>
      <div class="grid grid--3">
'''

for t in DACHTERMS:
    html += f'''        <a href="/glossar/{t["id"]}/" class="card card--link">
          <div class="card-badge" style="margin-top:0;margin-bottom:8px">{t["badge"]}</div>
          <h3>{t["title"]}</h3>
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

for t in HEATINGTERMS:
    html += f'''        <a href="/glossar/{t["id"]}/" class="card card--link">
          <div class="card-badge" style="margin-top:0;margin-bottom:8px">{t["badge"]}</div>
          <h3>{t["title"]}</h3>
        </a>
'''

html += '''
      </div>
    </div>
  </section>

  <section class="section cta-section" id="angebot">
    <div class="container">
      <div class="cta-grid">
        <div class="cta-content">
          <span class="section__tag" style="color:#bfdbfe">Kostenlos anfragen</span>
          <h2>Jetzt Angebote von regionalen Fachbetrieben einholen</h2>
          <p>Sie wissen jetzt, was die Fachbegriffe bedeuten. Der nächste Schritt: kostenlos bis zu drei Angebote von geprüften Betrieben in Ihrer Region.</p>
          <a href="/#angebot" class="btn btn--primary btn--lg">Kostenlos Angebot anfordern</a>
        </div>
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

with open("glossar/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated: glossar/index.html")