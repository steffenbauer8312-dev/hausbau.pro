#!/usr/bin/env python3
"""Generate heating/sanitary branch blog articles for /bad/blog/."""

SERVICES = ["waermepumpe", "heizungsbau", "sanitaer", "klimaanlage", "badsanierung", "solarthermie"]

ARTICLES = [
    {
        "id": "waermepumpe-kosten-2026",
        "title": "Wärmepumpe Kosten 2026 - Was Sie wirklich bezahlen",
        "meta_desc": "Wärmepumpe Kosten 2026: Anschaffung, Installation, Betrieb. Was eine Luft-Wärmepumpe, Sole-Wärmepumpe und Erdwärme wirklich kosten - mit Förderung.",
        "badge": "Kosten",
        "headline": "Wärmepumpe Kosten 2026 - Was Sie wirklich bezahlen",
        "sub": "Luft, Sole oder Erdwärme? Die Kosten für eine Wärmepumpe variieren stark je nach Typ. Hier sind realistische Zahlen für 2026.",
        "tag": "Wärmepumpe",
        "content": [
            {"h2": "Was kostet eine Luft-Wärmepumpe?", "p": "Die Luft-Wärmepumpe ist der günstigste Einstieg. Die Anlage selbst kostet zwischen 12.000 und 18.000 Euro. Hinzu kommen Installationskosten von 3.000 bis 6.000 Euro. Für ein Einfamilienhaus rechnet man mit Gesamtkosten von 15.000 bis 24.000 Euro - bevor die Förderung abgezogen wird."},
            {"h2": "Sole-Wärmepumpe (Erdwärme)", "p": "Eine Sole-Wärmepumpe nutzt die Erdwärme über Erdkollektoren oder Erdsonden. Die Anschaffungskosten liegen bei 18.000 bis 28.000 Euro. Dazu kommen die Kosten für die Erschließung: Erdkollektoren kosten 5.000 bis 12.000 Euro, Erdbohrungen 8.000 bis 15.000 Euro. Gesamtkosten: 25.000 bis 45.000 Euro."},
            {"h2": "Betriebskosten und Effizienz", "p": "Die jährlichen Betriebskosten hängen von der Effizienz der Anlage und Ihrem Wärmebedarf ab. Eine gut gedämmte Wohnung mit 120 m² braucht etwa 12.000 kWh pro Jahr. Bei einem Strompreis von 30 Cent pro kWh und einer Jahresarbeitszahl von 3,5 liegen die Heizkosten bei etwa 1.030 Euro pro Jahr."},
            {"h2": "Förderung abziehen", "p": "Die Bundesförderung für effiziente Gebäude (BEG) fördert Wärmepumpen mit bis zu 25 Prozent der Kosten. Eine Luft-Wärmepumpe für 20.000 Euro wird so um 5.000 Euro günstiger. Dazu kommen oft lokale Programme von KfW, Ländern und Kommunen."},
            {"h2": "Regionaler Kostenvergleich", "p": "Die Installationskosten variieren je nach Region. München und Hamburg sind am teuersten, Leipzig und Dortmund am günstigsten. Für eine Luft-Wärmepumpe inklusive Installation:<div class='cost-box'><p><strong>Luft-Wärmepumpe, Komplett inkl. Installation:</strong><br>München: 18.000 bis 26.000 Euro<br>Stuttgart: 17.000 bis 24.000 Euro<br>Hamburg: 16.000 bis 23.000 Euro<br>Köln: 15.500 bis 22.000 Euro<br>Dortmund: 14.000 bis 20.000 Euro<br>Leipzig: 13.000 bis 19.000 Euro"}
        ],
        "faq": [
            {"q": "Lohnt sich eine Wärmepumpe auch im Altbau?", "a": "Ja, aber nur wenn das Gebäude gut gedämmt ist. Bei einer Heizlast über 80 Watt pro m² ist die Wärmepumpe unwirtschaftlich. Erst ab etwa 60 Watt pro m² macht sie Sinn."},
            {"q": "Kann ich meine Gasheizung durch eine Wärmepumpe ersetzen?", "a": "Ja, in vielen Fällen. Bei einer Öl- oder Gasheizung über 20 Jahren ist der Austausch fast immer sinnvoll. Die bestehende Hydraulik kann oft weiter genutzt werden."},
            {"q": "Wie lange hält eine Wärmepumpe?", "a": "Eine Wärmepumpe hält 15 bis 25 Jahre. Die Lebensdauer hängt von der Nutzung und der Wartung ab."},
            {"q": "Was ist der Unterschied zwischen Luft-Wärmepumpe und Erdwärme?", "a": "Luft-Wärmepumpen holen die Wärme aus der Außenluft. Sie sind günstiger, aber bei sehr niedrigen Temperaturen weniger effizient. Erdwärme ist teurer in der Installation, liefert aber ganzjährig konstante Temperaturen."}
        ]
    },
    {
        "id": "waermepumpe-foerderung-2026",
        "title": "Wärmepumpe Förderung 2026 - Alle Programme im Überblick",
        "meta_desc": "Wärmepumpe Förderung 2026: BEG, KfW, BAFA, Landesprogramme. Wie Sie bis zu 40 Prozent der Kosten fördern lassen.",
        "badge": "Förderung",
        "headline": "Wärmepumpe Förderung 2026 - Alle Programme im Überblick",
        "sub": "BEG, KfW, BAFA, Landesförderung - die Förderlandschaft ist komplex. Hier finden Sie den Durchblick und erfahren, wie Sie möglichst viel Förderung bekommen.",
        "tag": "Wärmepumpe",
        "content": [
            {"h2": "Bundesförderung für effiziente Gebäude (BEG)", "p": "Die BEG ist das wichtigste Förderprogramm für Wärmepumpen. Sie zahlt 25 Prozent der Kosten als Zuschuss - bis zu 60.000 Euro pro Wohneinheit. Die Förderung gilt für Luft-Wärmepumpen, Sole-Wärmepumpen und Erdwärmepumpen."},
            {"h2": "KfW-Kredit 262", "p": "Die KfW vergibt zinsgünstige Kredite für Wärmepumpen über das Programm 262. Bis zu 150.000 Euro pro Wohnung zu einem Zinssatz von etwa 1,5 Prozent. Die Kredite können mit dem BEG-Zuschuss kombiniert werden."},
            {"h2": "BAFA-Heizungsförderung", "p": "Das BAFA fördert den Einbau von Wärmepumpen im Bestand mit 25 Prozent der Kosten. Antragstellung ist vor Beginn der Maßnahme erforderlich."},
            {"h2": "Landesprogramme und Kommunen", "p": "Zusätzlich zur Bundesförderung gibt es regionale Programme. Bayern fördert über die LfA, NRW über die NRW-Bank, Baden-Württemberg über die L-Bank. Manche Kommunen bieten eigene Zuschüsse."},
            {"h2": "Kombination und Максимум", "p": "Die Förderungen lassen sich oft kombinieren. Eine Luft-Wärmepumpe für 20.000 Euro kann so aussehen: BEG 5.000 Euro + KfW-Kredit 8.000 Euro + Landesprogramm 2.000 Euro = 15.000 Euro Eigenanteil."}
        ],
        "faq": [
            {"q": "Kann ich die Förderung auch für eine gemietete Wohnung beantragen?", "a": "Ja, aber als Mieter müssen Sie die Zustimmung des Eigentümers haben. Die Förderung wird trotzdem auf Ihren Namen beantragt."},
            {"q": "Was passiert wenn ich die Förderung beantragt habe, aber die Kosten niedriger ausfallen?", "a": "Sie müssen die Förderung anpassen lassen. Wenn die Kosten 20 Prozent unter dem geförderten Budget liegen, wird die Förderung entsprechend reduziert."},
            {"q": "Kann ich die Förderung auch für eine Wärmepumpe in einem Neubau bekommen?", "a": "Für Neubauten gelten andere Programme. Die BEG fördert primär Bestandssanierungen."},
            {"q": "Wie finde ich einen guten Energieberater?", "a": "Die Verbraucherzentrale bietet Energieberatungen an. Für die Beantragung der BEG-Förderung müssen Sie einen zertifizierten Energieeffizienz-Experten hinzuziehen."}
        ]
    },
    {
        "id": "klimaanlage-einbauen-kosten",
        "title": "Klimaanlage einbauen Kosten 2026 - Split, Multi-Split, mobil",
        "meta_desc": "Klimaanlage einbauen Kosten 2026: Split-Anlage ab 2.500 Euro, Multi-Split bis 8.000 Euro. Was Kühlung wirklich kostet.",
        "badge": "Kosten",
        "headline": "Klimaanlage einbauen Kosten 2026",
        "sub": "Klimaanlage einbauen: Split oder Multi-Split? Hier sind die Kosten für Kauf, Installation und Betrieb.",
        "tag": "Klimaanlage",
        "content": [
            {"h2": "Split-Klimaanlage Kosten", "p": "Eine Split-Klimaanlage ist die häufigste Wahl für Wohnungen und kleine Büros. Kosten für eine einzelne Split-Anlage: 2.500 bis 5.000 Euro inklusive Installation."},
            {"h2": "Multi-Split-Anlage Kosten", "p": "Wenn mehrere Räume gekühlt werden sollen, lohnt sich eine Multi-Split-Anlage. Ein Außengerät versorgt bis zu fünf Innengeräte. Die Kosten: 5.000 bis 12.000 Euro je nach Anzahl."},
            {"h2": "Betriebskosten", "p": "Eine Split-Anlage mit 3,5 kW verbraucht etwa 1,0 bis 1,5 kW Strom. Bei 500 Betriebsstunden pro Sommer sind das etwa 150 bis 225 Euro pro Jahr."},
            {"h2": "Was kostet die Installation?", "p": "Die Installationskosten sind oft höher als viele denken. Die Bohrung für die Kältemittelleitung kostet 150 bis 400 Euro. Rechnen Sie mit 500 bis 1.500 Euro für die Installation."},
            {"h2": "Mietgeräte als Alternative", "p": "Für eine Übergangszeit oder bei Mietwohnungen können mobile Klimageräte eine Lösung sein. Die Kosten: 30 bis 80 Euro pro Monat. Für eine dauerhafte Lösung lohnt sich die feste Installation."}
        ],
        "faq": [
            {"q": "Brauche ich eine Genehmigung für die Außeneinheit?", "a": "In Mietshäusern brauchen Sie die Zustimmung des Eigentümers. In Eigentumswohnungen entscheidet die Eigentümerversammlung."},
            {"q": "Wie laut ist eine Split-Klimaanlage?", "a": "Moderne Split-Anlagen sind leise: 20 bis 35 dB im Innenraum. Das Außengerät liegt bei 45 bis 60 dB."},
            {"q": "Kann ich die Klimaanlage auch zur Heizung nutzen?", "a": "Ja, die meisten Split- und Multi-Split-Anlagen können auch heizen. Sie funktionieren dann als Wärmepumpe."},
            {"q": "Wie oft muss ich die Klimaanlage warten?", "a": "Mindestens einmal pro Jahr, idealerweise vor der Sommersaison. Die Wartung kostet 80 bis 150 Euro."}
        ]
    },
    {
        "id": "bad-sanierung-kosten-2026",
        "title": "Bad Sanierung Kosten 2026 - Was kostet eine komplette Badrenovierung?",
        "meta_desc": "Bad Sanierung Kosten 2026: Kompletsanierung ab 12.000 Euro, Dusche statt Wanne ab 4.000 Euro. Was die Renovierung wirklich kostt.",
        "badge": "Kosten",
        "headline": "Bad Sanierung Kosten 2026",
        "sub": "Badrenovierung: Die Kosten hängen stark vom Umfang ab. Hier finden Sie realistische Preise.",
        "tag": "Bad Sanierung",
        "content": [
            {"h2": "Was kostet eine Kompletsanierung?", "p": "Eine Kompletsanierung des Badezimmers umfasst den Abbruch des alten Bads, Neueinbau aller Sanitärkeramik, Fliesen, Leitungen und Armaturen. Für ein 8 m² Bad liegen die Kosten zwischen 15.000 und 35.000 Euro."},
            {"h2": "Dusche statt Wanne", "p": "Viele wollen statt der alten Wanne eine ebenerdige Dusche. Die Kosten für den Rückbau der Wanne und den Einbau einer Dusche mit Glaswand: 4.000 bis 8.000 Euro."},
            {"h2": "Barrierefreies Bad", "p": "Ein barrierefreies Bad nach DIN 18040 kostet mehr als eine Standardrenovierung. Die Kosten liegen bei 25.000 bis 50.000 Euro für ein komplettes Bad."},
            {"h2": "Einzelne Gewerke", "p": "WC-Wechsel 400 bis 800 Euro, Waschbecken 200 bis 500 Euro, Armaturen 150 bis 400 Euro, Fliesenlegen 40 bis 80 Euro pro m²."},
            {"h2": "Regionaler Vergleich", "p": "München ist am teuersten, Leipzig am günstigsten. Für eine Kompletsanierung mit mittlerer Ausstattung:<div class='cost-box'><p><strong>Kompletsanierung Bad, 8 m²:</strong><br>München: 22.000 bis 32.000 Euro<br>Stuttgart: 20.000 bis 28.000 Euro<br>Hamburg: 18.000 bis 26.000 Euro<br>Köln: 17.000 bis 25.000 Euro<br>Leipzig: 13.000 bis 20.000 Euro"}
        ],
        "faq": [
            {"q": "Wie lange dauert eine Bad Kompletsanierung?", "a": "Eine Kompletsanierung dauert zwei bis vier Wochen, je nach Umfang und Verfügbarkeit der Handwerker."},
            {"q": "Kann ich während der Sanierung im Haus wohnen?", "a": "Ja, wenn Sie ein zweites Badezimmer oder eine Gästetoilette nutzen können."},
            {"q": "Wann lohnt sich eine Sanierung statt eines Neubaus?", "a": "Wenn die Substanz gut ist und nur die Optik und Ausstattung veraltet sind. Wenn aber die Leitungen marode sind, ist ein kompletter Rückbau oft die bessere Wahl."},
            {"q": "Wie finde ich gute Sanitärbetriebe?", "a": "Fragen Sie in Ihrem Bekanntenkreis nach Empfehlungen. Sie können auch drei Angebote einholen und diese vergleichen."}
        ]
    },
    {
        "id": "heizungsbauer-finden",
        "title": "Heizungsbauer finden - So finden Sie einen guten Betrieb",
        "meta_desc": "Heizungsbauer finden: Worauf Sie bei der Wahl achten sollten, welche Qualifikationen wichtig sind.",
        "badge": "Ratgeber",
        "headline": "Heizungsbauer finden - So finden Sie einen guten Betrieb",
        "sub": "Einen guten Heizungsbauer zu finden ist nicht leicht. Hier erfahren Sie, woran Sie einen seriösen Betrieb erkennen.",
        "tag": "Heizungsbau",
        "content": [
            {"h2": "Darauf kommt es an", "p": "Ein guter Heizungsbauer bietet eine Vor-Ort-Beratung an, kommt innerhalb weniger Tage, erklärt die verschiedenen Optionen verständlich und gibt Ihnen Zeit zur Entscheidung."},
            {"h2": "Welche Qualifikationen sind wichtig?", "p": "Der Betrieb sollte einen Meisterbrief haben oder ein eingetragenes Installateurunternehmen sein. Für Gas- und Ölheizungen braucht der Betrieb einen Eintrag in das Installateurverzeichnis."},
            {"h2": "Drei Angebote einholen", "p": "Holen Sie immer drei Angebote von verschiedenen Betrieben ein. Vergleichen Sie nicht nur den Gesamtpreis, sondern auch: Welche Materialien werden verwendet? Welche Garantie gibt es?"},
            {"h2": "Lokale Referenzen prüfen", "p": "Fragen Sie den Betrieb nach Referenzen in Ihrer Nähe. Ein Betrieb, der regelmäßig in Ihrem Viertel arbeitet, kennt die lokalen Gegebenheiten."},
            {"h2": "Warnsignale", "p": "Seien Sie vorsichtig bei: Drängeln zu schnellen Entscheidungen, Angeboten ohne Vor-Ort-Beratung, Preisen, die deutlich unter dem Durchschnitt liegen."}
        ],
        "faq": [
            {"q": "Wie finde ich einen Heizungsbauer in meiner Region?", "a": "Sie können das Installateurverzeichnis Ihrer Stadt oder Gemeinde einsehen. Oder Sie nutzen Empfehlungen von Nachbarn und Bekannten."},
            {"q": "Was kostet eine Beratung?", "a": "Eine gute Beratung vor Ort ist in der Regel kostenlos. Der Betrieb macht dies als Service."},
            {"q": "Wie lange dauert die Installation einer neuen Heizung?", "a": "Der Einbau einer neuen Gasheizung oder Wärmepumpe dauert ein bis zwei Wochen."},
            {"q": "Gibt es Garantie auf die Arbeit?", "a": "Ja, der Betrieb haftet für seine Arbeit. Die gesetzliche Gewährleistung beträgt zwei Jahre."}
        ]
    },
    {
        "id": "solarthermie-vs-photovoltaik",
        "title": "Solarthermie vs. Photovoltaik - Was ist besser für Ihr Haus?",
        "meta_desc": "Solarthermie oder Photovoltaik? Was die beiden Technologien unterscheidet, was sie kosten und für wen sich welche Lösung lohnt.",
        "badge": "Energie",
        "headline": "Solarthermie vs. Photovoltaik - Was ist besser?",
        "sub": "Beide nutzen die Sonne, aber unterschiedlich. Solarthermie für warmes Wasser, Photovoltaik für Strom.",
        "tag": "Solarthermie",
        "content": [
            {"h2": "Der grundlegende Unterschied", "p": "Solarthermie wandelt Sonnenlicht direkt in Wärme um. Die Photovoltaik erzeugt aus Licht elektrischen Strom. Solarthermie ist effizienter bei der Wärmeerzeugung, Photovoltaik bei der Stromerzeugung."},
            {"h2": "Was kostet Solarthermie?", "p": "Eine Solarthermieanlage für warmes Wasser kostet 4.000 bis 8.000 Euro inklusive Installation. Für eine Anlage mit Heizungsunterstützung liegen die Kosten bei 8.000 bis 14.000 Euro."},
            {"h2": "Was kostet Photovoltaik?", "p": "Eine Photovoltaikanlage mit 5 kWp kostet etwa 8.000 bis 12.000 Euro. Mit Speicher kommen 5.000 bis 10.000 Euro dazu."},
            {"h2": "Für wen lohnt sich Solarthermie?", "p": "Solarthermie lohnt sich besonders für Haushalte mit hohem Warmwasserverbrauch im Sommer. Die Amortisationszeit liegt bei 10 bis 15 Jahren."},
            {"h2": "Für wen lohnt sich Photovoltaik?", "p": "Photovoltaik lohnt sich fast immer, wenn Sie einen Teil des erzeugten Stroms selbst verbrauchen. Die Amortisationszeit liegt bei 8 bis 12 Jahren."}
        ],
        "faq": [
            {"q": "Kann ich beides kombinieren?", "a": "Ja, Sie können sowohl Solarthermie als auch Photovoltaik auf dem Dach haben."},
            {"q": "Was ist effizienter?", "a": "Photovoltaik ist in Bezug auf die Energieausbeute pro Fläche effizienter, weil Strom einen höheren Wert hat als Wärme."},
            {"q": "Welche Förderung gibt es?", "a": "Solarthermie wird über das BAFA gefördert, Photovoltaik über die KfW und das EEG."},
            {"q": "Wie lange halten die Anlagen?", "a": "Solarthermieanlagen halten 20 bis 30 Jahre, Photovoltaikmodule 25 bis 35 Jahre."}
        ]
    },
    {
        "id": "klimaanlage-wartung",
        "title": "Klimaanlage Wartung - Darauf sollten Sie achten",
        "meta_desc": "Klimaanlage Wartung: Wie oft, was wird gemacht, was kostet es. So halten Sie Ihre Anlage in Schuss.",
        "badge": "Wartung",
        "headline": "Klimaanlage Wartung - So halten Sie Ihre Anlage in Schuss",
        "sub": "Eine regelmäßige Wartung verlängert die Lebensdauer und senkt die Betriebskosten.",
        "tag": "Klimaanlage",
        "content": [
            {"h2": "Warum Wartung wichtig ist", "p": "Eine schlecht gewartete Klimaanlage verbraucht mehr Strom, kühlt schlechter und kann gesundheitsschädlich werden. Staub und Schmutz sammeln sich im Filter und im Verdampfer."},
            {"h2": "Was wird bei der Wartung gemacht?", "p": "Eine professionelle Wartung umfasst: Reinigung oder Austausch des Luftfilters, Reinigung des Verdampfers, Prüfung des Kältemittels, Kontrolle der elektrischen Verbindungen, Reinigung der Außeneinheit."},
            {"h2": "Wie oft warten?", "p": "Für private Split-Anlagen gilt: mindestens einmal pro Jahr warten, idealerweise vor der Sommersaison im April oder Mai."},
            {"h2": "Was kostet eine Wartung?", "p": "Eine professionelle Wartung kostet 80 bis 150 Euro pro Innengerät. Bei einer Multi-Split-Anlage mit drei Innengeräten liegen die Kosten bei 200 bis 350 Euro."},
            {"h2": "Warnsignale", "p": "Diese Zeichen deuten auf Probleme hin: Die Anlage kühlt weniger als früher, es riecht muffig, die Anlage läuft häufiger als gewöhnlich."}
        ],
        "faq": [
            {"q": "Kann ich die Wartung selbst machen?", "a": "Den Filter können Sie selbst reinigen. Die Kältemittelprüfung und die Kontrolle der elektrischen Anlage sollten Fachleute machen."},
            {"q": "Was passiert wenn ich die Wartung vernachlässige?", "a": "Die Anlage wird weniger effizient, verbraucht mehr Strom und kann schneller kaputtgehen."},
            {"q": "Gibt es einen Wartungsvertrag?", "a": "Ja, viele Installateure bieten Wartungsverträge an. Die Kosten liegen bei 80 bis 150 Euro pro Jahr."},
            {"q": "Wie erkenne ich einen guten Wartungsbetrieb?", "a": "Ein guter Betrieb kommt mit einem vollständigen Bericht zurück und erklärt was er gemacht hat."}
        ]
    },
    {
        "id": "sanitaer-installation-kosten",
        "title": "Sanitär Installation Kosten 2026 - Was Sie für Rohre und Armaturen zahlen",
        "meta_desc": "Sanitär Installation Kosten 2026: Neue Leitungen, Armaturen, Wasseraufbereitung. Was die wichtigsten Arbeiten kosten.",
        "badge": "Kosten",
        "headline": "Sanitär Installation Kosten 2026",
        "sub": "Wenn Sie neue Sanitärleitungen oder Armaturen brauchen, kommen schnell mehrere Tausend Euro zusammen.",
        "tag": "Sanitär",
        "content": [
            {"h2": "Neue Wasserleitungen verlegen", "p": "Wenn alte Wasserrohre ausgetauscht werden müssen, hängen die Kosten von der Länge und dem Material ab. Kupferrohre kosten 25 bis 40 Euro pro Meter. Für ein Einfamilienhaus mit 30 Metern liegen die Materialkosten bei 1.000 bis 2.000 Euro."},
            {"h2": "Abwasserleitungen erneuern", "p": "Abwasserleitungen sind oft schwieriger zu erneuern als Wasserleitungen. Die Kosten liegen bei 80 bis 150 Euro pro Meter."},
            {"h2": "Armaturen und Mischbatterien", "p": "Eine hochwertige Armatur für das Waschbecken kostet 150 bis 400 Euro. Für die Badewanne oder Dusche liegen die Kosten bei 200 bis 600 Euro."},
            {"h2": "Wasserenthärtungsanlage", "p": "In Regionen mit hartem Wasser kann eine Wasserenthärtungsanlage sinnvoll sein. Die Kosten: 1.500 bis 3.500 Euro für die Anlage, plus 200 bis 400 Euro pro Jahr für Salz und Wartung."},
            {"h2": "Was kostet ein Klempner?", "p": "Der Stundensatz liegt zwischen 50 und 90 Euro. Hinzu kommen Materialkosten. Für eine einfache Armaturen-Reparbeit sollten Sie 100 bis 200 Euro einplanen."}
        ],
        "faq": [
            {"q": "Wann sollten Wasserleitungen erneuert werden?", "a": "Wenn die Leitungen älter als 30 Jahre sind, wenn es häufig zu Lecks kommt, wenn das Wasser rostig oder trüb ist."},
            {"q": "Was ist besser: Kupfer oder Edelstahl?", "a": "Beide Materialien sind hochwertig und langlebig. Kupfer ist flexibler, Edelstahl ist resistenter gegen Kalk."},
            {"q": "Kann ich Sanitärarbeiten selbst machen?", "a": "Kleine Arbeiten wie das Wechseln von Armaturen können Sie selbst machen. Für Leitungsarbeiten brauchen Sie einen Fachbetrieb."},
            {"q": "Wie finde ich einen guten Sanitärbetrieb?", "a": "Empfehlungen von Nachbarn sind oft der beste Weg. Sie können auch drei Angebote einholen."}
        ]
    }
]


