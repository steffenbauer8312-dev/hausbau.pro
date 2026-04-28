#!/usr/bin/env python3
"""Generate heating/sanitary branch glossary for /bad/glossar/."""

TERMS = [
    {
        "id": "waermepumpe",
        "title": "Wärmepumpe - Was ist das und wie funktioniert sie?",
        "meta_desc": "Wärmepumpe erklärt: Funktionsweise, Typen (Luft, Sole, Erdwärme), Kosten, Förderung. Alles was Sie über Wärmepumpen wissen müssen.",
        "badge": "Heizung",
        "content": [
            {"h2": "Was ist eine Wärmepumpe?"},
            {"p": "Eine Wärmepumpe ist ein Heizsystem, das Wärme aus der Umgebung (Luft, Erde, Wasser) aufnimmt und für die Raumheizung nutzt. Sie funktioniert nach dem gleichen Prinzip wie ein Kühlschrank - nur umgekehrt."},
            {"h2": "Welche Arten von Wärmepumpen gibt es?"},
            {"p": "Es gibt drei Haupttypen: Luft-Wärmepumpen holen die Wärme aus der Außenluft. Sie sind am günstigsten. Sole-Wärmepumpen nutzen die Erdwärme über Flächenkollektoren oder Erdsonden. Sie sind effizienter, aber teurer."},
            {"h2": "Effizienz und Kosten"},
            {"p": "Die Effizienz einer Wärmepumpe wird durch die Jahresarbeitszahl (JAZ) ausgedrückt. Eine JAZ von 3,5 bedeutet: Für 1 kWh Strom erhalten Sie 3,5 kWh Wärme. Die Anschaffungskosten liegen zwischen 15.000 und 45.000 Euro je nach Typ."},
            {"h2": "Lohnt sich eine Wärmepumpe?"},
            {"p": "Eine Wärmepumpe lohnt sich besonders in gut gedämmten Gebäuden mit einer Vorlauftemperatur unter 55 Grad. Das sind Neubauten und sanierte Altbauten."}
        ],
        "related": ["fussbodenheizung", "brennwertheizung", "gasheizung"]
    },
    {
        "id": "fussbodenheizung",
        "title": "Fußbodenheizung - Komfort und Effizienz",
        "meta_desc": "Fußbodenheizung: Kosten, Installation, Vor- und Nachteile. Wann sie sich lohnt und wie sie mit einer Wärmepumpe zusammenarbeitet.",
        "badge": "Heizung",
        "content": [
            {"h2": "Was ist eine Fußbodenheizung?"},
            {"p": "Eine Fußbodenheizung ist ein Heizsystem, bei dem die Heizrohre unter dem Boden verlegt werden. Die Wärme wird gleichmäßig über die gesamte Fläche abgegeben."},
            {"h2": "Vorteile der Fußbodenheizung"},
            {"p": "Die Vorteile: Hoher Komfort durch gleichmäßige Wärme, keine sichtbaren Heizkörper, gut geeignet für Wärmepumpen wegen der niedrigen Vorlauftemperatur."},
            {"h2": "Nachteile und Kosten"},
            {"p": "Die Nachteile: Höhere Installationskosten als Heizkörper, langsame Reaktionszeit. Die Kosten liegen bei 80 bis 140 Euro pro m² inklusive Installation."}
        ],
        "related": ["waermepumpe", "thermostat", "heizkoerper"]
    },
    {
        "id": "durchlauferhitzer",
        "title": "Durchlauferhitzer - Dezentrale Warmwasserbereitung",
        "meta_desc": "Durchlauferhitzer: Kosten, Funktion, Vor- und Nachteile. Wann sich ein Durchlauferhitzer lohnt.",
        "badge": "Sanitär",
        "content": [
            {"h2": "Was ist ein Durchlauferhitzer?"},
            {"p": "Ein Durchlauferhitzer erhitzt das Wasser erst dann, wenn Sie es brauchen. Im Gegensatz zum Warmwasserspeicher hat er keinen Vorratstank."},
            {"h2": "Arten von Durchlauferhitzern"},
            {"p": "Es gibt zwei Arten: Gas-Durchlauferhitzer sind effizient und können große Mengen warmes Wasser liefern. Elektrische Durchlauferhitzer sind günstiger in der Anschaffung, aber teurer im Betrieb."},
            {"h2": "Kosten und Effizienz"},
            {"p": "Die Kosten für einen Gas-Durchlauferhitzer liegen bei 500 bis 1.500 Euro. Ein elektrischer Durchlauferhitzer kostet 200 bis 600 Euro."}
        ],
        "related": ["trinkwasser", "rohrleitungen"]
    },
    {
        "id": "gasheizung",
        "title": "Gasheizung - Der Klassiker unter den Heizsystemen",
        "meta_desc": "Gasheizung: Kosten, Funktion, Wirkungsgrad. Was Sie über Gasheizungen wissen müssen.",
        "badge": "Heizung",
        "content": [
            {"h2": "Was ist eine Gasheizung?"},
            {"p": "Eine Gasheizung verbrennt Erdgas oder Flüssiggas, um Wasser zu erwärmen. Das warme Wasser wird für die Raumheizung und die Warmwasserbereitung genutzt."},
            {"h2": "Brennwerttechnik"},
            {"p": "Moderne Gasheizungen nutzen die Brennwerttechnik. Das erhöht den Wirkungsgrad auf über 100 Prozent."},
            {"h2": "Kosten und Lebensdauer"},
            {"p": "Eine neue Gas-Brennwertheizung kostet 8.000 bis 18.000 Euro inklusive Installation. Die Lebensdauer liegt bei 15 bis 20 Jahren."}
        ],
        "related": ["brennwertheizung", "waermepumpe", "heizkoerper"]
    },
    {
        "id": "brennwertheizung",
        "title": "Brennwertheizung - Effiziente Nutzung der Energie",
        "meta_desc": "Brennwertheizung erklärt: Wie funktioniert sie, was bringt sie, welche Kosten kommen auf Sie zu.",
        "badge": "Heizung",
        "content": [
            {"h2": "Was ist eine Brennwertheizung?"},
            {"p": "Eine Brennwertheizung nutzt die Energie des Brennstoffs fast vollständig aus. Neben der Wärme der Flamme nutzt sie auch die Wärme aus den entstehenden Abgasen."},
            {"h2": "Brennwert bei Gas und Öl"},
            {"p": "Brennwerttechnik gibt es sowohl für Gas als auch für Öl. Gas hat den Vorteil, dass es bereits jetzt schon zu einem großen Teil aus erneuerbarem Methan gemischt werden kann."},
            {"h2": "Was bringt die Brennwerttechnik?"},
            {"p": "Im Vergleich zu einer alten Niedertemperaturheizung spart eine Brennwertheizung etwa 15 bis 30 Prozent Energie."},
            {"h2": "Kosten einer Brennwertheizung"},
            {"p": "Die Kosten für eine Gas-Brennwertheizung liegen bei 8.000 bis 18.000 Euro."}
        ],
        "related": ["gasheizung", "waermepumpe", "heizungssanierung"]
    },
    {
        "id": "klimaanlage",
        "title": "Klimaanlage - Kühlung für Wohnung und Büro",
        "meta_desc": "Klimaanlage: Kosten, Typen, Funktion. Split, Multi-Split, mobil - was für Ihr Zuhause passt.",
        "badge": "Klima",
        "content": [
            {"h2": "Wie funktioniert eine Klimaanlage?"},
            {"p": "Eine Klimaanlage funktioniert nach dem Prinzip der Wärmepumpe. Sie entzieht der Raumluft Wärme und leitet sie nach außen ab."},
            {"h2": "Arten von Klimaanlagen"},
            {"p": "Die Split-Klimaanlage hat ein Innengerät und ein Außengerät. Eine Multi-Split-Anlage hat ein Außengerät und mehrere Innengeräte."},
            {"h2": "Kosten einer Klimaanlage"},
            {"p": "Eine Split-Klimaanlage kostet 2.500 bis 5.000 Euro inklusive Installation. Eine Multi-Split-Anlage mit drei Innengeräten liegt bei 8.000 bis 12.000 Euro."}
        ],
        "related": ["waermepumpe"]
    },
    {
        "id": "solarthermie",
        "title": "Solarthermie - Wärme von der Sonne",
        "meta_desc": "Solarthermie: Kosten, Nutzen, Förderung. Wie Sie mit Solarthermie warmes Wasser erzeugen.",
        "badge": "Energie",
        "content": [
            {"h2": "Was ist Solarthermie?"},
            {"p": "Solarthermie nutzt die Sonnenenergie, um Wasser zu erwärmen. Auf dem Dach werden Sonnenkollektoren montiert, die die Wärme des Sonnenlichts einfangen."},
            {"h2": "Vorteile der Solarthermie"},
            {"p": "Die Vorteile: kostenlose Energiequelle, reduziert Heizkosten im Sommer, kann Heizung im Winter unterstützen. Im Sommer kann eine Solarthermieanlage den Großteil des Warmwasserbedarfs decken."},
            {"h2": "Kosten und Förderung"},
            {"p": "Die Kosten für eine Solarthermieanlage liegen bei 4.000 bis 8.000 Euro für reine Warmwasserbereitung. Die BAFA fördert Solarthermie mit 25 Prozent der Kosten."}
        ],
        "related": ["waermepumpe", "photovoltaik"]
    },
    {
        "id": "heizkoerper",
        "title": "Heizkörper - Funktion und Auswahl",
        "meta_desc": "Heizkörper: Typen, Kosten, Effizienz. Welcher Heizkörper für welche Situation geeignet ist.",
        "badge": "Heizung",
        "content": [
            {"h2": "Arten von Heizkörpern"},
            {"p": "Es gibt viele verschiedene Heizkörpertypen: Flachheizkörper sind flach und modern. Badheizkörper sind speziell fürs Badezimmer konzipiert."},
            {"h2": "Größe und Leistung"},
            {"p": "Die Leistung eines Heizkörpers wird in Watt angegeben und muss zum Raum passen. Für ein gut gedämmtes Zimmer mit 20 m² braucht man etwa 1.500 bis 2.000 Watt."},
            {"h2": "Kosten und Austausch"},
            {"p": "Die Kosten für einen neuen Flachheizkörper liegen bei 200 bis 500 Euro pro Stück. Dazu kommen die Installationskosten von 100 bis 300 Euro."}
        ],
        "related": ["fussbodenheizung", "thermostat", "gasheizung"]
    },
    {
        "id": "thermostat",
        "title": "Thermostat - Die Steuerung der Heizung",
        "meta_desc": "Thermostat: Funktion, Arten, smarte Lösungen. So steuern Sie Ihre Heizung effizient.",
        "badge": "Steuerung",
        "content": [
            {"h2": "Wie funktioniert ein Thermostat?"},
            {"p": "Ein Thermostat misst die Raumtemperatur und regelt die Heizleistung entsprechend. Wenn die gewünschte Temperatur erreicht ist, drosselt das Thermostat die Heizung."},
            {"h2": "Arten von Thermostaten"},
            {"p": "Mechanische Thermostate sind einfach und günstig. Elektronische Thermostate sind genauer. Smarte Thermostate können per App gesteuert werden und lernen aus Ihrem Verhalten."},
            {"h2": "Smarte Thermostate"},
            {"p": "Smarte Thermostate bieten viele Vorteile: Fernsteuerung per App, Zeitprogramme für jeden Raum. Sie können die Heizkosten um 10 bis 20 Prozent senken."}
        ],
        "related": ["fussbodenheizung", "heizkoerper", "waermepumpe"]
    },
    {
        "id": "rohrleitungen",
        "title": "Rohrleitungen - Das Netzwerk der Heizung",
        "meta_desc": "Rohrleitungen: Materialien, Kosten, Verlegung. Was Sie über Heizungsrohre wissen müssen.",
        "badge": "Sanitär",
        "content": [
            {"h2": "Materialien für Heizungsrohre"},
            {"p": "Die gängigsten Materialien für Heizungsrohre sind Kupfer, Stahl und Kunststoff. Kupferrohre sind langlebig und korrosionsbeständig. Kunststoffrohre sind günstig und korrosionsfrei."},
            {"h2": "Verlegung und Kosten"},
            {"p": "Heizungsrohre werden entweder aufputz oder unterputz verlegt. Die Kosten für Rohrleitungen liegen bei 25 bis 50 Euro pro Meter inklusive Verlegung."},
            {"h2": "Dämmung der Rohre"},
            {"p": "Heizungsrohre sollten gedämmt werden, um Wärmeverluste zu vermeiden. Das betrifft besonders Rohre in unbeheizten Räumen."}
        ],
        "related": ["trinkwasser", "abwasser"]
    },
    {
        "id": "abwasser",
        "title": "Abwasser - Der Weg des Schmutzwassers",
        "meta_desc": "Abwasser: Systeme, Kosten, Wartung. Was Sie über die Abwasserentsorgung wissen müssen.",
        "badge": "Sanitär",
        "content": [
            {"h2": "Wie funktioniert die Abwasserentsorgung?"},
            {"p": "Das Abwasser wird über ein Netzwerk von Rohren zu einer zentralen Kläranlage geleitet. Das Wasser muss über Gefälle abfließen können."},
            {"h2": "Arten von Abwassersystemen"},
            {"p": "Es gibt zwei Hauptarten: Mischwasserkanalisation führt alle Abwässer zusammen. Trennkanalisation führt Schmutz- und Regenwasser getrennt."},
            {"h2": "Wartung und Probleme"},
            {"p": "Abwasserrohre sind wartungsarm, können aber verstopfen. Bei Problemen helfen Rohrreinigungsfirmen - die Kosten liegen bei 100 bis 300 Euro."}
        ],
        "related": ["trinkwasser", "rohrleitungen"]
    },
    {
        "id": "trinkwasser",
        "title": "Trinkwasser - Qualität und Aufbereitung",
        "meta_desc": "Trinkwasser: Qualität, Filter, Enthärtung. Was Sie über Ihr Trinkwasser wissen sollten.",
        "badge": "Sanitär",
        "content": [
            {"h2": "Trinkwasserqualität in Deutschland"},
            {"p": "In Deutschland ist das Trinkwasser von hoher Qualität und muss strenge Grenzwerte einhalten. In einigen Regionen ist das Wasser aber sehr hart."},
            {"h2": "Wasserhärte und Kalk"},
            {"p": "Die Wasserhärte wird in Grad deutscher Härte (°dH) gemessen. In Regionen mit hartem Wasser können Kalkablagerungen in Rohren entstehen."},
            {"h2": "Wasserfilter"},
            {"p": "Wasserfilter werden am Hausanschluss oder an einzelnen Zapfstellen installiert. Sie entfernen Partikel wie Sand oder Rost."}
        ],
        "related": ["durchlauferhitzer", "rohrleitungen", "abwasser"]
    },
    {
        "id": "heizungssanierung",
        "title": "Heizungssanierung - Wann und warum sie sinnvoll ist",
        "meta_desc": "Heizungssanierung: Zeitpunkt, Kosten, Förderung. Wann sich der Austausch der Heizung lohnt.",
        "badge": "Sanierung",
        "content": [
            {"h2": "Wann ist eine Heizungssanierung nötig?"},
            {"p": "Eine Heizungssanierung ist nötig, wenn die Heizung älter als 15 bis 20 Jahre ist oder wenn die Reparaturkosten hoch werden."},
            {"h2": "Was wird gemacht?"},
            {"p": "Eine Heizungssanierung umfasst den Austausch des Wärmeerzeugers, die Erneuerung der Heizkörper und oft auch die Rohrleitungen."},
            {"h2": "Kosten und Förderung"},
            {"p": "Die Kosten für eine komplette Heizungssanierung liegen bei 15.000 bis 40.000 Euro je nach Umfang. Die BEG fördert den Austausch mit bis zu 25 Prozent."}
        ],
        "related": ["waermepumpe", "brennwertheizung", "gasheizung"]
    },
    {
        "id": "luft-waermepumpe",
        "title": "Luft-Wärmepumpe - Der günstige Einstieg in die Wärmepumpe",
        "meta_desc": "Luft-Wärmepumpe: Kosten, Funktion, Effizienz. Für wen sich die Luft-Wärmepumpe lohnt.",
        "badge": "Heizung",
        "content": [
            {"h2": "Was ist eine Luft-Wärmepumpe?"},
            {"p": "Eine Luft-Wärmepumpe nutzt die Wärme aus der Außenluft, um das Gebäude zu heizen. Das Außengerät saugt Außenluft an, entzieht ihr Wärme."},
            {"h2": "Vorteile und Nachteile"},
            {"p": "Die Vorteile: Günstiger als Sole- oder Wasser-Wärmepumpen, einfache Installation ohne Erdarbeiten. Die Nachteile: Bei niedrigen Außentemperaturen sinkt die Effizienz."},
            {"h2": "Kosten und Wirtschaftlichkeit"},
            {"p": "Die Kosten für eine Luft-Wärmepumpe liegen bei 15.000 bis 24.000 Euro inklusive Installation."}
        ],
        "related": ["waermepumpe", "erdwaerme", "fussbodenheizung"]
    },
    {
        "id": "erdwaerme",
        "title": "Erdwärme - Effiziente Heizung aus der Erde",
        "meta_desc": "Erdwärme: Kosten, Nutzung, Förderung. Wie Erdwärmepumpen funktionieren und was sie kosten.",
        "badge": "Heizung",
        "content": [
            {"h2": "Was ist Erdwärme?"},
            {"p": "Erdwärme nutzt die im Erdreich gespeicherte Sonnenenergie. Schon in einem Meter Tiefe ist die Temperatur relativ konstant bei etwa 10 bis 15 Grad."},
            {"h2": "Arten der Erdwärmenutzung"},
            {"p": "Erdkollektoren werden horizontal in etwa 1,5 Meter Tiefe verlegt. Erdbohrungen gehen vertikal in 50 bis 150 Meter Tiefe."},
            {"h2": "Kosten und Effizienz"},
            {"p": "Die Kosten für eine Erdwärmepumpe liegen bei 25.000 bis 45.000 Euro inklusive Erschließung. Die Effizienz ist sehr hoch."}
        ],
        "related": ["waermepumpe", "luft-waermepumpe", "fussbodenheizung"]
    },
    {
        "id": "badsanierung",
        "title": "Bad Sanierung - Vom alten Bad zum modernen Bad",
        "meta_desc": "Bad Sanierung: Kosten, Ablauf, Förderung. Was bei einer Badrenovierung alles auf Sie zukommt.",
        "badge": "Sanierung",
        "content": [
            {"h2": "Wann lohnt sich eine Bad Sanierung?"},
            {"p": "Eine Bad Sanierung lohnt sich, wenn das Bad alt und veraltet ist, wenn Sanitärkeramik nicht mehr funktioniert oder wenn Sie das Bad modernisieren wollen."},
            {"h2": "Was wird gemacht?"},
            {"p": "Bei einer Komplettsanierung werden alle Sanitärgegenstände erneuert, die Fliesen entfernt und neu verlegt, die Leitungen erneuert."},
            {"h2": "Kosten und Zeitrahmen"},
            {"p": "Die Kosten für eine Komplettsanierung liegen bei 15.000 bis 35.000 Euro je nach Ausstattung. Die Dauer beträgt zwei bis vier Wochen."}
        ],
        "related": ["sanitaer-installation", "rohrleitungen", "trinkwasser"]
    }
]


