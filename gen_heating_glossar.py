#!/usr/bin/env python3
"""Generate heating/sanitary branch glossary."""

TERMS = [
    {
        "id": "waermepumpe",
        "title": "Wärmepumpe - Was ist das und wie funktioniert sie?",
        "meta_desc": "Wärmepumpe erklärt: Funktionsweise, Typen (Luft, Sole, Erdwärme), Kosten, Förderung. Alles was Sie über Wärmepumpen wissen müssen.",
        "badge": "Heizung",
        "content": [
            {"h2": "Was ist eine Wärmepumpe?"},
            {"p": "Eine Wärmepumpe ist ein Heizsystem, das Wärme aus der Umgebung (Luft, Erde, Wasser) aufnimmt und für die Raumheizung nutzt. Sie funktioniert nach dem gleichen Prinzip wie ein Kühlschrank - nur umgekehrt. Während ein Kühlschrank seine Wärme an die Raumluft abgibt, entzieht die Wärmepumpe der Umwelt Wärme und gibt sie an das Heizsystem ab."},
            {"h2": "Welche Arten von Wärmepumpen gibt es?"},
            {"p": "Es gibt drei Haupttypen: Luft-Wärmepumpen holen die Wärme aus der Außenluft. Sie sind am günstigsten, aber bei niedrigen Temperaturen weniger effizient. Sole-Wärmepumpen nutzen die Erdwärme über Flächenkollektoren oder Erdsonden. Sie sind effizienter, aber teurer in der Installation. Wasser-Wärmepumpen nutzen Grundwasser oder Flusswasser - sehr effizient, aber nicht überall verfügbar."},
            {"h2": "Effizienz und Kosten"},
            {"p": "Die Effizienz einer Wärmepumpe wird durch die Jahresarbeitszahl (JAZ) ausgedrückt. Sie gibt an, wie viel Wärmeenergie pro eingesetzter Stromeinheit erzeugt wird. Eine JAZ von 3,5 bedeutet: Für 1 kWh Strom erhalten Sie 3,5 kWh Wärme. Die Anschaffungskosten liegen zwischen 15.000 und 45.000 Euro je nach Typ."},
            {"h2": "Lohnt sich eine Wärmepumpe?"},
            {"p": "Eine Wärmepumpe lohnt sich besonders in gut gedämmten Gebäuden mit einer Vorlauftemperatur unter 55 Grad. Das sind Neubauten und sanierte Altbauten. In schlecht gedämmten Gebäuden mit hohen Vorlauftemperaturen ist die Wärmepumpe oft unwirtschaftlich."}
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
            {"p": "Eine Fußbodenheizung ist ein Heizsystem, bei dem die Heizrohre unter dem Boden verlegt werden. Die Wärme wird gleichmäßig über die gesamte Fläche abgegeben. Das sorgt für einen hohen Komfort und gleichmäßige Temperaturen im Raum."},
            {"h2": "Vorteile der Fußbodenheizung"},
            {"p": "Die Vorteile: Hoher Komfort durch gleichmäßige Wärme, keine sichtbaren Heizkörper, gut geeignet für Wärmepumpen wegen der niedrigen Vorlauftemperatur, keine Staubaufwirbelung wie bei Konvektoren."},
            {"h2": "Nachteile und Kosten"},
            {"p": "Die Nachteile: Höhere Installationskosten als Heizkörper, langsame Reaktionszeit, nicht in allen Böden verlegbar. Die Kosten liegen bei 80 bis 140 Euro pro m² inklusive Installation."},
            {"h2": "Fußbodenheizung und Wärmepumpe"},
            {"p": "Die Fußbodenheizung ist der ideale Partner für Wärmepumpen. Sie arbeitet mit niedrigen Vorlauftemperaturen von 30 bis 45 Grad, was die Wärmepumpe effizienter macht. Eine Fußbodenheizung kann aber nicht in jedem Boden nachgerüstet werden - bei Estrich oder Fliesen ist die Installation möglich, bei Holzdielen oft nicht."}
        ],
        "related": ["waermepumpe", "thermostat", "heizkoerper"]
    },
    {
        "id": "durchlauferhitzer",
        "title": "Durchlauferhitzer - Dezentrale Warmwasserbereitung",
        "meta_desc": "Durchlauferhitzer: Kosten, Funktion, Vor- und Nachteile. Wann sich ein Durchlauferhitzer lohnt und welche Arten es gibt.",
        "badge": "Sanitär",
        "content": [
            {"h2": "Was ist ein Durchlauferhitzer?"},
            {"p": "Ein Durchlauferhitzer erhitzt das Wasser erst dann, wenn Sie es brauchen - also durchlaufend. Im Gegensatz zum Warmwasserspeicher hat er keinen Vorratstank. Das Wasser wird entweder durch Gas oder elektrisch erhitzt."},
            {"h2": "Arten von Durchlauferhitzern"},
            {"p": "Es gibt zwei Arten: Gas-Durchlauferhitzer sind effizient und können große Mengen warmes Wasser liefern. Sie eignen sich für Haushalte mit hohem Warmwasserverbrauch. Elektrische Durchlauferhitzer sind günstiger in der Anschaffung, aber deutlich teurer im Betrieb. Sie sind nur für kleine Mengen sinnvoll."},
            {"h2": "Kosten und Effizienz"},
            {"p": "Die Kosten für einen Gas-Durchlauferhitzer liegen bei 500 bis 1.500 Euro. Ein elektrischer Durchlauferhitzer kostet 200 bis 600 Euro. Die laufenden Kosten sind beim Gasgerät deutlich niedriger - ein elektrischer Durchlauferhitzer sollte nur für selten genutzte Zapfstellen verwendet werden."},
            {"h2": "Wann lohnt sich ein Durchlauferhitzer?"},
            {"p": "Ein Durchlauferhitzer lohnt sich, wenn Sie keine zentrale Warmwasserbereitung haben oder die Leitungswege zu lang sind. In einem Einfamilienhaus mit zentraler Heizung ist ein Warmwasserspeicher meistens die bessere Wahl."}
        ],
        "related": ["trinkwasser", "sanitaer-installation", "rohrleitungen"]
    },
    {
        "id": "gasheizung",
        "title": "Gasheizung - Der Klassiker unter den Heizsystemen",
        "meta_desc": "Gasheizung: Kosten, Funktion, Wirkungsgrad. Was Sie über Gasheizungen wissen müssen und wann sich ein Austausch lohnt.",
        "badge": "Heizung",
        "content": [
            {"h2": "Was ist eine Gasheizung?"},
            {"p": "Eine Gasheizung verbrennt Erdgas oder Flüssiggas, um Wasser zu erwärmen. Das warme Wasser wird dann für die Raumheizung und die Warmwasserbereitung genutzt. Gasheizungen sind weit verbreitet und gelten als zuverlässig."},
            {"h2": "Brennwerttechnik"},
            {"p": "Moderne Gasheizungen nutzen die Brennwerttechnik. Das bedeutet, sie nutzen nicht nur die Wärme der Flamme, sondern auch die Wärme aus den Abgasen. Das erhöht den Wirkungsgrad auf über 100 Prozent - bezogen auf den Heizwert des Gases. Eine Brennwertgasheizung ist deutlich effizienter als eine alte Niedertemperaturheizung."},
            {"h2": "Kosten und Lebensdauer"},
            {"p": "Eine neue Gas-Brennwertheizung kostet 8.000 bis 18.000 Euro inklusive Installation. Die Lebensdauer liegt bei 15 bis 20 Jahren. Nach dieser Zeit wird der Austausch meistens fällig, auch wenn die Heizung noch läuft - denn ab 20 Jahren steigt der Wartungsbedarf stark an."},
            {"h2": "Wann lohnt sich ein Austausch?"},
            {"p": "Ein Austausch lohnt sich, wenn Ihre Heizung älter als 15 Jahre ist oder wenn die Reparaturkosten hoch werden. Auch bei einer Sanierung, die den Heizbedarf senkt, kann eine neue effiziente Heizung sinnvoll sein. Ab 2024 sollten neue Heizungen zu 65 Prozent mit erneuerbaren Energien betrieben werden."}
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
            {"p": "Eine Brennwertheizung ist ein Heizsystem, das die Energie des Brennstoffs fast vollständig ausnutzt. Neben der Wärme der Flamme nutzt sie auch die Wärme aus den entstehenden Abgasen, indem sie den Wasserdampf darin kondensiert. Dadurch erreicht sie einen Wirkungsgrad von über 100 Prozent."},
            {"h2": "Brennwert bei Gas und Öl"},
            {"p": "Brennwerttechnik gibt es sowohl für Gas als auch für Öl. Die Kosten sind ähnlich, aber Gas hat den Vorteil, dass es bereits jetzt schon zu einem großen Teil aus erneuerbarem Methan (Bio-Methan) gemischt werden kann. Eine Öl-Brennwertheizung wird in Zukunft schwieriger zu betreiben sein."},
            {"h2": "Was bringt die Brennwerttechnik?"},
            {"p": "Im Vergleich zu einer alten Niedertemperaturheizung spart eine Brennwertheizung etwa 15 bis 30 Prozent Energie. Das bedeutet: Bei 2.000 Liter Öl pro Jahr sind das 300 bis 600 Liter Ersparnis. Bei Gas liegen die Ersparnisse bei etwa 10 bis 25 Prozent."},
            {"h2": "Kosten einer Brennwertheizung"},
            {"p": "Die Kosten für eine Gas-Brennwertheizung liegen bei 8.000 bis 18.000 Euro. Für Öl-Brennwert liegen sie etwas höher: 10.000 bis 20.000 Euro. Dazu kommen eventuelle Kosten für den Schornstein, wenn dieser für die Abgase umgebaut werden muss."}
        ],
        "related": ["gasheizung", "waermepumpe", "heizungssanierung"]
    },
    {
        "id": "klimaanlage",
        "title": "Klimaanlage - Kühlung für Wohnung und Büro",
        "meta_desc": "Klimaanlage: Kosten, Typen, Funktion. Split, Multi-Split, mobil - was für Ihr Zuhause oder Büro passt.",
        "badge": "Klima",
        "content": [
            {"h2": "Wie funktioniert eine Klimaanlage?"},
            {"p": "Eine Klimaanlage funktioniert nach dem Prinzip der Wärmepumpe. Sie entzieht der Raumluft Wärme und leitet sie nach außen ab. Das funktioniert über ein Kältemittel, das im Innengerät verdampft und im Außengerät wieder verflüssigt wird. Das Prinzip ist dasselbe wie bei einem Kühlschrank."},
            {"h2": "Arten von Klimaanlagen"},
            {"p": "Die Split-Klimaanlage hat ein Innengerät und ein Außengerät. Sie ist die häufigste Art und eignet sich für einzelne Räume. Eine Multi-Split-Anlage hat ein Außengerät und mehrere Innengeräte - ideal für Wohnungen oder ganze Stockwerke. Mobile Klimageräte sind weniger effizient und lauter, eignen sich aber für Übergangslösungen."},
            {"h2": "Kosten einer Klimaanlage"},
            {"p": "Eine Split-Klimaanlage kostet 2.500 bis 5.000 Euro inklusive Installation. Eine Multi-Split-Anlage mit drei Innengeräten liegt bei 8.000 bis 12.000 Euro. Die Betriebskosten liegen bei 150 bis 400 Euro pro Sommer je nach Nutzung."},
            {"h2": "Wann lohnt sich eine Klimaanlage?"},
            {"p": "Eine Klimaanlage lohnt sich, wenn die Räume im Sommer überhitzen und keine andere Kühlung möglich ist. In Dachgeschossen oder nach Süden ausgerichteten Wohnungen ist sie oft sinnvoll. In gut isolierten Neubauten mit Sonnenschutz ist sie seltener nötig."}
        ],
        "related": ["klimaanlage-wartung", "waermepumpe", "kuehldecke"]
    },
    {
        "id": "solarthermie",
        "title": "Solarthermie - Wärme von der Sonne",
        "meta_desc": "Solarthermie: Kosten, Nutzen, Förderung. Wie Sie mit Solarthermie warmes Wasser erzeugen und Ihre Heizung unterstützen.",
        "badge": "Energie",
        "content": [
            {"h2": "Was ist Solarthermie?"},
            {"p": "Solarthermie nutzt die Sonnenenergie, um Wasser zu erwärmen. Auf dem Dach werden Sonnenkollektoren montiert, die die Wärme des Sonnenlichts einfangen. Diese Wärme wird dann über einen Wärmetauscher an den Brauchwarmwasserspeicher oder die Heizung weitergegeben."},
            {"h2": "Vorteile der Solarthermie"},
            {"p": "Die Vorteile: kostenlose Energiequelle, reduziert Heizkosten im Sommer, kann Heizung im Winter unterstützen, umweltfreundlich, Lebensdauer 25 bis 30 Jahre. Im Sommer kann eine Solarthermieanlage den Großteil des Warmwasserbedarfs decken."},
            {"h2": "Kosten und Förderung"},
            {"p": "Die Kosten für eine Solarthermieanlage liegen bei 4.000 bis 8.000 Euro für reine Warmwasserbereitung. Für eine Anlage mit Heizungsunterstützung liegen sie bei 8.000 bis 14.000 Euro. Die BAFA fördert Solarthermie mit 25 Prozent der Kosten."},
            {"h2": "Solarthermie oder Photovoltaik?"},
            {"p": "Beide nutzen die Sonne, aber unterschiedlich. Solarthermie erzeugt Wärme, Photovoltaik erzeugt Strom. Solarthermie hat einen höheren Wirkungsgrad bei der Wärmegewinnung, Photovoltaik ist vielseitiger nutzbar. Für Warmwasser und Heizungsunterstützung ist Solarthermie oft die bessere Wahl."}
        ],
        "related": ["photovoltaik", "waermepumpe", "warmwasserspeicher"]
    },
    {
        "id": "heizkoerper",
        "title": "Heizkörper - Funktion und Auswahl",
        "meta_desc": "Heizkörper: Typen, Kosten, Effizienz. Welcher Heizkörper für welche Situation geeignet ist.",
        "badge": "Heizung",
        "content": [
            {"h2": "Arten von Heizkörpern"},
            {"p": "Es gibt viele verschiedene Heizkörpertypen: Flachheizkörper sind flach und modern, sie passen gut an Wände und haben eine große Wärmeabgabe. Badheizkörper sind speziell fürs Badezimmer konzipiert und haben oft Handtuchhalter. Fußbodenheizungen sind keine Heizkörper im klassischen Sinn, sondern ein Heizsystem im Boden. Altbau-Heizkörper sind oft aus Gusseisen und haben eine hohe Speichermasse."},
            {"h2": "Größe und Leistung"},
            {"p": "Die Leistung eines Heizkörpers wird in Watt angegeben und muss zum Raum passen. Für ein gut gedämmtes Zimmer mit 20 m² braucht man etwa 1.500 bis 2.000 Watt. Bei schlechter Dämmung oder großen Fenstern kann der Bedarf deutlich höher sein. Ein Heizungsfachmann kann die richtige Dimensionierung berechnen."},
            {"h2": "Kosten und Austausch"},
            {"p": "Die Kosten für einen neuen Flachheizkörper liegen bei 200 bis 500 Euro pro Stück. Dazu kommen die Installationskosten von 100 bis 300 Euro pro Heizkörper. Der Austausch aller Heizkörper in einem Einfamilienhaus kostet etwa 3.000 bis 8.000 Euro."},
            {"h2": "Heizkörper optimieren"},
            {"p": "Vor dem Austausch lohnt sich die Optimierung: Verkleidungen entfernen, hinter den Heizkörpern Reflektorfolie anbringen, regelmäßig entlüften. Diese Maßnahmen verbessern die Effizienz ohne große Kosten."}
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
            {"p": "Ein Thermostat misst die Raumtemperatur und regelt die Heizleistung entsprechend. Wenn die gewünschte Temperatur erreicht ist, drosselt das Thermostat die Heizung. Bei absinkender Temperatur wird wieder mehr geheizt. Moderne Thermostate können dies präzise und automatisch tun."},
            {"h2": "Arten von Thermostaten"},
            {"p": "Mechanische Thermostate sind einfach und günstig, aber nicht sehr präzise. Elektronische Thermostate sind genauer und haben timmer. Smarte Thermostate können per App gesteuert werden, lernen aus Ihrem Verhalten und integrieren sich in Smart-Home-Systeme. Die Kosten reichen von 10 Euro (mechanisch) bis 200 Euro (smart)."},
            {"h2": "Smarte Thermostate"},
            {"p": "Smarte Thermostate bieten viele Vorteile: Fernsteuerung per App, Zeitprogramme für jeden Raum, Erkennung von offenen Fenstern, Wettervorhersage-basierte Steuerung. Sie können die Heizkosten um 10 bis 20 Prozent senken. Bekannte Systeme sind tado°, Nest und Homematic."},
            {"h2": "Richtige Einstellung"},
            {"p": "Die optimale Raumtemperatur liegt bei 20 bis 22 Grad im Wohnbereich, 18 Grad im Schlafzimmer. Jedes Grad weniger spart etwa 6 Prozent Heizenergie. Ein smarter Thermostat hilft, diese Einstellungen automatisch einzuhalten."}
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
            {"p": "Die gängigsten Materialien für Heizungsrohre sind Kupfer, Stahl und Kunststoff. Kupferrohre sind langlebig und korrosionsbeständig, aber teurer. Stahlrohre (verzinkt) sind robust, können aber korrodieren. Kunststoffrohre (z.B. PE-X oder PB) sind günstig und korrosionsfrei, aber empfindlich gegen hohe Temperaturen."},
            {"h2": "Verlegung und Kosten"},
            {"p": "Heizungsrohre werden entweder aufputz (sichtbar) oder unterputz (verkleidet) verlegt. Die unterputz-Verlegung ist optisch besser, aber teurer und bei Reparaturen schwieriger. Die Kosten für Rohrleitungen liegen bei 25 bis 50 Euro pro Meter inklusive Verlegung."},
            {"h2": "Wann Rohre erneuern?"},
            {"p": "Rohre sollten erneuert werden, wenn sie undicht sind, wenn die Korrosion fortgeschritten ist oder wenn sie älter als 30 bis 40 Jahre sind. Bei einer Heizungssanierung ist es oft sinnvoll, auch die Rohre zu erneuern - besonders wenn sie Durchmesserprobleme geben könnte."},
            {"h2": "Dämmung der Rohre"},
            {"p": "Heizungsrohre sollten gedämmt werden, um Wärmeverluste zu vermeiden. Das betrifft besonders Rohre in unbeheizten Räumen wie Kellern oder Dachböden. Die Dämmung kostet wenig und spart viel Energie - sie amortisiert sich in der Regel innerhalb weniger Jahre."}
        ],
        "related": ["sanitaer-installation", "trinkwasser", "abwasser"]
    },
    {
        "id": "abwasser",
        "title": "Abwasser - Der Weg des Schmutzwassers",
        "meta_desc": "Abwasser: Systeme, Kosten, Wartung. Was Sie über die Abwasserentsorgung wissen müssen.",
        "badge": "Sanitär",
        "content": [
            {"h2": "Wie funktioniert die Abwasserentsorgung?"},
            {"p": "Das Abwasser aus Waschbecken, Duschen, Badewannen und Toiletten wird über ein Netzwerk von Rohren zu einer zentralen Kläranlage geleitet. In Deutschland ist das öffentliche Kanalnetz sehr gut ausgebaut. Das Wasser muss über Gefälle abfließen können - daher sind Abwasserrohre immer leicht geneigt."},
            {"h2": "Arten von Abwassersystemen"},
            {"p": "Es gibt zwei Hauptarten: Mischwasserkanalisation führt alle Abwässer (Schmutz- und Regenwasser) zusammen. Trennkanalisation führt Schmutz- und Regenwasser getrennt. Die Art hängt von der Region und dem Alter der Kanalisation ab."},
            {"h2": "Private Abwasserentsorgung"},
            {"p": "In einigen ländlichen Gebieten gibt es keine öffentliche Kanalisation. Dann sind private Lösungen nötig: Kleinkläranlagen reinigen das Abwasser, bevor es versickert oder in einen Vorfluter geleitet wird. Die Kosten für eine Kleinkläranlage liegen bei 3.000 bis 10.000 Euro."},
            {"h2": "Wartung und Probleme"},
            {"p": "Abwasserrohre sind wartungsarm, können aber verstopfen. Vermeiden Sie das Einleiten von Fett, Hygieneartikeln und anderen Gegenständen. Bei Problemen helfen Rohrreinigungsfirmen - die Kosten liegen bei 100 bis 300 Euro für eine Standardreinigung."}
        ],
        "related": ["trinkwasser", "rohrleitungen", "sanitaer-installation"]
    },
    {
        "id": "trinkwasser",
        "title": "Trinkwasser - Qualität und Aufbereitung",
        "meta_desc": "Trinkwasser: Qualität, Filter, Enthärtung. Was Sie über Ihr Trinkwasser wissen sollten.",
        "badge": "Sanitär",
        "content": [
            {"h2": "Trinkwasserqualität in Deutschland"},
            {"p": "In Deutschland ist das Trinkwasser von hoher Qualität und muss strenge Grenzwerte einhalten. Das Gesundheitsministerium überwacht die Qualität regelmäßig. In einigen Regionen ist das Wasser aber sehr hart oder enthält viel Kalk. Das kann zu Ablagerungen in Rohren und Geräten führen."},
            {"h2": "Wasserhärte und Kalk"},
            {"p": "Die Wasserhärte wird in Grad deutscher Härte (°dH) gemessen. Weiches Wasser hat weniger als 8 °dH, hartes Wasser über 14 °dH. In Regionen mit hartem Wasser können Kalkablagerungen in Rohren, Boilern und Haushaltsgeräten entstehen. Eine Wasserenthärtungsanlage kann helfen."},
            {"h2": "Wasserfilter"},
            {"p": "Wasserfilter werden am Hausanschluss oder an einzelnen Zapfstellen installiert. Sie entfernen Partikel wie Sand oder Rost. Aktivkohlefilter können Chlor und Geruchsstoffe entfernen. Die Kosten für Filteranlagen liegen bei 100 bis 500 Euro."},
            {"h2": "Trinkwasserschutz"},
            {"p": "Um die Trinkwasserqualität zu erhalten, sollten Sie das Wasser regelmäßig auf Verfärbung oder Geruch prüfen. Bei längerer Abwesenheit sollten Sie das Wasser kurz ablaufen lassen, bevor Sie es nutzen. Die Hauptleitungen sollten alle fünf Jahre vom Fachmann geprüft werden."}
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
            {"p": "Eine Heizungssanierung ist nötig, wenn die Heizung älter als 15 bis 20 Jahre ist, wenn die Reparaturkosten hoch werden oder wenn die Heizung nicht mehr effizient arbeitet. Auch bei einer umfassenden Dach- oder Fassadensanierung lohnt sich oft der Blick auf die Heizung."},
            {"h2": "Was wird gemacht?"},
            {"p": "Eine Heizungssanierung umfasst den Austausch des Wärmeerzeugers (Heizkessel oder Wärmepumpe), die Erneuerung der Heizkörper oder Fußbodenheizung und oft auch die Rohrleitungen. Dazu kommen eventuell Dämmung der Heizungsrohre und die Optimierung der Steuerung."},
            {"h2": "Kosten und Förderung"},
            {"p": "Die Kosten für eine komplette Heizungssanierung liegen bei 15.000 bis 40.000 Euro je nach Umfang. Die Bundesförderung für effiziente Gebäude (BEG) fördert den Austausch mit bis zu 25 Prozent. Dazu kommen oft regionale Programme. Eine Energieberatung hilft, die optimale Lösung zu finden."},
            {"h2": "Planung und Zeitrahmen"},
            {"p": "Eine Heizungssanierung braucht gute Planung. Von der Entscheidung bis zur Umsetzung vergehen oft drei bis sechs Monate. Die Installation selbst dauert ein bis zwei Wochen. Am besten plant man die Sanierung für das Frühjahr oder den Sommer, wenn die Heizung weniger wichtig ist."}
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
            {"p": "Eine Luft-Wärmepumpe nutzt die Wärme aus der Außenluft, um das Gebäude zu heizen. Sie besteht aus einem Außengerät und einem Innengerät. Das Außengerät saugt Außenluft an, entzieht ihr Wärme und leitet die kalte Luft wieder nach außen ab. Im Innengerät wird die gewonnene Wärme an das Heizungssystem abgegeben."},
            {"h2": "Vorteile und Nachteile"},
            {"p": "Die Vorteile: Günstiger als Sole- oder Wasser-Wärmepumpen, einfache Installation ohne Erdarbeiten, weit verbreitet und daher viel Installateur-Erfahrung. Die Nachteile: Bei niedrigen Außentemperaturen sinkt die Effizienz, das Außengerät ist nicht ganz leise, der Stromverbrauch ist höher als bei Erdwärme."},
            {"h2": "Kosten und Wirtschaftlichkeit"},
            {"p": "Die Kosten für eine Luft-Wärmepumpe liegen bei 15.000 bis 24.000 Euro inklusive Installation. Die jährlichen Heizkosten sind etwa 20 bis 30 Prozent niedriger als bei einer Gasheizung. Die Amortisationszeit beträgt 8 bis 12 Jahre, bevor die Förderung abgezogen wird."},
            {"h2": "Für wen eignet sich die Luft-Wärmepumpe?"},
            {"p": "Die Luft-Wärmepumpe eignet sich für gut gedämmte Neubauten und sanierte Altbauten mit Fußbodenheizung oder Niedertemperatur-Heizkörpern. In Gebäuden mit hoher Vorlauftemperatur (über 60 Grad) ist sie weniger effizient. In Regionen mit sehr kalten Wintern kann die Effizienz stark abnehmen."}
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
            {"p": "Erdwärme nutzt die im Erdreich gespeicherte Sonnenenergie. Schon in einem Meter Tiefe ist die Temperatur relativ konstant bei etwa 10 bis 15 Grad. Eine Erdwärmepumpe entzieht dem Erdreich diese Wärme über Flächenkollektoren oder Erdsonden und nutzt sie für die Raumheizung."},
            {"h2": "Arten der Erdwärmenutzung"},
            {"p": "Erdkollektoren werden horizontal in etwa 1,5 Meter Tiefe verlegt. Sie brauchen eine große Fläche - etwa das 1,5-fache der zu beheizenden Wohnfläche. Erdbohrungen gehen vertikal in 50 bis 150 Meter Tiefe. Sie brauchen weniger Platz, sind aber deutlich teurer."},
            {"h2": "Kosten und Effizienz"},
            {"p": "Die Kosten für eine Erdwärmepumpe liegen bei 25.000 bis 45.000 Euro inklusive Erschließung. Erdbohrungen kosten 8.000 bis 15.000 Euro, Erdkollektoren 5.000 bis 12.000 Euro. Die Effizienz ist sehr hoch: Die Jahresarbeitszahl liegt bei 4 bis 5. Das bedeutet: Für 1 kWh Strom erhalten Sie 4 bis 5 kWh Wärme."},
            {"h2": "Für wen eignet sich Erdwärme?"},
            {"p": "Erdwärme eignet sich für Grundstücke mit ausreichend Platz für Erdkollektoren oder für Bohrungen, die genehmigt werden können. In Wasserschutzgebieten sind Bohrungen oft nicht erlaubt. Die höheren Investitionskosten amortisieren sich über die niedrigen Betriebskosten."}
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
            {"p": "Eine Bad Sanierung lohnt sich, wenn das Bad alt und veraltet ist, wenn Sanitärkeramik und Armaturen nicht mehr funktionieren, wenn die Leitungen undicht sind oder wenn Sie das Bad modernisieren wollen. Auch bei einer Hauserweiterung oder dem Kauf einer Bestandswohnung ist eine Sanierung oft nötig."},
            {"h2": "Was wird gemacht?"},
            {"p": "Bei einer Komplettsanierung werden alle Sanitärgegenstände (Toilette, Waschbecken, Badewanne oder Dusche) erneuert, die Fliesen entfernt und neu verlegt, die Leitungen erneuert, die Elektrik angepasst und neue Armaturen installiert. Manchmal wird die Raumaufteilung verändert, zum Beispiel durch den Einbau einer bodengleichen Dusche."},
            {"h2": "Kosten und Zeitrahmen"},
            {"p": "Die Kosten für eine Komplettsanierung liegen bei 15.000 bis 35.000 Euro je nach Ausstattung und Größe. Die Dauer beträgt zwei bis vier Wochen. In dieser Zeit ist das Bad nicht nutzbar. Eine gute Planung und Abstimmung der Gewerke ist entscheidend für einen reibungslosen Ablauf."},
            {"h2": "Barrierefreiheit und Alterung"},
            {"p": "Wenn Sie planen, lange in der Wohnung zu bleiben, sollten Sie bei der Sanierung an Barrierefreiheit denken. Eine bodengleiche Dusche, Haltegriffe und ein höhenverstellbares WC erleichtern das Leben im Alter. Die Mehrkosten für Barrierefreiheit liegen bei etwa 3.000 bis 8.000 Euro."}
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
            related_html += f'''          <a href="/glossar/{rel_id}/" class="card card--link"><h3>{rel_title}</h3><p>{rel_desc_text}</p></a>
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
        <div class="card-badge"><a href="/glossar/" style="color:inherit">Glossar</a></div>
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


def generate_glossar_index():
    return '''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Heizung & Sanitär Glossar - Fachbegriffe erklärt</title>
  <meta name="description" content="Heizung & Sanitär Glossar: 16 Fachbegriffe rund um Wärmepumpe, Heizungsbau, Klimaanlage und Bad erklärt - nach Themen gruppiert und einfach erklärt.">
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
        <h1>Heizung & Sanitär Glossar - Fachbegriffe erklärt</h1>
        <p class="hero__sub">Was ist eine Wärmepumpe? Was bedeutet Brennwert? Was ist der Unterschied zwischen Trinkwasser und Abwasser? Hier finden Sie 16 Fachbegriffe rund um Heizung und Sanitär - nach Themen gruppiert und verständlich erklärt.</p>
      </div>
    </div>
  </section>

  <section class="section section--light">
    <div class="container">
      <div class="grid grid--3">
'''

GROUPS = {
    "heizung": {
        "title": "Heizung",
        "badge": "Heizung",
        "desc": "Wärmepumpe, Gasheizung, Brennwert, Heizkörper, Fußbodenheizung - die wichtigsten Heizungsbegriffe.",
        "terms": ["waermepumpe", "luft-waermepumpe", "erdwaerme", "gasheizung", "brennwertheizung", "fussbodenheizung", "heizkoerper", "thermostat", "heizungssanierung"]
    },
    "sanitaer": {
        "title": "Sanitär",
        "badge": "Sanitär",
        "desc": "Rohrleitungen, Abwasser, Trinkwasser, Durchlauferhitzer - alles rund um Sanitär.",
        "terms": ["sanitaer", "rohrleitungen", "abwasser", "trinkwasser", "durchlauferhitzer", "badsanierung"]
    },
    "klima": {
        "title": "Klima & Energie",
        "badge": "Klima",
        "desc": "Klimaanlage, Solarthermie - Kühlung und erneuerbare Energie.",
        "terms": ["klimaanlage", "solarthermie"]
    }
}


def main():
    import os
    os.makedirs("glossar", exist_ok=True)

    # Generate glossar index with groups
    index_html = generate_glossar_index()

    for group_id, group in GROUPS.items():
        index_html += f'''
        <a href="/glossar/{group_id}/" class="card card--link">
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
        index_html += f'''<a href="/glossar/{term['id']}/" class="card card--link">
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

    with open("glossar/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)
    print("Generated: glossar/index.html")

    # Generate individual terms
    for term in TERMS:
        dir_path = f"glossar/{term['id']}"
        os.makedirs(dir_path, exist_ok=True)

        html = generate_glossar_entry(term)
        with open(f"{dir_path}/index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated: {dir_path}/index.html")


if __name__ == "__main__":
    main()