def generate_blog_article(article):
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{article["title"]}</title>
  <meta name="description" content="{article["meta_desc"]}">
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
        <a href="/bad/blog/" class="nav__link nav__link--active">Blog</a>
        <a href="/bad/glossar/" class="nav__link">Glossar</a>
        <a href="#angebot" class="btn btn--header">Kostenlos anfragen</a>
      </nav>
      <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </header>

  <section class="hero hero--small">
    <div class="container">
      <div class="hero__content">
        <div class="card-badge"><a href="/bad/blog/" style="color:inherit">Blog</a></div>
        <h1>{article["headline"]}</h1>
        <p class="hero__sub">{article["sub"]}</p>
      </div>
    </div>
  </section>

  <section class="section section--light">
    <div class="container">
      <div class="grid grid--2">
        <div>
'''


def section_to_html(section):
    h2 = f"          <h2>{section['h2']}</h2>"
    p = f"          <p>{section['p']}</p>"
    return h2 + "\n" + p


def generate_blog_index():
    return '''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Heizung & Bad Blog - Ratgeber für Wärmepumpe, Klimaanlage und Bad</title>
  <meta name="description" content="Wärmepumpe Kosten, Förderung, Klimaanlage Wartung - Ratgeber für Heizung, Sanitär und Klimatechnik.">
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
        <a href="/bad/blog/" class="nav__link nav__link--active">Blog</a>
        <a href="/bad/glossar/" class="nav__link">Glossar</a>
        <a href="#angebot" class="btn btn--header">Kostenlos anfragen</a>
      </nav>
      <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </header>

  <section class="hero hero--small">
    <div class="container">
      <div class="hero__content">
        <h1>Heizung & Bad Blog</h1>
        <p class="hero__sub">Wärmepumpe Kosten, Förderung, Klimaanlage Wartung, Bad Sanierung - hier finden Sie Antworten auf die wichtigsten Fragen.</p>
      </div>
    </div>
  </section>

  <section class="section section--light">
    <div class="container">
      <div class="grid grid--3">
