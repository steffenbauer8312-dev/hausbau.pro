#!/usr/bin/env python3
"""Generate niche landing pages /dach/ and /bad/."""

DACH_SERVICES = [
    {"id": "dachdecker", "name": "Dachdecker", "desc": "Dacheindeckung, Ziegeldächer, Schieferdächer, Metalldächer. Neu, Sanierung, Reparatur.", "tag": "Steildach"},
    {"id": "flachdach", "name": "Flachdach", "desc": "Flachdachabdichtung, Bitumen, Kunststoffbahnen, Begrünung. Sanierung und Neuanlage.", "tag": "Flachdach"},
    {"id": "dachsanierung", "name": "Dachsanierung", "desc": "Vollständige Dachsanierung: Dämmung, Eindeckung, Unterkonstruktion. Fördermittel inklusive.", "tag": "Sanierung"},
    {"id": "dachausbau", "name": "Dachausbau", "desc": "Dachgeschoss ausbauen, Spitzboden nutzbar machen. Wohnraumerweiterung mit Expertise.", "tag": "Ausbau"},
    {"id": "dachfenster", "name": "Dachfenster & Velux", "desc": "Velux-Einbau, Dachflächenfenster, Tageslichtsysteme. Lichteinfall verbessern, Energie sparen.", "tag": "Velux"},
    {"id": "zimmermann", "name": "Zimmerei & Holzbau", "desc": "Dachstuhl bauen und sanieren, Carports, Terrassenüberdachungen, Pergolen. Alles aus einer Hand.", "tag": "Holzbau"},
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

def generate_dach_landing():
    services_html = ""
    for s in DACH_SERVICES:
        services_html += f'''        <a href="/dach/{s["id"]}/berlin/" class="service-card">
          <div class="service-card__icon">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z" stroke="#fff" stroke-width="2"/><polyline points="9,22 9,12 15,12 15,22" stroke="#fff" stroke-width="2"/></svg>
          </div>
          <h3>{s["name"]}</h3>
          <p>{s["desc"]}</p>
          <span class="service-card__tag">{s["tag"]}</span>
        </a>
'''

    cities_html = ""
    for c in CITIES:
        cities_html += f'''              <a href="/dach/dachdecker/{c["id"]}/" class="btn btn--primary">{c["name"]}</a>
'''

    return f'''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dachdecker & Zimmerei – Kostenlos Angebote vergleichen | hausbau.pro</title>
  <meta name="description" content="Dachdecker, Dachsanierung, Flachdach, Dachausbau - eine Anfrage, bis zu drei Angebote. 100% kostenlos für ganz Deutschland.">
  <link rel="stylesheet" href="/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
  <header class="header">
    <div class="container header__inner">
      <a href="/" class="logo">hausbau<span class="logo-accent">.pro</span></a>
      <nav class="nav">
        <a href="/dach/" class="nav__link nav__link--active">Dach</a>
        <a href="/bad/" class="nav__link">Heizung & Bad</a>
        <a href="/dach/blog/" class="nav__link">Blog</a>
        <a href="/dach/glossar/" class="nav__link">Glossar</a>
        <a href="#angebot" class="btn btn--header">Kostenlos anfragen</a>
      </nav>
      <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </header>

  <section class="hero hero--small">
    <div class="container">
      <div class="hero__content">
        <h1>Dachdecker & Zimmerei</h1>
        <p class="hero__sub">Dachdecker, Dachsanierung, Flachdach, Dachausbau und Zimmerei. Eine Anfrage - bis zu drei Angebote von geprüften Betrieben in Ihrer Region.</p>
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
      <h2 style="margin-bottom:2rem">Dachdecker in Ihrer Stadt</h2>
      <div style="display:flex;gap:1rem;flex-wrap:wrap;justify-content:center">
{cities_html}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <h2 style="margin-bottom:2rem">Mehr Wissen</h2>
      <div class="grid grid--3">
        <a href="/dach/blog/" class="card card--link"><h3>Dachdecker Blog</h3><p>Kosten, Förderung, GEG-Pflicht - alles rund ums Dach.</p></a>
        <a href="/dach/glossar/" class="card card--link"><h3>Dachdecker Glossar</h3><p>Fachbegriffe von Bitumenbahn bis Zwischensparrendämmung.</p></a>
        <a href="/dach/dachdecker/koeln/" class="card card--link"><h3>Dachdecker Köln</h3><p>Geprüfte Betriebe, NRW-Bank Förderung, Gründerzeit.</p></a>
      </div>
    </div>
  </section>

  <section class="section cta-section" id="angebot">
    <div class="container">
      <div class="cta-grid">
        <div class="cta-content">
          <span class="section__tag" style="color:#bfdbfe">Kostenlos anfragen</span>
          <h2>Jetzt Angebote von regionalen Dachdeckern einholen</h2>
          <p>Sie haben ein Dachprojekt? Eine Anfrage - bis zu drei Angebote von geprüften Dachdeckern in Ihrer Region. Keine Verpflichtung.</p>
          <a href="#angebot" class="btn btn--primary btn--lg">Kostenlos Angebot anfordern</a>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand"><span class="logo">hausbau<span class="logo-accent">.pro</span></span><p>Kostenlose Vermittlung von geprüften Dachdeckern und Zimmereien in ganz Deutschland.</p></div>
      <div class="footer__links"><h4>Wissen</h4><a href="/dach/glossar/">Glossar</a><a href="/dach/blog/">Blog</a></div>
      <div class="footer__links"><h4>Leistungen</h4><a href="/dach/dachdecker/">Dachdecker</a><a href="/dach/dachsanierung/">Dachsanierung</a><a href="/dach/flachdach/">Flachdach</a></div>
    </div>
  </footer>
  <script src="/js/main.js"></script>
</body>
</html>'''


BAD_SERVICES = [
    {"id": "waermepumpe", "name": "Wärmepumpe", "desc": "Luft-Wärmepumpe, Sole-Wärmepumpe, Erdwärme. Förderung inklusive. Effizient heizen.", "tag": "Wärmepumpe"},
    {"id": "heizungsbau", "name": "Heizungsbau", "desc": "Gasheizung, Brennwertheizung, Heizkörper, Fußbodenheizung. Neu und Austausch.", "tag": "Heizung"},
    {"id": "sanitaer", "name": "Sanitär", "desc": "Rohrleitungen, Armaturen, Wasseraufbereitung. Alles rund um Sanitär.", "tag": "Sanitär"},
    {"id": "klimaanlage", "name": "Klimaanlage", "desc": "Split-Klimaanlage, Multi-Split, Wartung. Kühlen und Heizen mit einer Anlage.", "tag": "Klima"},
    {"id": "badsanierung", "name": "Bad Sanierung", "desc": "Komplettsanierung, Dusche statt Wanne, barrierefreies Bad. Alles aus einer Hand.", "tag": "Bad"},
    {"id": "solarthermie", "name": "Solarthermie", "desc": "Solarthermieanlage für warmes Wasser. Förderung durch BAFA. Sonnenenergie nutzen.", "tag": "Solar"},
]

def generate_bad_landing():
    services_html = ""
    for s in BAD_SERVICES:
        services_html += f'''        <a href="/bad/{s["id"]}/berlin/" class="service-card">
          <div class="service-card__icon">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none"><path d="M12 2L2 7v15h20V7L12 2z" stroke="#fff" stroke-width="2" stroke-linejoin="round"/><path d="M12 22V12" stroke="#fff" stroke-width="2"/></svg>
          </div>
          <h3>{s["name"]}</h3>
          <p>{s["desc"]}</p>
          <span class="service-card__tag">{s["tag"]}</span>
        </a>
'''

    cities_html = ""
    for c in CITIES:
        cities_html += f'''              <a href="/bad/waermepumpe/{c["id"]}/" class="btn btn--primary">{c["name"]}</a>
'''

    return f'''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Heizung & Bad – Kostenlos Angebote vergleichen | hausbau.pro</title>
  <meta name="description" content="Wärmepumpe, Heizungsbau, Klimaanlage, Bad Sanierung - eine Anfrage, bis zu drei Angebote. 100% kostenlos für ganz Deutschland.">
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
        <a href="/bad/" class="nav__link nav__link--active">Heizung & Bad</a>
        <a href="/bad/blog/" class="nav__link">Blog</a>
        <a href="/bad/glossar/" class="nav__link">Glossar</a>
        <a href="#angebot" class="btn btn--header">Kostenlos anfragen</a>
      </nav>
      <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </header>

  <section class="hero hero--small">
    <div class="container">
      <div class="hero__content">
        <h1>Heizung & Bad</h1>
        <p class="hero__sub">Wärmepumpe, Heizungsbau, Klimaanlage und Bad Sanierung. Eine Anfrage - bis zu drei Angebote von geprüften Betrieben in Ihrer Region.</p>
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
      <h2 style="margin-bottom:2rem">Fachbetriebe in Ihrer Stadt</h2>
      <div style="display:flex;gap:1rem;flex-wrap:wrap;justify-content:center">
{cities_html}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <h2 style="margin-bottom:2rem">Mehr Wissen</h2>
      <div class="grid grid--3">
        <a href="/bad/blog/" class="card card--link"><h3>Heizung & Bad Blog</h3><p>Wärmepumpe Kosten, Förderung, Klimaanlage Wartung.</p></a>
        <a href="/bad/glossar/" class="card card--link"><h3>Heizung & Bad Glossar</h3><p>Fachbegriffe von Wärmepumpe bis Trinkwasser.</p></a>
        <a href="/bad/waermepumpe/berlin/" class="card card--link"><h3>Wärmepumpe Berlin</h3><p>Geprüfte Betriebe, Bundesförderung, lokale Expertise.</p></a>
      </div>
    </div>
  </section>

  <section class="section cta-section" id="angebot">
    <div class="container">
      <div class="cta-grid">
        <div class="cta-content">
          <span class="section__tag" style="color:#bfdbfe">Kostenlos anfragen</span>
          <h2>Jetzt Angebote von regionalen Fachbetrieben einholen</h2>
          <p>Sie haben ein Heizungs- oder Sanitärprojekt? Eine Anfrage - bis zu drei Angebote von geprüften Betrieben in Ihrer Region. Keine Verpflichtung.</p>
          <a href="#angebot" class="btn btn--primary btn--lg">Kostenlos Angebot anfordern</a>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand"><span class="logo">hausbau<span class="logo-accent">.pro</span></span><p>Kostenlose Vermittlung von geprüften Heizungsbauern und Installateuren in ganz Deutschland.</p></div>
      <div class="footer__links"><h4>Wissen</h4><a href="/bad/glossar/">Glossar</a><a href="/bad/blog/">Blog</a></div>
      <div class="footer__links"><h4>Leistungen</h4><a href="/bad/waermepumpe/">Wärmepumpe</a><a href="/bad/heizungsbau/">Heizungsbau</a><a href="/bad/klimaanlage/">Klimaanlage</a></div>
    </div>
  </footer>
  <script src="/js/main.js"></script>
</body>
</html>'''


def main():
    import os
    os.makedirs("dach", exist_ok=True)
    os.makedirs("bad", exist_ok=True)

    with open("dach/index.html", "w", encoding="utf-8") as f:
        f.write(generate_dach_landing())
    print("Generated: dach/index.html")

    with open("bad/index.html", "w", encoding="utf-8") as f:
        f.write(generate_bad_landing())
    print("Generated: bad/index.html")


if __name__ == "__main__":
    main()