#!/usr/bin/env python3
"""Generate heating/sanitary branch blog articles."""

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
            {
                "h2": "Was kostet eine Luft-Wärmepumpe?",
                "p": "Die Luft-Wärmepumpe ist der günstigste Einstieg. Die Anlage selbst kostet zwischen 12.000 und 18.000 Euro. Hinzu kommen Installationskosten von 3.000 bis 6.000 Euro. Für ein Einfamilienhaus rechnet man mit Gesamtkosten von 15.000 bis 24.000 Euro - bevor die Förderung abgezogen wird."
            },
            {
                "h2": "Sole-Wärmepumpe (Erdwärme)",
                "p": "Eine Sole-Wärmepumpe nutzt die Erdwärme über Erdkollektoren oder Erdsonden. Die Anschaffungskosten liegen bei 18.000 bis 28.000 Euro. Dazu kommen die Kosten für die Erschließung: Erdkollektoren kosten 5.000 bis 12.000 Euro, Erdbohrungen 8.000 bis 15.000 Euro. Gesamtkosten: 25.000 bis 45.000 Euro."
            },
            {
                "h2": "Betriebskosten und Effizienz",
                "p": "Die jährlichen Betriebskosten hängen von der Effizienz der Anlage und Ihrem Wärmebedarf ab. Eine gut gedämmte Wohnung mit 120 m² braucht etwa 12.000 kWh pro Jahr. Bei einem Strompreis von 30 Cent pro kWh und einer Jahresarbeitszahl von 3,5 liegen die Heizkosten bei etwa 1.030 Euro pro Jahr."
            },
            {
                "h2": "Förderung abziehen",
                "p": "Die Bundesförderung für effiziente Gebäude (BEG) fördert Wärmepumpen mit bis zu 25 Prozent der Kosten. Eine Luft-Wärmepumpe für 20.000 Euro wird so um 5.000 Euro günstiger. Dazu kommen oft lokale Programme von KfW, Ländern und Kommunen."
            },
            {
                "h2": "Regionaler Kostenvergleich",
                "p": "Die Installationskosten variieren je nach Region. München und Hamburg sind am teuersten, Leipzig und Dortmund am günstigsten. Für eine Luft-Wärmepumpe inklusive Installation:</p><div class='cost-box'><p><strong>Luft-Wärmepumpe, Komplett inkl. Installation:</strong><br>München: 18.000 bis 26.000 Euro<br>Stuttgart: 17.000 bis 24.000 Euro<br>Hamburg: 16.000 bis 23.000 Euro<br>Köln: 15.500 bis 22.000 Euro<br>Dortmund: 14.000 bis 20.000 Euro<br>Leipzig: 13.000 bis 19.000 Euro"
            }
        ],
        "faq": [
            {"q": "Lohnt sich eine Wärmepumpe auch im Altbau?", "a": "Ja, aber nur wenn das Gebäude gut gedämmt ist. Bei einer Heizlast über 80 Watt pro m² ist die Wärmepumpe unwirtschaftlich. Erst ab etwa 60 Watt pro m² macht sie Sinn."},
            {"q": "Kann ich meine Gasheizung durch eine Wärmepumpe ersetzen?", "a": "Ja, in vielen Fällen. Bei einer Öl- oder Gasheizung über 20 Jahren ist der Austausch fast immer sinnvoll. Die bestehende Hydraulik kann oft weiter genutzt werden."},
            {"q": "Wie lange hält eine Wärmepumpe?", "a": "Eine Wärmepumpe hält 15 bis 25 Jahre. Die Lebensdauer hängt von der Nutzung und der Wartung ab. Bei aggressivem Kalkwasser im Umlauf reduziert sich die Lebensdauer."},
            {"q": "Was ist der Unterschied zwischen Luft-Wärmepumpe und Erdwärme?", "a": "Luft-Wärmepumpen holen die Wärme aus der Außenluft. Sie sind günstiger, aber bei sehr niedrigen Temperaturen weniger effizient. Erdwärme ist teurer in der Installation, liefert aber ganzjährig konstante Temperaturen und ist effizienter."}
        ]
    },
    {
        "id": "waermepumpe-foerderung-2026",
        "title": "Wärmepumpe Förderung 2026 - Alle Programme im Überblick",
        "meta_desc": "Wärmepumpe Förderung 2026: BEG, KfW, BAFA, Landesprogramme. Wie Sie bis zu 40 Prozent der Kosten fördern lassen - Schritt für Schritt erklärt.",
        "badge": "Förderung",
        "headline": "Wärmepumpe Förderung 2026 - Alle Programme im Überblick",
        "sub": "BEG, KfW, BAFA, Landesförderung - die Förderlandschaft ist komplex. Hier finden Sie den Durchblick und erfahren, wie Sie möglichst viel Förderung bekommen.",
        "tag": "Wärmepumpe",
        "content": [
            {
                "h2": "Bundesförderung für effiziente Gebäude (BEG)",
                "p": "Die BEG ist das wichtigste Förderprogramm für Wärmepumpen. Sie zahlt 25 Prozent der Kosten als Zuschuss - bis zu 60.000 Euro pro Wohneinheit. Die Förderung gilt für Luft-Wärmepumpen, Sole-Wärmepumpen und Erdwärmepumpen. Wichtig: Sie müssen einen individuellen Sanierungsfahrplan (iSFP) haben oder ein CEE-Zertifikat vorlegen."
            },
            {
                "h2": "KfW-Kredit 262",
                "p": "Die KfW vergibt zinsgünstige Kredite für Wärmepumpen über das Programm 262. Bis zu 150.000 Euro pro Wohnung zu einem Zinssatz von derzeit etwa 1,5 Prozent. Die Kredite können mit dem BEG-Zuschuss kombiniert werden."
            },
            {
                "h2": "BAFA-Heizungsförderung",
                "p": "Das BAFA (Bundesamt für Wirtschaft und Ausfuhrkontrolle) fördert den Einbau von Wärmepumpen im Bestand. Die Förderung beträgt 25 Prozent der Kosten. Antragstellung ist vor Beginn der Maßnahme erforderlich. Das BAFA prüft die technischen Voraussetzungen und die Fachunternehmererklärung."
            },
            {
                "h2": "Landesprogramme und Kommunen",
                "p": "Zusätzlich zur Bundesförderung gibt es regionale Programme. Bayern fördert über die LfA, NRW über die NRW-Bank, Baden-Württemberg über die L-Bank. Manche Kommunen bieten eigene Zuschüsse. In München gibt es zum Beispiel einen Stadtwerkszuschuss von 500 bis 2.000 Euro für Wärmepumpen."
            },
            {
                "h2": "Kombination und Максимум",
                "p": "Die Förderungen lassen sich oft kombinieren. Eine Luft-Wärmepumpe für 20.000 Euro kann so aussehen: BEG 5.000 Euro + KfW-Kredit 8.000 Euro + Landesprogramm 2.000 Euro = 15.000 Euro Eigenanteil. Informieren Sie sich vor Beginn bei Ihrem Energieberater über die optimal Kombination."
            }
        ],
        "faq": [
            {"q": "Kann ich die Förderung auch für eine gemietete Wohnung beantragen?", "a": "Ja, aber als Mieter müssen Sie die Zustimmung des Eigentümers haben. Die Förderung wird trotzdem auf Ihren Namen beantragt, die Arbeiten müssen aber vom Eigentümer beauftragt werden."},
            {"q": "Was passiert wenn ich die Förderung beantragt habe, aber die Kosten niedriger ausfallen?", "a": "Sie müssen die Förderung anpassen lassen. Wenn die Kosten 20 Prozent unter dem geförderten Budget liegen, wird die Förderung entsprechend reduziert."},
            {"q": "Kann ich die Förderung auch für eine Wärmepumpe in einem Neubau bekommen?", "a": "Für Neubauten gelten andere Programme. Die BEG fördert primär Bestandssanierungen. Für Neubauten gibt es die KfW-Effizienzhaus-Standards."},
            {"q": "Wie finde ich einen guten Energieberater?", "a": "Die Verbraucherzentrale bietet Energieberatungen an. Für die Beantragung der BEG-Förderung müssen Sie einen zertifizierten Energieeffizienz-Experten hinzuziehen - eine Liste finden Sie auf der Website des BAFA."}
        ]
    },
    {
        "id": "klimaanlage-einbauen-kosten",
        "title": "Klimaanlage einbauen Kosten 2026 - Split, Multi-Split, mobil",
        "meta_desc": "Klimaanlage einbauen Kosten 2026: Split-Anlage ab 2.500 Euro, Multi-Split bis 8.000 Euro. Was Kühlung wirklich kostet - mit Betriebskosten und Wartung.",
        "badge": "Kosten",
        "headline": "Klimaanlage einbauen Kosten 2026",
        "sub": "Klimaanlage einbauen: Split oder Multi-Split? Hier sind die Kosten für Kauf, Installation und Betrieb - damit Sie wissen, was auf Sie zukommt.",
        "tag": "Klimaanlage",
        "content": [
            {
                "h2": "Split-Klimaanlage Kosten",
                "p": "Eine Split-Klimaanlage ist die häufigste Wahl für Wohnungen und kleine Büros. Das Außengerät wird an der Fassade montiert, das Innengerät im Raum. Kosten für eine einzelne Split-Anlage: 2.500 bis 5.000 Euro inklusive Installation. Für ein größeres Wohnzimmer oder eine Praxis reicht eine einzelne Anlage mit 3,5 bis 5 kW Kühlleistung."
            },
            {
                "h2": "Multi-Split-Anlage Kosten",
                "p": "Wenn mehrere Räume gekühlt werden sollen, lohnt sich eine Multi-Split-Anlage. Ein Außengerät versorgt bis zu fünf Innengeräte. Die Kosten: 5.000 bis 12.000 Euro je nach Anzahl der Innengeräte und Kühlleistung. Für ein Einfamilienhaus mit drei Schlafzimmern und Wohnzimmer liegt man bei etwa 8.000 bis 12.000 Euro."
            },
            {
                "h2": "Betriebskosten",
                "p": "Die laufenden Kosten hängen von der Nutzung ab. Eine Split-Anlage mit 3,5 kW verbraucht etwa 1,0 bis 1,5 kW Strom. Bei 500 Betriebsstunden pro Sommer (Juni bis August) und 30 Cent pro kWh sind das etwa 150 bis 225 Euro pro Jahr. Bei starker Nutzung können es 400 bis 600 Euro werden."
            },
            {
                "h2": "Was kostet die Installation?",
                "p": "Die Installationskosten sind oft höher als viele denken. Die Bohrung für die Kältemittelleitung kostet 150 bis 400 Euro. Die elektrische Verbindung 100 bis 200 Euro. Dazu kommen eventuelle Kabelkanäle und die Wandhalterung. Rechnen Sie mit 500 bis 1.500 Euro für die Installation, je nach Aufwand und Standort."
            },
            {
                "h2": "Mietgeräte als Alternative",
                "p": "Für eine Übergangszeit oder bei Mietwohnungen können mobile Klimageräte eine Lösung sein. Die Kosten: 30 bis 80 Euro pro Monat. Allerdings sind mobile Geräte weniger effizient und oft lauter als Split-Anlagen. Für eine dauerhafte Lösung lohnt sich die feste Installation."
            }
        ],
        "faq": [
            {"q": "Brauche ich eine Genehmigung für die Außeneinheit?", "a": "In Mietshäusern brauchen Sie die Zustimmung des Eigentümers. In Eigentumswohnungen entscheidet die Eigentümerversammlung. Bei freistehenden Häusern ist in der Regel keine Genehmigung nötig."},
            {"q": "Wie laut ist eine Split-Klimaanlage?", "a": "Moderne Split-Anlagen sind leise: 20 bis 35 dB im Innenraum. Das Außengerät liegt bei 45 bis 60 dB. Zum Vergleich: eine normale Unterhaltung liegt bei 50 dB."},
            {"q": "Kann ich die Klimaanlage auch zur Heizung nutzen?", "a": "Ja, die meisten Split- und Multi-Split-Anlagen können auch heizen. Sie funktionieren dann als Wärmepumpe. Die Effizienz ist im Heizbetrieb geringer als bei einer spezialisierten Wärmepumpe."},
            {"q": "Wie oft muss ich die Klimaanlage warten?", "a": "Mindestens einmal pro Jahr, idealerweise vor der Sommersaison. Die Wartung kostet 80 bis 150 Euro und umfasst die Reinigung des Filters, die Kältemittelprüfung und die Funktionskontrolle."}
        ]
    },
    {
        "id": "bad-sanierung-kosten-2026",
        "title": "Bad Sanierung Kosten 2026 - Was kostet eine komplette Badrenovierung?",
        "meta_desc": "Bad Sanierung Kosten 2026: Komplettsanierung ab 12.000 Euro, Dusche statt Wanne ab 4.000 Euro. Was die Renovierung wirklich kostt - nach Umfang und Ausstattung.",
        "badge": "Kosten",
        "headline": "Bad Sanierung Kosten 2026",
        "sub": "Badrenovierung: Die Kosten hängen stark vom Umfang ab. Hier finden Sie realistische Preise für Komplettsanierung, Teilrenovierung und einzelne Gewerke.",
        "tag": "Bad Sanierung",
        "content": [
            {
                "h2": "Was kostet eine Komplettsanierung?",
                "p": "Eine Komplettsanierung des Badezimmers umfasst den Abbruch des alten Bads, Neueinbau aller Sanitärkeramik, Fliesen, Leitungen und Armaturen. Für ein 8 m² Bad liegen die Kosten zwischen 15.000 und 35.000 Euro. Der große Preisunterschied hängt von der Ausstattung ab: eine Standardausstattung mit mittelpreisigen Fliesen und Sanitärkeramik kostet etwa 18.000 bis 25.000 Euro."
            },
            {
                "h2": "Dusche statt Wanne",
                "p": "Viele wollen statt der alten Wanne eine ebenerdige Dusche. Die Kosten für den Rückbau der Wanne und den Einbau einer Dusche mit Glaswand: 4.000 bis 8.000 Euro. Wenn die alten Fliesen entfernt und neu verfliest werden müssen, kommen 1.500 bis 3.000 Euro dazu."
            },
            {
                "h2": "Barrierefreies Bad",
                "p": "Ein barrierefreies Bad nach DIN 18040 kostet mehr als eine Standardrenovierung. Die Kosten liegen bei 25.000 bis 50.000 Euro für ein komplettes Bad. Dafür sind dann rutschfeste Fliesen, Haltegriffe, eine ebenerdige Dusche und ein höhenverstellbares WC eingebaut."
            },
            {
                "h2": "Einzelne Gewerke",
                "p": "Wenn Sie nicht alles auf einmal machen wollen, hier die Kosten für einzelne Arbeiten: WC-Wechsel 400 bis 800 Euro, Waschbecken 200 bis 500 Euro, Armaturen 150 bis 400 Euro, Fliesenlegen 40 bis 80 Euro pro m², Elektroarbeiten 200 bis 600 Euro."
            },
            {
                "h2": "Regionaler Vergleich",
                "p": "Die Handwerkerkosten variieren je nach Region. München ist am teuersten, Leipzig am günstigsten. Für eine Komplettsanierung mit mittlerer Ausstattung:</p><div class='cost-box'><p><strong>Komplettsanierung Bad, 8 m², mittlere Ausstattung:</strong><br>München: 22.000 bis 32.000 Euro<br>Stuttgart: 20.000 bis 28.000 Euro<br>Hamburg: 18.000 bis 26.000 Euro<br>Köln: 17.000 bis 25.000 Euro<br>Dortmund: 15.000 bis 22.000 Euro<br>Leipzig: 13.000 bis 20.000 Euro"
            }
        ],
        "faq": [
            {"q": "Wie lange dauert eine Bad Komplettsanierung?", "a": "Eine Komplettsanierung dauert zwei bis vier Wochen, je nach Umfang und Verfügbarkeit der Handwerker. In dieser Zeit ist das Bad nicht nutzbar."},
            {"q": "Kann ich während der Sanierung im Haus wohnen?", "a": "Ja, wenn Sie ein zweites Badezimmer oder eine Gästetoilette nutzen können. Wenn nicht, sollten Sie mit einem Hotelspende für die Zeit rechnen."},
            {"q": "Wann lohnt sich eine Sanierung statt eines Neubaus?", "a": "Wenn die Substanz gut ist und nur die Optik und Ausstattung veraltet sind. Wenn aber die Leitungen marode sind und die Feuchtigkeit die Bausubstanz angegriffen hat, ist ein kompletter Rückbau oft die bessere Wahl."},
            {"q": "Wie finde ich gute Sanitärbetriebe?", "a": "Fragen Sie in Ihrem Bekanntenkreis nach Empfehlungen. Sie können auch drei Angebote einholen und diese vergleichen. Achten Sie dabei nicht nur auf den Preis, sondern auch auf die Erfahrung mit ähnlichen Projekten."}
        ]
    },
    {
        "id": "heizungsbauer-finden",
        "title": "Heizungsbauer finden - So finden Sie einen guten Betrieb",
        "meta_desc": "Heizungsbauer finden: Worauf Sie bei der Wahl achten sollten, welche Qualifikationen wichtig sind und wie Sie Angebote vergleichen.",
        "badge": "Ratgeber",
        "headline": "Heizungsbauer finden - So finden Sie einen guten Betrieb",
        "sub": "Einen guten Heizungsbauer zu finden ist nicht leicht. Hier erfahren Sie, woran Sie einen seriösen Betrieb erkennen und wie Sie Angebote richtig vergleichen.",
        "tag": "Heizungsbau",
        "content": [
            {
                "h2": "Darauf kommt es an",
                "p": "Ein guter Heizungsbauer zeichnet sich durch mehrere Dinge aus: Er bietet eine Vor-Ort-Beratung an, kommt innerhalb weniger Tage, erklärt die verschiedenen Optionen verständlich und gibt Ihnen Zeit zur Entscheidung. Seriöse Betriebe drängen nicht zum Kauf und erstellen detaillierte Angebote mit Kostenaufstellung."
            },
            {
                "h2": "Welche Qualifikationen sind wichtig?",
                "p": "Der Betrieb sollte einen Meisterbrief haben oder ein eingetragenes Installateurunternehmen sein. Für Gas- und Ölheizungen braucht der Betrieb einen Eintrag in das Installateurverzeichnis der zuständigen Behörde. Für Wärmepumpen gibt es zusätzliche Qualifikationen, die das Unternehmen vorweisen sollte."
            },
            {
                "h2": "Drei Angebote einholen",
                "p": "Holen Sie immer drei Angebote von verschiedenen Betrieben ein. Vergleichen Sie nicht nur den Gesamtpreis, sondern prüfen Sie auch: Welche Materialien werden verwendet? Welche Garantie gibt es? Wie sind die Zahlungsbedingungen? Ein günstiges Angebot kann durch versteckte Kosten oder minderwertige Materialien teurer werden."
            },
            {
                "h2": "Lokale Referenzen prüfen",
                "p": "Fragen Sie den Betrieb nach Referenzen in Ihrer Nähe. Ein Betrieb, der regelmäßig in Ihrem Viertel arbeitet, kennt die lokalen Gegebenheiten und hat bereits Referenzen aus der Nachbarschaft. Das ist ein gutes Zeichen."
            },
            {
                "h2": "Warnsignale",
                "p": "Seien Sie vorsichtig bei: Drängeln zu schnellen Entscheidungen, Angeboten ohne Vor-Ort-Beratung, Preisen, die deutlich unter dem Durchschnitt liegen, mündlichen Zusagen, die nicht im Angebot stehen. Ein guter Betrieb hat normalerweise Wartezeiten von zwei bis sechs Wochen."
            }
        ],
        "faq": [
            {"q": "Wie finde ich einen Heizungsbauer in meiner Region?", "a": "Sie können das Installateurverzeichnis Ihrer Stadt oder Gemeinde einsehen. Oder Sie nutzen Empfehlungen von Nachbarn und Bekannten. Online-Bewertungen können auch hilfreich sein, sollten aber kritisch betrachtet werden."},
            {"q": "Was kostet eine Beratung?", "a": "Eine gute Beratung vor Ort ist in der Regel kostenlos. Der Betrieb macht dies als Service, um Sie als Kunden zu gewinnen. Wenn ein Betrieb für die Beratung Geld verlangt, ist das eher ungewöhnlich."},
            {"q": "Wie lange dauert die Installation einer neuen Heizung?", "a": "Der Einbau einer neuen Gasheizung oder Wärmepumpe dauert ein bis zwei Wochen. Bei einem kompletten Heizungstausch inklusive Leitungen kann es auch drei bis vier Wochen dauern."},
            {"q": "Gibt es Garantie auf die Arbeit?", "a": "Ja, der Betrieb haftet für seine Arbeit. Bei mangelhafter Ausführung können Sie nachbessern lassen oder den Schaden ersetzt bekommen. Die gesetzliche Gewährleistung beträgt zwei Jahre, bei arglistiger Täuschung bis zu dreißig Jahre."}
        ]
    },
    {
        "id": "solarthermie-vs-photovoltaik",
        "title": "Solarthermie vs. Photovoltaik - Was ist besser für Ihr Haus?",
        "meta_desc": "Solarthermie oder Photovoltaik? Was die beiden Technologien unterscheidet, was sie kosten und für wen sich welche Lösung lohnt.",
        "badge": "Energie",
        "headline": "Solarthermie vs. Photovoltaik - Was ist besser?",
        "sub": "Beide nutzen die Sonne, aber unterschiedlich. Solarthermie für warmes Wasser, Photovoltaik für Strom. Hier erfahren Sie, was für Ihr Haus sinnvoller ist.",
        "tag": "Solarthermie",
        "content": [
            {
                "h2": "Der grundlegende Unterschied",
                "p": "Solarthermie wandelt Sonnenlicht direkt in Wärme um. Die Photovoltaik erzeugt aus Licht elektrischen Strom. Solarthermie ist effizienter bei der Wärmeerzeugung, Photovoltaik bei der Stromerzeugung. Beide haben unterschiedliche Einsatzbereiche."
            },
            {
                "h2": "Was kostet Solarthermie?",
                "p": "Eine Solarthermieanlage für warmes Wasser kostet 4.000 bis 8.000 Euro inklusive Installation. Für eine Anlage mit Heizungsunterstützung liegen die Kosten bei 8.000 bis 14.000 Euro. Die Anlage hat einen Wirkungsgrad von 40 bis 60 Prozent bei der Wärmegewinnung."
            },
            {
                "h2": "Was kostet Photovoltaik?",
                "p": "Eine Photovoltaikanlage mit 5 kWp kostet etwa 8.000 bis 12.000 Euro. Mit Speicher kommen 5.000 bis 10.000 Euro dazu. Der Wirkungsgrad moderner Module liegt bei 20 bis 22 Prozent. Der erzeugte Strom kann selbst genutzt oder verkauft werden."
            },
            {
                "h2": "Für wen lohnt sich Solarthermie?",
                "p": "Solarthermie lohnt sich besonders für Haushalte mit hohem Warmwasserverbrauch im Sommer. Wenn Sie im Sommer fast kein warmes Wasser mit der Heizung erzeugen müssen, sparen Sie Heizkosten. Die Amortisationszeit liegt bei 10 bis 15 Jahren."
            },
            {
                "h2": "Für wen lohnt sich Photovoltaik?",
                "p": "Photovoltaik lohnt sich fast immer, wenn Sie einen Teil des erzeugten Stroms selbst verbrauchen. Mit einem Speicher können Sie bis zu 70 Prozent des produzierten Stroms selbst nutzen. Die Amortisationszeit liegt bei 8 bis 12 Jahren - deutlich schneller als Solarthermie."
            }
        ],
        "faq": [
            {"q": "Kann ich beides kombinieren?", "a": "Ja, Sie können sowohl Solarthermie als auch Photovoltaik auf dem Dach haben. Das ist sinnvoll, wenn Sie sowohl Warmwasser als auch Strom erzeugen wollen. Allerdings ist der Platz auf dem Dach begrenzt."},
            {"q": "Was ist effizienter?", "a": "Photovoltaik ist in Bezug auf die Energieausbeute pro Fläche effizienter, weil Strom einen höheren Wert hat als Wärme. Solarthermie nutzt die Sonnenenergie aber effizienter für die Wärmeerzeugung."},
            {"q": "Welche Förderung gibt es?", "a": "Solarthermie wird über das BAFA gefördert, Photovoltaik über die KfW und das EEG. Für Photovoltaik gibt es einen Einspeise tariff von etwa 8 Cent pro kWh."},
            {"q": "Wie lange halten die Anlagen?", "a": "Solarthermieanlagen halten 20 bis 30 Jahre, Photovoltaikmodule 25 bis 35 Jahre. Beide haben relativ geringe Wartungskosten."}
        ]
    },
    {
        "id": "klimaanlage-wartung",
        "title": "Klimaanlage Wartung - Darauf sollten Sie achten",
        "meta_desc": "Klimaanlage Wartung: Wie oft, was wird gemacht, was kostet es. So halten Sie Ihre Anlage in Schuss und vermeiden Folgeschäden.",
        "badge": "Wartung",
        "headline": "Klimaanlage Wartung - So halten Sie Ihre Anlage in Schuss",
        "sub": "Eine regelmäßige Wartung verlängert die Lebensdauer und senkt die Betriebskosten. Hier erfahren Sie, was gemacht wird und was es kostet.",
        "tag": "Klimaanlage",
        "content": [
            {
                "h2": "Warum Wartung wichtig ist",
                "p": "Eine schlecht gewartete Klimaanlage verbraucht mehr Strom, kühlt schlechter und kann gesundheitsschädlich werden. Staub und Schmutz sammeln sich im Filter und im Verdampfer. Das kann zu Atemwegsproblemen führen. Außerdem steigt die Wahrscheinlichkeit von Defekten."
            },
            {
                "h2": "Was wird bei der Wartung gemacht?",
                "p": "Eine professionelle Wartung umfasst: Reinigung oder Austausch des Luftfilters, Reinigung des Verdampfers, Prüfung des Kältemittels und Nachfüllen falls nötig, Kontrolle der elektrischen Verbindungen, Reinigung der Außeneinheit, Funktionsprüfung aller Einstellungen."
            },
            {
                "h2": "Wie oft wartung?",
                "p": "Für private Split-Anlagen gilt: mindestens einmal pro Jahr warten, idealerweise vor der Sommersaison im April oder Mai. Bei gewerblichen Anlagen oder bei starker Nutzung kann eine halbjährliche Wartung sinnvoll sein."
            },
            {
                "h2": "Was kostet eine Wartung?",
                "p": "Eine professionelle Wartung kostet 80 bis 150 Euro pro Innengerät. Bei einer Multi-Split-Anlage mit drei Innengeräten liegen die Kosten bei 200 bis 350 Euro. Wenn nur der Filter gereinigt werden soll, geht das auch selbst - folgen Sie der Anleitung in der Bedienungsanleitung."
            },
            {
                "h2": "Warnsignale",
                "p": "Diese Zeichen deuten auf Probleme hin: Die Anlage kühlt weniger als früher, es riecht muffig oder unangenehm, die Anlage läuft häufiger oder länger als gewöhnlich, es gibt ungewöhnliche Geräusche. In diesen Fällen sollten Sie einen Fachbetrieb rufen."
            }
        ],
        "faq": [
            {"q": "Kann ich die Wartung selbst machen?", "a": "Den Filter können Sie selbst reinigen. Die Kältemittelprüfung und die Kontrolle der elektrischen Anlage sollten Fachleute machen. Eine jährliche professionelle Wartung ist empfehlenswert."},
            {"q": "Was passiert wenn ich die Wartung vernachlässige?", "a": "Die Anlage wird weniger effizient, verbraucht mehr Strom und kann schneller kaputtgehen. Auch gesundheitliche Risiken durch Schimmel und Bakterien sind möglich."},
            {"q": "Gibt es einen Wartungsvertrag?", "a": "Ja, viele Installateure bieten Wartungsverträge an. Die Kosten liegen bei 80 bis 150 Euro pro Jahr und beinhalten eine jährliche Inspektion und eine eventuelle Reinigung."},
            {"q": "Wie erkenne ich einen guten Wartungsbetrieb?", "a": "Ein guter Betrieb kommt mit einem vollständigen Bericht zurück, erklärt was er gemacht hat und empfiehlt nur notwendige Arbeiten. Er drängt nicht zum Kauf neuer Geräte."}
        ]
    },
    {
        "id": "sanitaer-installation-kosten",
        "title": "Sanitär Installation Kosten 2026 - Was Sie für Rohre und Armaturen zahlen",
        "meta_desc": "Sanitär Installation Kosten 2026: Neue Leitungen, Armaturen, Wasseraufbereitung. Was die wichtigsten Arbeiten kosten und wie Sie sparen können.",
        "badge": "Kosten",
        "headline": "Sanitär Installation Kosten 2026",
        "sub": "Wenn Sie neue Sanitärleitungen oder Armaturen brauchen, kommen schnell mehrere Tausend Euro zusammen. Hier finden Sie realistische Kosten für die wichtigsten Arbeiten.",
        "tag": "Sanitär",
        "content": [
            {
                "h2": "Neue Wasserleitungen verlegen",
                "p": "Wenn alte Wasserrohre ausgetauscht werden müssen, hängen die Kosten von der Länge und dem Material ab. Kupferrohre kosten 25 bis 40 Euro pro Meter, Edelstahl-Wellrohre 30 bis 50 Euro pro Meter. Für ein Einfamilienhaus mit 30 Metern Gesamtlänge liegen die Materialkosten bei 1.000 bis 2.000 Euro. Mit Installation kommen 2.000 bis 4.000 Euro dazu."
            },
            {
                "h2": "Abwasserleitungen erneuern",
                "p": "Abwasserleitungen sind oft schwieriger zu erneuern als Wasserleitungen, weil sie Gefälle brauchen und oft in Böden oder Decken verlegt sind. Die Kosten liegen bei 80 bis 150 Euro pro Meter für die Erneuerung. Wenn Aufbrüche im Boden nötig sind, können die Kosten deutlich höher liegen."
            },
            {
                "h2": "Armaturen und Mischbatterien",
                "p": "Eine hochwertige Armatur für das Waschbecken kostet 150 bis 400 Euro. Für die Badewanne oder Dusche liegen die Kosten bei 200 bis 600 Euro pro Armatur. Billige Armaturen aus dem Baumarkt kosten 30 bis 80 Euro, halten aber oft nur wenige Jahre."
            },
            {
                "h2": "Wasserenthärtungsanlage",
                "p": "In Regionen mit hartem Wasser kann eine Wasserenthärtungsanlage sinnvoll sein. Die Kosten: 1.500 bis 3.500 Euro für die Anlage, plus 200 bis 400 Euro pro Jahr für Salz und Wartung. Die Anlage verlängert die Lebensdauer von Leitungen und Geräten."
            },
            {
                "h2": "Was kostet ein Klempner?",
                "p": "Die Kosten für den Installateur hängen von der Region und der Komplexität der Arbeit ab. Der Stundensatz liegt zwischen 50 und 90 Euro. Hinzu kommen Materialkosten und eventuelle Anfahrtskosten. Für eine einfache Armaturen-Reparbeit sollten Sie 100 bis 200 Euro einplanen, für eine Leitungsverlegung mehrere Tausend Euro."
            }
        ],
        "faq": [
            {"q": "Wann sollten Wasserleitungen erneuert werden?", "a": "Wenn die Leitungen älter als 30 Jahre sind, wenn es häufig zu Lecks kommt, wenn das Wasser rostig oder trüb ist. Bei verzinkten Eisenrohren ist eine Erneuerung nach 30 bis 40 Jahren fällig."},
            {"q": "Was ist besser: Kupfer oder Edelstahl?", "a": "Beide Materialien sind hochwertig und langlebig. Kupfer ist flexibler und einfacher zu verarbeiten, Edelstahl ist resistenter gegen Kalk und hat eine längere Lebensdauer. Der Preis ist ähnlich."},
            {"q": "Kann ich Sanitärarbeiten selbst machen?", "a": "Kleine Arbeiten wie das Wechseln von Armaturen können Sie selbst machen. Für Leitungsarbeiten und Arbeiten am Abwasser brauchen Sie einen Fachbetrieb. Bei nicht fachgerechter Installation können Versicherungsschutz und Gewährleistung verloren gehen."},
            {"q": "Wie finde ich einen guten Sanitärbetrieb?", "a": "Empfehlungen von Nachbarn und Bekannten sind oft der beste Weg. Sie können auch drei Angebote einholen und diese vergleichen. Achten Sie auf detaillierte Kostenaufstellungen."}
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
        <a href="/#so-funktionierts" class="nav__link">So funktioniert's</a>
        <a href="/#services" class="nav__link">Leistungen</a>
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
        <div class="card-badge"><a href="/blog/" style="color:inherit">Blog</a></div>
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
    html = '''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Heizung & Sanitär Blog - Ratgeber für Wärmepumpe, Klimaanlage und Bad</title>
  <meta name="description" content="Wärmepumpe Kosten, Förderung, Klimaanlage Wartung - Ratgeber und Preisinformationen für Heizung, Sanitär und Klimatechnik.">
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
      <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </header>

  <section class="hero hero--small">
    <div class="container">
      <div class="hero__content">
        <h1>Heizung & Sanitär Blog</h1>
        <p class="hero__sub">Wärmepumpe Kosten, Förderung, Klimaanlage Wartung, Bad Sanierung - hier finden Sie Antworten auf die wichtigsten Fragen rund um Heizung und Sanitär.</p>
      </div>
    </div>
  </section>

  <section class="section section--light">
    <div class="container">
      <div class="grid grid--3">
'''
    for article in ARTICLES:
        html += f'''
        <a href="/blog/{article["id"]}/" class="card card--link">
          <div class="card-badge" style="margin-top:0;margin-bottom:12px">{article["badge"]}</div>
          <h3>{article["title"]}</h3>
          <p>{article["sub"]}</p>
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
        <a href="/glossar/" class="card card--link"><h3>Heizung & Sanitär Glossar</h3><p>Fachbegriffe erklärt - von Wärmepumpe bis Trinkwasser.</p></a>
        <a href="/waermepumpe/berlin/" class="card card--link"><h3>Wärmepumpe Berlin</h3><p>Geprüfte Betriebe, Bundesförderung, lokale Expertise.</p></a>
        <a href="/heizungsbau/muenchen/" class="card card--link"><h3>Heizungsbau München</h3><p>LfA Bayern Förderung, lokale Betriebe.</p></a>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand"><span class="logo">hausbau<span class="logo-accent">.pro</span></span><p>Kostenlose Vermittlung von geprüften Heizungsbauern und Installateuren in ganz Deutschland.</p></div>
      <div class="footer__links"><h4>Wissen</h4><a href="/glossar/">Glossar</a><a href="/blog/">Blog</a></div>
      <div class="footer__links"><h4>Services</h4><a href="/waermepumpe/">Wärmepumpe</a><a href="/heizungsbau/">Heizungsbau</a><a href="/sanitaer/">Sanitär</a><a href="/klimaanlage/">Klimaanlage</a></div>
    </div>
  </footer>
  <script src="/js/main.js"></script>
</body>
</html>'''
    return html


def main():
    import os
    os.makedirs("blog", exist_ok=True)

    # Generate blog index
    with open("blog/index.html", "w", encoding="utf-8") as f:
        f.write(generate_blog_index())
    print("Generated: blog/index.html")

    # Generate individual articles
    for article in ARTICLES:
        dir_path = f"blog/{article['id']}"
        os.makedirs(dir_path, exist_ok=True)

        html = generate_blog_article(article)

        # Add content sections
        for section in article["content"]:
            html += section_to_html(section) + "\n"

        html += '''
        </div>
        <div>
'''
        # Add FAQ section
        if article.get("faq"):
            html += "          <h2 style='margin-bottom:1rem'>Häufige Fragen</h2>\n"
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
          <p>Sie wissen jetzt, was die Arbeiten kosten. Der nächste Schritt: kostenlos bis zu drei Angebote von geprüften Betrieben in Ihrer Region.</p>
          <a href="/#angebot" class="btn btn--primary btn--lg">Kostenlos Angebot anfordern</a>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand"><span class="logo">hausbau<span class="logo-accent">.pro</span></span><p>Kostenlose Vermittlung von geprüften Heizungsbauern und Installateuren in ganz Deutschland.</p></div>
      <div class="footer__links"><h4>Wissen</h4><a href="/glossar/">Glossar</a><a href="/blog/">Blog</a></div>
      <div class="footer__links"><h4>Services</h4><a href="/waermepumpe/">Wärmepumpe</a><a href="/heizungsbau/">Heizungsbau</a><a href="/sanitaer/">Sanitär</a><a href="/klimaanlage/">Klimaanlage</a></div>
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