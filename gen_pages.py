#!/usr/bin/env python3
"""
Generate dachdecker-preisvergleich/{city}/index.html for all 8 cities.
Usage: python gen_pages.py
"""

import os

CITIES = {
    "stuttgart": {
        "name": "Stuttgart",
        "region": "Baden-Württemberg",
        "plz": "70173 bis 70599",
        "neighborhoods": [
            "Bad Cannstatt", "Feuerbach", "Vaihingen", "Degerloch",
            "Möhringen", "Sillenbuch", "Hedelfingen", "Zuffenhausen",
            "Münster", "Untertürkheim", "Weilimdorf", "Birkach"
        ],
        "architecture": "Steildächer mit Tonziegeln und Schiefer, Flachdächer auf den Fildern, Mansarddächer in Bad Cannstatt",
        "intro": "Stuttgart liegt in einem Talkessel. Die Topografie der Stadt ist steil, die Dachformen sind es auch. In Degerloch und Sillenbuch stehen Villen mit steilen Satteldächern. Auf den Fildern dominieren Flachdächer. In Bad Cannstatt gibt es noch Halbwalmdächer aus der Zeit des Cannstatter Volksfests. Wer in Stuttgart ein Dachprojekt hat, braucht einen Betrieb, der sich mit diesen Bedingungen auskennt – nicht einen, der einfach irgendwo in Baden-Württemberg arbeitet.",
        "projects": [
            "Steildach in Degerloch: Die Villengegenden im Süden mit gehobener Altbaubsubstanz und steilen Satteldächern",
            "Flachdach in Vaihingen und Möhringen: Die Campus-Gegend und Neubaugebiete auf den Fildern",
            "Halbwalmdach in Bad Cannstatt: Das Volksfest-Viertel mit eigener Dachkultur",
            "Dachsanierung in der Innenstadt: Enge Gassen und wenig Platz stellen besondere Anforderungen"
        ],
        "dachdecker_page": "/dachdecker/stuttgart/",
        "testimonials": [
            {"text": "Unser Dach in Degerloch war nach dem Winter undicht. Drei Angebote geholt, Betrieb aus dem Süden genommen. Sauber gelaufen.", "name": "Monika W.", "city": "Degerloch"},
            {"text": "In Bad Cannstatt haben wir ein Halbwalmdach. Nicht jeder Dachdecker hat damit Erfahrung. Über hausbau.pro den richtigen gefunden.", "name": "Thomas K.", "city": "Bad Cannstatt"},
            {"text": "Flachdach in Vaihingen - dringend sanieren lassen. Noch am selben Tag hat sich ein Betrieb gemeldet.", "name": "Julia F.", "city": "Vaihingen"},
        ],
        "famous": "Mercedes-Benz, Porsche, Stuttgarter Weihnachtsmarkt",
        "keywords": ["Dachdecker Preisvergleich Stuttgart", "Dachdecker Angebote Stuttgart", "Dachsanierung Kosten Stuttgart", "günstiger Dachdecker Stuttgart", "Dachdecker Firmenvergleich Stuttgart"]
    },
    "koeln": {
        "name": "Köln",
        "region": "Nordrhein-Westfalen",
        "plz": "50667 bis 51149",
        "neighborhoods": [
            "Innenstadt", "Ehrenfeld", "Nippes", "Mülheim", "Lindenthal",
            "Deutz", "Kalk", "Porz", "Rodenkirchen", "Bilderstöckchen",
            "Worringen", "Chorweiler", "Meschenich"
        ],
        "architecture": "Satteldächer in den Altbauquartieren, Flachdächer in Porz und Chorweiler, Schieferdächer im Rheinland",
        "intro": "Köln wächst. Die Mieten in Ehrenfeld und Lindenthal steigen, und immer mehr Eigentümer investieren ins Dach. Die Gründerzeitbauten dort haben Satteldächer mit Gauben – anspruchsvoll, aber mit dem richtigen Betrieb kein Problem. Am Rhein, in Deutz und Porz, stehen dagegen Flachdächer aus den sechziger und siebziger Jahren, die langsam saniert werden müssen. Und dann ist da noch der Dom. Nur als Hintergrund. Unsere Kölner Betriebe kennen die Veedel.",
        "projects": [
            "Satteldach in Ehrenfeld: Die bunten Altbauviertel mit hohen Firsten und Gauben",
            "Schieferdach in Lindenthal: Die Villengegend am Grüngürtel mit anspruchsvollen Schieferdeckungen",
            "Flachdach in Mülheim: Die industrieprafte Vergangenheit hat dort viele Flachdächer hinterlassen",
            "Dachsanierung in der Altstadt: Denkmalschutz und enge Gassen stellen Betriebe vor besondere Aufgaben"
        ],
        "dachdecker_page": "/dachdecker/koeln/",
        "testimonials": [
            {"text": "Wir haben uns ein Angebot für unser Satteldach in Ehrenfeld geholt. Drei Betriebe, drei verschiedene Konzepte. Das beste genommen.", "name": "Anna L.", "city": "Ehrenfeld"},
            {"text": "In Mülheim ein altes Flachdach. Das Portal hat uns einen Betrieb aus der Nachbarschaft vermittelt. Schnell und fair.", "name": "Peter H.", "city": "Mülheim"},
            {"text": "Schieferdach in Lindenthal - da braucht man Spezialisten. Über hausbau.pro gleich zwei Betriebe gefunden, die das machen.", "name": "Sandra M.", "city": "Lindenthal"},
        ],
        "famous": "Kölner Dom, Karneval, Rhein, RTL",
        "keywords": ["Dachdecker Preisvergleich Köln", "Dachdecker Angebote Köln", "Dachsanierung Kosten Köln", "günstiger Dachdecker Köln", "Dachdecker Firmenvergleich Köln"]
    },
    "muenchen": {
        "name": "München",
        "region": "Bayern",
        "plz": "80331 bis 81939",
        "neighborhoods": [
            "Altstadt", "Maxvorstadt", "Schwabing", "Au", "Haidhausen",
            "Bogenhausen", "Sendling", "Pasing", "Neuhausen", "Giesing",
            "Neuperlach", "Moosach", "Feldmoching", "Trudering"
        ],
        "architecture": "Steile Satteldächer mit Biberschwanz, Flachdächer in den Neubaugebieten, historische Mansarddächer in der Altstadt",
        "intro": "München ist teuer – auch für Dachdecker. Die Handwerkerpreise liegen hier über dem Bundesdurchschnitt, und die Qualitätserwartungen sind hoch. In Schwabing und der Maxvorstadt stehen Altbauten mit Mansarddächern, die man nicht jedem Betrieb anvertrauen sollte. In Trudering und Neuperlach dominieren Flachdächer aus den Hochhausseptemberzeiten. Unsere Münchner Betriebe kennen die Szene und machen faire Preise.",
        "projects": [
            "Satteldach in Schwabing: Die akademischen Viertel mit gehobenen Altbauten und anspruchsvollen Dachlandschaften",
            "Mansarddach in der Maxvorstadt: Das Künstlerviertel mit historischer Bausubstanz und Denkmalschutz",
            "Flachdach in Neuperlach und Trudering: Die großen Neubaugebiete der 60er und 70er Jahre",
            "Dachausbau in Sendling und Giesing: Aus dem Speicher ein neues Zimmer machen - ein beliebtes Projekt"
        ],
        "dachdecker_page": "/dachdecker/muenchen/",
        "testimonials": [
            {"text": "Unser Satteldach in Schwabing war in die Jahre gekommen. Drei Angebote eingeholt, das mittlere genommen - guter Mittelweg zwischen Preis und Leistung.", "name": "Claudia R.", "city": "Schwabing"},
            {"text": "Für unser Flachdach in Trudering brauchten wir dringend jemanden. Noch am nächsten Tag hatte sich ein Betrieb gemeldet.", "name": "Michael S.", "city": "Trudering"},
            {"text": "Dachgeschoss ausbauen in der Au war unser Traum. Über das Portal einen Betrieb gefunden, der das komplett gemacht hat.", "name": "Lisa W.", "city": "Haidhausen"},
        ],
        "famous": "Oktoberfest, BMW, Allianz Arena, Marienplatz",
        "keywords": ["Dachdecker Preisvergleich München", "Dachdecker Angebote München", "Dachsanierung Kosten München", "günstiger Dachdecker München", "Dachdecker Firmenvergleich München"]
    },
    "hamburg": {
        "name": "Hamburg",
        "region": "Norddeutschland",
        "plz": "20095 bis 21149",
        "neighborhoods": [
            "Altstadt", "Neustadt", "HafenCity", "St. Pauli", "Altona",
            "Eppendorf", "Winterhude", "Uhlenhorst", "Barmbek", "Eilbek",
            "Wandsbek", "Bergedorf", "Blankenese", "Osdorf"
        ],
        "architecture": "Steile Satteldächer in den Altbauquartieren, Flachdächer am Hafen und in den Neubauvierteln, Reetdächer in Blankenese",
        "intro": "Hamburg hat drei Wetterlagen und entsprechend anspruchsvolle Dächer. In Blankenese stehen Reetdächer an den Elbhöfen. In Eppendorf und Winterhude gibt es die hohen Satteldächer der Altbauten. In der HafenCity sind es moderne Flachdächer. Und überall steht der Wind – der Hamburger Wind. Unsere Dachdecker in Hamburg wissen, was das für die Dachkonstruktion bedeutet.",
        "projects": [
            "Dachsanierung in Eppendorf: Die teuren Altbauten im Norden verlangen erfahrene Betriebe und hochwertige Materialien",
            "Flachdach in der HafenCity: Das Neubaugebiet am Wasser setzt auf moderne Flachdacharchitektur",
            "Reetdach in Blankenese: Die Elbvillen mit steilen, oft denkmalgeschützten Dächern",
            "Schornsteinsanierung in St. Pauli: Die alten Reethäuser brauchen regelmäßige Pflege"
        ],
        "dachdecker_page": "/dachdecker/hamburg/",
        "testimonials": [
            {"text": "In Eppendorf haben wir ein altes Satteldach sanieren lassen. Über das Portal gleich zwei Angebote von Betrieben aus dem Viertel bekommen.", "name": "Friedrich B.", "city": "Eppendorf"},
            {"text": "Die HafenCity war neu für uns. Flachdach sanieren lassen war unkompliziert - Anfrage online, Angebote kamen schnell.", "name": "Nina T.", "city": "HafenCity"},
            {"text": "Blankenese ist teuer, aber über das Portal haben wir einen fairen Preis für unser Reetdach gefunden.", "name": "Heike M.", "city": "Blankenese"},
        ],
        "famous": "Hafen, Elbphilharmonie, Reeperbahn, Hamburger SV",
        "keywords": ["Dachdecker Preisvergleich Hamburg", "Dachdecker Angebote Hamburg", "Dachsanierung Kosten Hamburg", "günstiger Dachdecker Hamburg", "Dachdecker Firmenvergleich Hamburg"]
    },
    "dortmund": {
        "name": "Dortmund",
        "region": "Nordrhein-Westfalen",
        "plz": "44135 bis 44379",
        "neighborhoods": [
            "Innenstadt", "Kreuzviertel", "Nordstadt", "Kaiserstraßenviertel",
            "Hörde", "Hombruch", "Brackel", "Wambel", "Schüren",
            "Aplerbeck", "Hörde", "Barop", "Kirchhörde"
        ],
        "architecture": "Steildächer mit Schiefer und Ziegel, Flachdächer in den Neubaugebieten, Industriekultur-Dächer",
        "intro": "Dortmund ist nicht nur der BVB. Die Stadt hat eine starke Industrie-Geschichte, und viele Dächer in der Innenstadt und am Hörder Platz erinnern noch daran. In Hombruch stehen Villen mit Schiefer gedeckt. Im Kreuzviertel werden Dachgeschosse zu Loftwohnungen ausgebaut. Und am Phoenix-See in Hörde entstehen gerade neue Dächer für neue Häuser. Unsere Dortmunder Betriebe kennen das.",
        "projects": [
            "Schieferdach in Hombruch: Die gehobenen Wohnviertel mit anspruchsvollen Schieferdeckungen",
            "Dachsanierung in der Nordstadt: Die Studentenquartiere mit vielen Altbauten",
            "Industriedach am Hörder Platz: Das Stahl- und Bier-Land hat seine eigene Dachkultur",
            "Dachausbau im Kreuzviertel: Aus dem Dachgeschoss eine Loftwohnung machen"
        ],
        "dachdecker_page": "/dachdecker/dortmund/",
        "testimonials": [
            {"text": "Unser Schieferdach in Hombruch war ein Projekt für sich. Über das Portal einen Betrieb gefunden, der sich damit auskennt.", "name": "Ursula K.", "city": "Hombruch"},
            {"text": "In der Nordstadt ein altes Reihenhaus mit undichtem Dach. Drei Angebote bekommen, schnell repariert.", "name": "Jens P.", "city": "Nordstadt"},
            {"text": "Für unseren Dachausbau in Hörde brauchten wir jemanden mit Erfahrung. Über hausbau.pro den richtigen gefunden.", "name": "Simone A.", "city": "Hörde"},
        ],
        "famous": "SIGNAL IDUNA PARK, Bier, Phoenix, Möller",
        "keywords": ["Dachdecker Preisvergleich Dortmund", "Dachdecker Angebote Dortmund", "Dachsanierung Kosten Dortmund", "günstiger Dachdecker Dortmund", "Dachdecker Firmenvergleich Dortmund"]
    },
    "duesseldorf": {
        "name": "Düsseldorf",
        "region": "Nordrhein-Westfalen",
        "plz": "40210 bis 40629",
        "neighborhoods": [
            "Altstadt", "Carlstadt", "Stadtmitte", "Pempelfort", "Düsseltal",
            "Golzheim", "Derendorf", "Oberkassel", "Niederkassel", "Heerdt",
            "Lörick", "Angermund", "Kaiserswerth", "Urdenbach"
        ],
        "architecture": "Steildächer in den Villenvierteln, Flachdächer am Rhein, moderne Architektur in Oberkassel",
        "intro": "Düsseldorf ist kompakt. Am Rhein entlang stehen Villen mit aufwendigen Steildächern. In Oberkassel hat sich in den letzten Jahren viel getan – dort entstehen moderne Stadthäuser mit Flachdächern. Die Carlstadt ist das kleine Szeneviertel mit Altbauten und Denkmalschutz. In Derendorf stehen die Büro- und Wohnkomplexe der neuen Mitte. Und überall: die Kö. Unsere Düsseldorfer Betriebe kennen die Stadt.",
        "projects": [
            "Villendach in Oberkassel: Die Rheinuferlage verlangt erstklassige Handwerker und hochwertige Materialien",
            "Flachdach in Derendorf: Die modernen Büro- und Wohnbauten am Rande der Stadt",
            "Steildach in Düsseltal: Die alten Villen am Zoopark mit aufwendigen Dachlandschaften",
            "Dachsanierung in der Carlstadt: Das Szeneviertel mit Denkmalschutz und Charme"
        ],
        "dachdecker_page": "/dachdecker/duesseldorf/",
        "testimonials": [
            {"text": "Unser Villendach in Oberkassel war ein großes Projekt. Über das Portal drei Angebote eingeholt, alle professionell.", "name": "Rolf H.", "city": "Oberkassel"},
            {"text": "Flachdach in Derendorf - nach 30 Jahren war eine Sanierung fällig. Schnell ging das über hausbau.pro.", "name": "Birgit S.", "city": "Derendorf"},
            {"text": "Die Altstadt hat enge Gassen und wenig Platz. Unsere Betriebe in Düsseldorf kennen das.", "name": "Dieter M.", "city": "Carlstadt"},
        ],
        "famous": "Altbier, Kö, Königsallee, Medienhafen, Rheinturm",
        "keywords": ["Dachdecker Preisvergleich Düsseldorf", "Dachdecker Angebote Düsseldorf", "Dachsanierung Kosten Düsseldorf", "günstiger Dachdecker Düsseldorf", "Dachdecker Firmenvergleich Düsseldorf"]
    },
    "leipzig": {
        "name": "Leipzig",
        "region": "Sachsen",
        "plz": "04107 bis 04357",
        "neighborhoods": [
            "Innenstadt", "Zentrum", "Plagwitz", "Lindenau", "Connewitz",
            "Stötteritz", "Schönefeld", "Gohlis", "Schleussig", "Zöbigker",
            "Möckern", "Wahren", "Lützschena", "Burghausen"
        ],
        "architecture": "Gründerzeit-Satteldächer, Industriekultur-Flächen, moderne Stadthäuser mit Flachdächern",
        "intro": "Leipzig boomt. Die Stadt wächst schneller als jede andere in Ostdeutschland, und die Dachdecker haben alle Hände voll zu tun. In Connewitz und Gohlis stehen die schönen Gründerzeitbauten mit ihren hohen Satteldächern. In Plagwitz werden alte Fabrikkomplexe zu Lofts umgebaut – mit Dachterrassen und Gauben. Die Mieten steigen, und Eigentümer investieren. Unsere Leipziger Betriebe sind mitten drin.",
        "projects": [
            "Gründerzeitdach in Connewitz: Die bunten Altbauten aus der Gründerzeit brauchen erfahrene Betriebe",
            "Industriedach in Plagwitz: Das Kreativquartier mit alten Fabrikhallen und anspruchsvollen Dachflächen",
            "Dachausbau in Lindenau: Aus dem Dachgeschoss loftartige Wohnungen schaffen",
            "Steildach in Gohlis: Die gehobenen Altbauquartiere mit hohen Dächern"
        ],
        "dachdecker_page": "/dachdecker/leipzig/",
        "testimonials": [
            {"text": "Unser Gründerzeit-Satteldach in Connewitz war ein Abenteuer. Über das Portal aber den richtigen Betrieb gefunden.", "name": "Martina B.", "city": "Connewitz"},
            {"text": "Plagwitz hat viele alte Hallen. Die Dachsanierung lief reibungslos - drei Angebote, schnelle Ausführung.", "name": "Frank S.", "city": "Plagwitz"},
            {"text": "Für unseren Dachausbau in Lindenau brauchten wir jemanden, der weiß was er tut. Über hausbau.pro super vermittelt worden.", "name": "Andrea K.", "city": "Lindenau"},
        ],
        "famous": "Bach, Gewandhaus, Spassgarde, Ausstellungszentrum",
        "keywords": ["Dachdecker Preisvergleich Leipzig", "Dachdecker Angebote Leipzig", "Dachsanierung Kosten Leipzig", "günstiger Dachdecker Leipzig", "Dachdecker Firmenvergleich Leipzig"]
    },
    "freiburg": {
        "name": "Freiburg",
        "region": "Baden-Württemberg",
        "plz": "79098 bis 79117",
        "neighborhoods": [
            "Altstadt", "Innenstadt", "Stühlinger", "Herdern",
            "Neuburg", "St. Georgen", "Vauban", "Landwasser",
            "Lehen", "Weygang", "Haslach", "Opfingen", "Tiengen"
        ],
        "architecture": "Dächer mit alemannischem Charakter, Steildächer mit Schneelasten aus dem Schwarzwald, Solardächer in der Ökostadt",
        "intro": "Freiburg ist die Sonnenstadt Deutschlands. Das merkt man auch bei Dächern: In Vauban stehen Häuser mit integrierten Solaranlagen, die das Dach gleich mitnutzen. In der Altstadt dominieren alemannische Steildächer, die dem Schwarzwald nahen Klima standhalten müssen. Und im Stühlinger wächst ein neues Viertel auf dem alten Bahnhofsareal. Unsere Freiburger Betriebe kennen die Gegend.",
        "projects": [
            "Steildach mit Solarpaneelen in Vauban: Das Ökoviertel als Vorreiter für Solar-Dachintegration",
            "Schwarzwald-typisches Steildach in Herdern: Die alten Freiburger Stadtteile mit alemannischem Charakter",
            "Flachdach in der Innenstadt: Die modernen Stadthäuser und Bürobauten",
            "Dachsanierung im Stühlinger: Die konvertierten Bahnhofsareale brauchen erfahrene Handwerker"
        ],
        "dachdecker_page": "/dachdecker/freiburg/",
        "testimonials": [
            {"text": "Vauban ist unser Viertel. Wir haben das Dach mit Solar gemacht - über hausbau.pro einen Betrieb gefunden, der beides kann.", "name": "Stefanie G.", "city": "Vauban"},
            {"text": "In Herdern haben wir ein altes alemannisches Steildach. Drei Angebote eingeholt, alle waren gut.", "name": "Martin W.", "city": "Herdern"},
            {"text": "Die Freiburger Innenstadt hat enge Gassen. Unsere Betriebe kennen das und planen dementsprechend.", "name": "Ute B.", "city": "Altstadt"},
        ],
        "famous": "Münster, Schwarzwald, Universitätsstadt, Vauban",
        "keywords": ["Dachdecker Preisvergleich Freiburg", "Dachdecker Angebote Freiburg", "Dachsanierung Kosten Freiburg", "günstiger Dachdecker Freiburg", "Dachdecker Firmenvergleich Freiburg"]
    },
}


