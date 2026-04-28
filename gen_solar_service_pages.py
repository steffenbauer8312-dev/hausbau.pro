#!/usr/bin/env python3
"""
Generate all Solar/Photovoltaik service pages.
12 services × 14 cities = 168 HTML pages.
Run: python gen_solar_service_pages.py
"""

import os

# =============================================================================
# CITY DATA (shared across all services)
# =============================================================================

CITIES = {
    "berlin": {
        "name": "Berlin",
        "region": "Berlin",
        "plz": "10115 bis 14199",
        "plz_short": "10115",
        "neighborhoods": ["Mitte", "Prenzlauer Berg", "Kreuzberg", "Charlottenburg", "Neukölln", "Schöneberg", "Wedding", "Tempelhof"],
        "architecture": "Gemischte Bausubstanz: Altbauten mit Satteldächern in Prenzlauer Berg, Flachdächer am Potsdamer Platz, Photovoltaik-Aufdachanlagen in Neubauten",
        "famous": "Brandenburger Tor, Berliner Mauer, Techno, Berlinale, BVG",
        "reviews": [
            {"text": "Unsere PV-Anlage auf dem Dach in Charlottenburg. Über das Portal drei Angebote bekommen - alle aus Berlin. Der Betrieb aus Schöneberg hat sauber installiert.", "name": "Thomas K.", "city": "Berlin-Charlottenburg", "service": "PV-Anlage 2025"},
            {"text": "Balkonkraftwerk für unsere Mietwohnung in Kreuzberg. Die Anlage liefert im Sommer genug Strom für unsere Geräte. Super einfache Installation.", "name": "Sabine M.", "city": "Berlin-Kreuzberg", "service": "Balkonkraftwerk 2024"},
            {"text": "Wallbox für unser E-Auto in Prenzlauer Berg. Schnelle Installation, gute Beratung. Lädt jetzt mit 11kW.", "name": "Mike R.", "city": "Berlin-Prenzlauer Berg", "service": "Wallbox 2025"},
        ],
        "faq": [
            {"q": "Welche Berliner Bezirke werden abgedeckt?", "a": "Alle 12 Bezirke: Mitte, Prenzlauer Berg, Kreuzberg, Charlottenburg, Neukölln, Schöneberg, Wedding, Tempelhof, Friedrichshain, Pankow, Spandau und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Berliner PV-Installateure melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine PV-Anlage in Berlin?", "a": "Für ein typisches Berliner Einfamilienhaus liegen die Kosten für eine 10 kWp Anlage zwischen 12.000 und 20.000 Euro. EEG und KfW machen es attraktiver."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich. Keinerlei Druck, keine Verpflichtung."},
            {"q": "Gibt es für Berlin spezielle Auflagen?", "a": "Das Erneuerbare-Energien-Gesetz (EEG) und das Baurecht regeln die Installation. Unsere Betriebe kennen die Vorschriften."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte, kein Spam."},
        ],
    },
    "muenchen": {
        "name": "München",
        "region": "Bayern",
        "plz": "80331 bis 81929",
        "plz_short": "80331",
        "neighborhoods": ["Altstadt", "Schwabing", "Maxvorstadt", "Bogenhausen", "Pasing", "Neuhausen", "Giesing", "Moosach"],
        "architecture": "Steile Satteldächer mit Biberschwanz in Schwabing, Flachdächer in Pasing, PV-Anlagen auf Villen in Bogenhausen",
        "famous": "Oktoberfest, BMW, Allianz Arena, Marienplatz",
        "reviews": [
            {"text": "PV-Anlage auf unserem Satteldach in Schwabing. Drei Angebote eingeholt, Betrieb aus dem Viertel genommen. Die Anlage läuft seit einem Jahr einwandfrei.", "name": "Ursula K.", "city": "München-Schwabing", "service": "PV-Anlage 2025"},
            {"text": "Balkonkraftwerk für unser Reihenhaus in Pasing. Die Beratung war gut - auch ehrlich wenn eine Volldachanlage sinnvoller wäre. Gute Beratung.", "name": "Florian M.", "city": "München-Pasing", "service": "Balkonkraftwerk 2025"},
            {"text": "PV-Speicher für unser Haus in Giesing. Neue Batterie für 10kWh. Der Eigenverbrauch ist von 30 auf 70% gestiegen.", "name": "Simone R.", "city": "München-Giesing", "service": "PV-Speicher 2024"},
        ],
        "faq": [
            {"q": "Welche Münchner Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, Lehel, Maxvorstadt, Schwabing, Neuhausen, Giesing, Sendling, Pasing, Bogenhausen, Moosach und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Münchner PV-Installateure melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine PV-Anlage in München?", "a": "München ist nicht billig - dementsprechend liegen die Kosten etwas höher. Eine 10 kWp Anlage liegt zwischen 14.000 und 22.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Die Angebote kommen unverbindlich. Wenn nichts dabei ist, gehen Sie woanders hin."},
            {"q": "Wie funktioniert das mit der Förderung?", "a": "BAFA und KfW fördern PV-Anlagen und Speicher. Unsere Betriebe helfen bei der Antragstellung."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "koeln": {
        "name": "Köln",
        "region": "Nordrhein-Westfalen",
        "plz": "50667 bis 51149",
        "plz_short": "50667",
        "neighborhoods": ["Innenstadt", "Ehrenfeld", "Nippes", "Mülheim", "Lindenthal", "Rodenkirchen", "Porz", "Deutz"],
        "architecture": "Rheinische Bausubstanz mit älteren Satteldächern, PV-Aufdachanlagen in Neubauten, Flachdächer in Porz",
        "famous": "Kölner Dom, Karneval, Rhein, RTL",
        "reviews": [
            {"text": "Unsere PV-Anlage in Ehrenfeld war ein großer Schritt. Drei Angebote eingeholt, auf 10kWp mit Speicher umgestiegen. Die Förderung hat viel gebracht.", "name": "Thomas B.", "city": "Köln-Ehrenfeld", "service": "PV-Anlage 2025"},
            {"text": "Wallbox für unser E-Auto in der Innenstadt. Schnelle Beratung, saubere Installation. Jetzt laden wir mit 22kW.", "name": "Sandra K.", "city": "Köln-Innenstadt", "service": "Wallbox 2025"},
            {"text": "Balkonkraftwerk für unsere Mietwohnung in Mülheim. Die Anlage ist seit dem Sommer in Betrieb und spart Stromkosten.", "name": "Marco L.", "city": "Köln-Mülheim", "service": "Balkonkraftwerk 2024"},
        ],
        "faq": [
            {"q": "Welche Kölner Stadtteile werden abgedeckt?", "a": "Unsere Partnerbetriebe arbeiten in ganz Köln: Ehrenfeld, Nippes, Mülheim, Lindenthal, Rodenkirchen, Porz, Deutz, Chorweiler, Kalk und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Kölner PV-Installateure melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine PV-Anlage in Köln?", "a": "Die Kosten hängen von Größe und Zustand ab. Eine 10 kWp Anlage liegt zwischen 12.000 und 20.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Die Angebote sind unverbindlich. Keinerlei Druck."},
            {"q": "Sind die Betriebe aus Köln oder aus dem Umland?", "a": "Wir leiten Ihre Anfrage zuerst an Kölner Betriebe weiter. Bei Bedarf erweitern wir auf das Umland."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "hamburg": {
        "name": "Hamburg",
        "region": "Norddeutschland",
        "plz": "20095 bis 21149",
        "plz_short": "20095",
        "neighborhoods": ["Altstadt", "Neustadt", "HafenCity", "St. Pauli", "Altona", "Eppendorf", "Winterhude", "Barmbek"],
        "architecture": "Klassische Hamburger Reihenhäuser mit Satteldächern, Flachdächer am Hafen, PV-Anlagen in Neubaugebieten",
        "famous": "Hafen, Elbphilharmonie, Reeperbahn, Hamburger SV",
        "reviews": [
            {"text": "PV-Anlage in Eppendorf war 40 Jahre alte Dacheindeckung. Drei Angebote bekommen, Betrieb aus dem Viertel genommen. Neue Anlage, 10kWp, läuft super.", "name": "Friedrich B.", "city": "Hamburg-Eppendorf", "service": "PV-Anlage 2025"},
            {"text": "Balkonkraftwerk für unser Reihenhaus in Winterhude. Die Beratung war gut - auch ehrlich wenn eine Volldachanlage sinnvoller wäre. Haben uns dann doch fürs Balkonkraftwerk entschieden.", "name": "Nina T.", "city": "Hamburg-Winterhude", "service": "Balkonkraftwerk 2025"},
            {"text": "PV-Speicher für unser Haus in der HafenCity. Die Batterie war die richtige Entscheidung. Eigenverbrauch jetzt bei 75%.", "name": "Heike M.", "city": "Hamburg-HafenCity", "service": "PV-Speicher 2025"},
        ],
        "faq": [
            {"q": "Welche Hamburger Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, Neustadt, HafenCity, St. Pauli, Altona, Eppendorf, Winterhude, Barmbek, Bergedorf, Blankenese und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Hamburger PV-Installateure melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine PV-Anlage in Hamburg?", "a": "Die Kosten in Hamburg liegen im oberen Bereich. Eine 10 kWp Anlage liegt zwischen 13.000 und 21.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich."},
            {"q": "Was ist mit dem Hamburger Wetter?", "a": "Die Feuchtigkeit und der Wind sind Themen. Unsere Hamburger Betriebe kennen die lokalen Bedingungen."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "stuttgart": {
        "name": "Stuttgart",
        "region": "Baden-Württemberg",
        "plz": "70173 bis 70599",
        "plz_short": "70173",
        "neighborhoods": ["Bad Cannstatt", "Feuerbach", "Vaihingen", "Degerloch", "Möhringen", "Sillenbuch", "Zuffenhausen", "Hedelfingen"],
        "architecture": "Steile Hanglagen mit Satteldächern, PV-Anlagen auf den Fildern, Flachdächer in Vaihingen",
        "famous": "Mercedes-Benz, Porsche, Stuttgarter Weihnachtsmarkt",
        "reviews": [
            {"text": "PV-Anlage in Degerloch war eine große Entscheidung. Drei Angebote geholt, Betrieb aus dem Süden genommen. Die Anlage war nach zwei Tagen installiert.", "name": "Monika W.", "city": "Stuttgart-Degerloch", "service": "PV-Anlage 2025"},
            {"text": "PV-Montage für unser Haus in Vaihingen. Die Beratung war umfassend. Wir haben uns dann für eine Aufdachanlage entschieden - passt gut.", "name": "Thomas K.", "city": "Stuttgart-Vaihingen", "service": "PV-Montage 2025"},
            {"text": "Wallbox in Bad Cannstatt. Neue Ladestation, 22kW. Der Betrieb war pünktlich und sauber.", "name": "Julia F.", "city": "Stuttgart-Bad Cannstatt", "service": "Wallbox 2025"},
        ],
        "faq": [
            {"q": "Welche Stuttgarter Stadtbezirke werden abgedeckt?", "a": "Alle PLZ-Gebiete: 70173 bis 70199 (Mitte), 70372 bis 70376 (Bad Cannstatt), 70431 bis 70469 (Feuerbach, Zuffenhausen), 70563 bis 70599 (Vaihingen, Degerloch)."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Innerhalb von 24 Stunden. In Stuttgart sind die Betriebe auch in den Stadtbezirken gut erreichbar."},
            {"q": "Was kostet eine PV-Anlage in Stuttgart?", "a": "Die Kosten liegen in Stuttgart etwas über dem Bundesdurchschnitt. Eine 10 kWp Anlage liegt zwischen 14.000 und 22.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich."},
            {"q": "Stuttgart ist hügelig - spielt das eine Rolle?", "a": "Ja. Die Topografie und die Südlage machen Stuttgart zu einer der besten Regionen für PV. Unsere Stuttgarter Betriebe kennen das."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur an die vermittelten Betriebe weitergegeben. Nicht an Dritte."},
        ],
    },
    "dortmund": {
        "name": "Dortmund",
        "region": "Nordrhein-Westfalen",
        "plz": "44135 bis 44379",
        "plz_short": "44135",
        "neighborhoods": ["Innenstadt", "Kreuzviertel", "Nordstadt", "Hörde", "Hombruch", "Brackel", "Aplerbeck", "Barop"],
        "architecture": "Ruhrgebiets-Bausubstanz mit älteren Satteldächern, PV-Anlagen in neueren Siedlungen, Flachdächer in Innenstadt",
        "famous": "SIGNAL IDUNA PARK, Bier, Phoenix, Möller",
        "reviews": [
            {"text": "PV-Anlage in Hombruch war eine große Entscheidung. Über das Portal drei Angebote bekommen, Betrieb aus dem Ruhrgebiet genommen. Neue Anlage, läuft einwandfrei.", "name": "Ursula K.", "city": "Dortmund-Hombruch", "service": "PV-Anlage 2025"},
            {"text": "Balkonkraftwerk für unser Reihenhaus in der Nordstadt. Drei Angebote, schnelle Ausführung. Die Förderung war ein großer Anteil.", "name": "Jens P.", "city": "Dortmund-Nordstadt", "service": "Balkonkraftwerk 2025"},
            {"text": "Wallbox für unser E-Auto in Hörde. Der Betrieb aus dem Umland hat kompetent beraten. Die Ladestation ist seit einem Jahr in Betrieb.", "name": "Simone A.", "city": "Dortmund-Hörde", "service": "Wallbox 2024"},
        ],
        "faq": [
            {"q": "Welche Dortmunder Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Innenstadt, Kreuzviertel, Nordstadt, Hörde, Hombruch, Brackel, Aplerbeck, Barop und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Dortmunder PV-Installateure melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine PV-Anlage in Dortmund?", "a": "Die Kosten im Ruhrgebiet sind günstiger als in den Großstädten. Eine 10 kWp Anlage liegt zwischen 10.000 und 18.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Die Angebote sind unverbindlich."},
            {"q": "Dortmund hat viel Industrie - spielt das eine Rolle?", "a": "Nein. Die pv-Anlage funktioniert unabhängig von der Umgebung. Wichtig ist die Ausrichtung des Daches."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "frankfurt": {
        "name": "Frankfurt am Main",
        "region": "Hessen",
        "plz": "60306 bis 60599",
        "plz_short": "60311",
        "neighborhoods": ["Innenstadt", "Sachsenhausen", "Westend", "Bornheim", "Nordend", "Ostend", "Bockenheim", "Bahnofsviertel"],
        "architecture": "Hochhäuser mit Flachdächern, Altbauten mit Satteldächern, moderne PV-Anlagen auf Bürobauten",
        "famous": "Römer, Commerzbank Tower, Goethe-Haus, Messe, Flughafen, Main",
        "reviews": [
            {"text": "PV-Anlage in Bornheim war eine große Entscheidung. Der Betrieb aus dem Umland hat schnell reagiert, fair kalkuliert und sauber gearbeitet. Nur 3 Tage bis alles fertig war.", "name": "Julia S.", "city": "Frankfurt-Bornheim", "service": "PV-Anlage 2025"},
            {"text": "PV-Speicher für unser Reihenhaus in Sachsenhausen. Drei Angebote eingeholt, alle aus dem Rhein-Main-Gebiet. Die Beratung war gut.", "name": "Andreas W.", "city": "Frankfurt-Sachsenhausen", "service": "PV-Speicher 2024"},
            {"text": "Wallbox für unser E-Auto in Bockenheim. Nach dem Sturm war schnelle Hilfe nötig. Das Team war am nächsten Tag da und hat provisorisch gesichert.", "name": "Claudia B.", "city": "Frankfurt-Bockenheim", "service": "Wallbox 2025"},
        ],
        "faq": [
            {"q": "Welche Frankfurter Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Innenstadt, Sachsenhausen, Westend, Bornheim, Nordend, Ostend, Bockenheim, Bahnhofsviertel und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Frankfurter PV-Installateure melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine PV-Anlage in Frankfurt?", "a": "Für ein typisches Reihenhaus in Frankfurt (80-120 qm) liegen die Kosten bei 12.000 bis 20.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich."},
            {"q": "Gibt es für das Westend besondere Auflagen?", "a": "Im Westend gelten strenge Gestaltungssatzungen. Unsere Partnerbetriebe kennen die Frankfurter Vorschriften."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "hannover": {
        "name": "Hannover",
        "region": "Niedersachsen",
        "plz": "30159 bis 30659",
        "plz_short": "30159",
        "neighborhoods": ["Mitte", "List", "Vahrenwald", "Döhren", "Linden", "Herrenhausen", "Oststadt", "Bothfeld"],
        "architecture": "Gründerzeitbauten mit Satteldächern, PV-Anlagen in neueren Siedlungen, Flachdächer in der Innenstadt",
        "famous": "Maschsee, Herrenhäuser Gärten, Neues Rathaus, Marktkirche, Expo-Gelände",
        "reviews": [
            {"text": "PV-Anlage in List war eine große Entscheidung. Drei Angebote, Betrieb aus Hannover genommen. Neue Anlage, 8kWp, einfache Bedienung.", "name": "Nina T.", "city": "Hannover-List", "service": "PV-Anlage 2025"},
            {"text": "Balkonkraftwerk für unser Reihenhaus in Döhren. Die Beratung war ehrlich - nicht immer ist eine Volldachanlage die beste Lösung. Haben uns dann doch fürs Balkonkraftwerk entschieden.", "name": "Frank D.", "city": "Hannover-Döhren", "service": "Balkonkraftwerk 2024"},
            {"text": "PV-Montage in Bothfeld. Neue Anlage auf dem Satteldach. Pünktlich, sauber, fair - was will man mehr?", "name": "Sandra J.", "city": "Hannover-Bothfeld", "service": "PV-Montage 2025"},
        ],
        "faq": [
            {"q": "Welche Hannoverschen Stadtteile werden abgedeckt?", "a": "Alle 51 Stadtteile: von Mitte über List, Vahrenwald und Linden bis Bothfeld, Misburg und Burg. Auch das Umland wie Laatzen und Langenhagen."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Sie erhalten innerhalb von 24 Stunden einen Rückruf."},
            {"q": "Was kostet eine PV-Anlage in Hannover?", "a": "Für ein typisches hannoversches Reihenhaus liegen die Kosten bei 11.000 bis 18.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich."},
            {"q": "Gibt es Fördermittel für Hannover?", "a": "Die Region und das Land Niedersachsen bieten Förderprogramme. Unsere Partner helfen bei der Antragstellung."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "duesseldorf": {
        "name": "Düsseldorf",
        "region": "Nordrhein-Westfalen",
        "plz": "40210 bis 40629",
        "plz_short": "40210",
        "neighborhoods": ["Altstadt", "Carlstadt", "Stadtmitte", "Pempelfort", "Düsseltal", "Oberkassel", "Niederkassel", "Derendorf"],
        "architecture": "Rheinische Villen mit Satteldächern, PV-Anlagen auf modernen Villen, Flachdächer in der Altstadt",
        "famous": "Altbier, Kö, Königsallee, Medienhafen, Rheinturm",
        "reviews": [
            {"text": "PV-Anlage in Oberkassel war ein großes Projekt. Drei Angebote eingeholt, alle professionell. Neue Anlage mit Speicher, die Rendite stimmt.", "name": "Rolf H.", "city": "Düsseldorf-Oberkassel", "service": "PV-Anlage 2025"},
            {"text": "Wallbox für die Praxis in Derendorf. Schnelle Beratung, saubere Installation. Die Ladestation funktioniert einwandfrei.", "name": "Birgit S.", "city": "Düsseldorf-Derendorf", "service": "Wallbox 2025"},
            {"text": "Balkonkraftwerk in der Altstadt. Enge Gassen, wenig Platz - unsere Betriebe in Düsseldorf kennen das und planen dementsprechend.", "name": "Dieter M.", "city": "Düsseldorf-Altstadt", "service": "Balkonkraftwerk 2024"},
        ],
        "faq": [
            {"q": "Welche Düsseldorfer Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, Carlstadt, Stadtmitte, Pempelfort, Düsseltal, Oberkassel, Niederkassel, Derendorf und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Düsseldorfer PV-Installateure melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine PV-Anlage in Düsseldorf?", "a": "Düsseldorf liegt im oberen Bereich. Eine 10 kWp Anlage liegt zwischen 13.000 und 21.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich."},
            {"q": "Die Rheinufer und die Kö - spielt das eine Rolle?", "a": "Die Rheinlage und die teils alte Bausubstanz in den Villenvierteln erfordern Erfahrung. Unsere Düsseldorfer Betriebe kennen das."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "leipzig": {
        "name": "Leipzig",
        "region": "Sachsen",
        "plz": "04107 bis 04357",
        "plz_short": "04107",
        "neighborhoods": ["Innenstadt", "Zentrum", "Plagwitz", "Lindenau", "Connewitz", "Stötteritz", "Gohlis", "Schleussig"],
        "architecture": "Gründerzeit-Altbauten mit Satteldächern, PV-Anlagen in sanierten Gebäuden, Flachdächer in Neubauten",
        "famous": "Bach, Gewandhaus, Spassgarde, Ausstellungszentrum",
        "reviews": [
            {"text": "PV-Anlage in Connewitz war ein Abenteuer. Über das Portal aber den richtigen Betrieb gefunden. Neue Anlage, 10kWp, läuft super.", "name": "Martina B.", "city": "Leipzig-Connewitz", "service": "PV-Anlage 2025"},
            {"text": "PV-Speicher für unser saniertes Gründerzeithaus in Plagwitz. Drei Angebote, schnelle Ausführung. Die Kombination mit PV war die richtige Wahl.", "name": "Frank S.", "city": "Leipzig-Plagwitz", "service": "PV-Speicher 2025"},
            {"text": "Balkonkraftwerk in Lindenau. Neue Anlage, Mieterstrom. Der Betrieb aus dem Viertel war super.", "name": "Andrea K.", "city": "Leipzig-Lindenau", "service": "Balkonkraftwerk 2024"},
        ],
        "faq": [
            {"q": "Welche Leipziger Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Innenstadt, Zentrum, Plagwitz, Lindenau, Connewitz, Stötteritz, Gohlis, Schleussig und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Leipziger PV-Installateure melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine PV-Anlage in Leipzig?", "a": "Leipzig ist günstiger als die westdeutschen Großstädte. Eine 10 kWp Anlage liegt zwischen 9.000 und 17.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Die Angebote sind unverbindlich."},
            {"q": "Leipzig wächst schnell - wie ist das bei der Vermittlung?", "a": "Leipzig boomt, und die PV-Installateure haben alle Hände voll zu tun. Deshalb ist der Vergleich über uns besonders wertvoll."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "bremen": {
        "name": "Bremen",
        "region": "Bremen",
        "plz": "28195 bis 28779",
        "plz_short": "28195",
        "neighborhoods": ["Mitte", "Neustadt", "Schwachhausen", "Horn-Lehe", "Borgfeld", "Gröpelingen", "Huchting", "Vegesack"],
        "architecture": "Backsteingotik mit älteren Satteldächern, PV-Anlagen in Villenvierteln, Flachdächer in Überseestadt",
        "famous": "Rathaus, Roland, Stadtmusikanten, Weser, Schlachte, Überseestadt",
        "reviews": [
            {"text": "PV-Anlage in Schwachhausen war 40 Jahre altes Dach. Drei Angebote, alle aus Bremen. Neue Anlage, 10kWp, spart ordentlich Strom.", "name": "Heike M.", "city": "Bremen-Schwachhausen", "service": "PV-Anlage 2025"},
            {"text": "Wallbox für unser E-Auto in der Neustadt. Schnelle Beratung, fairer Preis. Die Installation war in zwei Tagen durch.", "name": "Ralf S.", "city": "Bremen-Neustadt", "service": "Wallbox 2024"},
            {"text": "PV-Montage für unser Reihenhaus in Gröpelingen. Die Beratung war kompetent, das Angebot transparent.", "name": "Anke P.", "city": "Bremen-Gröpelingen", "service": "PV-Montage 2025"},
        ],
        "faq": [
            {"q": "Welche Bremer Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Mitte, Neustadt, Schwachhausen, Horn-Lehe, Borgfeld, Gröpelingen, Huchting, Vegesack und alle weiteren. Auch Bremerhaven."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Bremer PV-Installateure melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine PV-Anlage in Bremen?", "a": "Für ein typisches Bremer Reihenhaus liegen die Kosten bei 10.000 bis 18.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich."},
            {"q": "Gibt es Auflagen für die Bremer Altstadt?", "a": "Der Marktplatz und die umliegende Altstadt stehen unter Denkmalschutz. Unsere Bremer Partner kennen die Vorschriften."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "nuernberg": {
        "name": "Nürnberg",
        "region": "Bayern",
        "plz": "90317 bis 90491",
        "plz_short": "90317",
        "neighborhoods": ["Altstadt", "St. Lorenz", "St. Sebald", "Gostenhof", "Bärenschanze", "St. Leonhard", "Steinbühl", "Glockenhof"],
        "architecture": "Fachwerk-Altbauten mit Satteldächern, PV-Anlagen auf modernen Gebäuden, Flachdächer in Gewerbegebieten",
        "famous": "Kaiserburg, Christkindlesmarkt, Albrecht Dürer, Nürnberger Rostbratwurst",
        "reviews": [
            {"text": "PV-Anlage in der Altstadt war sanierungsbedürftig. Der Betrieb hat sich umfassend gekümmert, inklusive Abstimmung mit dem Denkmalschutz. Super Arbeit!", "name": "Monika H.", "city": "Nürnberg-Altstadt", "service": "PV-Anlage 2025"},
            {"text": "Balkonkraftwerk für unser Reihenhaus in St. Leonhard. Drei Angebote, der Betrieb aus dem Umland hatte das beste Konzept.", "name": "Stefan B.", "city": "Nürnberg-St. Leonhard", "service": "Balkonkraftwerk 2024"},
            {"text": "PV-Speicher für unser Haus in Gostenhof. Nach dem Starkregen letzte Woche war schnelle Hilfe nötig. Innerhalb von 24 Stunden war jemand da.", "name": "Petra K.", "city": "Nürnberg-Gostenhof", "service": "PV-Speicher 2025"},
        ],
        "faq": [
            {"q": "Welche Nürnberger Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, St. Lorenz, St. Sebald, Gostenhof, Bärenschanze, St. Leonhard, Steinbühl, Glockenhof und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Nürnberger PV-Installateure melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine PV-Anlage in Nürnberg?", "a": "Die Kosten in Nürnberg liegen im bayrischen Durchschnitt. Eine 10 kWp Anlage liegt zwischen 12.000 und 20.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich."},
            {"q": "Gibt es Auflagen für die Altstadt?", "a": "Unsere Nürnberger Partner kennen die strengen Auflagen des Denkmalschutzes in der Altstadt."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "mannheim": {
        "name": "Mannheim",
        "region": "Baden-Württemberg",
        "plz": "68159 bis 68309",
        "plz_short": "68159",
        "neighborhoods": ["Innenstadt", "Jungbusch", "Neckarstadt-Ost", "Käfertal", "Lindenhof", "Oststadt", "Schwetzingerstadt", "Waldhof"],
        "architecture": "Quadratestadt mit Satteldächern, PV-Anlagen auf modernen Bauten, Flachdächer in Gewerbegebieten",
        "famous": "Barockschloss, Quadratestadt, BASF, SAP Arena, Jungbusch",
        "reviews": [
            {"text": "PV-Anlage in der Neckarstadt-Ost war eine große Entscheidung. Drei Angebote, Betrieb aus Mannheim genommen. Neue Anlage, läuft einwandfrei.", "name": "Diana K.", "city": "Mannheim-Neckarstadt-Ost", "service": "PV-Anlage 2025"},
            {"text": "Wallbox für unser E-Auto in Käfertal. Die Beratung war gut, das Angebot transparent. Die Installation war schnell gemacht.", "name": "Thomas W.", "city": "Mannheim-Käfertal", "service": "Wallbox 2024"},
            {"text": "PV-Montage in der Oststadt. Neue Anlage auf dem Satteldach. Der Betrieb war pünktlich und sauber.", "name": "Sabine R.", "city": "Mannheim-Oststadt", "service": "PV-Montage 2025"},
        ],
        "faq": [
            {"q": "Welche Mannheimer Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Innenstadt, Jungbusch, Neckarstadt-Ost, Käfertal, Lindenhof, Oststadt, Schwetzingerstadt, Waldhof und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Sie erhalten innerhalb von 24 Stunden einen Rückruf."},
            {"q": "Was kostet eine PV-Anlage in Mannheim?", "a": "Für ein typisches Mannheimer Reihenhaus liegen die Kosten bei 11.000 bis 19.000 Euro."},
            {"q": "Musst ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich."},
            {"q": "Gibt es in Mannheim Auflagen?", "a": "Das Barockschloss und die umliegenden Quadrate stehen unter Denkmalschutz. Auch in der Oststadt gibt es denkmalgeschützte Bausubstanz."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "freiburg": {
        "name": "Freiburg",
        "region": "Baden-Württemberg",
        "plz": "79098 bis 79117",
        "plz_short": "79098",
        "neighborhoods": ["Altstadt", "Innenstadt", "Stühlinger", "Herdern", "Vauban", "Landwasser", "Haslach", "Opfingen"],
        "architecture": "Solarstadt mit vielen PV-Anlagen und Solaranlagen, Satteldächer in Altstadt, Flachdächer in Vauban",
        "famous": "Münster, Schwarzwald, Universitätsstadt, Vauban",
        "reviews": [
            {"text": "PV-Anlage für unser Haus in Vauban. Die Ökostadt braucht keine fossilen Brennstoffe. Drei Angebote, alle aus Freiburg.", "name": "Stefanie G.", "city": "Freiburg-Vauban", "service": "PV-Anlage 2025"},
            {"text": "Balkonkraftwerk für unser Reihenhaus in Herdern. Der Betrieb aus dem Schwarzwald hat die Anlage dimensioniert. Läuft seit einem Jahr einwandfrei.", "name": "Martin W.", "city": "Freiburg-Herdern", "service": "Balkonkraftwerk 2025"},
            {"text": "PV-Anlage in der Innenstadt war eine große Entscheidung. Der Betrieb kam schnell, hat einen fairen Preis gemacht und war mit der Arbeit in 3 Tagen fertig.", "name": "Ute B.", "city": "Freiburg-Innenstadt", "service": "PV-Anlage 2024"},
        ],
        "faq": [
            {"q": "Welche Freiburger Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, Innenstadt, Stühlinger, Herdern, Vauban, Landwasser, Haslach, Opfingen und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Freiburger PV-Installateure melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine PV-Anlage in Freiburg?", "a": "Freiburg ist etwas teurer als der Durchschnitt. Eine 10 kWp Anlage liegt zwischen 13.000 und 21.000 Euro."},
            {"q": "Musst ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich."},
            {"q": "Freiburg ist eine Solarstadt - spielt das eine Rolle?", "a": "Ja. Viele Freiburger setzen auf PV-Anlagen und Speicher. Unsere Betriebe kennen die lokalen Besonderheiten."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
}

# =============================================================================
# SERVICE DATA
# =============================================================================

SERVICES = {
    "balkonkraftwerk": {
        "page_title": "Balkonkraftwerk {city} - Mini-PV, Plug-in Solar, Mietstrom",
        "meta_desc": "Balkonkraftwerk {city}: Mini-Solaranlage für den Balkon. 800W Plug-in, EEG-frei, Mieterstrom. Kostenlos bis zu 3 Angebote. Unverbindlich.",
        "nav_active": "Balkonkraftwerk",
        "headline": "Balkonkraftwerk {city} - Solarstrom vom Balkon",
        "sub": "Das Balkonkraftwerk ist die günstigste Art, Solarstrom zu erzeugen. Mieter in {city} können jetzt mitmachen. Eine Anfrage - bis zu drei {city}er Fachbetriebe melden sich.",
        "benefits": [
            {"icon": "bolt", "title": "800 Watt Plug-in", "text": "Das Balkonkraftwerk liefert bis zu 800 Watt. Für {city}er Mieter und Eigenheimbesitzer - einfach in die Steckdose stöpseln."},
            {"icon": "sun", "title": "EEG-frei bis 800W", "text": "Anlagen bis 800W sind EEG-frei - keine Anmeldung beim Netzbetreiber nötig. In {city} ideal für Mieter."},
            {"icon": "shield", "title": "Mieterstrom möglich", "text": "In {city} können Mieter den Solarstrom selbst nutzen. Unser {city}er Betriebe helfen bei der Abstimmung mit dem Vermieter."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Fachbetriebe weiter."},
            {"icon": "settings", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "sun", "title": "800W Balkonkraftwerk", "desc": "Die Standardgröße: 800W, Plug-and-Play. Für {city}er Balkone, Terrassen und Gärten.", "tag": "800W"},
            {"icon": "expand", "title": "600W Mini-PV", "desc": "Die günstige Variante: 600W reichen für {city}er Durchschnittshaushalt im Sommer.", "tag": "600W"},
            {"icon": "pipe", "title": "Balkonhalterung", "desc": "Sichere Befestigung für {city}er Balkone. Von Sicherung bis Edelstahlhalterung.", "tag": "Halterung"},
            {"icon": "bolt", "title": "Wechselrichter", "desc": "Der Wechselrichter wandelt den Solarstrom in haushaltsüblichen Wechselstrom um. Für {city}er Steckdose."},
            {"icon": "settings", "title": "Anschluss-Service", "desc": "Von der Lieferung bis zur Montage in {city}. Unsere {city}er Betriebe machen alles aus einer Hand.", "tag": "Service"},
            {"icon": "check", "title": "Inbetriebnahme", "desc": "Die Inbetriebnahme in {city} ist einfach. Stecker rein, fertig. Unsere Betriebe helfen beim Start.", "tag": "Start"},
        ],
        "faq": None,
        "form_options": [
            {"value": "800w", "label": "800W Balkonkraftwerk"},
            {"value": "600w", "label": "600W Mini-PV"},
            {"value": "halterung", "label": "Balkonhalterung"},
            {"value": "komplett", "label": "Komplett-Set mit Montage"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Welcher Balkon? Südseite oder Ostseite? {neighborhoods[0]} oder {neighborhoods[1]}?",
    },
    "pv-anlage": {
        "page_title": "PV-Anlage {city} - Komplett-PV-Anlage, 5-15 kWp, Förderung",
        "meta_desc": "PV-Anlage {city}: Komplett-PV-Anlage für Hausdach. 5-15 kWp, Netzparallel oder Insel. Kostenlos bis zu 3 Angebote. Unverbindlich.",
        "nav_active": "PV-Anlage",
        "headline": "PV-Anlage {city} - Strom vom eigenen Dach",
        "sub": "Die PV-Anlage auf dem eigenen Dach ist die beste Art, Solarstrom zu erzeugen. In {city} lohnts sich besonders. Eine Anfrage - bis zu drei {city}er Fachbetriebe melden sich.",
        "benefits": [
            {"icon": "sun", "title": "Strom vom eigenen Dach", "text": "Die PV-Anlage auf Ihrem Dach in {city} erzeugt Solarstrom - tagsüber und in sonnigen Stunden."},
            {"icon": "bolt", "title": "Eigenverbrauch bis 80%", "text": "Mit Speicher erreichen {city}er Haushalte bis zu 80% Eigenverbrauch. Das spart Stromkosten."},
            {"icon": "shield", "title": "EEG-Vergütung", "text": "Der überschüssige Strom wird in {city} ins Netz eingespeist und vergütet. So verdienen Sie mit."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Fachbetriebe weiter."},
            {"icon": "settings", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "sun", "title": "5-10 kWp Aufdach", "desc": "Für {city}er Einfamilienhäuser: Die Standardgröße, 5-10 kWp, auf jedem Dach nachrüstbar.", "tag": "5-10kWp"},
            {"icon": "expand", "title": "10-15 kWp Großanlage", "desc": "Für {city}er Eigenheime mit hohem Stromverbrauch: 10-15 kWp, auch für Elektroauto und Wärmepumpe.", "tag": "10-15kWp"},
            {"icon": "pipe", "title": "Indach-PV", "desc": "Die elegante Lösung: PV-Module ersetzen die Dacheindeckung. Für {city}er Neubauten und Sanierungen.", "tag": "Indach"},
            {"icon": "settings", "title": "Wechselrichter", "desc": "Der Wechselrichter ist das Herz der Anlage. Für {city}er Betriebe beraten zur richtigen Größe.", "tag": "WR"},
            {"icon": "check", "title": "Überspannungsschutz", "desc": "Sicherheit für {city}er PV-Anlage: Überspannungsschutz und Blitzschutz vom Fachbetrieb.", "tag": "Schutz"},
            {"icon": "settings", "title": "Monitoring", "desc": "Überwachung der {city}er PV-Anlage per Smartphone. Ertragsdaten und Störungsmeldungen in Echtzeit.", "tag": "Monitor"},
        ],
        "faq": None,
        "form_options": [
            {"value": "5-10kwp", "label": "5-10 kWp Aufdach-PV"},
            {"value": "10-15kwp", "label": "10-15 kWp Großanlage"},
            {"value": "indach", "label": "Indach-PV"},
            {"value": "komplett", "label": "Komplett inklusive Speicher"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Welches Dach? Satteldach oder Flachdach? {neighborhoods[0]} oder {neighborhoods[1]}?",
    },
    "pv-anlage-angebot": {
        "page_title": "PV-Angebot {city} - Kostenloses Angebot für PV-Anlage",
        "meta_desc": "PV-Angebot {city}: Kostenloses Angebot für PV-Anlage einholen. Bis zu drei Betriebe aus {city}. Unverbindlich.",
        "nav_active": "PV-Angebot",
        "headline": "PV-Angebot {city} - kostenlos und unverbindlich",
        "sub": "Sie möchten wissen, was eine PV-Anlage für Ihr Haus in {city} kostet? Eine Anfrage - bis zu drei {city}er Fachbetriebe melden sich mit ihrem Angebot.",
        "benefits": [
            {"icon": "sun", "title": "Dach-Check inklusive", "text": "Der {city}er Betrieb prüft Ihr Dach auf Eignung. Ausrichtung, Neigung, Statik - alles wird gecheckt."},
            {"icon": "bolt", "title": "Kostenlose Beratung", "text": "Die Beratung in {city} ist kostenlos. Unsere {city}er Betriebe erklären Ihnen die Optionen."},
            {"icon": "shield", "title": "Fördermittel-Check", "text": "BAFA, KfW, regionale Programme - für {city}er PV-Anlagen gibt es viele Fördermittel. Unsere Betriebe helfen."},
            {"icon": "check", "title": "Drei Angebote vergleichen", "text": "Sie erhalten bis zu drei Angebote von {city}er Betrieben. So finden Sie den besten Preis."},
            {"icon": "settings", "title": "Keine Verpflichtung", "text": "Die Angebote sind unverbindlich. Wenn nichts dabei ist, gehen Sie woanders hin."},
        ],
        "services": [
            {"icon": "sun", "title": "Dach-Check", "desc": "Der {city}er Betrieb prüft, ob Ihr Dach für PV geeignet ist. Ergebnis: Empfehlung und Kostenschätzung.", "tag": "Check"},
            {"icon": "settings", "title": "Beratungsgespräch", "desc": "In {city} können Sie das Beratungsgespräch vor Ort oder per Video machen. Flexible Termine.", "tag": "Beratung"},
            {"icon": "file", "title": "Angebotsstellung", "desc": "Das Angebot für {city} enthält: Module, Wechselrichter, Montage, Inbetriebnahme. Alles aus einer Hand.", "tag": "Angebot"},
            {"icon": "shield", "title": "Förderantrag", "desc": "Für {city}er PV-Anlagen können Sie Fördermittel beantragen. Unsere Betriebe helfen beim Antrag.", "tag": "Förderung"},
            {"icon": "check", "title": "Angebotsvergleich", "desc": "Drei Angebote vergleichen in {city} - einfach, schnell, unverbindlich.", "tag": "Vergleich"},
            {"icon": "settings", "title": "Fragen klären", "desc": "Nach dem Angebot können Sie in {city} alle Fragen klären. Unsere Betriebe sind geduldig.", "tag": "Support"},
        ],
        "faq": None,
        "form_options": [
            {"value": "angebot-aufdach", "label": "Angebot für Aufdach-PV"},
            {"value": "angebot-indach", "label": "Angebot für Indach-PV"},
            {"value": "angebot-mit-speicher", "label": "Angebot mit Speicher"},
            {"value": "angebot-komplett", "label": "Komplettangebot inklusive Wallbox"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Was für ein Haus? Welches Dach? {neighborhoods[0]} oder {neighborhoods[1]}?",
    },
    "wallbox": {
        "page_title": "Wallbox {city} - E-Auto Ladestation, 11kW, 22kW",
        "meta_desc": "Wallbox {city}: E-Auto Ladestation für zu Hause. 11kW oder 22kW, mit oder ohne PV-Anbindung. Kostenlos bis zu 3 Angebote. Unverbindlich.",
        "nav_active": "Wallbox",
        "headline": "Wallbox {city} - E-Auto laden zu Hause",
        "sub": "Die Wallbox für Ihr E-Auto in {city}. Schnell, sicher, komfortabel. Eine Anfrage - bis zu drei {city}er Fachbetriebe melden sich.",
        "benefits": [
            {"icon": "bolt", "title": "11kW oder 22kW", "text": "Die Wallbox in {city} lädt mit 11kW oder 22kW. Das ist 3-10x schneller als die Haushaltssteckdose."},
            {"icon": "sun", "title": "PV-Integration", "text": "Wallbox mit PV-Anbindung lädt das {city}er E-Auto mit überschüssigem Solarstrom. Das ist kostenlos und umweltfreundlich."},
            {"icon": "shield", "title": "Sicherheit", "text": "Die Wallbox in {city} ist deutlich sicherer als die Haushaltssteckdose. SEPNO-zertifiziert."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Fachbetriebe weiter."},
            {"icon": "settings", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "bolt", "title": "11kW Wallbox", "desc": "Die Standard-Wallbox für {city}: 11kW reicht für die meisten E-Autos. Installation über Nacht möglich.", "tag": "11kW"},
            {"icon": "expand", "title": "22kW Wallbox", "desc": "Für {city}er mit starkem E-Auto oder Kurzzeitladung: 22kW lädt in 2-4 Stunden voll.", "tag": "22kW"},
            {"icon": "sun", "title": "PV-Wallbox", "desc": "Wallbox mit PV-Integration für {city}. Lädt nur mit überschüssigem Solarstrom - kostenlos und umweltfreundlich.", "tag": "PV"},
            {"icon": "settings", "title": "Installation", "desc": "Die Installation in {city} umfasst: Wallbox, Verkabelung, Absicherung. Alles aus einer Hand.", "tag": "Montage"},
            {"icon": "check", "title": "Lastmanagement", "desc": "Wenn mehrere E-Autos in {city} laden: Lastmanagement verhindert Überlastung der Hausinstallation.", "tag": "Smart"},
            {"icon": "settings", "title": "Wartung", "desc": "Regelmäßige Wartung hält die {city}er Wallbox in Schuss. Unsere Betriebe bieten Wartungsverträge.", "tag": "Check"},
        ],
        "faq": None,
        "form_options": [
            {"value": "11kw", "label": "11kW Wallbox"},
            {"value": "22kw", "label": "22kW Wallbox"},
            {"value": "pv-wallbox", "label": "PV-Wallbox"},
            {"value": "komplett", "label": "Komplett-Set mit Installation"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Welches E-Auto? Welche Ladeleistung? {neighborhoods[0]} oder {neighborhoods[1]}?",
    },
    "pv-speicher": {
        "page_title": "PV-Speicher {city} - Stromspeicher, 5-15 kWh, Lithium",
        "meta_desc": "PV-Speicher {city}: Stromspeicher für PV-Anlage. 5-15 kWh Lithium. Eigenverbrauch auf 80% steigern. Kostenlos bis zu 3 Angebote. Unverbindlich.",
        "nav_active": "PV-Speicher",
        "headline": "PV-Speicher {city} - mehr Eigenverbrauch, weniger Stromkosten",
        "sub": "Der PV-Speicher macht Ihre {city}er PV-Anlage perfekt. Den Solarstrom tagsüber speichern, abends und nachts nutzen. Eine Anfrage - bis zu drei {city}er Fachbetriebe melden sich.",
        "benefits": [
            {"icon": "bolt", "title": "Eigenverbrauch bis 80%", "text": "Mit PV-Speicher erreichen {city}er Haushalte bis zu 80% Eigenverbrauch. Das spart Stromkosten."},
            {"icon": "sun", "title": "Solarstrom nutzen", "text": "Der Speicher in {city} speichert den Solarstrom, den Sie nicht sofort verbrauchen. Abends und nachts nutzen Sie ihn."},
            {"icon": "shield", "title": "Notstromfähig", "text": "Viele {city}er PV-Speicher können bei Stromausfall als Notstromquelle dienen. Sicherheit inklusive."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Fachbetriebe weiter."},
            {"icon": "settings", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "bolt", "title": "5-10 kWh Speicher", "desc": "Für {city}er Durchschnittshaushalt: 5-10 kWh reichen für den Abend und die Nacht.", "tag": "5-10kWh"},
            {"icon": "expand", "title": "10-15 kWh Großspeicher", "desc": "Für {city}er mit hohem Verbrauch oder Elektroauto: 10-15 kWh speichern tagsüber genug für abends und nachts.", "tag": "10-15kWh"},
            {"icon": "sun", "title": "Hybridspeicher", "desc": "Hybridspeicher mit PV-Wechselrichter für {city}. Komplettpaket aus einer Hand.", "tag": "Hybrid"},
            {"icon": "settings", "title": "Nachrüstung", "desc": "Sie haben schon PV? Der {city}er Betrieb rüstet den Speicher nach. Flexible Integration.", "tag": "Nachrüst"},
            {"icon": "check", "title": "Kapazitätserweiterung", "desc": "Wenn der {city}er Speicher nicht mehr reicht: Erweiterung um weitere Module möglich.", "tag": "Erweit."},
            {"icon": "settings", "title": "Monitoring", "desc": "Überwachung des {city}er PV-Speichers per App. Ladezustand, Ertragsdaten, Prognosen.", "tag": "App"},
        ],
        "faq": None,
        "form_options": [
            {"value": "5-10kwh", "label": "5-10 kWh Speicher"},
            {"value": "10-15kwh", "label": "10-15 kWh Großspeicher"},
            {"value": "hybrid", "label": "Hybridspeicher mit WR"},
            {"value": "nachruestung", "label": "Nachrüstung bestehender PV"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Welche PV-Anlage? Bj. wann? {neighborhoods[0]} oder {neighborhoods[1]}?",
    },
    "pv-montage": {
        "page_title": "PV-Montage {city} - Installation, Montage, Anschluss",
        "meta_desc": "PV-Montage {city}: PV-Installation und Montage. Von Aufdach bis Indach. Kostenlos bis zu 3 Angebote von Fachbetrieben in {city}. Unverbindlich.",
        "nav_active": "PV-Montage",
        "headline": "PV-Montage {city} - fachgerechte Installation",
        "sub": "Die PV-Montage will fachgerecht sein. In {city} gibt es erfahrene Betriebe, die das können. Eine Anfrage - bis zu drei {city}er Fachbetriebe melden sich.",
        "benefits": [
            {"icon": "shield", "title": "Fachgerechte Montage", "text": "Die {city}er PV-Installateure montieren nach VDE-Norm. Sicherheit und Haltbarkeit inklusive."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Fachbetriebe weiter."},
            {"icon": "bolt", "title": "Schnelle Umsetzung", "text": "Die meisten {city}er PV-Installationen sind in 1-3 Tagen erledigt. Danach produziert Ihre Anlage Strom."},
            {"icon": "settings", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "sun", "title": "Aufdach-Montage", "desc": "Die Standard-Montage für {city}: Aufdach mit Aluschienen. Für jedes Dach geeignet.", "tag": "Aufdach"},
            {"icon": "expand", "title": "Indach-Montage", "desc": "Die elegante Lösung: PV-Module werden in das {city}er Dach integriert. Keine Aufdachoptik."},
            {"icon": "pipe", "title": "DC-Verkabelung", "desc": "Die Verkabelung der {city}er PV-Anlage: Von den Modulen zum Wechselrichter. Fachgerecht und sicher.", "tag": "Kabel"},
            {"icon": "settings", "title": "Wechselrichter-Installation", "desc": "Der Wechselrichter wird in {city} fachgerecht installiert. Wandmontage oder freistehend.", "tag": "WR"},
            {"icon": "check", "title": "AC-Anschluss", "desc": "Der Anschluss ans {city}er Hausnetz: Absicherung, Zähler, Netzanschluss. Alles aus einer Hand.", "tag": "Netz"},
            {"icon": "settings", "title": "Inbetriebnahme", "desc": "Die Inbetriebnahme in {city}: Erstprüfung, Parametrierung, Übergabe. Alles dokumentiert.", "tag": "Start"},
        ],
        "faq": None,
        "form_options": [
            {"value": "aufdach", "label": "Aufdach-Montage"},
            {"value": "indach", "label": "Indach-Montage"},
            {"value": "komplett", "label": "Komplett-Installation"},
            {"value": "nachruestung", "label": "Nachrüstung bestehender Anlage"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Welches Dach? Satteldach oder Flachdach? {neighborhoods[0]} oder {neighborhoods[1]}?",
    },
    "pv-wartung": {
        "page_title": "PV-Wartung {city} - Reinigung, Inspektion, Service",
        "meta_desc": "PV-Wartung {city}: Wartung, Reinigung, Inspektion Ihrer PV-Anlage. Ertragssicherheit und lange Lebensdauer. Kostenlos bis zu 3 Angebote. Unverbindlich.",
        "nav_active": "PV-Wartung",
        "headline": "PV-Wartung {city} - damit Ihre Anlage lange läuft",
        "sub": "Die PV-Wartung hält Ihre {city}er Anlage in Top-Zustand. Regelmäßige Reinigung und Inspektion lohnen sich. Eine Anfrage - bis zu drei {city}er Fachbetriebe melden sich.",
        "benefits": [
            {"icon": "sun", "title": "Ertragssicherheit", "text": "Eine gewartete {city}er PV-Anlage erzeugt bis zu 15% mehr Strom. Das lohnt sich."},
            {"icon": "shield", "title": "Lange Lebensdauer", "text": "PV-Anlagen in {city} halten 25-30 Jahre. Regelmäßige Wartung verlängert die Lebensdauer."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Fachbetriebe weiter."},
            {"icon": "settings", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "sun", "title": "Modul-Reinigung", "desc": "Die Reinigung der {city}er PV-Module: Professionell, mit entmineralisiertem Wasser. Ertrag steigt spürbar.", "tag": "Reinigung"},
            {"icon": "check", "title": "elektrische Inspektion", "desc": "Die elektrische Prüfung in {city}: Anschlüsse, Verkabelung, Wechselrichter. Alles wird gecheckt.", "tag": "Prüfung"},
            {"icon": "settings", "title": "Leistungsprüfung", "desc": "Die Leistungsprüfung der {city}er Anlage: Ist die Leistung noch optimal? Gibt es Probleme?", "tag": "Test"},
            {"icon": "bolt", "title": "Wechselrichter-Service", "desc": "Der Wechselrichter in {city} ist das Herz der Anlage. Regelmäßiger Service hält ihn in Schuss.", "tag": "WR"},
            {"icon": "pipe", "title": "Kabel-CHECK", "desc": "Die Kabel und Stecker Ihrer {city}er Anlage: Prüfung auf Beschädigungen und Korrosion.", "tag": "Kabel"},
            {"icon": "settings", "title": "Wartungsvertrag", "desc": "Der {city}er Wartungsvertrag: Jährliche Inspektion, Reinigung, Ertragsreporting.", "tag": "Vertrag"},
        ],
        "faq": None,
        "form_options": [
            {"value": "reinigung", "label": "Modul-Reinigung"},
            {"value": "inspektion", "label": "Elektrische Inspektion"},
            {"value": "komplett", "label": "Komplett-Wartung"},
            {"value": "vertrag", "label": "Wartungsvertrag"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Wann war die letzte Wartung? {neighborhoods[0]} oder {neighborhoods[1]}? Bj. wann?",
    },
    "pv-carport": {
        "page_title": "PV-Carport {city} - Solarcarport, Carport mit PV",
        "meta_desc": "PV-Carport {city}: Carport mit Solarüberdachung. E-Auto laden beim Parken. Doppelte Nutzung. Kostenlos bis zu 3 Angebote. Unverbindlich.",
        "nav_active": "PV-Carport",
        "headline": "PV-Carport {city} - Auto parken und Strom erzeugen",
        "sub": "Der PV-Carport in {city} ist mehr als ein Unterstand. Er erzeugt Solarstrom und lädt Ihr E-Auto. Eine Anfrage - bis zu drei {city}er Fachbetriebe melden sich.",
        "benefits": [
            {"icon": "sun", "title": "Doppelter Nutzen", "text": "Der {city}er PV-Carport ist Carport und Kraftwerk zugleich. Parking und Strom - perfekt kombiniert."},
            {"icon": "bolt", "title": "E-Auto laden", "text": "Ihr E-Auto lädt beim Parken in {city}. Mit bis zu 22kW, direkt vom eigenen Dach."},
            {"icon": "shield", "title": "Wetterschutz", "text": "Der {city}er PV-Carport schützt Ihr Auto vor Sonne, Regen und Hagel. Und erzeugt dabei Strom."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Fachbetriebe weiter."},
            {"icon": "settings", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "sun", "title": "Solarcarport", "desc": "Der {city}er Solarcarport: Vollständig mit PV-Modulen überdacht. Für jedes Fahrzeug geeignet.", "tag": "Solar"},
            {"icon": "expand", "title": "Überdachung mit PV", "desc": "Die {city}er Überdachung mit PV: Terrasse, Stellplatz oder Eingangsbereich - alles möglich.", "tag": "Überdach"},
            {"icon": "bolt", "title": "Wallbox integriert", "desc": "Wallbox und PV-Carport in {city}: Das E-Auto lädt automatisch, wenn die Sonne scheint.", "tag": "Wallbox"},
            {"icon": "settings", "title": "Fundament", "desc": "Das {city}er Fundament: Stahl oder Beton, je nach {city}er Bodenverhältnissen.", "tag": "Fundament"},
            {"icon": "check", "title": "Statik", "desc": "Die Statik des {city}er PV-Carports: Schnee, Wind, Dachlast - alles wird berücksichtigt.", "tag": "Statik"},
            {"icon": "settings", "title": "Individuelle Lösung", "desc": "Für {city}: Von der Standardlösung bis zur individuellen Fertigung. Alles ist möglich.", "tag": "Custom"},
        ],
        "faq": None,
        "form_options": [
            {"value": "solarcarport", "label": "Solarcarport"},
            {"value": "ueberdachung", "label": "Überdachung mit PV"},
            {"value": "komplett", "label": "Komplett mit Wallbox"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Welches Auto? PV-Fläche gewünscht? {neighborhoods[0]} oder {neighborhoods[1]}?",
    },
    "solarthermie": {
        "page_title": "Solarthermie {city} - Solarthermieanlage, Warmwasser, Heizung",
        "meta_desc": "Solarthermie {city}: Solarthermieanlage für warmes Wasser und Heizungsunterstützung. BAFA-Förderung. Kostenlos bis zu 3 Angebote. Unverbindlich.",
        "nav_active": "Solarthermie",
        "headline": "Solarthermie {city} - warmes Wasser von der Sonne",
        "sub": "Die Solarthermie nutzt die Sonne für warmes Wasser. In {city} eine bewährte Technik. Eine Anfrage - bis zu drei {city}er Fachbetriebe melden sich.",
        "benefits": [
            {"icon": "sun", "title": "Sonne nutzen", "text": "Die Solarthermie in {city} nutzt die Sonne für warmes Wasser. Im Sommer fast kostenlos."},
            {"icon": "shield", "title": "BAFA-Förderung", "text": "Solarthermie wird in {city} vom BAFA gefördert. Unsere Betriebe helfen beim Antrag."},
            {"icon": "flame", "title": "Heizungsunterstützung", "text": "Im Winter unterstützt die {city}er Solarthermie Ihre Heizung. Das spart Energie."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Fachbetriebe weiter."},
            {"icon": "settings", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "sun", "title": "Solarthermie für WW", "desc": "Die Solarthermieanlage für {city} deckt im Sommer den Großteil des Warmwasserbedarfs.", "tag": "Warmwasser"},
            {"icon": "flame", "title": "Heizungsunterstützung", "desc": "Die {city}er Solarthermie für die Heizung: Unterstützt Ihre Gas- oder Wärmepumpe im Winter.", "tag": "Heizung"},
            {"icon": "expand", "title": " Kombination mit PV", "desc": "In {city} lohnt sich die Kombination von Solarthermie und PV. Unsere Betriebe beraten dazu.", "tag": "PV"},
            {"icon": "settings", "title": "Speicher einbauen", "desc": "Der Solarthermiespeicher in {city} ist wichtig für die Wärmespeicherung vom Tag für die Nacht.", "tag": "Speicher"},
            {"icon": "pipe", "title": "Rohrleitung verlegen", "desc": "Wenn in {city} die Rohre verlegt werden müssen, koordinieren unsere {city}er Betriebe das mit.", "tag": "Rohre"},
            {"icon": "check", "title": "Wartung", "desc": "Regelmäßige Wartung hält die {city}er Solarthermieanlage in Schuss. Unsere Betriebe bieten Wartungsverträge.", "tag": "Wartung"},
        ],
        "faq": None,
        "form_options": [
            {"value": "solar-ww", "label": "Solarthermie für Warmwasser"},
            {"value": "solar-heizung", "label": "Solarthermie für Heizungsunterstützung"},
            {"value": "kombination-pv", "label": "Kombination mit PV"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Welche Heizung haben Sie? {neighborhoods[0]} oder {neighborhoods[1]}? Bj. wann?",
    },
    "pv-beratung": {
        "page_title": "PV-Beratung {city} - Beratung, Planung, Wirtschaftlichkeit",
        "meta_desc": "PV-Beratung {city}: Unabhängige PV-Beratung zu Anlage, Speicher, Wallbox. Kostenlose Vor-Ort-Beratung. Kostenlos bis zu 3 Angebote. Unverbindlich.",
        "nav_active": "PV-Beratung",
        "headline": "PV-Beratung {city} - unabhängig und professionell",
        "sub": "Die PV-Beratung in {city} klärt alle Fragen rund um Solarstrom. Eine Anfrage - bis zu drei {city}er Fachbetriebe melden sich.",
        "benefits": [
            {"icon": "sun", "title": "Dach-Check", "text": "Der {city}er Betrieb prüft, ob Ihr Dach für PV geeignet ist. Ausrichtung, Neigung, Statik."},
            {"icon": "bolt", "title": "Wirtschaftlichkeitsberechnung", "text": "Die {city}er Beratung zeigt: Wie viel Strom erzeugt die Anlage? Wann amortisiert sie sich?"},
            {"icon": "shield", "title": "Fördermittel-Beratung", "text": "Für {city}er PV-Anlagen gibt es viele Fördermittel. Unsere Betriebe kennen alle Programme."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Fachbetriebe weiter."},
            {"icon": "settings", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "sun", "title": "Dach-Check", "desc": "Der {city}er Dach-Check: Eignung, optimale Anlagengröße, Kostenschätzung. Alles aus einer Hand.", "tag": "Check"},
            {"icon": "file", "title": "Wirtschaftlichkeitsberechnung", "desc": "Die {city}er Wirtschaftlichkeitsberechnung zeigt: EEG-Ertrag, Eigenverbrauch, Amortisation.", "tag": "Rechnung"},
            {"icon": "shield", "title": "Fördermittel-Check", "desc": "BAFA, KfW, regionale Programme: Für {city}er PV-Anlagen gibt es viele Fördermittel.", "tag": "Förder"},
            {"icon": "settings", "title": "Planung", "desc": "Die Planung in {city}: Modulwahl, Wechselrichter, Speicher, Wallbox. Alles wird dokumentiert.", "tag": "Plan"},
            {"icon": "check", "title": "Angebotsvergleich", "desc": "Drei Angebote vergleichen in {city} - einfach, schnell, unverbindlich.", "tag": "Vergleich"},
            {"icon": "settings", "title": "Fragen klären", "desc": "Nach der {city}er Beratung können Sie alle Fragen klären. Unsere Betriebe sind geduldig.", "tag": "Support"},
        ],
        "faq": None,
        "form_options": [
            {"value": "dachcheck", "label": "Dach-Check"},
            {"value": "wirtschaftlichkeit", "label": "Wirtschaftlichkeitsberechnung"},
            {"value": "foerdermittel", "label": "Fördermittel-Beratung"},
            {"value": "komplett", "label": "Komplett-Beratung"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Was für ein Haus? Welches Dach? {neighborhoods[0]} oder {neighborhoods[1]}?",
    },
    "pv-nachruestung": {
        "page_title": "PV-Nachrüstung {city} - Speicher nachrüsten, erweitern, Wallbox nachrüsten",
        "meta_desc": "PV-Nachrüstung {city}: Speicher nachrüsten, PV erweitern, Wallbox nachrüsten. Bestehende Anlage optimieren. Kostenlos bis zu 3 Angebote. Unverbindlich.",
        "nav_active": "PV-Nachrüstung",
        "headline": "PV-Nachrüstung {city} - mehr aus Ihrer bestehenden Anlage",
        "sub": "Sie haben schon PV? Dann lohnt sich oft eine Nachrüstung. Speicher, Wallbox, Erweiterung. Eine Anfrage - bis zu drei {city}er Fachbetriebe melden sich.",
        "benefits": [
            {"icon": "bolt", "title": "Speicher nachrüsten", "text": "Der {city}er PV-Speicher macht Ihre bestehende Anlage perfekt. Eigenverbrauch steigt auf bis zu 80%."},
            {"icon": "sun", "title": "PV erweitern", "text": "Die {city}er PV-Erweiterung: Mehr Module auf dem Dach, mehr Strom vom eigenen Dach."},
            {"icon": "bolt", "title": "Wallbox nachrüsten", "text": "Die {city}er Wallbox-Nachrüstung: E-Auto laden mit eigenem Solarstrom. Das ist günstig."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Fachbetriebe weiter."},
            {"icon": "settings", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "bolt", "title": "Speicher-Nachrüstung", "desc": "Der {city}er Speicher für Ihre bestehende PV-Anlage: Hybrid oder AC-Kopplung, flexibel.", "tag": "Speicher"},
            {"icon": "expand", "title": "PV-Modul-Erweiterung", "desc": "Die {city}er PV-Erweiterung: Mehr Module, mehr Strom. Neue Module auf freien Flächen.", "tag": "Module"},
            {"icon": "bolt", "title": "Wallbox-Nachrüstung", "desc": "Die {city}er Wallbox für Ihre bestehende PV-Anlage: PV-Überschuss laden, smart und günstig.", "tag": "Wallbox"},
            {"icon": "settings", "title": "Wechselrichter-Tausch", "desc": "Wenn der {city}er Wechselrichter alt ist: Tausch auf modernen Hybriden mit Speicherfunktion.", "tag": "WR"},
            {"icon": "check", "title": "Optimierung", "desc": "Die {city}er Optimierung Ihrer PV-Anlage: Ertragsanalyse, Nachjustierung, Monitoring.", "tag": "Opt."},
            {"icon": "settings", "title": "Wartung", "desc": "Regelmäßige Wartung der {city}er Nachrüstungen. Unsere Betriebe bieten Wartungsverträge.", "tag": "Check"},
        ],
        "faq": None,
        "form_options": [
            {"value": "speicher", "label": "Speicher nachrüsten"},
            {"value": "pv-erweitern", "label": "PV-Module erweitern"},
            {"value": "wallbox", "label": "Wallbox nachrüsten"},
            {"value": "komplett", "label": "Komplett-Nachrüstung"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Was für eine PV-Anlage? Bj. wann? {neighborhoods[0]} oder {neighborhoods[1]}?",
    },
    "freiflaechen-pv": {
        "page_title": "Freiflächen-PV {city} - Agri-PV, Parkplatz-PV, Gewerbefläche",
        "meta_desc": "Freiflächen-PV {city}: Freiflächenanlage, Agri-PV, Parkplatz-PV. Gewerblich und privat. Kostenlos bis zu 3 Angebote. Unverbindlich.",
        "nav_active": "Freiflächen-PV",
        "headline": "Freiflächen-PV {city} - große Flächen, große Erträge",
        "sub": "Die Freiflächen-PV in {city} nutzt große Flächen für Solarstrom. Für Landwirte, Gewerbe und Kommunen. Eine Anfrage - bis zu drei {city}er Fachbetriebe melden sich.",
        "benefits": [
            {"icon": "sun", "title": "Große Erträge", "text": "Die {city}er Freiflächen-PV erzeugt viel Solarstrom. Große Fläche, große Erträge."},
            {"icon": "shield", "title": "EEG-Vergütung", "text": "Freiflächen-PV in {city} bekommt EEG-Vergütung. Das macht sie attraktiv für Investoren."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Fachbetriebe weiter."},
            {"icon": "settings", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "sun", "title": "Freiflächenanlage", "desc": "Die {city}er Freiflächen-PV: Ackerland, Gewerbefläche, Industrieareal. Alles möglich.", "tag": "Feld"},
            {"icon": "plant", "title": "Agri-PV", "desc": "Die {city}er Agri-PV: Landwirtschaft und Solarstrom kombiniert. Unter den Modulen wird weitergearbeitet.", "tag": "Agri"},
            {"icon": "car", "title": "Parkplatz-PV", "desc": "Die {city}er Parkplatz-PV: Überdachung mit Solar, lädt E-Autos beim Parken. Ideal für Firmen.", "tag": "Park"},
            {"icon": "settings", "title": "Planung", "desc": "Die {city}er Planung: Standort, Auslegung, Genehmigung. Unsere Betriebe machen alles.", "tag": "Plan"},
            {"icon": "check", "title": "Genehmigung", "desc": "Die {city}er Genehmigung: Baurecht, Naturschutz, Netzbetreiber. Unsere Betriebe kennen die Vorschriften.", "tag": "Genehm"},
            {"icon": "settings", "title": "Betriebsführung", "desc": "Die {city}er Freiflächen-PV braucht Betriebsführung. Unsere Partner bieten das an.", "tag": "Service"},
        ],
        "faq": None,
        "form_options": [
            {"value": "freiflaeche", "label": "Freiflächenanlage"},
            {"value": "agri-pv", "label": "Agri-PV"},
            {"value": "parkplatz-pv", "label": "Parkplatz-PV"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Welche Fläche? Wie groß? {neighborhoods[0]} oder {neighborhoods[1]}?",
    },
}

# =============================================================================
# ICONS (SVG paths)
# =============================================================================

ICONS = {
    "location": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="10" r="3" stroke="currentColor" stroke-width="2"/>',
    "home": '<path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z" stroke="currentColor" stroke-width="2"/><polyline points="9,22 9,12 15,12 15,22" stroke="currentColor" stroke-width="2"/>',
    "clock": '<circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/><polyline points="12 6 12 12 16 14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "check": '<path d="M22 11.08V12a10 10 0 11-5.93-9.14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><polyline points="22 4 12 14.01 9 11.01" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
    "star": '<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "bolt": '<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
    "flame": '<path d="M12 22c-4.97 0-9-2.69-9-6 0-3 3-5 5-8 1.5-2.14 3-4.36 3-6 0 0 2 2 5 2 2.5 0 5-2 5-2 1.82 0 3 1 3 2 0 1.64 1.5 3.86 1.5 3.86s1.5 1 1.5 4c0 3.31-4.03 6-9 6z" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
    "water": '<path d="M12 2c-4 4-7 7-7 11a7 7 0 0014 0c0-4-3-7-7-11z" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
    "wind": '<path d="M9.59 4.59A2 2 0 1111 8H2m10.59 11.41A2 2 0 1014 16H2m15.73-8.27A2.5 2.5 0 1119.5 12H2" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
    "sun": '<circle cx="12" cy="12" r="5" stroke="#fff" stroke-width="2"/><line x1="12" y1="1" x2="12" y2="3" stroke="#fff" stroke-width="2" stroke-linecap="round"/><line x1="12" y1="21" x2="12" y2="23" stroke="#fff" stroke-width="2" stroke-linecap="round"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64" stroke="#fff" stroke-width="2" stroke-linecap="round"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78" stroke="#fff" stroke-width="2" stroke-linecap="round"/><line x1="1" y1="12" x2="3" y2="12" stroke="#fff" stroke-width="2" stroke-linecap="round"/><line x1="21" y1="12" x2="23" y2="12" stroke="#fff" stroke-width="2" stroke-linecap="round"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36" stroke="#fff" stroke-width="2" stroke-linecap="round"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22" stroke="#fff" stroke-width="2" stroke-linecap="round"/>',
    "settings": '<circle cx="12" cy="12" r="3" stroke="#fff" stroke-width="2"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-2 2 2 2 0 01-2-2v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83 0 2 2 0 010-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 01-2-2 2 2 0 012-2h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 010-2.83 2 2 0 012.83 0l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 012-2 2 2 0 012 2v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 0 2 2 0 010 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 012 2 2 2 0 01-2 2h-.09a1.65 1.65 0 00-1.51 1z" stroke="#fff" stroke-width="2"/>',
    "pipe": '<path d="M4 4v5h.582a1 1 0 00.707-.293l6.414-6.414a1 1 0 01.707-.293h3.172a1 1 0 01.707.293l6.414 6.414a1 1 0 00.707.293H20v5" stroke="#fff" stroke-width="2" stroke-linecap="round"/><path d="M4 14v-3a3 3 0 013-3h5" stroke="#fff" stroke-width="2" stroke-linecap="round"/><path d="M16 14v-3a3 3 0 013-3h5" stroke="#fff" stroke-width="2" stroke-linecap="round"/>',
    "file": '<path d="M13 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V9z" stroke="#fff" stroke-width="2"/><polyline points="13 2 13 9 20 9" stroke="#fff" stroke-width="2"/>',
    "expand": '<polyline points="15 3 21 3 21 9" stroke="#fff" stroke-width="2"/><polyline points="9 21 3 21 3 15" stroke="#fff" stroke-width="2"/><line x1="21" y1="3" x2="14" y2="10" stroke="#fff" stroke-width="2"/><line x1="3" y1="21" x2="10" y2="14" stroke="#fff" stroke-width="2"/>',
    "car": '<path d="M5 17h14v-5l-2-4H7l-2 4v5z" stroke="#fff" stroke-width="2" stroke-linejoin="round"/><circle cx="7.5" cy="17.5" r="1.5" stroke="#fff" stroke-width="2"/><circle cx="16.5" cy="17.5" r="1.5" stroke="#fff" stroke-width="2"/>',
    "plant": '<path d="M12 22V8" stroke="#fff" stroke-width="2"/><path d="M5 12H2a10 10 0 0020 0h-3" stroke="#fff" stroke-width="2" stroke-linecap="round"/><path d="M8 8a4 4 0 018 0 4 4 0 018 0 4 4 0 018 0" stroke="#fff" stroke-width="2"/>',
}

# =============================================================================
# TEMPLATE
# =============================================================================

def generate_page(service_id, city_id, city_data, service_data):
    """Generate a single HTML page."""

    city_name = city_data["name"]
    plz = city_data["plz"]
    plz_short = city_data["plz_short"]
    neighborhoods = city_data["neighborhoods"]
    architecture = city_data["architecture"]
    famous = city_data["famous"]
    reviews = city_data["reviews"]
    faq = city_data["faq"]

    neighborhoods_str = ", ".join(neighborhoods)

    def preformat(text):
        text = text.replace("{neighborhoods[-1]}", neighborhoods[-1])
        for i, n in enumerate(neighborhoods):
            text = text.replace(f"{{neighborhoods[{i}]}}", n)
        return text

    headline = preformat(service_data["headline"]).format(
        city=city_name, neighborhoods=neighborhoods, architecture=architecture,
        neighborhoods_str=neighborhoods_str, plz_short=plz_short
    )
    sub = preformat(service_data["sub"]).format(
        city=city_name, neighborhoods=neighborhoods, architecture=architecture,
        neighborhoods_str=neighborhoods_str, plz_short=plz_short
    )
    page_title = service_data["page_title"].format(city=city_name)
    meta_desc = service_data["meta_desc"].format(city=city_name)

    benefits_html = ""
    for b in service_data["benefits"]:
        text = preformat(b["text"]).format(
            city=city_name, neighborhoods=neighborhoods, architecture=architecture,
            neighborhoods_str=neighborhoods_str, plz_short=plz_short
        )
        title = b["title"].format(city=city_name)
        icon_path = ICONS.get(b["icon"], "")
        benefits_html += f'''
        <div class="benefit">
          <div class="benefit__icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none">{icon_path}</svg>
          </div>
          <h3>{title}</h3>
          <p>{text}</p>
        </div>'''

    services_html = ""
    for s in service_data["services"]:
        icon_id = s.get("icon", "home")
        icon_path = ICONS.get(icon_id, ICONS["home"])
        title = s["title"].format(city=city_name)
        raw_desc = s.get("desc") or s.get("text", "")
        desc = preformat(raw_desc).format(
            city=city_name, neighborhoods=neighborhoods, architecture=architecture,
            neighborhoods_str=neighborhoods_str, plz_short=plz_short
        )
        tag = s.get("tag", "")
        services_html += f'''
        <div class="service-item">
          <div class="service-item__icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">{icon_path}</svg>
          </div>
          <div class="service-item__content">
            <h4>{title}</h4>
            <p>{desc}</p>
          </div>
        </div>'''

    form_options_html = ""
    for opt in service_data["form_options"]:
        form_options_html += f'<option value="{opt["value"]}">{opt["label"]}</option>'

    reviews_html = ""
    for r in reviews:
        text = preformat(r["text"]).format(
            city=city_name, neighborhoods=neighborhoods, architecture=architecture,
            neighborhoods_str=neighborhoods_str, plz_short=plz_short
        )
        reviews_html += f'''
        <div class="review">
          <p class="review__text">"{text}"</p>
          <div class="review__author">{r["name"]} — {r["city"]}</div>
        </div>'''

    faq_html = ""
    if faq:
        for f in faq:
            q = preformat(f["q"]).format(
                city=city_name, neighborhoods=neighborhoods, architecture=architecture,
                neighborhoods_str=neighborhoods_str, plz_short=plz_short
            )
            a = preformat(f["a"]).format(
                city=city_name, neighborhoods=neighborhoods, architecture=architecture,
                neighborhoods_str=neighborhoods_str, plz_short=plz_short
            )
            faq_html += f'''
          <div class="faq-item">
            <h4>{q}</h4>
            <p>{a}</p>
          </div>'''

    placeholder_plz = service_data.get("form_placeholder_plz", "{plz_short}").format(
        plz_short=plz_short, neighborhoods=neighborhoods, city=city_name, architecture=architecture,
        neighborhoods_str=neighborhoods_str
    )
    placeholder_msg = preformat(service_data.get("form_message_placeholder", "")).format(
        plz_short=plz_short, neighborhoods=neighborhoods, city=city_name, architecture=architecture,
        neighborhoods_str=neighborhoods_str
    )

    return f'''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <meta name="description" content="{meta_desc}">
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

  <section class="hero">
    <div class="container">
      <div class="hero__content">
        <span class="hero__tag">Solar & PV — {city_name}</span>
        <h1>{headline}</h1>
        <p class="hero__sub">{sub}</p>
      </div>
    </div>
  </section>

  <section class="section section--dark" id="benefits">
    <div class="container">
      <h2 class="section__title section__title--light">Ihre Vorteile in {city_name}</h2>
      <div class="benefits">
        {benefits_html}
      </div>
    </div>
  </section>

  <section class="section" id="services">
    <div class="container">
      <h2 style="margin-bottom:2rem">Was wir für Sie tun</h2>
      <div class="services-list">
        {services_html}
      </div>
    </div>
  </section>

  <section class="section section--light" id="reviews">
    <div class="container">
      <h2 style="margin-bottom:2rem">Das sagen Kunden in {city_name}</h2>
      <div class="reviews">
        {reviews_html}
      </div>
    </div>
  </section>

  <section class="section" id="faq">
    <div class="container">
      <h2 style="margin-bottom:2rem">Häufige Fragen in {city_name}</h2>
      <div class="faq">
        {faq_html}
      </div>
    </div>
  </section>

  <section class="section cta-section" id="angebot">
    <div class="container">
      <div class="cta-grid">
        <div class="cta-content">
          <span class="section__tag" style="color:#bfdbfe">Kostenlos anfragen</span>
          <h2>Jetzt Angebot für {city_name} anfordern</h2>
          <p>Sie haben Fragen oder möchten ein Angebot? Eine Anfrage - bis zu drei Angebote von Fachbetrieben in {city_name}. Unverbindlich.</p>
        </div>
        <div class="cta-form">
          <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
            <div class="form-group">
              <label for="service">Gewünschte Leistung</label>
              <select id="service" name="service" required>
                <option value="">Bitte wählen...</option>
                {form_options_html}
              </select>
            </div>
            <div class="form-group">
              <label for="plz">PLZ {city_name}</label>
              <input type="text" id="plz" name="plz" placeholder="{placeholder_plz}" required pattern="[0-9]{{5}}">
            </div>
            <div class="form-group">
              <label for="message">Ihre Nachricht</label>
              <textarea id="message" name="message" rows="4" placeholder="{placeholder_msg}">{placeholder_msg}</textarea>
            </div>
            <input type="hidden" name="city" value="{city_id}">
            <input type="hidden" name="service_type" value="{service_id}">
            <button type="submit" class="btn btn--primary btn--lg" style="width:100%">Kostenlos Angebot anfordern</button>
            <p class="form-privacy">Keine Verpflichtung. Keine Weitergabe an Dritte.</p>
          </form>
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

def main():
    count = 0
    for service_id, service_data in SERVICES.items():
        for city_id, city_data in CITIES.items():
            output_dir = f"solar/{service_id}/{city_id}"
            os.makedirs(output_dir, exist_ok=True)
            html = generate_page(service_id, city_id, city_data, service_data)
            with open(f"{output_dir}/index.html", "w", encoding="utf-8") as f:
                f.write(html)
            count += 1
    print(f"Generated {count} Solar service pages (12 services × 14 cities)")

if __name__ == "__main__":
    main()