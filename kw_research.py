import json
import urllib.request
import csv
import sys

BASE_URL = "https://api.dataforseo.com/v3"
AUTH = "aW5mb0BidWxrc2VlZHNpbnRlcm5hdGlvbmFsLmNvbTo5MzI2YWU1ZWE2MTdkZjAx"
LOCATION = 2276
LANGUAGE = "de"

REGIONS = {
    "Köln": ["Köln", "Bonn", "Leverkusen", "Bergisch Gladbach",
             "Köln Ehrenfeld", "Köln Nippes", "Köln Mülheim", "Köln Porz", "Köln Rodenkirchen",
             "Köln Lindenthal", "Köln Deutz", "Köln Chorweiler", "Köln Kalk"],
    "Düsseldorf": ["Düsseldorf", "Essen", "Dortmund", "Bochum", "Duisburg",
                   "Düsseldorf Oberkassel", "Düsseldorf Pempelfort", "Düsseldorf Gerresheim", "Düsseldorf Benrath",
                   "Düsseldorf Bilk", "Essen Rüttenscheid", "Dortmund Hörde"],
    "Stuttgart": ["Stuttgart", "Ludwigsburg", "Böblingen", "Esslingen", "Sindelfingen",
                  "Stuttgart Bad Cannstatt", "Stuttgart Vaihingen", "Stuttgart Zuffenhausen", "Stuttgart Degerloch",
                  "Stuttgart Feuerbach", "Stuttgart Möhringen"],
    "München": ["München", "Augsburg", "Ingolstadt", "Freising", "Dachau",
                "München Schwabing", "München Maxvorstadt", "München Pasing", "München Bogenhausen",
                "München Neuhausen", "München Sendling", "München Giesing", "München Moosach"],
    "Hamburg": ["Hamburg", "Lübeck", "Kiel",
                "Hamburg Altona", "Hamburg Eimsbüttel", "Hamburg Wandsbek", "Hamburg Harburg",
                "Hamburg Bergedorf", "Hamburg Rahlstedt", "Hamburg Blankenese", "Hamburg Barmbek"],
    "Freiburg": ["Freiburg", "Karlsruhe", "Mannheim", "Heidelberg",
                 "Freiburg Wiehre", "Freiburg Haslach", "Karlsruhe Durlach", "Karlsruhe Mühlburg",
                 "Mannheim Neckarstadt", "Heidelberg Rohrbach"],
    "Leipzig": ["Leipzig", "Dresden", "Chemnitz", "Halle",
                "Leipzig Gohlis", "Leipzig Connewitz", "Leipzig Plagwitz", "Dresden Neustadt",
                "Dresden Blasewitz", "Leipzig Schleußig", "Dresden Striesen"],
}

SERVICES = {
    "Dachdecker": [
        "Dachdecker",
        "Dachdeckermeister",
        "Dachdecker Betrieb",
        "Dachdecker Fachbetrieb",
        "Dachdecker Angebot",
        "Dachdecker Kosten",
        "Dachdecker Notdienst",
        "Dach reparieren",
        "Dach reparieren lassen",
        "Dachreparatur",
        "Dach sanieren",
        "Dachsanierung",
        "Dachsanierung Kosten",
        "Dachsanierung Angebot",
        "Dach neu decken",
        "Dacheindeckung",
        "Dach undicht",
        "Dach erneuern",
    ],
    "Dachfenster": [
        "Dachfenster einbauen",
        "Dachfenster einbauen lassen",
        "Dachfenster Kosten",
        "Dachfenster Montage",
        "Velux einbauen",
        "Velux Montage",
        "Dachfenster tauschen",
        "Dachfenster erneuern",
    ],
    "Zimmerei": [
        "Zimmerei",
        "Zimmermann",
        "Zimmerer",
        "Dachstuhl bauen",
        "Dachstuhl sanieren",
        "Dachstuhl erneuern",
        "Holzbau",
        "Holzbau Betrieb",
        "Carport bauen lassen",
        "Carport Holz",
        "Carport Kosten",
        "Terrassenüberdachung Holz",
        "Terrassenüberdachung bauen lassen",
        "Terrassenüberdachung Kosten",
        "Holzterrasse bauen lassen",
        "Pergola bauen lassen",
    ],
    "Dachausbau": [
        "Dachausbau",
        "Dachgeschoss ausbauen",
        "Dachausbau Kosten",
        "Dachausbau Angebot",
        "Spitzboden ausbauen",
        "Dachboden ausbauen",
        "Dachgeschoss ausbauen lassen",
        "Dachausbau Handwerker",
    ],
    "Flachdach": [
        "Flachdach sanieren",
        "Flachdach abdichten",
        "Flachdach erneuern",
        "Flachdach Kosten",
        "Flachdach undicht",
        "Flachdachabdichtung",
    ],
}

REGION_SERVICES = {
    "Köln": ["Dachdecker", "Zimmerei", "Dachausbau"],
    "Düsseldorf": ["Dachdecker", "Dachausbau", "Flachdach"],
    "Stuttgart": ["Dachdecker", "Zimmerei", "Dachfenster"],
    "München": ["Dachdecker", "Dachfenster", "Zimmerei"],
    "Hamburg": ["Dachdecker", "Zimmerei", "Flachdach"],
    "Freiburg": ["Dachdecker", "Dachausbau", "Zimmerei"],
    "Leipzig": ["Dachdecker", "Zimmerei", "Dachausbau"],
}


def post(endpoint, payload):
    data = json.dumps([payload]).encode()
    req = urllib.request.Request(
        BASE_URL + endpoint, data=data,
        headers={"Authorization": f"Basic {AUTH}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def main():
    keywords = []
    for region, services in REGION_SERVICES.items():
        cities = REGIONS[region]
        for service in services:
            for phrase in SERVICES[service]:
                for city in cities:
                    keywords.append(f"{phrase} {city}")

    print(f"Total keywords: {len(keywords)}", file=sys.stderr)

    results = []
    for batch in chunks(keywords, 1000):
        res = post("/keywords_data/google_ads/search_volume/live", {
            "keywords": batch,
            "location_code": LOCATION,
            "language_code": LANGUAGE,
        })
        items = res["tasks"][0]["result"] or []
        results.extend(items)
        print(f"  fetched {len(results)}/{len(keywords)}", file=sys.stderr)

    results.sort(key=lambda x: -(x.get("search_volume") or 0))

    writer = csv.writer(sys.stdout)
    writer.writerow(["Keyword", "Volume", "Competition", "CPC"])
    for r in results:
        if (r.get("search_volume") or 0) > 0:
            cpc = ""
            if r.get("cpc"):
                cpc = round(r["cpc"], 2)
            writer.writerow([r["keyword"], r.get("search_volume") or 0, r.get("competition", ""), cpc])


if __name__ == "__main__":
    main()