def generate_page(city_id, data):
    """Generate the HTML page for a given city."""
    nl = "\n"
    testimonials_html = "\n".join(
        f'''        <div class="review-card">
          <div class="review-stars">★★★★★</div>
          <p class="review-text">"{t["text"]}"</p>
          <p class="review-author"><strong>{t["name"]}</strong> · {t["city"]}</p>
        </div>''' for t in data["testimonials"]
    )
    neighborhoods_html = ", ".join(data["neighborhoods"])

    return f'''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dachdecker Preisvergleich {data["name"]} – Kostenlos bis zu 3 Angebote vergleichen</title>
  <meta name="description" content="Dachdecker Preisvergleich {data["name"]}: Eine Anfrage, bis zu drei Angebote von Dachdeckern in {data["name"]}. ✓ Kostenlos ✓ Unverbindlich ✓ Geprüfte Betriebe. Jetzt Angebote einholen!">
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
        <a href="/#services" class="nav__link">Leistungen</a>
        <a href="/blog/" class="nav__link">Blog</a>
        <a href="/#faq" class="nav__link">FAQ</a>
        <a href="/#angebot" class="btn btn--header">Kostenlos anfragen</a>
      </nav>
      <button class="nav-toggle" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <section class="hero">
    <div class="container">
      <div class="hero__content">
        <div class="card-badge">{data["name"]}</div>
        <h1>Dachdecker Preisvergleich {data["name"]} – <span class="text-accent">einfach & kostenlos Angebote einholen</span></h1>
        <p class="hero__sub">{data["intro"]}</p>
        <div class="hero__trust">
          <span>Kostenlos</span>
          <span>Unverbindlich</span>
          <span>Geprüfte Betriebe</span>
        </div>
        <a href="#angebot" class="btn btn--primary btn--lg">Jetzt kostenloses Angebot anfordern</a>
      </div>
    </div>
  </section>

  <section class="section section--light">
    <div class="container">
      <div class="section__header">
        <span class="section__tag">Warum Preisvergleich?</span>
        <h2>Dachdecker-Preise vergleichen in {data["name"]} – ohne Aufwand</h2>
      </div>
      <div class="grid grid--2" style="margin-bottom: 2rem;">
        <div>
          <p>Wer ein Dachprojekt hat – ob <strong>Dachsanierung</strong>, <strong>Neueindeckung</strong>, <strong>Dachausbau</strong> oder eine <strong>Dachreparatur</strong> – steht irgendwann vor der Frage: Was kostet ein Dachdecker in {data["name"]}? Pauschale Preise gibt es nicht. Jedes Dach ist anders, jeder Betrieb kalkuliert anders.</p>
          <p>Statt selbst tagelang zu suchen, anzurufen und Angebote anzufragen, machen Sie bei hausbau.pro <strong>eine einzige Anfrage</strong>. Wir leiten Ihr Projekt an bis zu drei passende Dachdecker-Betriebe aus {data["name"]} und Umgebung weiter. Die melden sich direkt bei Ihnen – mit einem Angebot.</p>
          <p>Sie vergleichen dann in Ruhe und entscheiden frei. Ohne Verkaufsdruck, ohne versteckte Kosten.</p>
        </div>
        <div>
          <h3>Was beeinflusst die Kosten?</h3>
          <p>Die Preise für Dachdecker-Arbeiten in {data["name"]} hängen von mehreren Faktoren ab:</p>
          <ul>
            <li><strong>Dachfläche und Form:</strong> Steildächer sind aufwendiger als Flachdächer. {data["architecture"]}.</li>
            <li><strong>Material:</strong> Tondachziegel, Schiefer, Metall oder FPO – die Wahl des Materials macht einen großen Unterschied.</li>
            <li><strong>Zustand des Daches:</strong> Eine Teilsanierung kostet weniger als eine Komplettrenovierung.</li>
            <li><strong>Zusatzleistungen:</strong> Gerüstbau, Entsorgung, Dämmung nach GEG treiben die Kosten.</li>
            <li><strong>Standort:</strong> Die PLZ-Gebiete {data["plz"]} in {data["name"]} haben unterschiedliche Rahmenbedingungen.</li>
          </ul>
          <p>Genau deshalb lohnt sich der Vergleich: Drei Angebote zeigen Ihnen die Bandbreite – und Sie finden das beste Preis-Leistungs-Verhältnis.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section__header">
        <span class="section__tag">So funktioniert's</span>
        <h2>Preise vergleichen in {data["name"]} – in 3 Schritten</h2>
      </div>
      <div class="steps">
        <div class="step">
          <div class="step__num">1</div>
          <h3>Anfrage stellen</h3>
          <p>Beschreiben Sie Ihr Dachprojekt – was muss gemacht werden? Welche PLZ haben Sie in {data["name"]}? Wir leiten alles an passende Betriebe weiter.</p>
        </div>
        <div class="step-arrow">→</div>
        <div class="step">
          <div class="step__num">2</div>
          <h3>Angebote erhalten</h3>
          <p>Bis zu drei Dachdecker aus {data["name"]} und Umgebung melden sich innerhalb von 24 Stunden mit einem unverbindlichen Angebot.</p>
        </div>
        <div class="step-arrow">→</div>
        <div class="step">
          <div class="step__num">3</div>
          <h3>Vergleichen & wählen</h3>
          <p>Sie prüfen die Angebote, fragen nach Referenzen und beauftragen den Betrieb, der am besten zu Ihrem Projekt passt.</p>
        </div>
      </div>
      <div class="steps-cta">
        <a href="#angebot" class="btn btn--primary btn--lg">Jetzt Angebote anfordern</a>
      </div>
    </div>
  </section>

  <section class="section section--light">
    <div class="container">
      <div class="section__header">
        <span class="section__tag">{data["name"]}</span>
        <h2>Dachprojekte in {data["name"]} – was wir vermitteln</h2>
      </div>
      <div class="grid grid--3">
        <div class="card">
          <h3>Neueindeckung & Steildach</h3>
          <p>Ein neues Steildach für Ihr Haus? Mit Ziegeln, Schiefer oder Metalldachziegeln. Unsere Betriebe in {data["name"]} beraten Sie zur Auswahl und setzen sauber um.</p>
          <span class="card__tag">Steildach</span>
        </div>
        <div class="card">
          <h3>Dachsanierung</h3>
          <p>Wenn das Dach in die Jahre gekommen ist, wird eine Sanierung fällig. Dämmung nach GEG, neue Eindeckung, Unterkonstruktion prüfen – alles aus einer Hand.</p>
          <span class="card__tag">Sanierung</span>
        </div>
        <div class="card">
          <h3>Flachdach</h3>
          <p>Flachdächer haben in {data["name"]} eine lange Tradition. Sanierung mit FPO oder Bitumen, Neubau mit moderner Abdichtung – unsere Betriebe kennen die Techniken.</p>
          <span class="card__tag">Flachdach</span>
        </div>
        <div class="card">
          <h3>Dachausbau</h3>
          <p>Mehr Wohnraum unterm Dach schaffen – in {data["name"]} ein beliebtes Projekt. Mit Gauben, Dachfenstern oder einem kompletten Dachgeschoss-Ausbau.</p>
          <span class="card__tag">Ausbau</span>
        </div>
        <div class="card">
          <h3>Dachfenster & Velux</h3>
          <p>Tageslicht ins Dachgeschoss bringen. Velux, Roto, Fakro – Einbau, Austausch und Eindeckrahmen. Geeignet für alle Dächer in {data["name"]}.</p>
          <span class="card__tag">Velux</span>
        </div>
        <div class="card">
          <h3>Zimmerei & Gauben</h3>
          <p>Carports, Gauben, Dachstühle. In {data["name"]} mit seinen vielfältigen Baustilen ein eigenes Thema. Unsere Zimmereibetriebe haben Erfahrung in der Region.</p>
          <span class="card__tag">Holzbau</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section__header">
        <span class="section__tag">Region</span>
        <h2>Dachdecker in {data["name"]} – PLZ-Gebiete und Stadtteile</h2>
      </div>
      <div class="grid grid--2">
        <div>
          <p>{data["name"]} ist eine Stadt mit vielen Gesichtern – und entsprechend unterschiedlichen Dachlandschaften. Unsere Betriebe kennen die Besonderheiten jedes Stadtteils und haben die Erfahrung, die in {data["region"]} gebraucht wird.</p>
          <p>Wir decken alle PLZ-Gebiete ab: <strong>{data["plz"]}</strong>. Ob Sie in der Innenstadt ein denkmalgeschütztes Dach haben oder in einem der Außenviertel ein modernes Flachdach sanieren lassen wollen – wir haben den passenden Betrieb.</p>
          <p>Stadtteile, die wir besonders gut abdecken: {neighborhoods_html}.</p>

          <h3>Typische Projekte in {data["name"]}</h3>
          <ul>
            <li><strong>Steildach in {data["neighborhoods"][0]}:</strong> {data["projects"][0]}.</li>
            <li><strong>Flachdach in {data["neighborhoods"][2]}:</strong> {data["projects"][1]}.</li>
            <li><strong>Dachausbau in {data["neighborhoods"][4]}:</strong> {data["projects"][2]}.</li>
            <li><strong>Dachsanierung in {data["neighborhoods"][1]}:</strong> {data["projects"][3]}.</li>
          </ul>
        </div>
        <div>
          <h3>Was kostet ein Dachdecker in {data["name"]}?</h3>
          <p>Eine grobe Orientierung für {data["name"]} ({data["region"]}):</p>
          <div class="cost-box">
            <p><strong>Dachneueindeckung:</strong> ab ca. 120 €/m² inkl. Material, abhängig von Bedachungsart</p>
          </div>
          <div class="cost-box">
            <p><strong>Flachdach-Sanierung:</strong> ab ca. 80–150 €/m² je nach Zustand und Material</p>
          </div>
          <div class="cost-box">
            <p><strong>Dachausbau:</strong> ab ca. 800–1.500 €/m² Wohnfläche, je nach Umfang</p>
          </div>
          <div class="cost-box">
            <p><strong>Dachfenster (Velux):</strong> ab ca. 350–600 €/Stück inkl. Einbau</p>
          </div>
          <p>Die tatsächlichen Kosten hängen immer vom Einzelfall ab. Deshalb gilt: Angebote einholen und vergleichen. Das spart in {data["name"]} oft mehrere hundert bis tausend Euro.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--light">
    <div class="container">
      <div class="section__header">
        <span class="section__tag">Vorteile</span>
        <h2>Preisvergleich über hausbau.pro – das spricht dafür</h2>
      </div>
      <div class="grid grid--3">
        <div class="card">
          <h3>Zeitersparnis</h3>
          <p>Statt selbst drei, vier oder fünf Betriebe anzurufen, reicht eine einzige Anfrage über hausbau.pro. Wir kümmern uns um die Vermittlung.</p>
        </div>
        <div class="card">
          <h3>Kein Verkaufsdruck</h3>
          <p>Die Betriebe melden sich mit einem Angebot. Sie entscheiden in Ruhe. Kein Telefonstress, keine Druckverkaufsgespräche.</p>
        </div>
        <div class="card">
          <h3>Geprüfte Betriebe</h3>
          <p>Alle Dachdecker, die über uns vermittelt werden, sind Meisterbetriebe mit Erfahrung in {data["name"]}. Sie kennen die lokalen Bauvorschriften.</p>
        </div>
        <div class="card">
          <h3>Kostenlos für Sie</h3>
          <p>Unser Service kostet Sie keinen Cent. Wir werden von den Betrieben bezahlt, nicht von Ihnen. Die Angebote sind kostenlos und unverbindlich.</p>
        </div>
        <div class="card">
          <h3>Regional & persönlich</h3>
          <p>Alle Betriebe kommen aus {data["name"]} und Umgebung. Das bedeutet kurze Anfahrtswege und Kenntnis der lokalen Baustile – wie {data["architecture"].lower()}.</p>
        </div>
        <div class="card">
          <h3>Mehr Transparenz</h3>
          <p>Drei Angebote zum Vergleichen zeigen Ihnen die Preisspanne. So erkennen Sie, ob ein Angebot fair ist – oder ob es Luft nach unten gibt.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section__header">
        <span class="section__tag">Bewertungen</span>
        <h2>Kundenstimmen aus {data["name"]}</h2>
      </div>
      <div class="grid grid--3">
        {testimonials_html}
      </div>
    </div>
  </section>

  <section class="section section--light" id="faq">
    <div class="container">
      <div class="section__header">
        <span class="section__tag">FAQ</span>
        <h2>Häufige Fragen zum Dachdecker-Preisvergleich</h2>
      </div>
      <div class="faq-list">
        <details class="faq-item">
          <summary>Ist der Preisvergleich wirklich kostenlos?</summary>
          <p>Ja. Für Sie als Anfragesteller fallen keine Kosten an. hausbau.pro verdient an den Betrieben, die vermittelte Leads erhalten. Sie zahlen nie etwas.</p>
        </details>
        <details class="faq-item">
          <summary>Wie viele Angebote erhalte ich?</summary>
          <p>Sie erhalten bis zu drei Angebote von Dachdeckern aus {data["name"]} und Umgebung. Wie viele sich melden, hängt davon ab, wie spezialisiert Ihr Projekt ist.</p>
        </details>
        <details class="faq-item">
          <summary>Wie schnell melden sich die Betriebe?</summary>
          <p>Innerhalb von 24 Stunden. In den meisten Fällen melden sich die Dachdecker noch am selben Tag bei Ihnen.</p>
        </details>
        <details class="faq-item">
          <summary>Bin ich verpflichtet, ein Angebot anzunehmen?</summary>
          <p>Nein. Alle Angebote sind unverbindlich. Sie entscheiden komplett frei, ob und welchen Betrieb Sie beauftragen.</p>
        </details>
        <details class="faq-item">
          <summary>Welche PLZ-Gebiete in {data["name"]} werden abgedeckt?</summary>
          <p>Wir arbeiten mit Dachdeckern in ganz {data["name"]}. Alle PLZ-Gebiete {data["plz"]} werden abgedeckt.</p>
        </details>
        <details class="faq-item">
          <summary>Was passiert mit meinen Daten?</summary>
          <p>Ihre Daten werden nur an die von Ihnen ausgewählten Dachdecker-Betriebe weitergegeben. Keine Weitergabe an Dritte, keine Werbung.</p>
        </details>
      </div>
    </div>
  </section>

  <section class="section cta-section" id="angebot">
    <div class="container">
      <div class="cta-grid">
        <div class="cta-content">
          <span class="section__tag" style="color:#bfdbfe">Kostenlos anfragen</span>
          <h2>Dachdecker-Preise in {data["name"]} vergleichen – einfach und schnell</h2>
          <p>Erzählen Sie uns, was bei Ihnen ansteht. Beschreiben Sie kurz Ihr Dachprojekt und teilen Sie Ihren Standort mit. Wir leiten Ihre Anfrage an bis zu drei passende Dachdecker-Betriebe in {data["name"]} weiter – kostenlos und unverbindlich.</p>
          <div class="trust-list">
            <div class="trust-item">
              <svg width="20" height="20" fill="none"><path d="M9 12l5 5L23 7" stroke="#bfdbfe" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <span>Keine versteckten Kosten</span>
            </div>
            <div class="trust-item">
              <svg width="20" height="20" fill="none"><path d="M9 12l5 5L23 7" stroke="#bfdbfe" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <span>Meisterbetriebe aus {data["name"]}</span>
            </div>
            <div class="trust-item">
              <svg width="20" height="20" fill="none"><path d="M9 12l5 5L23 7" stroke="#bfdbfe" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <span>Innerhalb von 24 Stunden gemeldet</span>
            </div>
            <div class="trust-item">
              <svg width="20" height="20" fill="none"><path d="M9 12l5 5L23 7" stroke="#bfdbfe" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <span>Vergleichen Sie bis zu 3 Angebote</span>
            </div>
          </div>
        </div>
        <div class="form-card">
          <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
            <input type="hidden" name="quelle" value="dachdecker-preisvergleich-{city_id}">
            <div class="form-group">
              <label for="name">Ihr Name</label>
              <input type="text" id="name" name="name" placeholder="Max Mustermann" required>
            </div>
            <div class="form-group">
              <label for="email">E-Mail</label>
              <input type="email" id="email" name="email" placeholder="ihre@email.de" required>
            </div>
            <div class="form-group">
              <label for="phone">Telefon</label>
              <input type="tel" id="phone" name="phone" placeholder="Ihr Telefon">
            </div>
            <div class="form-group">
              <label for="plz">PLZ in {data["name"]}</label>
              <input type="text" id="plz" name="plz" placeholder="{data["plz"].split(" bis ")[0]}" required pattern="[0-9]{{5}}">
            </div>
            <div class="form-group">
              <label for="service">Was brauchen Sie?</label>
              <select id="service" name="service" required>
                <option value="">Bitte auswählen</option>
                <option value="dachsanierung">Dachsanierung</option>
                <option value="neueindeckung">Neueindeckung / Steildach</option>
                <option value="flachdach">Flachdach</option>
                <option value="dachausbau">Dachausbau</option>
                <option value="dachfenster">Dachfenster / Velux</option>
                <option value="zimmermann">Zimmermann / Gauben / Carport</option>
                <option value="dachreparatur">Dachreparatur / Notdienst</option>
                <option value="sonstiges">Sonstiges</option>
              </select>
            </div>
            <div class="form-group">
              <label for="message">Beschreibung (optional)</label>
              <textarea id="message" name="message" rows="3" placeholder="Kurze Beschreibung Ihres Projekts..."></textarea>
            </div>
            <button type="submit" class="btn btn--primary btn--full">Kostenlos Angebot anfordern</button>
            <p class="form-note">Mit dem Absenden stimmen Sie zu, dass wir Ihre Daten an Dachdecker-Betriebe in {data["name"]} weiterleiten. Keine Weitergabe an Dritte.</p>
          </form>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand">
        <span class="logo">hausbau<span class="logo-accent">.pro</span></span>
        <p>Kostenlose Vermittlung von geprüften Dachdeckern in {data["name"]} und ganz Deutschland.</p>
      </div>
      <div class="footer__links">
        <h4>Dachdecker in {data["name"]}</h4>
        <a href="{data["dachdecker_page"]}">Dachdecker {data["name"]}</a>
        <a href="/dachsanierung/{city_id}/">Dachsanierung</a>
        <a href="/dachausbau/{city_id}/">Dachausbau</a>
        <a href="/dachfenster/{city_id}/">Dachfenster</a>
        <a href="/flachdach/{city_id}/">Flachdach</a>
      </div>
      <div class="footer__links">
        <h4>Weitere Städte</h4>
        <a href="/dachdecker-preisvergleich/koeln/">Köln</a>
        <a href="/dachdecker-preisvergleich/muenchen/">München</a>
        <a href="/dachdecker-preisvergleich/hamburg/">Hamburg</a>
        <a href="/dachdecker-preisvergleich/stuttgart/">Stuttgart</a>
      </div>
      <div class="footer__links">
        <h4>Rechtliches</h4>
        <a href="#">Impressum</a>
        <a href="#">Datenschutz</a>
      </div>
    </div>
    <div class="footer__bottom">
      <div class="container">
        <p>© 2026 hausbau.pro - Alle Rechte vorbehalten.</p>
      </div>
    </div>
  </footer>

  <script src="/js/main.js"></script>
</body>
</html>'''


def main():
    for city_id, data in CITIES.items():
        path = f"dachdecker-preisvergleich/{city_id}/index.html"
        content = generate_page(city_id, data)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {path}")


if __name__ == "__main__":
    main()