''' + "\n".join([f'''        <a href="/bad/blog/{a["id"]}/" class="card card--link">
          <div class="card-badge" style="margin-top:0;margin-bottom:12px">{a["badge"]}</div>
          <h3>{a["title"]}</h3>
          <p>{a["sub"]}</p>
        </a>''' for a in ARTICLES]) + '''
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <h2 style="margin-bottom:2rem">Mehr Wissen</h2>
      <div class="grid grid--3">
        <a href="/bad/glossar/" class="card card--link"><h3>Heizung & Bad Glossar</h3><p>Fachbegriffe erklärt - von Wärmepumpe bis Trinkwasser.</p></a>
        <a href="/bad/waermepumpe/berlin/" class="card card--link"><h3>Wärmepumpe Berlin</h3><p>Geprüfte Betriebe, Bundesförderung, lokale Expertise.</p></a>
        <a href="/bad/heizungsbau/muenchen/" class="card card--link"><h3>Heizungsbau München</h3><p>LfA Bayern Förderung, lokale Betriebe.</p></a>
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


def main():
    import os
    os.makedirs("bad/blog", exist_ok=True)

    with open("bad/blog/index.html", "w", encoding="utf-8") as f:
        f.write(generate_blog_index())
    print("Generated: bad/blog/index.html")

    for article in ARTICLES:
        dir_path = f"bad/blog/{article['id']}"
        os.makedirs(dir_path, exist_ok=True)

        html = generate_blog_article(article)

        for section in article["content"]:
            html += section_to_html(section) + "\n"

        html += '''
        </div>
        <div>
'''
        if article.get("faq"):
            html += '          <h2 style="margin-bottom:1rem">Häufige Fragen</h2>\n'
            for faq in article["faq"]:
                html += f'''          <div class="faq-item" style="margin-bottom:1.5rem">
            <h3 style="font-size:1.1rem;margin-bottom:0.5rem">{faq["q"]}</h3>
            <p style="color:#64748b">{faq["a"]}</p>
          </div>
'''

        html += '''
        </div>
      </div>
    </div>
  </section>

  <section class="section cta-section" id="angebot">
    <div class="container">
      <div class="cta-grid">
        <div class="cta-content">
          <span class="section__tag" style="color:#bfdbfe">Kostenlos anfragen</span>
          <h2>Jetzt Angebote von regionalen Fachbetrieben einholen</h2>
          <p>Sie wissen jetzt, was die Arbeiten kosten. Der nächste Schritt: kostenlos bis zu drei Angebote.</p>
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

        with open(f"{dir_path}/index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated: {dir_path}/index.html")


if __name__ == "__main__":
    main()