#!/usr/bin/env python3
"""
Generate all service/city pages using the rich dachdecker/muenchen layout.
6 services × 8 cities = 48 HTML pages.
Run: python gen_service_pages.py
"""

import os

# =============================================================================
# CITY DATA (shared across all services)
# =============================================================================

CITIES = {
    "muenchen": {
        "name": "München",
        "region": "Bayern",
        "plz": "80331 bis 81929",
        "plz_short": "80331",
        "neighborhoods": ["Altstadt", "Schwabing", "Maxvorstadt", "Bogenhausen", "Pasing", "Neuhausen", "Giesing", "Moosach"],
        "architecture": "Steile Satteldächer mit Biberschwanz, Flachdächer in den Neubaugebieten, historische Mansarddächer in der Altstadt",
        "famous": "Oktoberfest, BMW, Allianz Arena, Marienplatz",
        "dachdecker_page": "/dach/dachdecker/muenchen/",
        "reviews": [
            {"text": "Unser Satteldach in Schwabing war in die Jahre gekommen. Über hausbau.pro drei Angebote bekommen - alle aus München. Den Betrieb aus Bogenhausen genommen. Die Arbeit war erstklassig.", "name": "Ursula K.", "city": "München-Schwabing", "service": "Dachsanierung 2025"},
            {"text": "Flachdach auf dem Reihenhaus in Pasing war undicht. Noch am selben Tag kam jemand vom Betrieb aus Pasing vorbei, hat provisorisch abgedichtet und zwei Tage später das Angebot geschickt. Sehr schneller Service.", "name": "Florian M.", "city": "München-Pasing", "service": "Flachdach-Reparatur 2025"},
            {"text": "Dachgeschoss ausbauen ließ für das Kinderzimmer. Anfrage über die Seite gestellt, drei Angebote bekommen, den Betrieb aus Sendling genommen. Preis war fair und die Arbeit sauber.", "name": "Simone R.", "city": "München-Giesing", "service": "Dachausbau 2024"},
        ],
        "faq": [
            {"q": "Welche Münchner Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, Lehel, Maxvorstadt, Schwabing, Neuhausen, Giesing, Sendling, Pasing, Bogenhausen, Moosach, Milbertshofen und alle weiteren. Sagen Sie uns Ihre PLZ - wir leiten an den nächstgelegenen Betrieb weiter."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Münchner Betriebe melden sich innerhalb von 24 Stunden. Wenn Sie es eilig haben, schreiben Sie das ins Formular - manche können am selben oder nächsten Tag zu einer Besichtigung kommen."},
            {"q": "Was kostet eine Dachsanierung in München?", "a": "München ist nicht billig - dementsprechend liegen die Kosten etwas höher als im Bundesdurchschnitt. Ein mittleres Steildach liegt typischerweise zwischen 10.000 und 28.000 Euro. Fördermittel von der KfW und der LfA Bayern helfen. Deshalb lohnt sich der Vergleich erst recht."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Die Angebote kommen unverbindlich. Wenn nichts dabei ist, gehen Sie woanders hin. Keinerlei Druck, keine Verpflichtung."},
            {"q": "Wie funktioniert das mit der PLZ?", "a": "Wir leiten Ihre Anfrage zuerst an Betriebe aus Ihrer PLZ-Region weiter. Wenn sich nicht genug melden, schalten wir auf das erweiterte Umfeld: Freising, Dachau, Starnberg, Germering."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Kein Verkauf, keine Weitergabe an Dritte ohne Ihre Einwilligung."},
        ],
    },
    "koeln": {
        "name": "Köln",
        "region": "Nordrhein-Westfalen",
        "plz": "50667 bis 51149",
        "plz_short": "50667",
        "neighborhoods": ["Innenstadt", "Ehrenfeld", "Nippes", "Mülheim", "Lindenthal", "Rodenkirchen", "Porz", "Deutz"],
        "architecture": "Satteldächer in den Altbauquartieren, Flachdächer in Porz und Chorweiler, Schieferdächer im Rheinland",
        "famous": "Kölner Dom, Karneval, Rhein, RTL",
        "dachdecker_page": "/dach/dachdecker/koeln/",
        "reviews": [
            {"text": "Unser Satteldach in Ehrenfeld war nach 40 Jahren fällig. Über hausbau.pro drei Angebote bekommen, den Betrieb aus Lindenthal genommen. Saubere Arbeit, fairer Preis.", "name": "Thomas B.", "city": "Köln-Ehrenfeld", "service": "Dachsanierung 2025"},
            {"text": "Flachdach auf dem Mehrfamilienhaus in Mülheim war undicht. Noch am selben Tag kam jemand vom Betrieb aus Porz vorbei und hat provisorisch abgedichtet. Am nächsten Tag kam das Angebot.", "name": "Sandra K.", "city": "Köln-Mülheim", "service": "Flachdach-Reparatur 2025"},
            {"text": "Wir wollten das Dachgeschoss ausbauen lassen, seit Jahren schon. Über die Seite Anfrage gestellt, drei Angebote bekommen - wir haben uns für den Betrieb aus Nippes entschieden. War die richtige Wahl.", "name": "Marco L.", "city": "Köln-Innenstadt", "service": "Dachausbau 2024"},
        ],
        "faq": [
            {"q": "Welche Kölner Stadtteile werden abgedeckt?", "a": "Unsere Partnerbetriebe arbeiten in ganz Köln: Ehrenfeld, Nippes, Mülheim, Lindenthal, Rodenkirchen, Porz, Deutz, Chorweiler, Kalk und alle weiteren Stadtteile."},
            {"q": "Wie schnell meldet sich ein Dachdecker?", "a": "Die meisten Kölner Betriebe melden sich innerhalb von 24 Stunden. Wenn Sie es eilig haben, vermerken Sie das im Formular."},
            {"q": "Was kostet eine Dachsanierung in Köln?", "a": "Das hängt stark von Größe, Zustand und Material ab. Ein mittleres Steildach in Köln liegt typischerweise zwischen 8.000 und 25.000 Euro. Drei Angebote einholen und vergleichen."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Sie erhalten die Angebote unverbindlich. Wenn keines passt, gehen Sie woanders hin - völlig in Ordnung."},
            {"q": "Sind die Betriebe aus Köln oder aus dem Umland?", "a": "Wir leiten Ihre Anfrage zuerst an Betriebe aus Köln weiter. Wenn sich nicht genug melden, schalten wir auf das erweiterte Umland: Leverkusen, Bergisch Gladbach, Bornheim."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote von Dachdeckern zu vermitteln. Sie werden nicht verkauft und nicht an Dritte weitergegeben."},
        ],
    },
    "hamburg": {
        "name": "Hamburg",
        "region": "Norddeutschland",
        "plz": "20095 bis 21149",
        "plz_short": "20095",
        "neighborhoods": ["Altstadt", "Neustadt", "HafenCity", "St. Pauli", "Altona", "Eppendorf", "Winterhude", "Barmbek"],
        "architecture": "Steile Satteldächer in den Altbauquartieren, Flachdächer am Hafen und in den Neubauvierteln, Reetdächer in Blankenese",
        "famous": "Hafen, Elbphilharmonie, Reeperbahn, Hamburger SV",
        "dachdecker_page": "/dach/dachdecker/hamburg/",
        "reviews": [
            {"text": "In Eppendorf haben wir ein altes Satteldach sanieren lassen. Über das Portal gleich zwei Angebote von Betrieben aus dem Viertel bekommen. Die Arbeit war gut.", "name": "Friedrich B.", "city": "Hamburg-Eppendorf", "service": "Dachsanierung 2025"},
            {"text": "Die HafenCity war neu für uns. Flachdach sanieren lassen war unkompliziert - Anfrage online, Angebote kamen schnell.", "name": "Nina T.", "city": "Hamburg-HafenCity", "service": "Flachdach 2025"},
            {"text": "Blankenese ist teuer, aber über das Portal haben wir einen fairen Preis für unser Reetdach gefunden.", "name": "Heike M.", "city": "Hamburg-Blankenese", "service": "Reetdach 2024"},
        ],
        "faq": [
            {"q": "Welche Hamburger Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, Neustadt, HafenCity, St. Pauli, Altona, Eppendorf, Winterhude, Barmbek, Bergedorf, Blankenese und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Hamburger Betriebe melden sich innerhalb von 24 Stunden. Auch am Wochenende sind wir erreichbar."},
            {"q": "Was kostet eine Dachsanierung in Hamburg?", "a": "Die Kosten hängen von Größe, Zustand und Material ab. Ein mittleres Steildach in Hamburg liegt zwischen 9.000 und 26.000 Euro. Drei Angebote vergleichen lohnt sich."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich. Keinerlei Druck."},
            {"q": "Was ist mit dem Hamburger Wetter?", "a": "Der Wind und die Feuchtigkeit sind Themen, die Hamburger Dachdecker kennen. Für die Region typische Witterungsbedingungen planen wir immer ein."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "stuttgart": {
        "name": "Stuttgart",
        "region": "Baden-Württemberg",
        "plz": "70173 bis 70599",
        "plz_short": "70173",
        "neighborhoods": ["Bad Cannstatt", "Feuerbach", "Vaihingen", "Degerloch", "Möhringen", "Sillenbuch", "Zuffenhausen", "Hedelfingen"],
        "architecture": "Steildächer mit Tonziegeln und Schiefer, Flachdächer auf den Fildern, Mansarddächer in Bad Cannstatt",
        "famous": "Mercedes-Benz, Porsche, Stuttgarter Weihnachtsmarkt",
        "dachdecker_page": "/dach/dachdecker/stuttgart/",
        "reviews": [
            {"text": "Unser Dach in Degerloch war nach dem Winter undicht. Drei Angebote geholt, Betrieb aus dem Süden genommen. Sauber gelaufen.", "name": "Monika W.", "city": "Stuttgart-Degerloch", "service": "Dachsanierung 2025"},
            {"text": "In Bad Cannstatt haben wir ein Halbwalmdach. Nicht jeder Dachdecker hat damit Erfahrung. Über hausbau.pro den richtigen gefunden.", "name": "Thomas K.", "city": "Stuttgart-Bad Cannstatt", "service": "Dachsanierung 2025"},
            {"text": "Flachdach in Vaihingen - dringend sanieren lassen. Noch am selben Tag hat sich ein Betrieb gemeldet.", "name": "Julia F.", "city": "Stuttgart-Vaihingen", "service": "Flachdach 2025"},
        ],
        "faq": [
            {"q": "Welche Stuttgarter Stadtbezirke werden abgedeckt?", "a": "Alle PLZ-Gebiete: 70173 bis 70199 (Mitte), 70372 bis 70376 (Bad Cannstatt), 70431 bis 70469 (Feuerbach, Zuffenhausen), 70563 bis 70599 (Vaihingen, Degerloch, Möhringen)."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Innerhalb von 24 Stunden. In Stuttgart sind die Betriebe auch in den Stadtbezirken gut erreichbar - oft melden sich mehrere am selben Tag."},
            {"q": "Was kostet eine Dachsanierung in Stuttgart?", "a": "Die Kosten liegen in Stuttgart etwas über dem Bundesdurchschnitt. Ein Steildach mittlerer Größe liegt zwischen 10.000 und 27.000 Euro. Förderung über L-Bank und KfW möglich."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich. Wenn keines passt, gehen Sie woanders hin."},
            {"q": "Stuttgart ist hügelig - spielt das eine Rolle?", "a": "Ja. Die Topografie Stuttgart ist einzigartig - und die Dachdecker hier kennen die Hanglagen, die Weinberge und die Innenstadt gleichermaßen. Das wird bei der Planung berücksichtigt."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur an die vermittelten Betriebe weitergegeben. Nicht an Dritte, nicht zu Werbezwecken."},
        ],
    },
    "dortmund": {
        "name": "Dortmund",
        "region": "Nordrhein-Westfalen",
        "plz": "44135 bis 44379",
        "plz_short": "44135",
        "neighborhoods": ["Innenstadt", "Kreuzviertel", "Nordstadt", "Hörde", "Hombruch", "Brackel", "Aplerbeck", "Barop"],
        "architecture": "Steildächer mit Schiefer und Ziegel, Flachdächer in den Neubaugebieten, Industriekultur-Dächer",
        "famous": "SIGNAL IDUNA PARK, Bier, Phoenix, Möller",
        "dachdecker_page": "/dach/dachdecker/dortmund/",
        "reviews": [
            {"text": "Unser Schieferdach in Hombruch war ein Projekt für sich. Über das Portal einen Betrieb gefunden, der sich damit auskennt.", "name": "Ursula K.", "city": "Dortmund-Hombruch", "service": "Dachsanierung 2025"},
            {"text": "In der Nordstadt ein altes Reihenhaus mit undichtem Dach. Drei Angebote bekommen, schnell repariert.", "name": "Jens P.", "city": "Dortmund-Nordstadt", "service": "Dachreparatur 2025"},
            {"text": "Für unseren Dachausbau in Hörde brauchten wir jemanden mit Erfahrung. Über hausbau.pro den richtigen gefunden.", "name": "Simone A.", "city": "Dortmund-Hörde", "service": "Dachausbau 2024"},
        ],
        "faq": [
            {"q": "Welche Dortmunder Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Innenstadt, Kreuzviertel, Nordstadt, Hörde, Hombruch, Brackel, Aplerbeck, Barop und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Dortmunder Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine Dachsanierung in Dortmund?", "a": "Die Kosten in Dortmund liegen im Bundesdurchschnitt. Ein mittleres Steildach liegt zwischen 8.000 und 22.000 Euro. Drei Angebote einholen und vergleichen."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Die Angebote sind unverbindlich. Keinerlei Verpflichtung."},
            {"q": "Dortmund hat viel Industriekultur - spielt das eine Rolle?", "a": "Bei älteren Gebäuden in der Innenstadt und am Hörder Platz kann das relevant sein. Unsere Betriebe kennen die lokalen Besonderheiten."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "duesseldorf": {
        "name": "Düsseldorf",
        "region": "Nordrhein-Westfalen",
        "plz": "40210 bis 40629",
        "plz_short": "40210",
        "neighborhoods": ["Altstadt", "Carlstadt", "Stadtmitte", "Pempelfort", "Düsseltal", "Oberkassel", "Niederkassel", "Derendorf"],
        "architecture": "Steildächer in den Villenvierteln, Flachdächer am Rhein, moderne Architektur in Oberkassel",
        "famous": "Altbier, Kö, Königsallee, Medienhafen, Rheinturm",
        "dachdecker_page": "/dach/dachdecker/duesseldorf/",
        "reviews": [
            {"text": "Unser Villendach in Oberkassel war ein großes Projekt. Über das Portal drei Angebote eingeholt, alle professionell.", "name": "Rolf H.", "city": "Düsseldorf-Oberkassel", "service": "Dachsanierung 2025"},
            {"text": "Flachdach in Derendorf - nach 30 Jahren war eine Sanierung fällig. Schnell ging das über hausbau.pro.", "name": "Birgit S.", "city": "Düsseldorf-Derendorf", "service": "Flachdach 2025"},
            {"text": "Die Altstadt hat enge Gassen und wenig Platz. Unsere Betriebe in Düsseldorf kennen das.", "name": "Dieter M.", "city": "Düsseldorf-Altstadt", "service": "Dachreparatur 2024"},
        ],
        "faq": [
            {"q": "Welche Düsseldorfer Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, Carlstadt, Stadtmitte, Pempelfort, Düsseltal, Oberkassel, Niederkassel, Derendorf und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Düsseldorfer Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine Dachsanierung in Düsseldorf?", "a": "Düsseldorf liegt im oberen Bereich des Bundesdurchschnitts. Ein mittleres Steildach liegt zwischen 9.000 und 24.000 Euro. Drei Angebote vergleichen lohnt sich."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich. Keinerlei Druck."},
            {"q": "Die Kö und die Rheinufer - spielt das eine Rolle?", "a": "Die Rheinlage und die teils alte Bausubstanz in den Villenvierteln erfordern Erfahrung. Unsere Düsseldorfer Betriebe kennen die lokalen Gegebenheiten."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "leipzig": {
        "name": "Leipzig",
        "region": "Sachsen",
        "plz": "04107 bis 04357",
        "plz_short": "04107",
        "neighborhoods": ["Innenstadt", "Zentrum", "Plagwitz", "Lindenau", "Connewitz", "Stötteritz", "Gohlis", "Schleussig"],
        "architecture": "Gründerzeit-Satteldächer, Industriekultur-Flächen, moderne Stadthäuser mit Flachdächern",
        "famous": "Bach, Gewandhaus, Spassgarde, Ausstellungszentrum",
        "dachdecker_page": "/dach/dachdecker/leipzig/",
        "reviews": [
            {"text": "Unser Gründerzeit-Satteldach in Connewitz war ein Abenteuer. Über das Portal aber den richtigen Betrieb gefunden.", "name": "Martina B.", "city": "Leipzig-Connewitz", "service": "Dachsanierung 2025"},
            {"text": "Plagwitz hat viele alte Hallen. Die Dachsanierung lief reibungslos - drei Angebote, schnelle Ausführung.", "name": "Frank S.", "city": "Leipzig-Plagwitz", "service": "Dachsanierung 2025"},
            {"text": "Für unseren Dachausbau in Lindenau brauchten wir jemanden, der weiß was er tut. Über hausbau.pro super vermittelt worden.", "name": "Andrea K.", "city": "Leipzig-Lindenau", "service": "Dachausbau 2024"},
        ],
        "faq": [
            {"q": "Welche Leipziger Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Innenstadt, Zentrum, Plagwitz, Lindenau, Connewitz, Stötteritz, Gohlis, Schleussig und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Leipziger Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine Dachsanierung in Leipzig?", "a": "Leipzig ist günstiger als die westdeutschen Großstädte. Ein mittleres Steildach liegt zwischen 7.000 und 20.000 Euro. Drei Angebote einholen lohnt sich."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Die Angebote sind unverbindlich. Keinerlei Verpflichtung."},
            {"q": "Leipzig wächst schnell - wie ist das bei der Vermittlung?", "a": "Leipzig boomt, und die Dachdecker haben alle Hände voll zu tun. Deshalb ist der Vergleich über uns besonders wertvoll - Sie finden trotzdem den passenden Betrieb."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "freiburg": {
        "name": "Freiburg",
        "region": "Baden-Württemberg",
        "plz": "79098 bis 79117",
        "plz_short": "79098",
        "neighborhoods": ["Altstadt", "Innenstadt", "Stühlinger", "Herdern", "Vauban", "Landwasser", "Haslach", "Opfingen"],
        "architecture": "Dächer mit alemannischem Charakter, Steildächer mit Schneelasten aus dem Schwarzwald, Solardächer in der Ökostadt",
        "famous": "Münster, Schwarzwald, Universitätsstadt, Vauban",
        "dachdecker_page": "/dach/dachdecker/freiburg/",
        "reviews": [
            {"text": "Vauban ist unser Viertel. Wir haben das Dach mit Solar gemacht - über hausbau.pro einen Betrieb gefunden, der beides kann.", "name": "Stefanie G.", "city": "Freiburg-Vauban", "service": "Dachsanierung 2025"},
            {"text": "In Herdern haben wir ein altes alemannisches Steildach. Drei Angebote eingeholt, alle waren gut.", "name": "Martin W.", "city": "Freiburg-Herdern", "service": "Dachsanierung 2025"},
            {"text": "Die Freiburger Innenstadt hat enge Gassen. Unsere Betriebe kennen das und planen dementsprechend.", "name": "Ute B.", "city": "Freiburg-Altstadt", "service": "Dachreparatur 2024"},
        ],
        "faq": [
            {"q": "Welche Freiburger Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, Innenstadt, Stühlinger, Herdern, Vauban, Landwasser, Haslach, Opfingen und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Freiburger Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine Dachsanierung in Freiburg?", "a": "Freiburg ist etwas teurer als der Durchschnitt in Baden-Württemberg. Ein mittleres Steildach liegt zwischen 9.000 und 23.000 Euro. Drei Angebote vergleichen lohnt sich."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich. Keinerlei Druck."},
            {"q": "Freiburg liegt am Schwarzwald - spielt die Schneelast eine Rolle?", "a": "Ja. Die Schneelastzone in Freiburg ist höher als im Flachland. Unsere Betriebe kennen die lokalen Werte und dimensionieren dementsprechend."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "berlin": {
        "name": "Berlin",
        "region": "Berlin",
        "plz": "10115 bis 14199",
        "plz_short": "10115",
        "neighborhoods": ["Mitte", "Prenzlauer Berg", "Kreuzberg", "Charlottenburg", "Neukölln", "Schöneberg", "Wedding", "Tempelhof"],
        "architecture": "Berlins Dachlandschaft ist extrem vielfältig - vom historischen Altbau mit Satteldächern in Prenzlauer Berg, über das distinctive Berliner Dach in Kreuzberg und Schöneberg, bis zu den Plattenbauten in Marzahn-Hellersdorf. In Mitte dominieren moderne Flachdächer, während das Westend mit villenartigen Steildächern punktet.",
        "famous": "Brandenburger Tor, Berliner Mauer, Techno, Berlinale, BVG, Alexanderplatz, Fernsehturm",
        "dachdecker_page": "/dach/dachdecker/berlin/",
        "reviews": [
            {"text": "Das Team kam pünktlich und hat unser Satteldach in Prenzlauer Berg komplett neu eingedeckt. Wir hatten vorher Undichtigkeiten an mehreren Stellen. Jetzt ist alles dicht, und die Jungs waren super sauber.", "name": "Thomas K.", "city": "Berlin-Prenzlauer Berg", "service": "Dachsanierung 2025"},
            {"text": "Wir haben eine Dachgaube in Kreuzberg anbauen lassen. Der Betrieb hat sich um alles gekümmert, von der Genehmigung bis zur Ausführung. Preis war fair, Qualität top.", "name": "Sabine M.", "city": "Berlin-Kreuzberg", "service": "Dachgaube 2024"},
            {"text": "Flachdach auf unserem Neubau in Tempelhof. Alles aus einer Hand, inklusive Dämmung. Die Beratung war ehrlich und nicht aufgedrängt.", "name": "Mike R.", "city": "Berlin-Tempelhof", "service": "Flachdach Neubau 2025"},
        ],
        "faq": [
            {"q": "Welche Berliner Bezirke werden abgedeckt?", "a": "Alle 12 Bezirke: Mitte, Prenzlauer Berg, Kreuzberg, Charlottenburg, Neukölln, Schöneberg, Wedding, Tempelhof, Friedrichshain, Pankow, Spandau und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Berliner Betriebe melden sich innerhalb von 24 Stunden. Für dringende Notfälle wie Sturmschäden sind wir besonders schnell."},
            {"q": "Was kostet eine Dachsanierung in Berlin?", "a": "Die Kosten in Berlin liegen je nach Bezirk und Zustand zwischen 8.000 und 35.000 Euro. Für ein typisches Altbaudach (120qm) liegen wir oft bei 15.000-22.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich. Keinerlei Druck, keine Verpflichtung."},
            {"q": "Gibt es Auflagen für Dacharbeiten in Berlin?", "a": "In Sanierungsgebieten wie Kreuzberg oder Prenzlauer Berg gibt es denkmalgeschützte Fassaden. Unsere Betriebe kennen die Vorschriften für jeden Bezirk."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte, kein Spam."},
        ],
    },
    "frankfurt": {
        "name": "Frankfurt am Main",
        "region": "Hessen",
        "plz": "60306 bis 60599",
        "plz_short": "60311",
        "neighborhoods": ["Innenstadt", "Sachsenhausen", "Westend", "Bornheim", "Nordend", "Ostend", "Bockenheim", "Bahnofsviertel"],
        "architecture": "Frankfurts Skyline ist geprägt von Hochhäusern mit modernen Flachdächern im Bankenviertel, während die Altbauquartiere wie Sachsenhausen und das Nordend klassische Satteldächer und Walmdächer aufweisen. Das Westend verbindet Gründerzeitvillen mit aufwendigen Steildächern.",
        "famous": "Römer, Commerzbank Tower, Goethe-Haus, Messe, Flughafen, Main, Skyline, Apfelweinkultur",
        "dachdecker_page": "/dach/dachdecker/frankfurt/",
        "reviews": [
            {"text": "Unser Reihenmittelhaus in Bornheim hatte ein undichtes Satteldach. Der Betrieb aus dem Umland hat schnell reagiert, fair kalkuliert und sauber gearbeitet. Nur 3 Tage bis alles fertig war.", "name": "Julia S.", "city": "Frankfurt-Bornheim", "service": "Dachreparatur 2025"},
            {"text": "Ich habe mir drei Angebote eingeholt und mich für einen Betrieb aus dem Netzwerk entschieden. Die Dachsanierung in Sachsenhausen war professionell, inklusive Dämmung nach EnEV.", "name": "Andreas W.", "city": "Frankfurt-Sachsenhausen", "service": "Dachsanierung 2024"},
            {"text": "Wir brauchten kurzfristig jemanden nach dem Sturm. Am nächsten Tag war ein Team da und hat das Flachdach provisorisch gesichert. Top Service!", "name": "Claudia B.", "city": "Frankfurt-Bockenheim", "service": "Notdach nach Sturm 2025"},
        ],
        "faq": [
            {"q": "Welche Frankfurter Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Innenstadt, Sachsenhausen, Westend, Bornheim, Nordend, Ostend, Bockenheim, Bahnhofsviertel und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Frankfurter Betriebe melden sich innerhalb von 24 Stunden. Drei Angebote bekommen Sie in der Regel innerhalb von 3-5 Werktagen."},
            {"q": "Was kostet eine Dachsanierung in Frankfurt?", "a": "Für ein typisches Reihenhaus in Frankfurt (80-120 qm) liegen die Kosten bei 12.000 bis 25.000 Euro. Drei Angebote vergleichen lohnt sich."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich. Keinerlei Druck."},
            {"q": "Gibt es Auflagen für das Westend?", "a": "Im Westend gelten strenge Gestaltungssatzungen wegen des Denkmalschutzes. Unsere Partnerbetriebe kennen die Frankfurter Vorschriften."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "nuernberg": {
        "name": "Nürnberg",
        "region": "Bayern",
        "plz": "90317 bis 90491",
        "plz_short": "90317",
        "neighborhoods": ["Altstadt", "St. Lorenz", "St. Sebald", "Gostenhof", "Bärenschanze", "St. Leonhard", "Steinbühl", "Glockenhof"],
        "architecture": "Nürnbergs Altstadt ist berühmt für ihre Fachwerkhäuser mit steilen Satteldächern und die markante Kaiserburg. Die modernen Stadtteile wie Glockenhof und Steinbühl zeigen eine Mischung aus Altbauten mit Satteldächern und neueren Flachdachbauten. Die Stadt wurde nach dem Krieg sorgfältig wiederaufgebaut.",
        "famous": "Kaiserburg, Christkindlesmarkt, Albrecht Dürer, Nürnberger Rostbratwurst, Dokumentationszentrum, Spielwarenmesse",
        "dachdecker_page": "/dach/dachdecker/nuernberg/",
        "reviews": [
            {"text": "Die Fachwerkfassade und das Steildach unseres Hauses in der Altstadt waren in keinem guten Zustand. Der Betrieb hat sich umfassend gekümmert, inklusive Abstimmung mit dem Denkmalschutz. Super Arbeit!", "name": "Monika H.", "city": "Nürnberg-Altstadt", "service": "Dachsanierung Fachwerkhaus 2025"},
            {"text": "Wir haben eine Photovoltaik-Anlage aufs Dach in St. Leonhard bringen lassen. Der Dachdecker hat die Montage sauber gemacht und alles erklärt.", "name": "Stefan B.", "city": "Nürnberg-St. Leonhard", "service": "Dach Photovoltaik 2024"},
            {"text": "Nach dem Starkregen letzte Woche hat sich herausgestellt, dass unser Satteldach in Gostenhof Undichtigkeiten hatte. Innerhalb von 24 Stunden war jemand da und hat geflickt.", "name": "Petra K.", "city": "Nürnberg-Gostenhof", "service": "Dachreparatur 2025"},
        ],
        "faq": [
            {"q": "Welche Nürnberger Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Altstadt, St. Lorenz, St. Sebald, Gostenhof, Bärenschanze, St. Leonhard, Steinbühl, Glockenhof und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Nürnberger Betriebe melden sich innerhalb von 24 Stunden."},
            {"q": "Was kostet eine Dachsanierung in Nürnberg?", "a": "Die Kosten in Nürnberg liegen im bayrischen Durchschnitt. Ein mittleres Steildach liegt zwischen 9.000 und 24.000 Euro."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich. Keinerlei Verpflichtung."},
            {"q": "Gibt es Auflagen für die Altstadt?", "a": "Unsere Nürnberger Partner kennen die strengen Auflagen des Denkmalschutzes in der Altstadt und übernehmen die Abstimmung."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "hannover": {
        "name": "Hannover",
        "region": "Niedersachsen",
        "plz": "30159 bis 30659",
        "plz_short": "30159",
        "neighborhoods": ["Mitte", "List", "Vahrenwald", "Döhren", "Linden", "Herrenhausen", "Oststadt", "Bothfeld"],
        "architecture": "Hannovers Stadtbild zeigt eine Mischung aus Backsteingotik in der Altstadt, Gründerzeitbauten mit Satteldächern in List und Vahrenwald, sowie moderne Architektur rund um den Maschsee. Viele Dächer in Linden und Döhren sind als Steildächer erhalten.",
        "famous": "Maschsee, Herrenhäuser Gärten, Neues Rathaus, Marktkirche, Expo-Gelände, Zoo Hannover, Leineschloss",
        "dachdecker_page": "/dach/dachdecker/hannover/",
        "reviews": [
            {"text": "Unser Reihenendhaus in List hatte ein älteres Satteldach mit div. Problemen. Der Dachdecker aus Hannover hat einen fairen Preis gemacht und das ganze in 4 Tagen neu gemacht. Inklusive Dämmung. Sehr zufrieden.", "name": "Nina T.", "city": "Hannover-List", "service": "Dachkomplettsanierung 2025"},
            {"text": "Wir haben eine Dachgaube in Döhren anbauen lassen. Der Betrieb war zuverlässig, hat sich an den Zeitplan gehalten und sauber gearbeitet. Das Ergebnis sieht gut aus.", "name": "Frank D.", "city": "Hannover-Döhren", "service": "Dachgaube Anbau 2024"},
            {"text": "Nach dem Sturm letzte Woche hat uns schnell jemand geholfen. Unser Flachdach in Bothfeld war beschädigt. Die Notabdichtung war schnell gemacht, und die endgültige Reparatur kam auch zügig.", "name": "Sandra J.", "city": "Hannover-Bothfeld", "service": "Flachdach Reparatur 2025"},
        ],
        "faq": [
            {"q": "Welche Hannoverschen Stadtteile werden abgedeckt?", "a": "Alle 51 Stadtteile: von Mitte über List, Vahrenwald und Linden bis Bothfeld, Misburg und Burg. Auch das Umland wie Laatzen, Langenhagen und Garbsen."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Sie erhalten innerhalb von 24 Stunden einen Rückruf und innerhalb von 3-5 Werktagen drei Vergleichsangebote."},
            {"q": "Was kostet eine Dachsanierung in Hannover?", "a": "Für ein typisches hannoversches Reihenhaus mit Satteldach (ca. 100 qm) liegen die Kosten bei 10.000 bis 20.000 Euro inklusive Dämmung."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich. Keinerlei Druck."},
            {"q": "Gibt es Fördermittel für Dachsanierung?", "a": "Die Region Hannover und das Land Niedersachsen bieten Förderprogramme für energetische Sanierungen. Unsere Partner helfen bei der Antragstellung."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "bremen": {
        "name": "Bremen",
        "region": "Bremen",
        "plz": "28195 bis 28779",
        "plz_short": "28195",
        "neighborhoods": ["Mitte", "Neustadt", "Schwachhausen", "Horn-Lehe", "Borgfeld", "Gröpelingen", "Huchting", "Vegesack"],
        "architecture": "Bremens Stadtbild ist geprägt von Backsteingotik und Weserrenaissance, sichtbar am Rathaus und den Giebelhäusern am Marktplatz. Die Straßenzüge in Schwachhausen und Borgfeld zeigen großbürgerliche Villen mit steilen Satteldächern, während die Neustadt gemischte Bebauung mit Sattel- und Flachdächern aufweist.",
        "famous": "Rathaus, Roland, Stadtmusikanten, Weser, Schlachte, Überseestadt, Beck's, Airbus",
        "dachdecker_page": "/dach/dachdecker/bremen/",
        "reviews": [
            {"text": "Wir leben in Schwachhausen in einem älteren Haus mit Satteldach. Die Ziegel waren porös und es gab Undichtigkeiten. Der Bremer Betrieb hat das Dach komplett neu eingedeckt, inklusive Dämmung. Faire Preise, gute Arbeit.", "name": "Heike M.", "city": "Bremen-Schwachhausen", "service": "Dachsanierung 2025"},
            {"text": "Unser Reihenhaus in der Neustadt brauchte eine neue Dachabdichtung. Der Betrieb kam schnell, hat einen fairen Preis gemacht und war mit der Arbeit in 2 Tagen fertig. Sauber und zuverlässig.", "name": "Ralf S.", "city": "Bremen-Neustadt", "service": "Dachabdichtung 2024"},
            {"text": "Ich wollte eine Dachbegrünung für unser Flachdach in Gröpelingen. Die Beratung war kompetent, das Angebot transparent. Das Ergebnis ist richtig schön geworden.", "name": "Anke P.", "city": "Bremen-Gröpelingen", "service": "Dachbegrünung 2025"},
        ],
        "faq": [
            {"q": "Welche Bremer Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Mitte, Neustadt, Schwachhausen, Horn-Lehe, Borgfeld, Gröpelingen, Huchting, Vegesack und alle weiteren. Auch Bremerhaven."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Die meisten Bremer Betriebe melden sich innerhalb von 24 Stunden. Drei Vergleichsangebote bekommen Sie in der Regel innerhalb von 3-5 Werktagen."},
            {"q": "Was kostet eine Dachsanierung in Bremen?", "a": "Für ein typisches Bremer Reihenhaus mit Satteldach (ca. 90-110 qm) liegen die Kosten bei 9.000 bis 18.000 Euro inklusive Dämmung."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich. Keinerlei Druck."},
            {"q": "Gibt es Auflagen für die Bremer Altstadt?", "a": "Der Marktplatz und die umliegende Altstadt stehen unter Denkmalschutz. Unsere Bremer Partner kennen die Vorschriften."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
    "mannheim": {
        "name": "Mannheim",
        "region": "Baden-Württemberg",
        "plz": "68159 bis 68309",
        "plz_short": "68159",
        "neighborhoods": ["Innenstadt", "Jungbusch", "Neckarstadt-Ost", "Käfertal", "Lindenhof", "Oststadt", "Schwetzingerstadt", "Waldhof"],
        "architecture": "Mannheims Innenstadt ist als Quadratestadt mit dem typischen Rastergrundriss angelegt. Das Barockschloss Mannheim ist das architektonische Highlight. Die Neckarstadt zeigt eine Mischung aus Altbauten mit Satteldächern und modernen Flachdachbauten. Lindenhof und Oststadt sind geprägt von Gründerzeitbauten.",
        "famous": "Barockschloss, Quadratestadt, BASF, SAP Arena, Jungbusch, Rheinufer, Wasserturm, Vogelstang",
        "dachdecker_page": "/dach/dachdecker/mannheim/",
        "reviews": [
            {"text": "Unser Haus in der Neckarstadt-Ost hatte ein altes Satteldach mit vielen Schäden. Der Mannheimer Betrieb hat schnell reagiert und das Dach komplett neu gemacht. Die Beratung war ehrlich, der Preis fair. Sehr zu empfehlen.", "name": "Diana K.", "city": "Mannheim-Neckarstadt-Ost", "service": "Dachsanierung 2025"},
            {"text": "Wir haben eine Photovoltaik-Anlage auf unser Flachdach in Käfertal montieren lassen. Der Dachdecker hat sich mit dem Solarteur abgestimmt und sauber gearbeitet. Alles aus einer Hand.", "name": "Thomas W.", "city": "Mannheim-Käfertal", "service": "Photovoltaik Aufdach 2024"},
            {"text": "Nach dem Starkregen mussten wir schnell jemanden haben. Unser Satteldach in der Oststadt hatte eine Undichtigkeit. Innerhalb von Stunden war ein Team da und hat das Problem behoben.", "name": "Sabine R.", "city": "Mannheim-Oststadt", "service": "Dach-Notdienst 2025"},
        ],
        "faq": [
            {"q": "Welche Mannheimer Stadtteile werden abgedeckt?", "a": "Alle Stadtteile: Innenstadt, Jungbusch, Neckarstadt-Ost, Käfertal, Lindenhof, Oststadt, Schwetzingerstadt, Waldhof und alle weiteren."},
            {"q": "Wie schnell meldet sich ein Betrieb?", "a": "Sie erhalten innerhalb von 24 Stunden einen Rückruf und innerhalb von 3-5 Werktagen drei Vergleichsangebote von geprüften Dachdeckern."},
            {"q": "Was kostet eine Dachsanierung in Mannheim?", "a": "Für ein typisches Mannheimer Reihenhaus (ca. 100 qm Dachfläche) liegen die Kosten bei 10.000 bis 20.000 Euro inklusive Dämmung."},
            {"q": "Muss ich mich für ein Angebot entscheiden?", "a": "Nein. Alle Angebote sind unverbindlich. Keinerlei Druck."},
            {"q": "Gibt es in Mannheim Auflagen für Dacharbeiten?", "a": "Das Barockschloss und die umliegenden Quadrate stehen unter Denkmalschutz. Auch in der Oststadt und in Lindenhof gibt es denkmalgeschützte Bausubstanz."},
            {"q": "Was passiert mit meinen Daten?", "a": "Ihre Daten werden nur dazu genutzt, Ihnen Angebote zu vermitteln. Keine Weitergabe an Dritte."},
        ],
    },
}


# =============================================================================
# SERVICE DATA
# =============================================================================

SERVICES = {
    "dachdecker": {
        "page_title": "Dachdecker {city} - Kostenlose Angebote von Dachdeckern in {city}",
        "meta_desc": "Dachdecker in {city}: Eine Anfrage, bis zu drei Angebote von Dachdeckern aus {city}. Kostenlos und unverbindlich.",
        "nav_active": "Dachdecker",
        "headline": "Dachdecker in {city} - <span class='text-accent'>regional, schnell, geprüft</span>",
        "sub": "Ob Altbau in {neighborhoods[0]}, Reihenhaus in {neighborhoods[2]} oder Mehrfamilienhaus in {neighborhoods[4]}. Eine Anfrage an uns - und bis zu drei Dachdecker aus {city} melden sich mit ihrem Angebot.",
        "benefits": [
            {"icon": "location", "title": "Vor Ort in jedem Viertel", "text": "{neighborhoods_str} - die {city}er Betriebe kennen ihre Viertel und sind schnell bei Ihnen."},
            {"icon": "home", "title": "{city}er Bauformen kennenlernen", "text": "{architecture} Lokale Dachdecker wissen, womit sie es zu tun haben."},
            {"icon": "clock", "title": "Schnelle Hilfe, auch am Wochenende", "text": "Undichte Stelle nach dem letzten Gewitter? Die {city}er Betriebe reagieren schnell."},
            {"icon": "shield", "title": "Eine Anfrage, drei Angebote", "text": "Sie müssen nicht selbst drei Betriebe heraussuchen und anrufen. Wir leiten Ihre Anfrage an bis zu drei geprüfte {city}er Dachdecker weiter."},
            {"icon": "check", "title": "Preise vergleichen ohne Aufwand", "text": "Drei Angebote, direkt von {city}er Betrieben. Sofort sehen Sie, wer was anbietet und zu welchem Preis."},
            {"icon": "star", "title": "Völlig kostenlos für Sie", "text": "Keine Gebühren, keine Provision für Sie. Die Dachdecker-Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "home", "title": "Dachdecker / Neueindeckung", "desc": "Ziegeldächer, Schiefer, Kupfer, Titanzink. In {city} typisch: {architecture}", "tag": "Steildach"},
            {"icon": "flat", "title": "Flachdach", "desc": "Bitumen, FPO, PVC, Begrünung. Flachdächer sind in {city} bei gewerblichen Bauten und in den Neubauvierteln verbreitet.", "tag": "Flachdach"},
            {"icon": "layer", "title": "Dachsanierung", "desc": "Komplette Erneuerung inklusive Dämmung nach GEG. Für {city}er Altbauten besonders relevant.", "tag": "Sanierung"},
            {"icon": "expand", "title": "Dachausbau", "desc": "Wohnraum unter dem Dach gewinnen - in Zeiten hoher Mieten in {city} eine beliebte Alternative.", "tag": "Ausbau"},
            {"icon": "window", "title": "Dachfenster & Velux", "desc": "Velux, Dachflächenfenster, Lichtkuppeln. In den {city}er Altbauten oft die einzige Möglichkeit für Tageslicht.", "tag": "Velux"},
            {"icon": "frame", "title": "Zimmerei & Holzbau", "desc": "Dachstuhl sanieren, Carport, Terrassenüberdachung. Für den Garten oder die neue Überdachung in {city}.", "tag": "Holzbau"},
        ],
        "faq": None,  # use city faq
        "form_options": [
            {"value": "dachdecker", "label": "Dachdecker / Neueindeckung"},
            {"value": "dachsanierung", "label": "Dachsanierung"},
            {"value": "dachausbau", "label": "Dachausbau"},
            {"value": "flachdach", "label": "Flachdach"},
            {"value": "dachfenster", "label": "Dachfenster / Velux"},
            {"value": "zimmerei", "label": "Zimmerei / Holzbau"},
            {"value": "notdienst", "label": "Notdienst / Reparatur"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "z.B. Reihenhaus, Satteldach, Bj. 1970er, PLZ {plz_short} {city} - Sanierung oder Neubau?",
    },
    "dachsanierung": {
        "page_title": "Dachsanierung {city} - Kosten, Ablauf und Förderung",
        "meta_desc": "Dachsanierung {city}: Sanierung, Neueindeckung und Wärmedämmung. Kostenlos bis zu 3 Angebote von Dachdeckern in {city}. Unverbindlich.",
        "nav_active": "Dachsanierung",
        "headline": "Dachsanierung {city} - das Dach wieder auf Vordermann bringen",
        "sub": "{city} ist eine Stadt mit anspruchsvollen Dächern - {architecture}. Wir vermitteln Ihnen bis zu drei {city}er Dachdecker für die Sanierung.",
        "benefits": [
            {"icon": "location", "title": "Vor Ort in jedem Viertel", "text": "Von {neighborhoods[0]} bis {neighborhoods[-1]} - unsere {city}er Partner kennen die lokalen Gegebenheiten."},
            {"icon": "home", "title": "Sanierung nach GEG", "text": "Das GEG schreibt bei einer Sanierung mindestens 140 mm Dämmung vor. Unsere {city}er Betriebe kennen die Anforderungen."},
            {"icon": "clock", "title": "Schnelle Hilfe bei Undichtigkeiten", "text": "Wenn das Dach undicht ist, muss es schnell gehen. Unsere {city}er Betriebe reagieren zügig."},
            {"icon": "shield", "title": "Fördermittel nutzen", "text": "KfW und regionale Förderbanken unterstützen energetische Sanierung. Unsere {city}er Betriebe beraten Sie dazu."},
            {"icon": "check", "title": "Komplette Sanierung aus einer Hand", "text": "Dämmung, Neueindeckung, Gauben, Anschlüsse - unsere {city}er Betriebe koordinieren alles."},
            {"icon": "star", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Dachdecker-Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "home", "title": "Steildach - komplette Sanierung", "desc": "Satteldächer in {city}: {neighborhoods[0]}, {neighborhoods[2]}, {neighborhoods[4]} haben anspruchsvolle Dächer. Eine Sanierung erhält den Dachstuhl.", "tag": "Steildach"},
            {"icon": "flat", "title": "Flachdach - Sanierung", "desc": "Nach 20 bis 30 Jahren ist ein Flachdach reif für Sanierung. Bitumen, FPO oder PIB - unsere {city}er Betriebe kennen die Materialien.", "tag": "Flachdach"},
            {"icon": "layer", "title": "Dämmung nachrüsten", "desc": "Das GEG schreibt mindestens 140 mm vor. Aufsparrendämmung, Zwischensparrendämmung - je nach Zustand des Daches gibt es verschiedene Wege.", "tag": "Dämmung"},
            {"icon": "expand", "title": "Gauben und Dachfenster", "desc": "Undichte Anschlüsse an Gauben und Dachfenstern sind häufige Ursachen für Feuchtigkeit. Ein guter {city}er Betrieb findet und behebt sie.", "tag": "Gaube"},
            {"icon": "window", "title": "Schornstein und Anschlüsse", "desc": "Schornsteinkopf, Wandanschlüsse, Fensterbank - diese Details entscheiden über die Lebensdauer der Sanierung.", "tag": "Anschlüsse"},
            {"icon": "frame", "title": "Schneelast und Sturmschäden", "desc": "{city} hat seine eigenen Witterungsbedingungen. Unsere Betriebe kennen die lokalen Werte und dimensionieren dementsprechend.", "tag": "Sturm"},
        ],
        "faq": None,
        "form_options": [
            {"value": "steildach-saniert", "label": "Steildach sanieren"},
            {"value": "flachdach-saniert", "label": "Flachdach sanieren"},
            {"value": "daemmung", "label": "Dämmung nachrüsten"},
            {"value": "komplett", "label": "Komplette Neueindeckung"},
            {"value": "sturmschaden", "label": "Sturmschaden"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Welche Dachfläche? Welche Probleme? {neighborhoods[0]} oder {neighborhoods[1]}? Gründerzeit?",
    },
    "zimmermann": {
        "page_title": "Zimmermann {city} - Carport, Gaube, Dachstuhl und mehr",
        "meta_desc": "Zimmermann {city}: Carport, Gaube, Dachstuhl, Holzterrasse. Kostenlos bis zu 3 Angebote von Zimmerleuten in {city}. Unverbindlich.",
        "nav_active": "Zimmermann",
        "headline": "Zimmermann {city} - Carport, Gaube, Dachstuhl und mehr",
        "sub": "Alles aus Holz - vom Carport bis zum Dachstuhl. Wir vermitteln Ihnen bis zu drei {city}er Zimmerleute für Ihr Projekt.",
        "benefits": [
            {"icon": "location", "title": "Vor Ort in jedem Viertel", "text": "Von {neighborhoods[0]} bis {neighborhoods[-1]} - unsere {city}er Zimmerleute kennen ihre Viertel."},
            {"icon": "home", "title": "Dachstuhl sanieren und verstärken", "text": "Der Dachstuhl ist das Herzstück des Daches. In {city}er Altbauten oft noch original erhalten - eine Sanierung lohnt sich."},
            {"icon": "clock", "title": "Schnelle Hilfe bei Sturmschäden", "text": "Wenn der Sturm etwas beschädigt hat, sind unsere {city}er Zimmerleute schnell zur Stelle."},
            {"icon": "shield", "title": "Carport und Holzterrasse", "text": "Platzsparend und flexibel - Holzkonstruktionen passen sich dem Stil des Hauses an. In {city} besonders beliebt."},
            {"icon": "check", "title": "Gaube für mehr Raum", "text": "Eine Gaube bringt Licht und Raum unter das Dach. In {city} eine verbreitete Lösung beim Dachausbau."},
            {"icon": "star", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Zimmerleute tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "home", "title": "Carport bauen", "desc": "Ein Carport aus Holz ist in {city} die günstigere Alternative zur Garage. Für jedes Grundstück und jeden Stil - platzsparend und flexibel.", "tag": "Carport"},
            {"icon": "flat", "title": "Gaube bauen", "desc": "Eine Gaube bringt Licht und Raum unter das Dach. Spitzgaube, Trapezgaube oder Rundgaube - für jedes Dach die passende Form.", "tag": "Gaube"},
            {"icon": "layer", "title": "Dachstuhl - neu oder reparieren", "desc": "Der Dachstuhl ist das Herzstück des Daches. Wenn er marode ist, muss ein Zimmermann ran. In {city}er Altbauten oft noch erhalten.", "tag": "Dachstuhl"},
            {"icon": "expand", "title": "Holzterrasse bauen", "desc": "Eine Holzterrasse erweitert den Wohnraum nach draußen. In {city}, wo die Sommer lang und warm sind, fast ein Muss.", "tag": "Terrasse"},
            {"icon": "window", "title": "Anbauten und Aufstockungen", "desc": "Wer in {city} Platz braucht, baut in die Höhe. Aufstockung auf dem Flachdach oder Anbau - genehmigungspflichtig, aber machbar.", "tag": "Anbau"},
            {"icon": "frame", "title": "DachCheck", "desc": "Sie wissen nicht, ob Ihr Dach noch in Ordnung ist? Ein DachCheck zeigt, was zu tun ist. Für {city}er Altbauten alle 5 bis 10 Jahre sinnvoll.", "tag": "Check"},
        ],
        "faq": None,
        "form_options": [
            {"value": "carport", "label": "Carport bauen"},
            {"value": "gaube", "label": "Gaube bauen"},
            {"value": "dachstuhl", "label": "Dachstuhl reparieren / neu"},
            {"value": "terrasse", "label": "Holzterrasse bauen"},
            {"value": "anbau", "label": "Anbau oder Aufstockung"},
            {"value": "dachcheck", "label": "DachCheck"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Was genau soll gebaut oder repariert werden? Welche Größe ungefähr? {neighborhoods[0]} oder Villenviertel?",
    },
    "dachausbau": {
        "page_title": "Dachausbau {city} - Speicher ausbauen, Dachboden zur Wohnung machen",
        "meta_desc": "Dachausbau {city}: Aus dem Speicher neuen Wohnraum schaffen. Kostenlos bis zu 3 Angebote von Handwerkern in {city}. Unverbindlich.",
        "nav_active": "Dachausbau",
        "headline": "Dachausbau {city} - aus dem Speicher wird Wohnraum",
        "sub": "In {city} sind die Immobilienpreise hoch - der Dachboden ist oft die letzte ungenutzte Reserve. Wir vermitteln Ihnen bis zu drei {city}er Fachbetriebe für Ihren Dachausbau.",
        "benefits": [
            {"icon": "location", "title": "Vor Ort in jedem Viertel", "text": "Von {neighborhoods[0]} bis {neighborhoods[-1]} - unsere {city}er Betriebe kennen die lokalen Baustile."},
            {"icon": "home", "title": "Wohnraum gewinnen", "text": "Mehr Quadratmeter ohne Umzug - in {city} besonders wertvoll. Das Dachgeschoss ausbauen und neuem Wohnraum schaffen."},
            {"icon": "clock", "title": "Schnelle Planung und Umsetzung", "text": "Die {city}er Betriebe haben Erfahrung mit allen gängigen Dachformen. Die Planung geht schnell."},
            {"icon": "shield", "title": "GEG-konforme Dämmung", "text": "Der Dachausbau muss auch die Dämmung nach GEG berücksichtigen. Unsere {city}er Betriebe wissen, was gefordert ist."},
            {"icon": "check", "title": "Gauben und Dachfenster", "text": "Mehr Licht und Stehfläche - Gauben und Dachfenster machen den Dachausbau erst richtig wohnlich."},
            {"icon": "star", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "home", "title": "Penthouse-Wohnung", "desc": "In {city} ist der ausgebaute Dachboden das begehrteste Objekt im Haus. Mit Gauben, Dachterrasse und Panoramablick - eine Wertanlage."},
            {"icon": "flat", "title": "Einliegerwohnung", "desc": "Der Dachboden zur Mietwohnung - in {city}, wo die Mieten stark gestiegen sind, rechtfertigt das die Investition besonders gut."},
            {"icon": "layer", "title": "Homeoffice oder Studio", "desc": "Tageslicht und Ruhe - was will man mehr für konzentriertes Arbeiten? Ein Dachstudio in {city} ist besonders gefragt."},
            {"icon": "expand", "title": "Maisonette", "desc": "Wenn die Treppe ins Dachgeschoss verlegt wird, entsteht eine zweigeschossige Wohnung. In {city}er Altbauten besonders beliebt."},
            {"icon": "window", "title": "Gauben einbauen", "desc": "Stehfläche und Licht - eine Gaube macht den Dachausbau erst richtig nutzbar. In {city} eine verbreitete Lösung."},
            {"icon": "frame", "title": "Dachstuhl verstärken", "desc": "Bevor der Ausbau losgeht, muss der Dachstuhl gegebenenfalls verstärkt werden. Unsere {city}er Zimmerleute prüfen das."},
        ],
        "faq": None,
        "form_options": [
            {"value": "kompletter-ausbau", "label": "Kompletter Dachausbau"},
            {"value": "gaube", "label": "Gaube einbauen"},
            {"value": "dachfenster", "label": "Dachfenster einbauen"},
            {"value": "dachstuhl-praed", "label": "Dachstuhl verstärken"},
            {"value": "einliegerwohnung", "label": "Einliegerwohnung"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Was soll entstehen? Welche Größe? {neighborhoods[0]} oder {neighborhoods[1]}? Gründerzeit?",
    },
    "dachfenster": {
        "page_title": "Dachfenster {city} - Einbau, Austausch und Gaube",
        "meta_desc": "Dachfenster {city}: Einbau, Austausch und Gaube. Kostenlos bis zu 3 Angebote von Fachbetrieben in {city}. Unverbindlich.",
        "nav_active": "Dachfenster",
        "headline": "Dachfenster {city} - Einbau, Austausch und Gaube",
        "sub": "Mehr Licht unterm Dach: Wir vermitteln Ihnen bis zu drei {city}er Fachbetriebe für Ihren Dachfenster-Einbau.",
        "benefits": [
            {"icon": "location", "title": "Vor Ort in jedem Viertel", "text": "Von {neighborhoods[0]} bis {neighborhoods[-1]} - unsere {city}er Betriebe kennen die lokalen Dächer."},
            {"icon": "home", "title": "Mehr Licht und Wohnqualität", "text": "Ein Dachfenster macht aus dem dunklen Dachboden einen Raum, in dem man arbeiten oder schlafen will."},
            {"icon": "clock", "title": "Schnelle Hilfe bei Undichtigkeiten", "text": "Alte Dachfenster sind oft undicht. Unsere {city}er Betriebe tauschen sie schnell aus."},
            {"icon": "shield", "title": "Velux, Roto, Fakro", "text": "Alle gängigen Marken werden eingebaut. Die {city}er Betriebe beraten Sie zur richtigen Wahl."},
            {"icon": "check", "title": "Gaube als Alternative", "text": "Wer mehr Licht und mehr Raum will, setzt eine Gaube drauf. In {city} eine verbreitete Lösung."},
            {"icon": "star", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "home", "title": "Dachfenster - Einbau", "desc": "Velux, Roto, Fakro - Einbau in alle gängigen Dachformen. In {city}er Altbauten besonders beliebt."},
            {"icon": "flat", "title": "Dachfenster - Austausch", "desc": "Die alten Fenster in {city}er Altbauten stammen oft aus den 70ern und 80ern. Undicht, schlecht gedämmt. Ein Austausch spart Heizkosten."},
            {"icon": "layer", "title": "Gaube mit Dachfenster", "desc": "Wer mehr Licht und mehr Raum will, setzt eine Gaube drauf. In {city} eine verbreitete Lösung."},
            {"icon": "expand", "title": "Lichtkuppeln", "desc": "Licht unterm Flachdach - mit Lichtkuppeln. Auch als RWA-Lichtkuppeln für den Brandschutz."},
            {"icon": "window", "title": "Eindeckrahmen erneuern", "desc": "Der Eindeckrahmen ist das Puzzlestück zwischen Fenster und Dach. Wenn er marode ist, muss er erneuert werden."},
            {"icon": "frame", "title": "Notdienst bei Undichtigkeiten", "desc": "Wenn ein altes Dachfenster undicht ist und es reinregnet, kommen unsere {city}er Betriebe auch kurzfristig."},
        ],
        "faq": None,
        "form_options": [
            {"value": "neueinbau", "label": "Neues Dachfenster einbauen"},
            {"value": "austausch", "label": "Altes Fenster austauschen"},
            {"value": "gaube", "label": "Gaube einbauen"},
            {"value": "lichtkuppel", "label": "Lichtkuppel einbauen"},
            {"value": "eindeckrahmen", "label": "Eindeckrahmen erneuern"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Welche Art von Dachfenster? {neighborhoods[0]} oder {neighborhoods[1]}? Altbau oder Neubau?",
    },
    "flachdach": {
        "page_title": "Flachdach {city} - Sanierung, Neubau und Begrünung",
        "meta_desc": "Flachdach {city}: Sanierung, Neubau und Begrünung. Kostenlos bis zu 3 Angebote von Dachdeckern in {city}. Unverbindlich.",
        "nav_active": "Flachdach",
        "headline": "Flachdach {city} - Sanierung, Neubau und Begrünung",
        "sub": "Ein Flachdach in {city} ist besonders beansprucht - {architecture}. Wir vermitteln Ihnen bis zu drei {city}er Dachdecker für Ihr Flachdach-Projekt.",
        "benefits": [
            {"icon": "location", "title": "Vor Ort in jedem Viertel", "text": "Von {neighborhoods[0]} bis {neighborhoods[-1]} - unsere {city}er Betriebe kennen die lokalen Flachdächer."},
            {"icon": "home", "title": "Sanierung nach 20-30 Jahren", "text": "Nach 20 bis 30 Jahren ist ein Flachdach reif für Sanierung. Die Bitumenbahn ist porös, die Nähte sind undicht."},
            {"icon": "clock", "title": "Schnelle Hilfe bei Undichtigkeiten", "text": "Wenn es reinregnet, ist schnelles Handeln gefragt. Unsere {city}er Betriebe reagieren schnell."},
            {"icon": "shield", "title": "GEG-konforme Dämmung", "text": "Das GEG schreibt bei einer Sanierung mindestens 140 mm vor. Unsere {city}er Betriebe kennen die Anforderungen."},
            {"icon": "check", "title": "Begrünung möglich", "text": "Ein begrüntes Flachdach ist in {city} besonders beliebt. Die Stadt fördert das. Fragen Sie nach den Möglichkeiten."},
            {"icon": "star", "title": "Kostenlos für Sie", "text": "Keine Gebühren für Sie. Die Betriebe tragen die Vermittlungskosten."},
        ],
        "services": [
            {"icon": "home", "title": "Flachdach - Sanierung", "desc": "Nach 20 bis 30 Jahren ist ein Flachdach reif für Sanierung. Bitumen, FPO oder PIB - unsere {city}er Betriebe kennen die Materialien."},
            {"icon": "flat", "title": "Flachdach - Neubau", "desc": "Bei einem Anbau oder einer Aufstockung brauchen Sie ein neues Flachdach. In {city} ein häufiges Projekt."},
            {"icon": "layer", "title": "Flachdach - Begrünung", "desc": "Ein begrüntes Flachdach schafft Ausgleich, dämmt im Sommer und hält im Winter. In {city} besonders beliebt."},
            {"icon": "expand", "title": "Abdichtung", "desc": "Ob Bitumen, FPO oder PIB - wir vermitteln Ihnen einen {city}er Dachdecker, der die richtige Lösung findet."},
            {"icon": "window", "title": "Dämmung nachrüsten", "desc": "Ältere Flachdächer haben oft kaum Dämmung. Das GEG schreibt bei einer Sanierung mindestens 140 mm vor."},
            {"icon": "frame", "title": "Dachfenster im Flachdach", "desc": "Licht unterm Flachdach - mit Flachdachfenstern oder Lichtkuppeln. In {city} besonders in der Innenstadt wertvoll."},
        ],
        "faq": None,
        "form_options": [
            {"value": "sanierung", "label": "Flachdach sanieren"},
            {"value": "neubau", "label": "Flachdach neu bauen"},
            {"value": "begruenung", "label": "Begrünung"},
            {"value": "abdichtung", "label": "Abdichtung reparieren"},
            {"value": "daemmung", "label": "Dämmung nachrüsten"},
            {"value": "dachfenster-flach", "label": "Dachfenster / Lichtkuppel"},
            {"value": "sonstiges", "label": "Sonstiges"},
        ],
        "form_placeholder_plz": "{plz_short}",
        "form_message_placeholder": "Welche Art von Flachdach? Wie alt? {neighborhoods[0]} oder {neighborhoods[1]}?",
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
    "flat": '<rect x="2" y="8" width="20" height="13" rx="2" stroke="#fff" stroke-width="2"/><line x1="2" y1="13" x2="22" y2="13" stroke="#fff" stroke-width="2"/>',
    "layer": '<path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" stroke="#fff" stroke-width="2" stroke-linejoin="round"/>',
    "expand": '<polyline points="3 9 12 2 21 9 21 21 3 21 3 9" stroke="#fff" stroke-width="2" stroke-linejoin="round"/><rect x="9" y="14" width="6" height="7" stroke="#fff" stroke-width="2"/>',
    "window": '<rect x="3" y="1" width="18" height="18" rx="2" stroke="#fff" stroke-width="2"/><line x1="3" y1="10" x2="21" y2="10" stroke="#fff" stroke-width="2"/>',
    "frame": '<path d="M12 2L2 7v15h20V7L12 2z" stroke="#fff" stroke-width="2" stroke-linejoin="round"/><path d="M12 22V12M12 12L2 7M12 12l10-5" stroke="#fff" stroke-width="2"/>',
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
    dachdecker_page = city_data["dachdecker_page"]
    reviews = city_data["reviews"]
    faq = city_data["faq"]

    neighborhoods_str = ", ".join(neighborhoods)

    # Pre-format text strings that contain {neighborhoods[X]} before passing to .format()
    # Python's str.format() doesn't support list indexing like {neighborhoods[0]}, so we
    # replace those placeholders with precomputed neighborhood values first
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
        <div class="review">
          <div class="review__stars">★★★★★</div>
          <p>"{r["text"]}"</p>
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

    message_placeholder = service_data["form_message_placeholder"].format(
        city=city_name, neighborhoods=neighborhoods, architecture=architecture,
        neighborhoods_str=neighborhoods_str, plz_short=plz_short
    )

    # Footer links - Leistungen
    footer_leistungen = f'''
        <a href="/dach/dachsanierung/{city_id}/">Dachsanierung {city_name}</a>
        <a href="/dach/dachausbau/{city_id}/">Dachausbau {city_name}</a>
        <a href="/dach/dachfenster/{city_id}/">Dachfenster {city_name}</a>
        <a href="/dach/zimmermann/{city_id}/">Zimmermann {city_name}</a>
        <a href="/dach/flachdach/{city_id}/">Flachdach {city_name}</a>'''

    # Footer links - Stadtteile
    footer_stadtteile = "\n        ".join([f'<a href="/dach/dachdecker/{city_id}/">{n}</a>' for n in neighborhoods[:5]])

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

  <!-- Header -->
  <header class="header">
    <div class="container header__inner">
      <a href="/" class="logo">hausbau<span class="logo-accent">.pro</span></a>
      <nav class="nav">
        <a href="/#so-funktionierts" class="nav__link">So funktioniert's</a>
        <a href="/#services" class="nav__link">Leistungen</a>
        <a href="/dach/blog/" class="nav__link">Blog</a>
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
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z" stroke="#fff" stroke-width="2" stroke-linejoin="round"/><polyline points="9,22 9,12 15,12 15,22" stroke="#fff" stroke-width="2" stroke-linejoin="round"/></svg>
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
      <h2 class="section__title">Warum ein Betrieb aus {city_name}?</h2>
      <div class="benefits">
        {benefits_html}
      </div>
    </div>
  </section>

  <!-- Steps -->
  <section class="section" id="so-funktionierts">
    <div class="container">
      <h2 class="section__title">So kommen Sie zu Ihrem Angebot</h2>
      <div class="steps">
        <div class="step">
          <div class="step__num">1</div>
          <h3>Formular ausfüllen</h3>
          <p>Kurz gesagt: Was für ein Dach, wo in {city_name}, und wann soll es losgehen. Dauert zwei Minuten.</p>
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
      <h2 class="section__title section__title--light">Was unsere {city_name}er Partner anbieten</h2>
      <div class="services">
        {services_html}
      </div>
      <div class="services-cta">
        <a href="#angebot" class="btn btn--hero">Kostenlos Angebot anfordern</a>
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
          <p>Eine Anfrage - bis zu drei Angebote von Betrieben aus {city_name} und Umgebung. Keine Verpflichtung.</p>
          <div class="form-trust">
            <span>✓ Kostenlos</span>
            <span>✓ Unverbindlich</span>
            <span>✓ {city_name}er Betriebe</span>
          </div>
        </div>
        <form class="lead-form" id="leadForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
          <div class="form-row">
            <div class="form-group">
              <label for="name">Ihr Name *</label>
              <input type="text" id="name" name="name" required placeholder="Max Mustermann">
            </div>
            <div class="form-group">
              <label for="phone">Telefon *</label>
              <input type="tel" id="phone" name="phone" required placeholder="+49 170 123 4567">
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label for="plz">Postleitzahl in {city_name} *</label>
              <input type="text" id="plz" name="plz" required placeholder="{plz_short}" pattern="[0-9]{{5}}">
            </div>
            <div class="form-group">
              <label for="service">Gewünschte Leistung *</label>
              <select id="service" name="service" required>
                <option value="" disabled selected>Bitte wählen</option>
                {form_options_html}
              </select>
            </div>
          </div>
          <div class="form-group form-group--full">
            <label for="message">Beschreibung Ihres Projekts</label>
            <textarea id="message" name="message" rows="4" placeholder="{message_placeholder}"></textarea>
          </div>
          <div class="form-group form-group--full">
            <label for="timeline">Zeitraum</label>
            <select id="timeline" name="timeline">
              <option value="sofort">So schnell wie möglich</option>
              <option value="1-3monate">In 1 bis 3 Monaten</option>
              <option value="3-6monate">In 3 bis 6 Monaten</option>
              <option value="planung">Noch in Planung</option>
            </select>
          </div>
          <button type="submit" class="btn btn--form">
            Kostenloses Angebot anfordern
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
          <p class="form-legal">Mit dem Absenden stimmen Sie unserer <a href="#">Datenschutzerklärung</a> zu. Keine Weitergabe an Dritte ohne Ihre Einwilligung.</p>
          <div class="form-success" id="formSuccess">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M22 11.08V12a10 10 0 11-5.93-9.14" stroke="#22c55e" stroke-width="2"/><polyline points="22 4 12 14.01 9 11.01" stroke="#22c55e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <div>
              <strong>Anfrage erfolgreich!</strong><br>
              Sie erhalten in Kürze bis zu drei Angebote von Betrieben aus {city_name}.
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section section--gray" id="faq">
    <div class="container">
      <h2 class="section__title">Fragen zu {service_data["nav_active"]} in {city_name}</h2>
      <div class="faq">
        {faq_html}
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand">
        <span class="logo">hausbau<span class="logo-accent">.pro</span></span>
        <p>Kostenlose Vermittlung von geprüften Betrieben in {city_name} und ganz Deutschland.</p>
      </div>
      <div class="footer__links">
        <h4>Leistungen</h4>
        {footer_leistungen}
      </div>
      <div class="footer__links">
        <h4>Stadtteile</h4>
        {footer_stadtteile}
      </div>
      <div class="footer__links">
        <h4>Rechtliches</h4>
        <a href="#">Impressum</a>
        <a href="#">Datenschutz</a>
        <a href="#">AGB</a>
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
    service_ids = ["dachdecker", "dachsanierung", "zimmermann", "dachausbau", "dachfenster", "flachdach"]
    city_ids = ["muenchen", "koeln", "hamburg", "stuttgart", "dortmund", "duesseldorf", "leipzig", "freiburg",
                "berlin", "frankfurt", "nuernberg", "hannover", "bremen", "mannheim"]

    for service_id in service_ids:
        service_data = SERVICES[service_id]
        for city_id in city_ids:
            city_data = CITIES[city_id]
            content = generate_page(service_id, city_id, city_data, service_data)
            path = f"dach/{service_id}/{city_id}/index.html"
            os.makedirs(f"dach/{service_id}/{city_id}", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Generated: {path}")


if __name__ == "__main__":
    main()