#!/usr/bin/env python3
"""
Generate all heating/sanitary/air-con service pages using the rich layout.
6 services × 14 cities = 84 HTML pages.
Run: python gen_heating_pages.py
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
        "architecture": "Gemischte Bausubstanz: Altbauten mit Gasheizung in Prenzlauer Berg, Wärmepumpen in Neubauten, Flachdächer am Potsdamer Platz",
        "famous": "Brandenburger Tor, Berliner Mauer, Techno, Berlinale, BVG",
        "reviews": [
            {"text": "Unsere Gasheizung in Prenzlauer Berg war 25 Jahre alt. Über das Portal drei Angebote bekommen - alle aus Berlin. Der Betrieb aus Mitte hat das komplett neu gemacht.", "name": "Thomas K.", "city": "Berlin-Prenzlauer Berg", "service": "Heizungsbau 2025"},
            {"text": "Wärmepumpe für unser Reihenhaus in Kreuzberg. Die Beratung war ehrlich - manchmal ist eine Gasheizung mit Solar noch die bessere Lösung. Gute Beratung.", "name": "Sabine M.", "city": "Berlin-Kreuzberg", "service": "Wärmepumpe 2024"},
            {"text": "Klimaanlage für die Bürofläche in Mitte. Schnelle Installation, saubere Arbeit. Die Kühlung funktioniert einwandfrei.", "name": "Mike R.", "city": "Berlin-Mitte", "service": "Klimaanlage 2025"},
        ],
        "faq": [
            {"q": "Welche Berliner Bezirke werden abgedeckt?", "a": "Alle 12 Bezirke: Mitte, Prenzlauer Berg, Kreuzberg, Charlottenburg, Neukölln, Schöneberg, Wedding, Tempelhof, Friedrichshain, Pankow, Spandau und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Berliner Betriebe melden sich innerhalb von 24 Stunden. Für Notfälle wie Heizungsausfall besonders schnell."},
            {"q": "Was kostet eine Wärmepumpe in Berlin?", "a": "Für ein typisches Berliner Einfamilienhaus liegen die Kosten zwischen 15.000 und 30.000 Euro. Fördermittel über BAFA und KfW machen es attraktiver."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich. Keinerlei Druck, keine Verpflichtung."},
            {"q": "Gibt es für Berlin spezielle Auflagen?", "a": "Das Erneuerbare-Energien-Gesetz (EEG) und das GEG schreiben bei Neubauten Wärmepumpen vor. Unsere Betriebe kennen die Vorschriften."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte, kein Spam."},
        ],
    },
    "muenchen": {
        "name": "München",
        "region": "Bayern",
        "plz": "80331 bis 81929",
        "plz_short": "80331",
        "neighborhoods": ["Altstadt", "Schwabing", "Maxvorstadt", "Bogenhausen", "Pasing", "Neuhausen", "Giesing", "Moosach"],
        "architecture": "Stadtvillen mit Ölheizung, moderne Neubauten mit Wärmepumpe, Altbauten mit Gas und Fernwärme",
        "famous": "Oktoberfest, BMW, Allianz Arena, Marienplatz",
        "reviews": [
            {"text": "Unsere Heizung in Schwabing war hinüber. Drei Angebote bekommen, Betrieb aus dem Viertel genommen. Die neue Gas-Brennwertheizung läuft super.", "name": "Ursula K.", "city": "München-Schwabing", "service": "Heizungsbau 2025"},
            {"text": "Wärmepumpe für unser Reihenhaus in Pasing. Die Beratung war gut - wir haben uns dann doch für eine Wärmepumpe entschieden. Die Fördermittel haben wir auch genehmigt bekommen.", "name": "Florian M.", "city": "München-Pasing", "service": "Wärmepumpe 2025"},
            {"text": "Badezimmer komplett saniert in Giesing. Neue Leitungen, neue Fliesen, neue Armaturen. Saubere Arbeit, fairer Preis.", "name": "Simone R.", "city": "München-Giesing", "service": "Bad Sanierung 2024"},
        ],
        "faq": [
            {"q": "Welche Münchner Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, Lehel, Maxvorstadt, Schwabing, Neuhausen, Giesing, Sendling, Pasing, Bogenhausen, Moosach und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Münchner Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine Heizungssanierung in München?", "a": "München ist nicht billig - dementsprechend liegen die Kosten etwas höher. Eine neue Gas-Brennwertheizung liegt zwischen 8.000 und 18.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Die Angebote kommen unverbindlich. Wenn nichts dabei ist, gehen Sie woanders hin."},
            {"q": "Wie funktioniert das mit der Förderung?", "a": "BAFA und KfW fördern Wärmepumpen und Heizungssanierungen. Unsere Betriebe helfen bei der Antragstellung."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "koeln": {
        "name": "Köln",
        "region": "Nordrhein-Westfalen",
        "plz": "50667 bis 51149",
        "plz_short": "50667",
        "neighborhoods": ["Innenstadt", "Ehrenfeld", "Nippes", "Mülheim", "Lindenthal", "Rodenkirchen", "Porz", "Deutz"],
        "architecture": "Rheinische Bausubstanz mit älteren Ölheizungen, Wärmepumpen in Neubauten, Gasheizungen im Rheinland",
        "famous": "Kölner Dom, Karneval, Rhein, RTL",
        "reviews": [
            {"text": "Unsere alte Ölheizung in Ehrenfeld war ein Energiefresser. Drei Angebote eingeholt, auf Wärmepumpe umgestiegen. Die Förderung hat viel gebracht.", "name": "Thomas B.", "city": "Köln-Ehrenfeld", "service": "Heizungssanierung 2025"},
            {"text": "Klimaanlage für unser Büro in der Innenstadt. Schnelle Beratung, saubere Installation. Alles funktioniert bestens.", "name": "Sandra K.", "city": "Köln-Innenstadt", "service": "Klimaanlage 2025"},
            {"text": "Bad komplett saniert in Mülheim. Neue Dusche, neue Toilette, neue Leitungen. Der Betrieb aus Porz hat sauber gearbeitet.", "name": "Marco L.", "city": "Köln-Mülheim", "service": "Bad Sanierung 2024"},
        ],
        "faq": [
            {"q": "Welche Kölner Stadtteile werden abgedeckt?", "a": "Unsere Partnerbetriebe arbeiten in ganz Köln: Ehrenfeld, Nippes, Mülheim, Lindenthal, Rodenkirchen, Porz, Deutz, Chorweiler, Kalk und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Kölner Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine Wärmepumpe in Köln?", "a": "Die Kosten hängen von Größe und Zustand ab. Ein mittleres Einfamilienhaus liegt zwischen 14.000 und 28.000 Euro."},
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
        "architecture": "Klassische Hamburger Reihenhäuser mit Gasheizung, Altbauten mit Öl, Wärmepumpen in Neubaugebieten",
        "famous": "Hafen, Elbphilharmonie, Reeperbahn, Hamburger SV",
        "reviews": [
            {"text": "Heizung in Eppendorf war 30 Jahre alt. Drei Angebote bekommen, Betrieb aus dem Viertel genommen. Neue Brennwertheizung, Gas spart jetzt einiges.", "name": "Friedrich B.", "city": "Hamburg-Eppendorf", "service": "Heizungsbau 2025"},
            {"text": "Wärmepumpe für unser Reihenhaus in Winterhude. Die Beratung war gut - auch ehrlich wenn eine Wärmepumpe nicht passt. Haben uns dann doch für Hybrid entschieden.", "name": "Nina T.", "city": "Hamburg-Winterhude", "service": "Wärmepumpe 2025"},
            {"text": "Klimaanlage für die Praxis in der HafenCity. Saubere Installation, gute Kühlleistung. Patientenzufriedenheit gestiegen.", "name": "Heike M.", "city": "Hamburg-HafenCity", "service": "Klimaanlage 2025"},
        ],
        "faq": [
            {"q": "Welche Hamburger Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, Neustadt, HafenCity, St. Pauli, Altona, Eppendorf, Winterhude, Barmbek, Bergedorf, Blankenese und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Hamburger Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine Heizungssanierung in Hamburg?", "a": "Die Kosten in Hamburg liegen im oberen Bereich. Eine Gas-Brennwertheizung liegt zwischen 9.000 und 20.000 Euro."},
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
        "architecture": "Steile Hanglagen mit Ölheizungen, Wärmepumpen auf den Fildern, Gas in den Neubaugebieten",
        "famous": "Mercedes-Benz, Porsche, Stuttgarter Weihnachtsmarkt",
        "reviews": [
            {"text": "Heizung in Degerloch war undicht. Drei Angebote geholt, Betrieb aus dem Süden genommen. Neue Gasheizung, läuft einwandfrei.", "name": "Monika W.", "city": "Stuttgart-Degerloch", "service": "Heizungsbau 2025"},
            {"text": "Wärmepumpe für unser Haus in Vaihingen. Die Beratung war umfassend. Wir haben uns dann für eine Luft-Wärmepumpe entschieden - passt gut.", "name": "Thomas K.", "city": "Stuttgart-Vaihingen", "service": "Wärmepumpe 2025"},
            {"text": "Bad saniert in Bad Cannstatt. Neue Wanne, neue Fliesen, neue Armaturen. Der Betrieb aus dem Viertel war pünktlich und sauber.", "name": "Julia F.", "city": "Stuttgart-Bad Cannstatt", "service": "Bad Sanierung 2025"},
        ],
        "faq": [
            {"q": "Welche Stuttgarter Stadtbezirke werden abgedeckt?", "a": "Alle PLZ-Gebiete: 70173 bis 70199 (Mitte), 70372 bis 70376 (Bad Cannstatt), 70431 bis 70469 (Feuerbach, Zuffenhausen), 70563 bis 70599 (Vaihingen, Degerloch)."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Innerhalb von 24 Stunden. In Stuttgart sind die Betriebe auch in den Stadtbezirken gut erreichbar."},
            {"q": "Was kostet eine Heizungssanierung in Stuttgart?", "a": "Die Kosten liegen in Stuttgart etwas über dem Bundesdurchschnitt. Eine Wärmepumpe mittlerer Größe liegt zwischen 15.000 und 30.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich."},
            {"q": "Stuttgart ist hügelig - spielt das eine Rolle?", "a": "Ja. Die Topografie und die Höhenlagen erfordern angepasste Heizsysteme. Unsere Stuttgarter Betriebe kennen das."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur an die vermittelten Betriebe weitergegeben. Nicht an Dritte."},
        ],
    },
    "dortmund": {
        "name": "Dortmund",
        "region": "Nordrhein-Westfalen",
        "plz": "44135 bis 44379",
        "plz_short": "44135",
        "neighborhoods": ["Innenstadt", "Kreuzviertel", "Nordstadt", "Hörde", "Hombruch", "Brackel", "Aplerbeck", "Barop"],
        "architecture": "Ruhrgebiets-Bausubstanz mit älteren Ölheizungen, Gas in neueren Bauten, Wärmepumpen im Aufwind",
        "famous": "SIGNAL IDUNA PARK, Bier, Phoenix, Möller",
        "reviews": [
            {"text": "Heizung in Hombruch war uralt. Über das Portal drei Angebote bekommen, Betrieb aus dem Ruhrgebiet genommen. Neue Brennwertheizung, spart jetzt Gas.", "name": "Ursula K.", "city": "Dortmund-Hombruch", "service": "Heizungsbau 2025"},
            {"text": "Wärmepumpe für unser Reihenhaus in der Nordstadt. Drei Angebote, schnelle Ausführung. Die Förderung war ein großer Anteil.", "name": "Jens P.", "city": "Dortmund-Nordstadt", "service": "Wärmepumpe 2025"},
            {"text": "Solarthermie für unser Haus in Hörde. Der Betrieb aus dem Umland hat kompetent beraten. Die Anlage ist seit einem Jahr in Betrieb.", "name": "Simone A.", "city": "Dortmund-Hörde", "service": "Solarthermie 2024"},
        ],
        "faq": [
            {"q": "Welche Dortmunder Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Innenstadt, Kreuzviertel, Nordstadt, Hörde, Hombruch, Brackel, Aplerbeck, Barop und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Dortmunder Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine Heizungssanierung in Dortmund?", "a": "Die Kosten im Ruhrgebiet sind günstiger als in den Großstädten. Eine neue Gasheizung liegt zwischen 7.000 und 16.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Die Angebote sind unverbindlich."},
            {"q": "Dortmund hat viel Industrie - spielt das eine Rolle?", "a": "Bei älteren Gebäuden in der Innenstadt kann das relevant sein. Unsere Betriebe kennen die lokalen Gegebenheiten."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "frankfurt": {
        "name": "Frankfurt am Main",
        "region": "Hessen",
        "plz": "60306 bis 60599",
        "plz_short": "60311",
        "neighborhoods": ["Innenstadt", "Sachsenhausen", "Westend", "Bornheim", "Nordend", "Ostend", "Bockenheim", "Bahnofsviertel"],
        "architecture": "Hochhäuser mit Fernwärme, Altbauten mit Gas, Wärmepumpen in modernen Bürobauten",
        "famous": "Römer, Commerzbank Tower, Goethe-Haus, Messe, Flughafen, Main",
        "reviews": [
            {"text": "Heizung in Bornheim war undicht. Der Betrieb aus dem Umland hat schnell reagiert, fair kalkuliert und sauber gearbeitet. Nur 3 Tage bis alles fertig war.", "name": "Julia S.", "city": "Frankfurt-Bornheim", "service": "Heizungsbau 2025"},
            {"text": "Wärmepumpe für unser Reihenhaus in Sachsenhausen. Drei Angebote eingeholt, alle aus dem Rhein-Main-Gebiet. Die Beratung war gut.", "name": "Andreas W.", "city": "Frankfurt-Sachsenhausen", "service": "Wärmepumpe 2024"},
            {"text": "Klimaanlage für unser Büro in Bockenheim. Nach dem Sturm war schnelle Hilfe nötig. Das Team war am nächsten Tag da und hat provisorisch gesichert.", "name": "Claudia B.", "city": "Frankfurt-Bockenheim", "service": "Klimaanlage 2025"},
        ],
        "faq": [
            {"q": "Welche Frankfurter Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Innenstadt, Sachsenhausen, Westend, Bornheim, Nordend, Ostend, Bockenheim, Bahnhofsviertel und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Frankfurter Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine neue Heizung in Frankfurt?", "a": "Für ein typisches Reihenhaus in Frankfurt (80-120 qm) liegen die Kosten bei 10.000 bis 22.000 Euro."},
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
        "architecture": "Gründerzeitbauten mit älteren Ölheizungen, Wärmepumpen in neueren Siedlungen, Gasheizungen in Reihenhäusern",
        "famous": "Maschsee, Herrenhäuser Gärten, Neues Rathaus, Marktkirche, Expo-Gelände",
        "reviews": [
            {"text": "Heizung in List war 25 Jahre alt. Drei Angebote, Betrieb aus Hannover genommen. Neue Gas-Brennwertheizung, einfache Bedienung.", "name": "Nina T.", "city": "Hannover-List", "service": "Heizungsbau 2025"},
            {"text": "Wärmepumpe für unser Reihenhaus in Döhren. Die Beratung war ehrlich - nicht immer ist Wärmepumpe die beste Lösung. Haben uns dann doch dafür entschieden.", "name": "Frank D.", "city": "Hannover-Döhren", "service": "Wärmepumpe 2024"},
            {"text": "Bad komplett saniert in Bothfeld. Neue Dusche, neue Toilette, neue Leitungen. Pünktlich, sauber, fair - was will man mehr?", "name": "Sandra J.", "city": "Hannover-Bothfeld", "service": "Bad Sanierung 2025"},
        ],
        "faq": [
            {"q": "Welche Hannoverschen Stadtteile werden abgedeckt?", "a": "Alle 51 Stadtteile: von Mitte über List, Vahrenwald und Linden bis Bothfeld, Misburg und Burg. Auch das Umland wie Laatzen und Langenhagen."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Sie erhalten innerhalb von 24 Stunden einen Rückruf."},
            {"q": "Was kostet eine Heizungssanierung in Hannover?", "a": "Für ein typisches hannoversches Reihenhaus liegen die Kosten bei 8.000 bis 18.000 Euro."},
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
        "architecture": "Rheinische Villen mit Öl- und Gasheizungen, Wärmepumpen in modernen Bauten, Fernwärme in der Altstadt",
        "famous": "Altbier, Kö, Königsallee, Medienhafen, Rheinturm",
        "reviews": [
            {"text": "Heizung in Oberkassel war ein großes Projekt. Drei Angebote eingeholt, alle professionell. Neue Hybridheizung mit Solar.", "name": "Rolf H.", "city": "Düsseldorf-Oberkassel", "service": "Heizungsbau 2025"},
            {"text": "Klimaanlage für die Praxis in Derendorf. Schnelle Beratung, saubere Installation. Die Kühlung funktioniert einwandfrei.", "name": "Birgit S.", "city": "Düsseldorf-Derendorf", "service": "Klimaanlage 2025"},
            {"text": "Bad saniert in der Altstadt. Enge Gassen, wenig Platz - unsere Betriebe in Düsseldorf kennen das und planen dementsprechend.", "name": "Dieter M.", "city": "Düsseldorf-Altstadt", "service": "Bad Sanierung 2024"},
        ],
        "faq": [
            {"q": "Welche Düsseldorfer Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, Carlstadt, Stadtmitte, Pempelfort, Düsseltal, Oberkassel, Niederkassel, Derendorf und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Düsseldorfer Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine Heizungssanierung in Düsseldorf?", "a": "Düsseldorf liegt im oberen Bereich. Eine neue Gasheizung liegt zwischen 9.000 und 20.000 Euro."},
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
        "architecture": "Gründerzeit-Altbauten mit alten Ölheizungen, Wärmepumpen in sanierten Gebäuden, Gas in Neubauten",
        "famous": "Bach, Gewandhaus, Spassgarde, Ausstellungszentrum",
        "reviews": [
            {"text": "Heizung in Connewitz war ein Abenteuer. Über das Portal aber den richtigen Betrieb gefunden. Neue Gasheizung, läuft super.", "name": "Martina B.", "city": "Leipzig-Connewitz", "service": "Heizungsbau 2025"},
            {"text": "Wärmepumpe für unser saniertes Gründerzeithaus in Plagwitz. Drei Angebote, schnelle Ausführung. Die Kombination mit Solarthermie war die richtige Wahl.", "name": "Frank S.", "city": "Leipzig-Plagwitz", "service": "Wärmepumpe 2025"},
            {"text": "Bad komplett saniert in Lindenau. Neue Fliesen, neue Sanitärkeramik, neue Leitungen. Der Betrieb aus dem Viertel war super.", "name": "Andrea K.", "city": "Leipzig-Lindenau", "service": "Bad Sanierung 2024"},
        ],
        "faq": [
            {"q": "Welche Leipziger Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Innenstadt, Zentrum, Plagwitz, Lindenau, Connewitz, Stötteritz, Gohlis, Schleussig und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Leipziger Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine Heizungssanierung in Leipzig?", "a": "Leipzig ist günstiger als die westdeutschen Großstädte. Eine neue Gasheizung liegt zwischen 6.000 und 15.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Die Angebote sind unverbindlich."},
            {"q": "Leipzig wächst schnell - wie ist das bei der Vermittlung?", "a": "Leipzig boomt, und die Installateure haben alle Hände voll zu tun. Deshalb ist der Vergleich über uns besonders wertvoll."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "bremen": {
        "name": "Bremen",
        "region": "Bremen",
        "plz": "28195 bis 28779",
        "plz_short": "28195",
        "neighborhoods": ["Mitte", "Neustadt", "Schwachhausen", "Horn-Lehe", "Borgfeld", "Gröpelingen", "Huchting", "Vegesack"],
        "architecture": "Backsteingotik mit älteren Ölheizungen, Wärmepumpen in Villenvierteln, Gas in Reihenhausgebieten",
        "famous": "Rathaus, Roland, Stadtmusikanten, Weser, Schlachte, Überseestadt",
        "reviews": [
            {"text": "Heizung in Schwachhausen war 40 Jahre alt. Drei Angebote, alle aus Bremen. Neue Brennwertheizung, spart ordentlich Gas.", "name": "Heike M.", "city": "Bremen-Schwachhausen", "service": "Heizungsbau 2025"},
            {"text": "Klimaanlage für unser Büro in der Neustadt. Schnelle Beratung, fairer Preis. Die Installation war in zwei Tagen durch.", "name": "Ralf S.", "city": "Bremen-Neustadt", "service": "Klimaanlage 2024"},
            {"text": "Solarthermie für unser Reihenhaus in Gröpelingen. Die Beratung war kompetent, das Angebot transparent.", "name": "Anke P.", "city": "Bremen-Gröpelingen", "service": "Solarthermie 2025"},
        ],
        "faq": [
            {"q": "Welche Bremer Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Mitte, Neustadt, Schwachhausen, Horn-Lehe, Borgfeld, Gröpelingen, Huchting, Vegesack und alle weiteren. Auch Bremerhaven."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Bremer Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine neue Heizung in Bremen?", "a": "Für ein typisches Bremer Reihenhaus liegen die Kosten bei 8.000 bis 17.000 Euro."},
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
        "architecture": "Fachwerk-Altbauten mit Ölheizungen, Wärmepumpen in sanierten Gebäuden, Gas in Neubauten",
        "famous": "Kaiserburg, Christkindlesmarkt, Albrecht Dürer, Nürnberger Rostbratwurst",
        "reviews": [
            {"text": "Heizung in der Altstadt war sanierungsbedürftig. Der Betrieb hat sich umfassend gekümmert, inklusive Abstimmung mit dem Denkmalschutz. Super Arbeit!", "name": "Monika H.", "city": "Nürnberg-Altstadt", "service": "Heizungsbau 2025"},
            {"text": "Solarthermie für unser Reihenhaus in St. Leonhard. Drei Angebote, der Betrieb aus dem Umland hatte das beste Konzept.", "name": "Stefan B.", "city": "Nürnberg-St. Leonhard", "service": "Solarthermie 2024"},
            {"text": "Wärmepumpe für unser Haus in Gostenhof. Nach dem Starkregen letzte Woche war schnelle Hilfe nötig. Innerhalb von 24 Stunden war jemand da.", "name": "Petra K.", "city": "Nürnberg-Gostenhof", "service": "Wärmepumpe 2025"},
        ],
        "faq": [
            {"q": "Welche Nürnberger Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, St. Lorenz, St. Sebald, Gostenhof, Bärenschanze, St. Leonhard, Steinbühl, Glockenhof und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Nürnberger Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine Heizungssanierung in Nürnberg?", "a": "Die Kosten in Nürnberg liegen im bayrischen Durchschnitt. Eine neue Gasheizung liegt zwischen 8.000 und 18.000 Euro."},
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
        "architecture": "Quadratestadt mit Gasheizungen, Wärmepumpen in modernen Bauten, Öl in älteren Gebäuden",
        "famous": "Barockschloss, Quadratestadt, BASF, SAP Arena, Jungbusch",
        "reviews": [
            {"text": "Heizung in der Neckarstadt-Ost war uralt. Drei Angebote, Betrieb aus Mannheim genommen. Neue Gasheizung, läuft einwandfrei.", "name": "Diana K.", "city": "Mannheim-Neckarstadt-Ost", "service": "Heizungsbau 2025"},
            {"text": "Klimaanlage für unser Büro in Käfertal. Die Beratung war gut, das Angebot transparent. Die Installation war schnell gemacht.", "name": "Thomas W.", "city": "Mannheim-Käfertal", "service": "Klimaanlage 2024"},
            {"text": "Bad komplett saniert in der Oststadt. Neue Wanne, neue Fliesen, neue Armaturen. Der Betrieb war pünktlich und sauber.", "name": "Sabine R.", "city": "Mannheim-Oststadt", "service": "Bad Sanierung 2025"},
        ],
        "faq": [
            {"q": "Welche Mannheimer Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Innenstadt, Jungbusch, Neckarstadt-Ost, Käfertal, Lindenhof, Oststadt, Schwetzingerstadt, Waldhof und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Sie erhalten innerhalb von 24 Stunden einen Rückruf."},
            {"q": "Was kostet eine Heizungssanierung in Mannheim?", "a": "Für ein typisches Mannheimer Reihenhaus liegen die Kosten bei 8.000 bis 18.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich."},
            {"q": "Gibt es in Mannheim Auflagen für Dacharbeiten?", "a": "Das Barockschloss und die umliegenden Quadrate stehen unter Denkmalschutz. Auch in der Oststadt gibt es denkmalgeschützte Bausubstanz."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "freiburg": {
        "name": "Freiburg",
        "region": "Baden-Württemberg",
        "plz": "79098 bis 79117",
        "plz_short": "79098",
        "neighborhoods": ["Altstadt", "Innenstadt", "Stühlinger", "Herdern", "Vauban", "Landwasser", "Haslach", "Opfingen"],
        "architecture": "Solarstadt mit vielen Wärmepumpen und Solaranlagen, Gas in älteren Gebäuden, Fernwärme in Vauban",
        "famous": "Münster, Schwarzwald, Universitätsstadt, Vauban",
        "reviews": [
            {"text": "Wärmepumpe für unser Haus in Vauban. Die Ökostadt braucht keine fossilen Brennstoffe. Drei Angebote, alle aus Freiburg.", "name": "Stefanie G.", "city": "Freiburg-Vauban", "service": "Wärmepumpe 2025"},
            {"text": "Solarthermie für unser Reihenhaus in Herdern. Der Betrieb aus dem Schwarzwald hat die Anlage dimensioniert. Läuft seit einem Jahr einwandfrei.", "name": "Martin W.", "city": "Freiburg-Herdern", "service": "Solarthermie 2025"},
            {"text": "Heizung in der Innenstadt war undicht. Der Betrieb kam schnell, hat einen fairen Preis gemacht und war mit der Arbeit in 3 Tagen fertig.", "name": "Ute B.", "city": "Freiburg-Innenstadt", "service": "Heizungsbau 2024"},
        ],
        "faq": [
            {"q": "Welche Freiburger Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, Innenstadt, Stühlinger, Herdern, Vauban, Landwasser, Haslach, Opfingen und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Freiburger Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine Heizungssanierung in Freiburg?", "a": "Freiburg ist etwas teurer als der Durchschnitt. Eine Wärmepumpe liegt zwischen 14.000 und 28.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich."},
            {"q": "Freiburg ist eine Solarstadt - spielt das eine Rolle?", "a": "Ja. Viele Freiburger setzen auf Wärmepumpen und Solarthermie. Unsere Betriebe kennen die lokalen Besonderheiten."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
}

# =============================================================================
# SERVICE DATA
# =============================================================================

SERVICES = {
    "waermepumpe": {
        "page_title": "Wärmepumpe {city} - Einbau, Austausch und Förderung",
        "meta_desc": "Wärmepumpe {city}: Einbau, Austausch und Förderung. Kostenlos bis zu 3 Angebote von Fachbetrieben in {city}. Unverbindlich.",
        "nav_active": "Wärmepumpe",
        "headline": "Wärmepumpe {city} - einbauen, austauschen, sparen",
        "sub": "Die Wärmepumpe ist die Heizung der Zukunft. Eine Anfrage an uns - und bis zu drei {city}er Fachbetriebe melden sich mit ihrem Angebot.",
        "benefits": [
            {"icon": "bolt", "title": "Strom statt Gas", "text": "Wärmepumpen nutzen Strom - und werden immer mehr mit Solarstrom betrieben. In {city} eine zunehmend beliebte Lösung."},
            {"icon": "flame", "title": "Günstiger Betrieb", "text": "Die Betriebskosten einer Wärmepumpe sind deutlich niedriger als bei einer Gasheizung. In {city} macht sich das bemerkbar."},
            {"icon": "shield", "title": "BAFA und KfW Förderung", "text": "Bis zu 40% der Kosten werden gefördert. Unsere {city}er Betriebe helfen bei der Antragstellung."},
            {"icon": "wind", "title": "Luft, Wasser oder Erdreich", "text": "Es gibt verschiedene Wärmepumpen-Typen. Für {city} eignet sich oft die Luft-Wärmepumpe - günstig und effizient."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Fachbetriebe weiter."},
            {"icon": "settings", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "bolt", "title": "Luft-Wärmepumpe", "desc": "Die günstigste Variante: Luft-Wärmepumpen sind in {city} besonders verbreitet. Für jedes Haus nachrüstbar.", "tag": "Luft-WP"},
            {"icon": "flame", "title": "Sole-Wärmepumpe", "desc": "Für Neubauten undsanierte Gebäude: Die Sole-Wärmepumpe nutzt Erdwärme. Effizient, aber aufwendiger zu installieren.", "tag": "Erdreich"},
            {"icon": "water", "title": "Wasser-Wärmepumpe", "desc": "Nutzt Grundwasser als Wärmequelle. Nur geeignet, wenn die hydrogeologischen Bedingungen in {city} passen.", "tag": "Grundwasser"},
            {"icon": "expand", "title": "Hybridheizung", "desc": "Wärmepumpe und Gasheizung kombiniert - in {city} oft die beste Lösung beim Austausch einer alten Ölheizung.", "tag": "Hybrid"},
            {"icon": "settings", "title": "Heizungs-Check", "desc": "Sie wissen nicht, ob eine Wärmepumpe für Ihr Haus in {city} infrage kommt? Ein Heizungs-Check zeigt es.", "tag": "Check"},
            {"icon": "pipe", "title": "Heizungsrohr-Verlegung", "desc": "Wenn Sie in {city} eine Wärmepumpe einbauen, müssen oft auch Rohre verlegt werden. Unsere Betriebe koordinieren das.", "tag": "Rohre"},
        ],
        "faq": None,
        "form_options": [
            {"value": "luft-wp", "label": "Luft-Wärmepumpe"},
            {"value": "erdreich-wp", "label": "Sole-Wärmepumpe (Erdreich)"},
            {"value": "wasser-wp", "label": "Wasser-Wärmepumpe"},
            {"value": "hybrid", "label": "Hybridheizung"},
            {"value": "heizungscheck", "label": "Heizungs-Check"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Welche Heizung haben Sie aktuell? Altbau oder Neubau? {neighborhoods[0]} oder {neighborhoods[1]}?",
    },
    "heizungsbau": {
        "page_title": "Heizungsbau {city} - Installation, Austausch und Wartung",
        "meta_desc": "Heizungsbau {city}: Installation, Austausch und Wartung. Kostenlos bis zu 3 Angebote von Installateuren in {city}. Unverbindlich.",
        "nav_active": "Heizungsbau",
        "headline": "Heizungsbau {city} - neue Heizung, fairer Preis",
        "sub": "Ihre Heizung ist zu alt oder zu teuer? Eine Anfrage an uns - und bis zu drei {city}er Installateure melden sich mit ihrem Angebot.",
        "benefits": [
            {"icon": "flame", "title": "Gas oder Wärmepumpe?", "text": "In {city} gibt es für jedes Haus die richtige Heizung. Unsere Betriebe beraten Sie unabhängig - auch über Hybridlösungen."},
            {"icon": "shield", "title": "Brennwert oder Wärmepumpe", "text": "Die beste Heizung für {city} hängt von Ihrem Haus ab. Unsere {city}er Installateure kennen die lokalen Gegebenheiten."},
            {"icon": "clock", "title": "Schnelle Hilfe bei Ausfall", "text": "Wenn die Heizung ausfällt, ist schnelles Handeln gefragt. Unsere {city}er Betriebe reagieren schnell."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Installateure weiter."},
            {"icon": "settings", "title": "Wartung und Pflege", "text": "Regelmäßige Wartung hält Ihre Heizung in {city} am Laufen. Unsere Betriebe bieten Wartungsverträge an."},
            {"icon": "star", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "flame", "title": "Gasheizung", "desc": "Gas-Brennwertheizungen sind in {city} nach wie vor eine gute Wahl - besonders wenn Gas günstig ist und die Heizung neu ist.", "tag": "Gas"},
            {"icon": "bolt", "title": "Ölheizung Austausch", "desc": "Wenn Ihre Ölheizung in {city} alt ist, lohnt sich ein Austausch. Gas, Wärmepumpe oder Hybrid - wir vermitteln den richtigen Betrieb.", "tag": "Öl"},
            {"icon": "expand", "title": "Hybridheizung", "desc": "Wärmepumpe und Gasheizung kombiniert - in {city} oft die beste Lösung beim Austausch einer alten Ölheizung.", "tag": "Hybrid"},
            {"icon": "pipe", "title": "Heizungsrohr-Erneuerung", "desc": "Wenn in {city} die Rohre alt sind, müssen sie bei einer Heizungssanierung gleich mit erneuert werden. Unsere Betriebe beraten dazu.", "tag": "Rohre"},
            {"icon": "thermometer", "title": "Heizkörper-Tausch", "desc": "Niedertemperatur-Heizkörper für Wärmepumpen, klassische Radiatoren für Gasheizungen. In {city} gibt es für jede Heizung die passenden Heizkörper.", "tag": "Heizkörper"},
            {"icon": "settings", "title": "Notdienst", "desc": "Wenn Ihre Heizung in {city} ausfällt, kommen unsere {city}er Betriebe auch kurzfristig - Notdienst 24/7.", "tag": "Notdienst"},
        ],
        "faq": None,
        "form_options": [
            {"value": "gasheizung", "label": "Gasheizung einbauen"},
            {"value": "oel-ersetzen", "label": "Ölheizung ersetzen"},
            {"value": "hybrid", "label": "Hybridheizung"},
            {"value": "rohr-erneuern", "label": "Heizungsrohre erneuern"},
            {"value": "heizkoerper", "label": "Heizkörper tauschen"},
            {"value": "notdienst", "label": "Notdienst / Reparatur"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Welche Heizung haben Sie aktuell? Altbau? {neighborhoods[0]} oder {neighborhoods[1]}? Bj. wann?",
    },
    "sanitaer": {
        "page_title": "Sanitär {city} - Installation, Wartung und Reparatur",
        "meta_desc": "Sanitär {city}: Installation, Wartung und Reparatur. Kostenlos bis zu 3 Angebote von Sanitär-Profis in {city}. Unverbindlich.",
        "nav_active": "Sanitär",
        "headline": "Sanitär {city} - Leitungen, Anschlüsse, Reparatur",
        "sub": "Wasser, Abwasser, sanitäre Anlagen - wir vermitteln Ihnen bis zu drei {city}er Sanitär-Profis für Ihr Projekt.",
        "benefits": [
            {"icon": "water", "title": "Wasser und Abwasser", "text": "In {city} sorgen unsere Sanitär-Profis für sauberes Trinkwasser und problemloses Abwasser."},
            {"icon": "flame", "title": "Warmwasser", "text": "Durchlauferhitzer oder Warmwasserspeicher - in {city} gibt es für jedes Haus die richtige Lösung."},
            {"icon": "clock", "title": "Schnelle Hilfe bei Rohrbrüchen", "text": "Ein Rohrbruch in {city}? Unsere {city}er Sanitär-Profis reagieren schnell und beheben das Problem."},
            {"icon": "shield", "title": "Trinkwasserschutz", "text": "In {city} gelten strenge Regeln für Trinkwasserinstallation. Unsere Betriebe kennen die Vorschriften."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Sanitär-Profis weiter."},
            {"icon": "star", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "pipe", "title": "Rohr-Installation", "desc": "Wenn in {city} neue Rohre verlegt werden müssen, koordinieren unsere {city}er Profis das sauber und fachgerecht.", "tag": "Rohre"},
            {"icon": "water", "title": "Wasseranschluss", "desc": "Für Neubauten und Sanierungen in {city}: Wasseranschlüsse nach DIN normgerecht verlegen.", "tag": "Wasser"},
            {"icon": "bath", "title": "Abwasser-Entsorgung", "desc": "Abflussrohre, Grundleitungen, Hebeanlagen - in {city} kennen unsere Betriebe die lokalen Gegebenheiten.", "tag": "Abwasser"},
            {"icon": "flame", "title": "Durchlauferhitzer", "desc": "Elektrischer Durchlauferhitzer oder gasbetrieben? Für {city}er Altbauten oft die Lösung beiwarmwasserproblemen.", "tag": "Warmwasser"},
            {"icon": "settings", "title": "Wartung und Reinigung", "desc": "Regelmäßige Wartung der sanitären Anlagen in {city} verhindert große Schäden. Unsere Betriebe bieten Wartungsverträge.", "tag": "Wartung"},
            {"icon": "check", "title": "Dichtigkeitsprüfung", "desc": "Nach DIN 1988 müssen Trinkwasserinstallationen in {city} auf Dichtigkeit geprüft werden. Unsere Betriebe machen das.", "tag": "Prüfung"},
        ],
        "faq": None,
        "form_options": [
            {"value": "rohr-installation", "label": "Rohr-Installation"},
            {"value": "wasseranschluss", "label": "Wasseranschluss"},
            {"value": "abwasser", "label": "Abwasser-Entsorgung"},
            {"value": "durchlauferhitzer", "label": "Durchlauferhitzer"},
            {"value": "wartung", "label": "Wartung und Reinigung"},
            {"value": "pruefung", "label": "Dichtigkeitsprüfung"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Was genau soll gemacht werden? {neighborhoods[0]} oder {neighborhoods[1]}? Altbau oder Neubau?",
    },
    "klimaanlage": {
        "page_title": "Klimaanlage {city} - Einbau, Wartung und Reparatur",
        "meta_desc": "Klimaanlage {city}: Einbau, Wartung und Reparatur. Kostenlos bis zu 3 Angebote von Kälte-Technikern in {city}. Unverbindlich.",
        "nav_active": "Klimaanlage",
        "headline": "Klimaanlage {city} - kühlen bei Sommerhitze",
        "sub": "Wenn die Sommer in {city} heiß werden, ist eine Klimaanlage keine Luxus mehr. Wir vermitteln Ihnen bis zu drei {city}er Kälte-Techniker.",
        "benefits": [
            {"icon": "wind", "title": "Kühlung für jede Räumlichkeit", "text": "Ob Büro in {city} oder Wohnung in {neighborhoods[0]} - für jede Räumlichkeit gibt es die passende Klimaanlage."},
            {"icon": "settings", "title": "Wartung für Leistung", "text": "Eine regelmäßig gewartete Klimaanlage kühlt in {city} effizienter und hält länger."},
            {"icon": "shield", "title": "Keimfreie Luft", "text": "Filtersysteme sorgen in {city} für saubere, keimfreie Luft. Gerade für Büros und Praxen wichtig."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Kälte-Techniker weiter."},
            {"icon": "clock", "title": "Schnelle Hilfe bei Ausfall", "text": "Wenn Ihre Klimaanlage in {city} ausfällt, kommen unsere {city}er Betriebe schnell."},
            {"icon": "star", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "wind", "title": "Split-Klimaanlage", "desc": "Für Wohnungen und kleine Büros in {city}: Split-Klimaanlagen sind günstig und effizient.", "tag": "Split"},
            {"icon": "expand", "title": "Multisplit-Anlage", "desc": "Für größere Wohnungen und Reihenhäuser in {city}: Eine Außeneinheit versorgt mehrere Räume.", "tag": "Multisplit"},
            {"icon": "bolt", "title": "Kühldecke", "desc": "Für Büros und Gewerbe in {city}: Kühldecken sind leise und effizient - auch in Wohnungen eine Option."},
            {"icon": "settings", "title": "Wartung", "desc": "Regelmäßige Wartung hält Ihre Klimaanlage in {city} in Schuss. Filterreinigung, Kältemittel-Check, Funktionsprüfung.", "tag": "Wartung"},
            {"icon": "check", "title": "Notdienst", "desc": "Wenn Ihre Klimaanlage in {city} an einem heißen Tag ausfällt, kommt unser Notdienst schnell.", "tag": "Notdienst"},
            {"icon": "pipe", "title": "Kältemittel-Ersatz", "desc": "Alte Klimaanlagen in {city} nutzen oft noch R410A oder R22. Unsere Betriebe tauschen auf umweltfreundlichere Kältemittel.", "tag": "Kältemittel"},
        ],
        "faq": None,
        "form_options": [
            {"value": "split", "label": "Split-Klimaanlage"},
            {"value": "multisplit", "label": "Multisplit-Anlage"},
            {"value": "kuehldecke", "label": "Kühldecke"},
            {"value": "wartung", "label": "Wartung"},
            {"value": "notdienst", "label": "Notdienst / Reparatur"},
            {"value": "kaeltemittel", "label": "Kältemittel ersetzen"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Was soll gekühlt werden? Büro, Praxis, Wohnung? {neighborhoods[0]} oder {neighborhoods[1]}?",
    },
    "badsanierung": {
        "page_title": "Bad Sanierung {city} - complete Badsanierung, Installateur",
        "meta_desc": "Bad Sanierung {city}: Complete Sanierung, neue Fliesen, neue Sanitärkeramik. Kostenlos bis zu 3 Angebote von Profis in {city}. Unverbindlich.",
        "nav_active": "Bad Sanierung",
        "headline": "Bad Sanierung {city} - aus dem alten Bad wird Neues",
        "sub": "Ihr Bad in {city} ist alt und sanierungsbedürftig? Wir vermitteln Ihnen bis zu drei {city}er Fachbetriebe für Ihre Bad Sanierung.",
        "benefits": [
            {"icon": "bath", "title": "Neue Sanitärkeramik", "text": "Wanne, Dusche, Toilette, Waschbecken - in {city} sorgen unsere Profis für moderne Sanitärkeramik."},
            {"icon": "water", "title": "Neue Fliesen", "text": "Moderne Fliesen in {city} - von klassisch bis modern. Unsere {city}er Fliesenleger verlegen sie professionell."},
            {"icon": "pipe", "title": "Neue Leitungen", "text": "Wenn in {city} die alten Leitungen erneuert werden müssen, koordinieren unsere {city}er Profis das mit."},
            {"icon": "flame", "title": "Armaturen und mix", "text": "Armaturen, Duschkopf, Handtuchheizkörper - in {city} gibt es für jeden Geschmack und jedes Budget die passenden Produkte."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Profis weiter."},
            {"icon": "star", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "bath", "title": "Komplettsanierung", "desc": "Wenn in {city} das Bad nicht mehr zu retten ist: Komplettsanierung mit allen Gewerken aus einer Hand.", "tag": "Komplett"},
            {"icon": "expand", "title": "Dusche statt Wanne", "desc": "In {city} oft gewünscht: Die alte Wanne raus, ebenerdige Dusche rein. Unsere {city}er Profis machen das.", "tag": "Dusche"},
            {"icon": "water", "title": "Barrierefreies Bad", "desc": "Für {city}er Senioren oder Menschen mit Behinderung: Barrierefreie Badgestaltung nach DIN 18040.", "tag": "Barrierefrei"},
            {"icon": "flame", "title": "Handtuchheizkörper", "desc": "Ein beheizter Handtuchheizkörper macht das Bad in {city} wohnlicher. Gas oder elektrisch - unsere Betriebe beraten.", "tag": "Heizkörper"},
            {"icon": "pipe", "title": "Rohrleitungs-Erneuerung", "desc": "Wenn in {city} die alten Rohre erneuert werden müssen, macht man das am besten gleich bei der Bad Sanierung.", "tag": "Rohre"},
            {"icon": "check", "title": "Schimmelbekämpfung", "desc": "Schimmel im Bad - in {city} ein häufiges Problem. Unsere {city}er Profis beseitigen Schimmel dauerhaft.", "tag": "Schimmel"},
        ],
        "faq": None,
        "form_options": [
            {"value": "komplett", "label": "Komplettsanierung"},
            {"value": "dusche", "label": "Dusche statt Wanne"},
            {"value": "barrierefrei", "label": "Barrierefreies Bad"},
            {"value": "heizkoerper", "label": "Handtuchheizkörper"},
            {"value": "rohr-erneuern", "label": "Rohre erneuern"},
            {"value": "schimmel", "label": "Schimmel entfernen"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Was soll gemacht werden? {neighborhoods[0]} oder {neighborhoods[1]}? Altbau oder Neubau?",
    },
    "solarthermie": {
        "page_title": "Solarthermie {city} - Solarthermieanlage einbauen und Förderung",
        "meta_desc": "Solarthermie {city}: Solarthermieanlage einbauen und Förderung. Kostenlos bis zu 3 Angebote von Fachbetrieben in {city}. Unverbindlich.",
        "nav_active": "Solarthermie",
        "headline": "Solarthermie {city} - warmes Wasser von der Sonne",
        "sub": "Solarthermie nutzt die Sonne für warmes Wasser - ohne große Geräte. Wir vermitteln Ihnen bis zu drei {city}er Fachbetriebe für Ihre Solarthermieanlage.",
        "benefits": [
            {"icon": "sun", "title": "Sonne nutzen", "text": "Die Sonne liefert in {city} genug Energie für warmes Wasser im Sommer. Im Winter unterstützt die Anlage Ihre Heizung."},
            {"icon": "shield", "title": "BAFA und KfW Förderung", "text": "Solarthermie wird gefördert. Unsere {city}er Betriebe helfen bei der Antragstellung."},
            {"icon": "flame", "title": "Heizungsunterstützung", "text": "Im Sommer deckt Solarthermie in {city} den Warmwasserbedarf. Im Winter unterstützt sie die Heizung."},
            {"icon": "check", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen. Wir leiten Ihre Anfrage an bis zu drei {city}er Fachbetriebe weiter."},
            {"icon": "pipe", "title": "Rohr-Verlegung", "text": "Wenn in {city} eine Solarthermieanlage installiert wird, müssen oft Rohre verlegt werden. Unsere Betriebe koordinieren das."},
            {"icon": "star", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "sun", "title": "Solarthermie für WW", "desc": "Die Solarthermieanlage für {city} deckt im Sommer den Großteil des Warmwasserbedarfs. Effizient und umweltfreundlich.", "tag": "Warmwasser"},
            {"icon": "flame", "title": "Heizungsunterstützung", "desc": "In {city} lohnt sich Solarthermie besonders in Kombination mit einer Wärmepumpe oder Gasheizung.", "tag": "Heizung"},
            {"icon": "expand", "title": " Kombination mit PV", "desc": "Wer in {city} eine Photovoltaik-Anlage hat, kann die Solarthermie damit kombinieren. Unsere Betriebe beraten dazu.", "tag": "PV"},
            {"icon": "settings", "title": "Speicher einbauen", "desc": "Ein Solarthermiespeicher ist in {city} wichtig, um die Wärme vom Tag für die Nacht zu speichern.", "tag": "Speicher"},
            {"icon": "pipe", "title": "Rohrleitung verlegen", "desc": "Wenn in {city} die Rohre für die Solarthermie verlegt werden müssen, macht das unsere {city}er Betriebe mit."},
            {"icon": "check", "title": "Wartung", "desc": "Regelmäßige Wartung hält Ihre Solarthermieanlage in {city} in Schuss. Unsere Betriebe bieten Wartungsverträge.", "tag": "Wartung"},
        ],
        "faq": None,
        "form_options": [
            {"value": "solar-ww", "label": "Solarthermie für Warmwasser"},
            {"value": "solar-heizung", "label": "Solarthermie für Heizungsunterstützung"},
            {"value": "kombination-pv", "label": "Kombination mit Photovoltaik"},
            {"value": "speicher", "label": "Solarthermiespeicher"},
            {"value": "wartung", "label": "Wartung"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Welche Solaranlage haben Sie? {neighborhoods[0]} oder {neighborhoods[1]}? Bj. wann?",
    },
}

# =============================================================================
# ICONS (SVG paths) - heating/sanitary themed
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
    "bath": '<path d="M4 12h16a2 2 0 012 2v4a2 2 0 01-2 2H4a2 2 0 01-2-2v-4a2 2 0 012-2z" stroke="#fff" stroke-width="2" stroke-linecap="round"/><path d="M6 12V5a2 2 0 012-2h3v2.25L8.25 8H6v4z" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><line x1="6" y1="9" x2="6" y2="12" stroke="#fff" stroke-width="2" stroke-linecap="round"/>',
    "thermometer": '<path d="M14 14.76V3.5a2.5 2.5 0 00-5 0v11.26a4.5 4.5 0 105 0z" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
    "pipe": '<path d="M4 4v5h.582a1 1 0 00.707-.293l6.414-6.414a1 1 0 01.707-.293h3.172a1 1 0 01.707.293l6.414 6.414a1 1 0 00.707.293H20v5" stroke="#fff" stroke-width="2" stroke-linecap="round"/><path d="M4 14v-3a3 3 0 013-3h5" stroke="#fff" stroke-width="2" stroke-linecap="round"/><path d="M16 14v-3a3 3 0 013-3h5" stroke="#fff" stroke-width="2" stroke-linecap="round"/>',
    "settings": '<circle cx="12" cy="12" r="3" stroke="#fff" stroke-width="2"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-2 2 2 2 0 01-2-2v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83 0 2 2 0 010-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 01-2-2 2 2 0 012-2h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 010-2.83 2 2 0 012.83 0l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 012-2 2 2 0 012 2v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 0 2 2 0 010 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 012 2 2 2 0 01-2 2h-.09a1.65 1.65 0 00-1.51 1z" stroke="#fff" stroke-width="2"/>',
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
    reviews = city_data["reviews"]
    faq = city_data["faq"]

    neighborhoods_str = ", ".join(neighborhoods)

    def preformat(text):
        text = text.replace("{neighborhoods[-1]}", neighborhoods[-1])
        for i, n in enumerate(neighborhoods):
            text = text.replace(f"{{neighborhoods[{i}]}}", n)
        return text

    # Replace placeholders in service data
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

    # Benefits
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

    # Services
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
        <div class="service-card">
          <div class="service-card__icon">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none">{icon_path}</svg>
          </div>
          <h3>{title}</h3>
          <p>{desc}</p>
          <span class="service-card__tag">{tag}</span>
        </div>'''

    # Reviews
    reviews_html = ""
    for r in reviews:
        reviews_html += f'''
        <div class="review-card">
          <p class="review__text">"{r["text"]}"</p>
          <div class="review__meta">- {r["name"]}, <strong>{r["city"]}</strong>, {r["service"]}</div>
        </div>'''

    # FAQ
    faq_html = ""
    for item in faq:
        faq_html += f'''
        <details class="faq-item">
          <summary>{item["q"]}</summary>
          <p>{item["a"]}</p>
        </details>'''

    # Form options
    form_options_html = ""
    for opt in service_data["form_options"]:
        form_options_html += f'<option value="{opt["value"]}">{opt["label"]}</option>'

    # Footer Stadtteile links (use first 6 neighborhoods)
    footer_stadtteile = ""
    for n in neighborhoods[:6]:
        href = f"/{service_id}/{city_id}/"
        footer_stadtteile += f'<a href="{href}">{n}</a>'

    # Footer Leistungen links
    footer_leistungen = ""
    other_services = [k for k in SERVICES.keys() if k != service_id]
    for sid in other_services[:5]:
        footer_leistungen += f'<a href="/bad/{sid}/{city_id}/">{SERVICES[sid]["nav_active"]}</a>'

    form_placeholder = service_data.get("form_placeholder_plz", "{plz_short}").replace("{plz_short}", plz_short)
    form_message_placeholder = preformat(service_data.get("form_message_placeholder", "")).format(
        city=city_name, neighborhoods=neighborhoods, architecture=architecture,
        neighborhoods_str=neighborhoods_str, plz_short=plz_short
    )

    html = f'''<!DOCTYPE html>
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

  <!-- Header -->
  <header class="header">
    <div class="container header__inner">
      <a href="/" class="logo">hausbau<span class="logo-accent">.pro</span></a>
      <nav class="nav">
        <a href="/#so-funktionierts" class="nav__link">So funktioniert's</a>
        <a href="/#services" class="nav__link">Leistungen</a>
        <a href="/bad/blog/" class="nav__link">Blog</a>
        <a href="/#faq" class="nav__link">FAQ</a>
        <a href="#angebot" class="btn btn--header">Kostenlos anfragen</a>
      </nav>
      <button class="nav-toggle" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- Hero -->
  <section class="hero">
    <div class="container hero__inner">
      <div class="hero__text">
        <h1 class="hero__headline">
          {headline}
        </h1>
        <p class="hero__sub">
          {sub}
        </p>
        <a href="#angebot" class="btn btn--hero btn--shadow">
          Jetzt Angebot anfordern
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
        <div class="hero__trust">
          <span>✓ Kostenlos</span>
          <span>✓ Unverbindlich</span>
          <span>✓ {city_name}er Betriebe</span>
        </div>
      </div>
      <div class="hero__visual">
        <div class="hero__card">
          <div class="card-icon">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none"><path d="M12 22c-4.97 0-9-2.69-9-6 0-3 3-5 5-8 1.5-2.14 3-4.36 3-6 0 0 2 2 5 2 2.5 0 5-2 5-2 1.82 0 3 1 3 2 0 1.64 1.5 3.86 1.5 3.86s1.5 1 1.5 4c0 3.31-4.03 6-9 6z" stroke="#fff" stroke-width="2"/></svg>
          </div>
          <p class="card-label">Ihr Projekt in {city_name}</p>
          <div class="card-check">✓ Anfrage einreichen</div>
          <div class="card-check card-check--active">✓ 3 Angebote aus {city_name}</div>
          <div class="card-check">✓ In Ruhe vergleichen</div>
          <div class="card-badge">PLZ {plz}</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Benefits -->
  <section class="section section--gray" id="vorteile">
    <div class="container">
      <h2 class="section__title">Darum über uns</h2>
      <div class="benefits-grid">
        {benefits_html}
      </div>
    </div>
  </section>

  <!-- Steps -->
  <section class="section" id="so-funktionierts">
    <div class="container">
      <h2 class="section__title">So funktioniert's</h2>
      <div class="steps">
        <div class="step">
          <div class="step__num">1</div>
          <h3>Formular ausfüllen</h3>
          <p>Sie sagen uns, was Sie brauchen - Heizung, Wärmepumpe, Klimaanlage oder Sanitär. PLZ {plz_short} genügt.</p>
        </div>
        <div class="step-arrow">→</div>
        <div class="step">
          <div class="step__num">2</div>
          <h3>Wir leiten weiter</h3>
          <p>Ihre Anfrage geht an bis zu drei Betriebe aus {city_name} und Umgebung. Die melden sich dann direkt bei Ihnen mit einem Angebot.</p>
        </div>
        <div class="step-arrow">→</div>
        <div class="step">
          <div class="step__num">3</div>
          <h3>Angebote vergleichen</h3>
          <p>Sie entscheiden in Ruhe, welchen Betrieb Sie beauftragen. Kein Druck, kein Verkaufsgespräch.</p>
        </div>
      </div>
      <div class="steps-cta">
        <a href="#angebot" class="btn btn--primary">Jetzt Angebot anfordern</a>
      </div>
    </div>
  </section>

  <!-- Services -->
  <section class="section section--dark" id="services">
    <div class="container">
      <h2 class="section__title section__title--light">Was wir vermitteln</h2>
      <div class="services-grid">
        {services_html}
      </div>
    </div>
  </section>

  <!-- Reviews -->
  <section class="section" id="bewertungen">
    <div class="container">
      <h2 class="section__title">{city_name}er Kunden über uns</h2>
      <div class="reviews">
        {reviews_html}
      </div>
    </div>
  </section>

  <!-- Lead Form -->
  <section class="section section--form" id="angebot">
    <div class="container">
      <div class="form-wrapper">
        <div class="form-header">
          <h2>{service_data["nav_active"]} in {city_name}: Kostenlos Angebot anfordern</h2>
          <p>Eine Anfrage - bis zu drei Betriebe aus {city_name} melden sich mit ihrem Angebot.</p>
        </div>
        <form class="form" action="https://formspree.io/YOUR_FORM_ID" method="POST">
          <input type="hidden" name="_subject" value="Anfrage {service_data["nav_active"]} {city_name}">
          <div class="form__group">
            <label for="name">Ihr Name</label>
            <input type="text" id="name" name="name" required placeholder="Max Mustermann">
          </div>
          <div class="form__group">
            <label for="phone">Telefon (für Rückfragen)</label>
            <input type="tel" id="phone" name="phone" required placeholder="+49 123 456789">
          </div>
          <div class="form__group">
            <label for="plz">PLZ</label>
            <input type="text" id="plz" name="plz" required placeholder="{form_placeholder}" value="{plz_short}">
          </div>
          <div class="form__group">
            <label for="service">Was brauchen Sie?</label>
            <select id="service" name="service" required>
              <option value="">Bitte auswählen</option>
              {form_options_html}
            </select>
          </div>
          <div class="form__group form__group--full">
            <label for="message">Ihre Nachricht (optional)</label>
            <textarea id="message" name="message" rows="4" placeholder="{form_message_placeholder}"></textarea>
          </div>
          <div class="form__group form__group--full">
            <label class="checkbox-label">
              <input type="checkbox" name="consent" required>
              <span>Ich stimme der Verarbeitung meiner Daten gemäß der Datenschutzerklärung zu.</span>
            </label>
          </div>
          <button type="submit" class="btn btn--primary btn--full">Kostenlos Angebot anfordern</button>
        </form>
        <p class="form__note">✓ Kostenlos & unverbindlich &bull; Keine Verpflichtung &bull; Ihre Daten werden nicht weitergegeben</p>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section" id="faq">
    <div class="container">
      <h2 class="section__title">Häufige Fragen</h2>
      <div class="faq">
        {faq_html}
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__col">
          <a href="/" class="logo">hausbau<span class="logo-accent">.pro</span></a>
          <p>Lead-Generierung für Handwerker in Deutschland. Kostenlos für Sie - die Betriebe tragen die Vermittlungskosten.</p>
        </div>
        <div class="footer__col">
          <h4>Leistungen</h4>
          {footer_leistungen}
        </div>
        <div class="footer__col">
          <h4>Stadtteile</h4>
          {footer_stadtteile}
        </div>
        <div class="footer__col">
          <h4>Rechtliches</h4>
          <a href="/impressum/">Impressum</a>
          <a href="/datenschutz/">Datenschutz</a>
          <a href="/agb/">AGB</a>
        </div>
      </div>
      <div class="footer__bottom">
        <p>&copy; 2024 hausbau.pro - Alle Rechte vorbehalten.</p>
      </div>
    </div>
  </footer>

  <script src="/js/main.js"></script>
</body>
</html>'''

    return html


def main():
    service_ids = ["waermepumpe", "heizungsbau", "sanitaer", "klimaanlage", "badsanierung", "solarthermie"]
    city_ids = ["berlin", "muenchen", "hamburg", "koeln", "stuttgart", "dortmund", "frankfurt", "hannover",
                "duesseldorf", "leipzig", "bremen", "nuernberg", "mannheim", "freiburg"]

    for service_id in service_ids:
        service_data = SERVICES[service_id]
        for city_id in city_ids:
            city_data = CITIES[city_id]
            content = generate_page(service_id, city_id, city_data, service_data)
            path = f"bad/{service_id}/{city_id}/index.html"
            os.makedirs(f"bad/{service_id}/{city_id}", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Generated: {path}")


if __name__ == "__main__":
    main()