def generate_glossar_entry(term):
    content_html = ""
    for section in term["content"]:
        if "h2" in section:
            content_html += f"          <h2>{section['h2']}</h2>\n"
        if "p" in section:
            content_html += f"          <p>{section['p']}</p>\n"

    related_html = ""
    if term.get("related"):
        related_html = """
      <div>
        <h2>Verwandte Begriffe</h2>
        <div class="grid grid--3">
"""
        for rel_id in term["related"]:
            titles = {
                "waermepumpe": "Wärmepumpe",
                "fussbodenheizung": "Fußbodenheizung",
                "durchlauferhitzer": "Durchlauferhitzer",
                "gasheizung": "Gasheizung",
                "brennwertheizung": "Brennwertheizung",
                "klimaanlage": "Klimaanlage",
                "solarthermie": "Solarthermie",
                "heizkoerper": "Heizkörper",
                "thermostat": "Thermostat",
                "rohrleitungen": "Rohrleitungen",
                "abwasser": "Abwasser",
                "trinkwasser": "Trinkwasser",
                "heizungssanierung": "Heizungssanierung",
                "luft-waermepumpe": "Luft-Wärmepumpe",
                "erdwaerme": "Erdwärme",
                "badsanierung": "Bad Sanierung"
            }
            rel_title = titles.get(rel_id, rel_id)
            rel_desc = {
                "waermepumpe": "Effiziente Heizung aus Umweltwärme.",
                "fussbodenheizung": "Komfortable Niedertemperatur-Heizung.",
                "durchlauferhitzer": "Dezentrale Warmwasserbereitung.",
                "gasheizung": "Der Klassiker unter den Heizsystemen.",
                "brennwertheizung": "Effiziente Nutzung der Energie.",
                "klimaanlage": "Kühlung für Wohnung und Büro.",
                "solarthermie": "Wärme von der Sonne.",
                "heizkoerper": "Die klassische Art zu heizen.",
                "thermostat": "Steuerung der Heizung.",
                "rohrleitungen": "Das Netzwerk der Heizung.",
                "abwasser": "Der Weg des Schmutzwassers.",
                "trinkwasser": "Qualität und Aufbereitung.",
                "heizungssanierung": "Wann und warum sie sinnvoll ist.",
                "luft-waermepumpe": "Der günstige Einstieg.",
                "erdwaerme": "Heizen mit Erdwärme.",
                "badsanierung": "Vom alten Bad zum Neuen."
            }
            rel_desc_text = rel_desc.get(rel_id, "")
            related_html += f'''          <a href="/bad/glossar/{rel_id}/" class="card card--link"><h3>{rel_title}</h3><p>{rel_desc_text}</p></a>
'''

        related_html += "        </div>\n      </div>\n"

    return f'''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{term["title"]}</title>
  <meta name="description" content="{term["meta_desc"]}">
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
        <a href="/bad/blog/" class="nav__link">Blog</a>
        <a href="/bad/glossar/" class="nav__link nav__link--active">Glossar</a>
        <a href="#angebot" class="btn btn--header">Kostenlos anfragen</a>
      </nav>
      <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </header>

  <section class="hero hero--small">
    <div class="container">
      <div class="hero__content">
        <div class="card-badge"><a href="/bad/glossar/" style="color:inherit">Glossar</a></div>
        <h1>{term["title"]}</h1>
        <p class="hero__sub">{term["meta_desc"]}</p>
      </div>
    </div>
  </section>

  <section class="section section--light">
    <div class="container">
      <div class="grid grid--2">
        <div>
{content_html}
        </div>
{related_html}
      </div>
    </div>
  </section>

  <section class="section cta-section" id="angebot">
    <div class="container">
      <div class="cta-grid">
        <div class="cta-content">
          <span class="section__tag" style="color:#bfdbfe">Kostenlos anfragen</span>
          <h2>Jetzt Angebote von regionalen Fachbetrieben einholen</h2>
          <p>Sie wissen jetzt, was die Arbeit kostet. Der nächste Schritt: kostenlos bis zu drei Angebote von geprüften Betrieben in Ihrer Region.</p>
          <a href="#angebot" class="btn btn--primary btn--lg">Kostenlos Angebot anfordern</a>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand"><span class="logo">hausbau<span class="logo-accent">.pro</span></span><p>Kostenlose Vermittlung von geprüften Heizungsbauern und Installateuren in ganz Deutschland.</p></div>
      <div class="footer__links"><h4>Wissen</h4><a href="/bad/glossar/">Glossar</a><a href="/bad/blog/">Blog</a></div>
      <div class="footer__links"><h4>Services</h4><a href="/bad/waermepumpe/">Wärmepumpe</a><a href="/bad/heizungsbau/">Heizungsbau</a><a href="/bad/sanitaer/">Sanitär</a></div>
    </div>
  </footer>
  <script src="/js/main.js"></script>
</body>
</html>'''


