#!/usr/bin/env python3
"""Generate Solar/Photovoltaik niche landing page /solar/."""

SOLAR_SERVICES = [
    {"id": "balkonkraftwerk", "name": "Balkonkraftwerk", "desc": "Mini-Solaranlage für den Balkon. 800W Plug-in, Mieterstrom, EEG-frei. Jetzt anmelden.", "tag": "Mini PV"},
    {"id": "pv-anlage", "name": "PV-Anlage", "desc": "Komplett-PV-Anlage für Hausdach. 5-15 kWp, Netzparallel oder Insel. Förderung inklusive.", "tag": "Photovoltaik"},
    {"id": "pv-anlage-angebot", "name": "PV-Angebot", "desc": "Kostenloses Angebot für PV-Anlage einholen. Bis zu drei Betriebe aus Ihrer Region.", "tag": "Angebot"},
    {"id": "wallbox", "name": "Wallbox", "desc": "E-Auto Ladestation für zu Hause. 11kW oder 22kW, with oder ohne PV-Anbindung.", "tag": "E-Mobilität"},
    {"id": "pv-speicher", "name": "PV-Speicher", "desc": "Stromspeicher für PV-Anlage. 5-15 kWh Lithium. Eigenverbrauch auf 80% steigern.", "tag": "Batterie"},
    {"id": "pv-montage", "name": "PV-Montage", "desc": "PV-Installation und Montage. Von Aufdach bis Indach. Alles aus einer Hand.", "tag": "Montage"},
    {"id": "pv-wartung", "name": "PV-Wartung", "desc": "Wartung, Reinigung, Inspektion. Ertragssicherheit und lange Lebensdauer.", "tag": "Service"},
    {"id": "pv-carport", "name": "PV-Carport", "desc": "Carport mit Solarüberdachung. E-Auto laden beim Parken. Doppelte Nutzung.", "tag": "Carport"},
    {"id": "solarthermie", "name": "Solarthermie", "desc": "Solarthermie für warmes Wasser. Heizungsunterstützung möglich. BAFA-Förderung.", "tag": "Solar"},
    {"id": "pv-beratung", "name": "PV-Beratung", "desc": "Beratung zu PV, Speicher, Wallbox. Unabhängig, professionell, vor Ort.", "tag": "Beratung"},
    {"id": "pv-nachruestung", "name": "PV-Nachrüstung", "desc": "Speicher nachrüsten, PV erweitern, Wallbox nachrüsten. Bestehende Anlage optimieren.", "tag": "Nachrüstung"},
    {"id": "freiflaechen-pv", "name": "Freiflächen-PV", "desc": "Freiflächenanlage, Agri-PV, Parkplatz-PV. Gewerblich und privat. Flächennutzung.", "tag": "Freifläche"},
]

CITIES = [
    {"id": "berlin", "name": "Berlin"},
    {"id": "muenchen", "name": "München"},
    {"id": "hamburg", "name": "Hamburg"},
    {"id": "koeln", "name": "Köln"},
    {"id": "stuttgart", "name": "Stuttgart"},
    {"id": "dortmund", "name": "Dortmund"},
    {"id": "hannover", "name": "Hannover"},
    {"id": "frankfurt", "name": "Frankfurt"},
    {"id": "duesseldorf", "name": "Düsseldorf"},
    {"id": "leipzig", "name": "Leipzig"},
    {"id": "bremen", "name": "Bremen"},
    {"id": "nuernberg", "name": "Nürnberg"},
    {"id": "mannheim", "name": "Mannheim"},
    {"id": "freiburg", "name": "Freiburg"},
]

