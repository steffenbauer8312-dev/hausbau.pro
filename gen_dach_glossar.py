#!/usr/bin/env python3
"""Generate dach branch glossary for /dach/glossar/."""

TERMS = [
    {
        "id": "bitumenbahn",
        "title": "Bitumenbahn - Das klassische Abdichtungsmaterial",
        "meta_desc": "Bitumenbahn: Eigenschaften, Verwendung, Kosten. Alles über das traditionelle Material für Flachdächer.",
        "badge": "Material",
        "content": [
            {"h2": "Was ist eine Bitumenbahn?"},
            {"p": "Eine Bitumenbahn ist ein Abdichtungsmaterial aus Bitumen, das auf Flachdächern und geneigten Dächern verwendet wird. Sie besteht aus einer Trägereinlage (Glasvlies oder Polyester) die mit Bitumen beschichtet ist."},
            {"h2": "Arten von Bitumenbahnen"},
            {"p": "Es gibt Schweißbahnen, die mit dem Brenner aufgeschweißt werden, und kaltselbstklebende Bahnen. Schweißbahnen sind robuster und werden für dauerhafte Abdichtungen verwendet."},
            {"h2": "Verwendung und Kosten"},
            {"p": "Bitumenbahnen werden hauptsächlich für Flachdächer verwendet. Die Kosten liegen bei 10 bis 25 Euro pro m² für Material und Verlegung."}
        ],
        "related": ["fpo-bahn", "pib-bahn", "flachdach"]
    },
    {
        "id": "fpo-bahn",
        "title": "FPO-Bahn - Moderne Kunststoffabdichtung",
        "meta_desc": "FPO-Bahn: Eigenschaften, Vorteile, Kosten. Die moderne Alternative zu Bitumenbahnen.",
        "badge": "Material",
        "content": [
            {"h2": "Was ist eine FPO-Bahn?"},
            {"p": "FPO (Flexible Polyolefin) ist ein moderner Kunststoff für Dachabdichtungen. FPO-Bahnen sind frei von Bitumen und Weichmachern, dadurch langlebiger und umweltfreundlicher."},
            {"h2": "Vorteile der FPO-Bahn"},
            {"p": "Die Vorteile: hohe Lebensdauer von 30 bis 40 Jahren, beständig gegen UV-Strahlung und Temperaturschwankungen, wurzelfest für Begrünungen, recyclebar."},
            {"h2": "Kosten und Verlegung"},
            {"p": "FPO-Bahnen kosten 20 bis 40 Euro pro m² inklusive Verlegung. Sie werden lose verlegt und an den Nähten verschweißt."}
        ],
        "related": ["bitumenbahn", "pib-bahn", "gruendach"]
    },
    {
        "id": "pib-bahn",
        "title": "PIB-Bahn - Elastische Kunststoffabdichtung",
        "meta_desc": "PIB-Bahn: Eigenschaften, Vorteile, Kosten. Für Dachabdichtungen mit höchsten Ansprüchen.",
        "badge": "Material",
        "content": [
            {"h2": "Was ist eine PIB-Bahn?"},
            {"p": "PIB (Polyisobutylen) ist ein hochwertiger Kunststoff für Dachabdichtungen. PIB-Bahnen sind besonders elastisch und haben eine hohe Lebensdauer."},
            {"h2": "Vorteile"},
            {"p": "PIB-Bahnen sind beständig gegen Säuren, Laugen und andere Chemikalien. Sie eignen sich daher besonders für Industriedächer oder Dächer mit besonderen Anforderungen."},
            {"h2": "Kosten"},
            {"p": "PIB-Bahnen kosten 30 bis 50 Euro pro m² und sind damit die hochwertigste Wahl unter den Kunststoffbahnen."}
        ],
        "related": ["bitumenbahn", "fpo-bahn"]
    },
    {
        "id": "tonpfanne",
        "title": "Tonpfanne - Der Klassiker unter den Dacheindeckungen",
        "meta_desc": "Tonpfanne: Eigenschaften, Farben, Kosten. Der traditionelle Werkstoff für Steildächer.",
        "badge": "Material",
        "content": [
            {"h2": "Was ist eine Tonpfanne?"},
            {"p": "Die Tonpfanne ist der klassische Dachziegel in Deutschland. Sie wird aus Ton geformt und bei hoher Temperatur gebrannt. Die Lebensdauer liegt bei 60 bis 100 Jahren."},
            {"h2": "Formen und Farben"},
            {"p": "Es gibt viele Formen: Mönch und Nonne (historisch), Frankfurter Pfanne (weit verbreitet), Harzer Pfanne (für niedrige Dachneigungen). Die Farben reichen von rot über braun bis zu engobiertem schwarz."},
            {"h2": "Kosten"},
            {"p": "Tonpfannen kosten 15 bis 30 Euro pro m² Material. Dazu kommen 40 bis 80 Euro pro m² für die Verlegung."}
        ],
        "related": ["biberschwanz", "schiefer", "dachformen-aufbauten"]
    },
    {
        "id": "biberschwanz",
        "title": "Biberschwanz - Elegante historische Dacheindeckung",
        "meta_desc": "Biberschwanz: Eigenschaften, Verlegung, Kosten. Der elegante Dachziegel für besondere Dächer.",
        "badge": "Material",
        "content": [
            {"h2": "Was ist Biberschwanz?"},
            {"p": "Der Biberschwanz ist ein flacher, rechteckiger Dachziegel mit abgerundeter Unterseite. Er wird in doppelter Lage verlegt und erzeugt eine elegante, historische Optik."},
            {"h2": "Verwendung"},
            {"p": "Biberschwanz eignet sich besonders für Denkmäler und historische Gebäude, aber auch für moderne Architektur mit Bezug auf Tradition."},
            {"h2": "Kosten"},
            {"p": "Biberschwanz kostet 20 bis 40 Euro pro m² Material. Die Verlegung ist aufwendiger als bei Normalziegeln: 60 bis 100 Euro pro m²."}
        ],
        "related": ["tonpfanne", "schiefer", "denkmalschutz-dach"]
    },
    {
        "id": "schiefer",
        "title": "Schiefer - Premium-Dacheindeckung",
        "meta_desc": "Schiefer: Eigenschaften, Vorteile, Kosten. Der langlebige Naturstein für anspruchsvolle Dächer.",
        "badge": "Material",
        "content": [
            {"h2": "Was ist Schiefer?"},
            {"p": "Schiefer ist ein Naturstein, der in dünnen Platten gespalten werden kann. Er wird vor allem in Rheinland-Pfalz, im Schwarzwald und in Spanien abgebaut."},
            {"h2": "Vorteile des Schieferdachs"},
            {"p": "Ein Schieferdach hält 80 bis 150 Jahre. Der Stein ist unfrostsicher, wasserundurchlässig und behält seine Farbe. Schiefer gilt als die hochwertigste Dacheindeckung."},
            {"h2": "Kosten"},
            {"p": "Schiefer kostet 40 bis 80 Euro pro m² Material und Verlegung. Dafür ist ein Schieferdach praktisch wartungsfrei."}
        ],
        "related": ["tonpfanne", "biberschwanz", "dachkonstruktion"]
    },
    {
        "id": "dachkonstruktion",
        "title": "Dachkonstruktion - Das Gerüst des Dachs",
        "meta_desc": "Dachkonstruktion: Sparrendach, Pfettendach, Kehlbalkendach. Die verschiedenen Tragwerke für Dächer.",
        "badge": "Konstruktion",
        "content": [
            {"h2": "Was ist die Dachkonstruktion?"},
            {"p": "Die Dachkonstruktion ist das Tragwerk des Dachs. Sie besteht aus Hölzern, die die Lasten des Dachs aufnehmen und an die Wände weiterleiten."},
            {"h2": "Arten von Dachkonstruktionen"},
            {"p": "Das Sparrendach ist die häufigste Art: Zwei geneigte Sparren bilden ein Dreieck. Das Pfettendach hat waagerechte Pfetten, die die Last auffangen. Das Kehlbalkendach ist eine Kombination."},
            {"h2": "Kosten"},
            {"p": "Die Kosten für eine neue Dachkonstruktion liegen bei 15.000 bis 30.000 Euro für ein Einfamilienhaus, je nach Größe und Komplexität."}
        ],
        "related": ["lattung", "dampfsperre", "zimmermann"]
    },
    {
        "id": "lattung",
        "title": "Lattung - Die Träger für die Dacheindeckung",
        "meta_desc": "Lattung: Material, Maße, Verlegung. Die Holz- oder Metallkonstruktion für Dachziegel.",
        "badge": "Konstruktion",
        "content": [
            {"h2": "Was ist die Lattung?"},
            {"p": "Die Lattung ist ein System aus waagerechten oder senkrechten Hölzern, auf denen die Dacheindeckung befestigt wird. Sie liegt auf der Konterlattung, die wiederum auf den Sparren befestigt ist."},
            {"h2": "Materialien und Maße"},
            {"p": " Traditionell使用的是 Holzlatten (Fichte oder Tanne), 40 bis 60 mm dick. Für größere Spannweiten oder bei Metalldächern werden auch Metallprofile verwendet."},
            {"h2": "Abstände"},
            {"p": "Der Lattenabstand richtet sich nach dem Ziegelformat. Bei einer Frankfurter Pfanne beträgt der Abstand etwa 33 bis 36 cm."}
        ],
        "related": ["dachkonstruktion", "unterspannbahn", "tonpfanne"]
    },
    {
        "id": "dampfsperre",
        "title": "Dampfsperre - Schutz vor Feuchtigkeit",
        "meta_desc": "Dampfsperre: Funktion, Einbau, Kosten. Die unsichtbare Schicht gegen Feuchtigkeitsschäden.",
        "badge": "Konstruktion",
        "content": [
            {"h2": "Was ist eine Dampfsperre?"},
            {"p": "Eine Dampfsperre ist eine Folie, die unter der Dämmung angebracht wird. Sie verhindert, dass warme, feuchte Raumluft in die Dämmung eindringt und dort kondensiert."},
            {"h2": "Warum ist sie wichtig?"},
            {"p": "Wenn Feuchtigkeit in die Dämmung eindringt, reduziert das die Dämmwirkung und kann zu Schimmelbildung und Bauschäden führen. Die Dampfsperre ist daher ein wichtiger Teil des Dachaufbaus."},
            {"h2": "Einbau und Kosten"},
            {"p": "Die Dampfsperre wird vor der Dämmung an den Innenseiten der Sparren befestigt. Die Kosten liegen bei 5 bis 15 Euro pro m²."}
        ],
        "related": ["unterspannbahn", "daemmung-energie", "dachausbau"]
    },
    {
        "id": "unterspannbahn",
        "title": "Unterspannbahn - Die Regenschutzschicht",
        "meta_desc": "Unterspannbahn: Funktion, Eigenschaften, Verwendung. Die wasserdichte Schicht unter den Dachziegeln.",
        "badge": "Konstruktion",
        "content": [
            {"h2": "Was ist eine Unterspannbahn?"},
            {"p": "Eine Unterspannbahn ist eine wasserdichte, aber dampfdurchlässige Folie, die unter den Dachziegeln verlegt wird. Sie schützt die Dämmung vor Regen, der durch die Ziegel dringt."},
            {"h2": "Vorteile"},
            {"p": "Die Unterspannbahn ermöglicht es, auf eine zusätzliche Unterspannung zu verzichten. Sie leitet eingedrungenen Regen nach außen ab und schützt die Dämmung."},
            {"h2": "Kosten"},
            {"p": "Unterspannbahnen kosten 5 bis 15 Euro pro m² Material. Die Verlegung ist einfach und kostengünstig."}
        ],
        "related": ["dampfsperre", "lattung", "tonpfanne"]
    },
    {
        "id": "dachformen-aufbauten",
        "title": "Dachformen & Aufbauten - Formen und Varianten",
        "meta_desc": "Dachformen: Satteldach, Walmdach, Pultdach, Flachdach. Die verschiedenen Dachformen im Überblick.",
        "badge": "Formen",
        "content": [
            {"h2": "Das Satteldach"},
            {"p": "Das Satteldach ist das verbreitetste Dach in Deutschland. Zwei geneigte Flächen treffen sich am First. Es ist günstig, einfach zu bauen und bietet viel Stauraum."},
            {"h2": "Das Walmdach"},
            {"p": "Beim Walmdach sind alle Seiten geneigt. Das macht es windfester als das Satteldach, ist aber aufwendiger und 20 bis 30 Prozent teurer."},
            {"h2": "Pultdach und Flachdach"},
            {"p": "Das Pultdach hat nur eine geneigte Fläche. Das Flachdach ist praktisch flach und bietet nutzbare Fläche für Solar oder Dachterrasse."}
        ],
        "related": ["tonpfanne", "flachdach", "lichtkuppel"]
    },
    {
        "id": "lichtkuppel",
        "title": "Lichtkuppel - Tageslicht durchs Flachdach",
        "meta_desc": "Lichtkuppel: Funktion, Kosten, Einbau. So bringen Sie Tageslicht in Räume unter Flachdächern.",
        "badge": "Aufbauten",
        "content": [
            {"h2": "Was ist eine Lichtkuppel?"},
            {"p": "Eine Lichtkuppel ist ein Aufbau im Flachdach, der Licht in den Raum lässt. Sie besteht aus einer Rahmenkonstruktion und einer Kuppel aus Kunststoff oder Glas."},
            {"h2": "Kosten und Größen"},
            {"p": "Lichtkuppeln kosten 200 bis 800 Euro je nach Größe. Die Verlegung kostet 300 bis 600 Euro zusätzlich. Größen von 60 x 60 cm bis 150 x 150 cm sind üblich."},
            {"h2": "Alternativen"},
            {"p": "Als Alternative gibt es Lichtbänder (lange, schmale Aufbauten) und Flachdachfenster. Diese bieten mehr Licht als runde Lichtkuppel."}
        ],
        "related": ["flachdach", "dachformen-aufbauten", "dachfenster"]
    },
    {
        "id": "neueindeckung",
        "title": "Neueindeckung - Wenn das Dach neu muss",
        "meta_desc": "Neueindeckung: Wann nötig, was kostet es, wie geht man vor. Der komplette Ratgeber.",
        "badge": "Sanierung",
        "content": [
            {"h2": "Wann ist eine Neueindeckung nötig?"},
            {"p": "Eine Neueindeckung ist nötig, wenn mehr als 30 Prozent der Ziegel beschädigt sind, wenn die Dachsubstanz nicht mehr reparabel ist oder wenn ein komplett neues Dach gewünscht wird."},
            {"h2": "Ablauf"},
            {"p": "Zuerst wird die alte Eindeckung entfernt. Dann wird die Lattung geprüft und gegebenenfalls erneuert. Danach werden die neuen Ziegel verlegt."},
            {"h2": "Kosten"},
            {"p": "Eine Neueindeckung mit Tonziegeln kostet 12.000 bis 20.000 Euro für ein 150 m² Dach. Mit Schiefer sind es 18.000 bis 30.000 Euro."}
        ],
        "related": ["dachsanierung", "sanierung-ausbau", "daemmung-energie"]
    },
    {
        "id": "sanierung-ausbau",
        "title": "Sanierung & Ausbau - Wohnraum unter dem Dach",
        "meta_desc": "Dachgeschoss ausbauen: Kosten, Planung, Genehmigung. So schaffen Sie Wohnraum unterm Dach.",
        "badge": "Sanierung",
        "content": [
            {"h2": "Wann lohnt sich ein Ausbau?"},
            {"p": "Ein Dachgeschossausbau lohnt sich, wenn das Dachgeschoss ungenutzt ist und genügend Stehhöhe bietet. Ein Ausbau ist günstiger als ein Anbau oder Umzug."},
            {"h2": "Was muss gemacht werden?"},
            {"p": "Der Ausbau umfasst Dämmung, Dampfsperre, Beplankung, Fenstereinbau und Innenausbau. Bei zu niedriger Raumhöhe kann eine Gaube helfen."},
            {"h2": "Kosten"},
            {"p": "Für einen kompletten Ausbau eines 50 m² Dachgeschosses liegen die Kosten bei 25.000 bis 70.000 Euro, je nach Ausstattung."}
        ],
        "related": ["dachausbau", "gaube-einbauen-kosten", "daemmung-energie"]
    },
    {
        "id": "daemmung-energie",
        "title": "Dämmung & Energie - Das energieeffiziente Dach",
        "meta_desc": "Dachdämmung: Materialien, Kosten, Förderung. So dämmen Sie Ihr Dach nach GEG.",
        "badge": "Energie",
        "content": [
            {"h2": "Warum Dämmung?"},
            {"p": "Ein ungedämmtes Dach verliert viel Wärme. Die Dachdämmung ist daher eine der wichtigsten Energiesparmaßnahmen am Haus."},
            {"h2": "Arten der Dämmung"},
            {"p": "Die gängigsten Arten: Zwischen sparren dämmung (20-30 Euro/m²), Aufsparren dämmung (100-150 Euro/m²), Untersparren dämmung (40-60 Euro/m²)."},
            {"h2": "Förderung"},
            {"p": "Die BEG fördert Dachdämmung mit 25 Prozent der Kosten. Die Förderung kann mit anderen Programmen kombiniert werden."}
        ],
        "related": ["dampfsperre", "geg-dach-pflicht-2026", "foerderung-baurecht"]
    },
    {
        "id": "gruendach",
        "title": "Gründach - Das Dach als Garten",
        "meta_desc": "Gründach: Aufbau, Kosten, Vorteile. So entsteht ein Garten auf dem Dach.",
        "badge": "Energie",
        "content": [
            {"h2": "Was ist ein Gründach?"},
            {"p": "Ein Gründach ist ein begrüntes Dach. Die Begrünung kann extensiv sein (Moose, Gräser) oder intensiv (Sträucher, Bäume)."},
            {"h2": "Vorteile"},
            {"p": "Ein Gründach verlängert die Lebensdauer der Abdichtung um 10 bis 20 Jahre, verbessert das Mikroklima und speichert Regenwasser."},
            {"h2": "Kosten und Förderung"},
            {"p": "Eine extensive Begrünung kostet 80 bis 150 Euro pro m². Die KfW fördert mit bis zu 7.500 Euro pro Wohneinheit."}
        ],
        "related": ["flachdach", "fpo-bahn", "gruendach-foerderung-2026"]
    },
    {
        "id": "foerderung-baurecht",
        "title": "Förderung & Baurecht - Geld vom Staat",
        "meta_desc": "Förderung fürs Dach: BEG, KfW, Landesprogramme. So finanzieren Sie Ihre Dachsanierung.",
        "badge": "Förderung",
        "content": [
            {"h2": "Bundesförderung für effiziente Gebäude (BEG)"},
            {"p": "Die BEG fördert Dachdämmung und Dachsanierung mit 25 Prozent der Kosten. Der Antrag muss vor Beginn der Maßnahme gestellt werden."},
            {"h2": "KfW-Programme"},
            {"p": "Die KfW vergibt zinsgünstige Kredite für energetische Sanierungen. Für den Dachgeschossausbau gibt es das Programm 261."},
            {"h2": "Landesprogramme"},
            {"p": "Viele Bundesländer haben eigene Förderprogramme. Bayern fördert über die LfA, NRW über die NRW-Bank."}
        ],
        "related": ["daemmung-energie", "geg-dach-pflicht-2026", "neueindeckung"]
    },
    {
        "id": "denkmalschutz-dach",
        "title": "Denkmalschutz - Das geschützte Dach",
        "meta_desc": "Denkmalschutz: Besonderheiten, Genehmigung, Kosten. So sanieren Sie ein denkmalgeschütztes Dach.",
        "badge": "Förderung",
        "content": [
            {"h2": "Was bedeutet Denkmalschutz?"},
            {"p": "Wenn ein Gebäude unter Denkmalschutz steht, dürfen äußere Änderungen nur mit Genehmigung der Denkmalbehörde vorgenommen werden."},
            {"h2": "Besonderheiten bei der Dachersatz"},
            {"p": "Bei denkmalgeschützten Gebäuden muss oft historisches Material verwendet werden. Schiefer oder Biberschwanz statt moderner Betonsteine."},
            {"h2": "Förderung für Denkmäler"},
            {"p": "Es gibt spezielle Förderprogramme für denkmalgeschützte Gebäude. Die Denkmalbehörde kann Informationen zu lokalen Programmen geben."}
        ],
        "related": ["biberschwanz", "schiefer", "neueindeckung"]
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
                "bitumenbahn": "Bitumenbahn",
                "fpo-bahn": "FPO-Bahn",
                "pib-bahn": "PIB-Bahn",
                "tonpfanne": "Tonpfanne",
                "biberschwanz": "Biberschwanz",
                "schiefer": "Schiefer",
                "dachkonstruktion": "Dachkonstruktion",
                "lattung": "Lattung",
                "dampfsperre": "Dampfsperre",
                "unterspannbahn": "Unterspannbahn",
                "dachformen-aufbauten": "Dachformen",
                "lichtkuppel": "Lichtkuppel",
                "neueindeckung": "Neueindeckung",
                "sanierung-ausbau": "Sanierung & Ausbau",
                "daemmung-energie": "Dämmung & Energie",
                "gruendach": "Gründach",
                "foerderung-baurecht": "Förderung & Baurecht",
                "denkmalschutz-dach": "Denkmalschutz"
            }
            rel_title = titles.get(rel_id, rel_id)
            rel_desc = {
                "bitumenbahn": "Klassisches Abdichtungsmaterial für Flachdächer.",
                "fpo-bahn": "Moderne Kunststoffabdichtung.",
                "pib-bahn": "Elastische Kunststoffabdichtung.",
                "tonpfanne": "Der klassische Dachziegel.",
                "biberschwanz": "Elegante historische Dacheindeckung.",
                "schiefer": "Premium-Dacheindeckung.",
                "dachkonstruktion": "Das Gerüst des Dachs.",
                "lattung": "Träger für die Dacheindeckung.",
                "dampfsperre": "Schutz vor Feuchtigkeit.",
                "unterspannbahn": "Regenschutzschicht.",
                "dachformen-aufbauten": "Formen und Varianten.",
                "lichtkuppel": "Tageslicht durchs Flachdach.",
                "neueindeckung": "Wenn das Dach neu muss.",
                "sanierung-ausbau": "Wohnraum unter dem Dach.",
                "daemmung-energie": "Das energieeffiziente Dach.",
                "gruendach": "Das Dach als Garten.",
                "foerderung-baurecht": "Geld vom Staat.",
                "denkmalschutz-dach": "Das geschützte Dach."
            }
            rel_desc_text = rel_desc.get(rel_id, "")
            related_html += f'''          <a href="/dach/glossar/{rel_id}/" class="card card--link"><h3>{rel_title}</h3><p>{rel_desc_text}</p></a>
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
        <a href="/dach/" class="nav__link nav__link--active">Dach</a>
        <a href="/bad/" class="nav__link">Heizung & Bad</a>
        <a href="/dach/blog/" class="nav__link">Blog</a>
        <a href="/dach/glossar/" class="nav__link nav__link--active">Glossar</a>
        <a href="#angebot" class="btn btn--header">Kostenlos anfragen</a>
      </nav>
      <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </header>

  <section class="hero hero--small">
    <div class="container">
      <div class="hero__content">
        <div class="card-badge"><a href="/dach/glossar/" style="color:inherit">Glossar</a></div>
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
          <h2>Jetzt Angebote von regionalen Dachdeckern einholen</h2>
          <p>Sie wissen jetzt, was die Arbeit kostet. Der nächste Schritt: kostenlos bis zu drei Angebote von geprüften Betrieben in Ihrer Region.</p>
          <a href="#angebot" class="btn btn--primary btn--lg">Kostenlos Angebot anfordern</a>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand"><span class="logo">hausbau<span class="logo-accent">.pro</span></span><p>Kostenlose Vermittlung von geprüften Dachdeckern und Zimmereien in ganz Deutschland.</p></div>
      <div class="footer__links"><h4>Wissen</h4><a href="/dach/glossar/">Glossar</a><a href="/dach/blog/">Blog</a></div>
      <div class="footer__links"><h4>Services</h4><a href="/dach/dachdecker/">Dachdecker</a><a href="/dach/dachsanierung/">Dachsanierung</a><a href="/dach/flachdach/">Flachdach</a></div>
    </div>
  </footer>
  <script src="/js/main.js"></script>
</body>
</html>'''


def generate_glossar_index():
    GROUPS = {
        "material": {
            "title": "Material",
            "badge": "Material",
            "desc": "Bitumenbahn, FPO, Tonpfanne, Schiefer.",
            "terms": ["bitumenbahn", "fpo-bahn", "pib-bahn", "tonpfanne", "biberschwanz", "schiefer"]
        },
        "konstruktion": {
            "title": "Konstruktion",
            "badge": "Konstruktion",
            "desc": "Dachkonstruktion, Lattung, Dampfsperre.",
            "terms": ["dachkonstruktion", "lattung", "dampfsperre", "unterspannbahn"]
        },
        "sanierung": {
            "title": "Sanierung & Ausbau",
            "badge": "Sanierung",
            "desc": "Neueindeckung, Dämmung, Gaube.",
            "terms": ["neueindeckung", "sanierung-ausbau", "daemmung-energie"]
        }
    }

    index_html = '''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dachdecker Glossar - Fachbegriffe rund ums Dach</title>
  <meta name="description" content="Dachdecker Glossar: Fachbegriffe von Bitumenbahn bis Zwischensparrendämmung einfach erklärt.">
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
        <a href="/dach/glossar/" class="nav__link nav__link--active">Glossar</a>
        <a href="#angebot" class="btn btn--header">Kostenlos anfragen</a>
      </nav>
      <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </header>

  <section class="hero hero--small">
    <div class="container">
      <div class="hero__content">
        <h1>Dachdecker Glossar - Fachbegriffe rund ums Dach</h1>
        <p class="hero__sub">Was ist eine Bitumenbahn? Was bedeutet GEG? Was ist der Unterschied zwischen Sparrendach und Pfettendach? Hier finden Sie Fachbegriffe rund ums Dach.</p>
      </div>
    </div>
  </section>

  <section class="section section--light">
    <div class="container">
      <div class="grid grid--3">
'''
    for group_id, group in GROUPS.items():
        index_html += f'''
        <a href="/dach/glossar/{group_id}/" class="card card--link">
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
        index_html += f'''<a href="/dach/glossar/{term['id']}/" class="card card--link">
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
          <h2>Jetzt Angebote von regionalen Dachdeckern einholen</h2>
          <p>Sie wissen jetzt, was die Fachbegriffe bedeuten. Der nächste Schritt: kostenlos bis zu drei Angebote von geprüften Betrieben in Ihrer Region.</p>
          <a href="#angebot" class="btn btn--primary btn--lg">Kostenlos Angebot anfordern</a>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand"><span class="logo">hausbau<span class="logo-accent">.pro</span></span><p>Kostenlose Vermittlung von geprüften Dachdeckern und Zimmereien in ganz Deutschland.</p></div>
      <div class="footer__links"><h4>Wissen</h4><a href="/dach/glossar/">Glossar</a><a href="/dach/blog/">Blog</a></div>
      <div class="footer__links"><h4>Services</h4><a href="/dach/dachdecker/">Dachdecker</a><a href="/dach/dachsanierung/">Dachsanierung</a><a href="/dach/flachdach/">Flachdach</a></div>
    </div>
  </footer>
  <script src="/js/main.js"></script>
</body>
</html>'''
    return index_html


def main():
    import os
    os.makedirs("dach/glossar", exist_ok=True)

    with open("dach/glossar/index.html", "w", encoding="utf-8") as f:
        f.write(generate_glossar_index())
    print("Generated: dach/glossar/index.html")

    for term in TERMS:
        dir_path = f"dach/glossar/{term['id']}"
        os.makedirs(dir_path, exist_ok=True)

        html = generate_glossar_entry(term)
        with open(f"{dir_path}/index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated: {dir_path}/index.html")


if __name__ == "__main__":
    main()