def generate_glossar_index():
    GROUPS = {
        "heizung": {
            "title": "Heizung",
            "badge": "Heizung",
            "desc": "Wärmepumpe, Gasheizung, Brennwert, Heizkörper, Fußbodenheizung.",
            "terms": ["waermepumpe", "luft-waermepumpe", "erdwaerme", "gasheizung", "brennwertheizung", "fussbodenheizung", "heizkoerper", "thermostat", "heizungssanierung"]
        },
        "sanitaer": {
            "title": "Sanitär",
            "badge": "Sanitär",
            "desc": "Rohrleitungen, Abwasser, Trinkwasser, Durchlauferhitzer.",
            "terms": ["rohrleitungen", "abwasser", "trinkwasser", "durchlauferhitzer", "badsanierung"]
        },
        "klima": {
            "title": "Klima & Energie",
            "badge": "Klima",
            "desc": "Klimaanlage, Solarthermie.",
            "terms": ["klimaanlage", "solarthermie"]
        }
    }

    index_html = '''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Heizung & Bad Glossar - Fachbegriffe erklärt</title>
  <meta name="description" content="Heizung & Bad Glossar: Fachbegriffe rund um Wärmepumpe, Heizungsbau, Klimaanlage und Bad erklärt.">
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
        <a href="/bad/blog/" class="nav__link">Blog</a>
        <a href="/bad/glossar/" class="nav__link nav__link--active">Glossar</a>
        <a href="#angebot" class="btn btn--header">Kostenlos anfragen</a>
      </nav>
      <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </header>

  <section class="hero hero--small">
    <div class="container">
      <div class="hero__content">
        <h1>Heizung & Bad Glossar - Fachbegriffe erklärt</h1>
        <p class="hero__sub">Was ist eine Wärmepumpe? Was bedeutet Brennwert? Was ist der Unterschied zwischen Trinkwasser und Abwasser? Hier finden Sie Fachbegriffe rund um Heizung und Sanitär.</p>
      </div>
    </div>
  </section>

  <section class="section section--light">
    <div class="container">
      <div class="grid grid--3">
'''
    for group_id, group in GROUPS.items():
        index_html += f'''
        <a href="/bad/glossar/{group_id}/" class="card card--link">
          <div class="card-badge" style="margin-top:0;margin-bottom:12px">{group["badge"]}</div>
          <h3>{group["title"]}</h3>
          <p>{group["desc"]}</p>
          <span class="card__tag">{len(group["terms"])} Begriffe</span>
        </a>
'''

    index_html += '''
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <h2 style="margin-bottom:2rem">Alle Begriffe</h2>
      <div class="grid grid--3">
'''

    for term in TERMS:
        index_html += f'''<a href="/bad/glossar/{term['id']}/" class="card card--link">
          <div class="card-badge" style="margin-top:0;margin-bottom:8px">{term["badge"]}</div>
          <h3>{term["title"].split(" - ")[0]}</h3>
          <p>{term["meta_desc"][:100]}...</p>
        </a>
'''

    index_html += '''
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
          <a href="#angebot" class="btn btn--primary btn--lg">Kostenlos Angebot anfordern</a>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand"><span class="logo">hausbau<span class="logo-accent">.pro</span></span><p>Kostenlose Vermittlung von geprüften Heizungsbauern und Installateuren in ganz Deutschland.</p></div>
      <div class="footer__links"><h4>Wissen</h4><a href="/bad/glossar/">Glossar</a><a href="/bad/blog/">Blog</a></div>
      <div class="footer__links"><h4>Services</h4><a href="/bad/waermepumpe/">Wärmepumpe</a><a href="/bad/heizungsbau/">Heizungsbau</a><a href="/bad/sanitaer/">Sanitär</a></div>
    </div>
  </footer>
  <script src="/js/main.js"></script>
</body>
</html>'''
    return index_html


def main():
    import os
    os.makedirs("bad/glossar", exist_ok=True)

    with open("bad/glossar/index.html", "w", encoding="utf-8") as f:
        f.write(generate_glossar_index())
    print("Generated: bad/glossar/index.html")

    for term in TERMS:
        dir_path = f"bad/glossar/{term['id']}"
        os.makedirs(dir_path, exist_ok=True)

        html = generate_glossar_entry(term)
        with open(f"{dir_path}/index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated: {dir_path}/index.html")


if __name__ == "__main__":
    main()