def generate_solar_landing():
    services_html = ""
    for s in SOLAR_SERVICES:
        services_html += f'''        <a href="/solar/{s["id"]}/berlin/" class="service-card">
          <div class="service-card__icon">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="5" stroke="#fff" stroke-width="2"/><line x1="12" y1="1" x2="12" y2="3" stroke="#fff" stroke-width="2"/><line x1="12" y1="21" x2="12" y2="23" stroke="#fff" stroke-width="2"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64" stroke="#fff" stroke-width="2"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78" stroke="#fff" stroke-width="2"/><line x1="1" y1="12" x2="3" y2="12" stroke="#fff" stroke-width="2"/><line x1="21" y1="12" x2="23" y2="12" stroke="#fff" stroke-width="2"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36" stroke="#fff" stroke-width="2"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22" stroke="#fff" stroke-width="2"/></svg>
          </div>
          <h3>{s["name"]}</h3>
          <p>{s["desc"]}</p>
          <span class="service-card__tag">{s["tag"]}</span>
        </a>
'''

    cities_html = ""
    for c in CITIES:
        cities_html += f'''              <a href="/solar/pv-anlage/{c["id"]}/" class="btn btn--primary">{c["name"]}</a>
'''

    return f'''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Photovoltaik & Solar - Kostenlos Angebote vergleichen | hausbau.pro</title>
  <meta name="description" content="PV-Anlage, Balkonkraftwerk, Speicher, Wallbox - eine Anfrage, bis zu drei Angebote. 100% kostenlos für ganz Deutschland.">
  <link rel="stylesheet" href="/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
  <header class="header">
    <div class="container header__inner">
      <a href="/" class="logo">hausbau<span class="logo-accent">.pro</span></a>
      <nav class="nav">
        <a href="/dach/" class="nav__link">Dach</a>
        <a href="/bad/" class="nav__link">Heizung & Bad</a>
        <a href="/solar/" class="nav__link nav__link--active">Solar & PV</a>
        <a href="/solar/blog/" class="nav__link">Blog</a>
        <a href="/solar/glossar/" class="nav__link">Glossar</a>
        <a href="#angebot" class="btn btn--header">Kostenlos anfragen</a>
      </nav>
      <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </header>

  <section class="hero hero--small">
    <div class="container">
      <div class="hero__content">
        <h1>Solar & Photovoltaik</h1>
        <p class="hero__sub">PV-Anlage, Balkonkraftwerk, Speicher, Wallbox und mehr. Eine Anfrage - bis zu drei Angebote von geprüften Betrieben in Ihrer Region.</p>
      </div>
    </div>
  </section>

  <section class="section section--dark" id="services">
    <div class="container">
      <h2 class="section__title section__title--light">Unsere Leistungen</h2>
      <div class="services">
{services_html}
      </div>
    </div>
  </section>

  <section class="section section--light">
    <div class="container">
      <h2 style="margin-bottom:2rem">PV-Anlage in Ihrer Stadt</h2>
      <div style="display:flex;gap:1rem;flex-wrap:wrap;justify-content:center">
{cities_html}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <h2 style="margin-bottom:2rem">Mehr Wissen</h2>
      <div class="grid grid--3">
        <a href="/solar/blog/" class="card card--link"><h3>Solar Blog</h3><p>Kosten, Förderung, EEG 2023 - alles rund um Solar und PV.</p></a>
        <a href="/solar/glossar/" class="card card--link"><h3>Solar Glossar</h3><p>Fachbegriffe von Wechselrichter bis Balkonkraftwerk.</p></a>
        <a href="/solar/pv-anlage/koeln/" class="card card--link"><h3>PV-Anlage Köln</h3><p>Geprüfte Betriebe, NRW-Förderung, Rheinland.</p></a>
      </div>
    </div>
  </section>

  <section class="section cta-section" id="angebot">
    <div class="container">
      <div class="cta-grid">
        <div class="cta-content">
          <span class="section__tag" style="color:#bfdbfe">Kostenlos anfragen</span>
          <h2>Jetzt Angebote von regionalen PV-Installateuren einholen</h2>
          <p>Sie haben ein Solarprojekt? Eine Anfrage - bis zu drei Angebote von geprüften PV-Installateuren in Ihrer Region. Keine Verpflichtung.</p>
          <a href="#angebot" class="btn btn--primary btn--lg">Kostenlos Angebot anfordern</a>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand"><span class="logo">hausbau<span class="logo-accent">.pro</span></span><p>Kostenlose Vermittlung von geprüften PV-Installateuren in ganz Deutschland.</p></div>
      <div class="footer__links"><h4>Wissen</h4><a href="/solar/glossar/">Glossar</a><a href="/solar/blog/">Blog</a></div>
      <div class="footer__links"><h4>Leistungen</h4><a href="/solar/balkonkraftwerk/">Balkonkraftwerk</a><a href="/solar/pv-anlage/">PV-Anlage</a><a href="/solar/pv-speicher/">PV-Speicher</a></div>
    </div>
  </footer>
  <script src="/js/main.js"></script>
</body>
</html>'''

if __name__ == "__main__":
    import os
    os.makedirs("solar", exist_ok=True)
    html = generate_solar_landing()
    with open("solar/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated solar/index.html")