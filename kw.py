import sys
import json
import urllib.request
import urllib.error

BASE_URL = "https://api.dataforseo.com/v3"
AUTH = "aW5mb0BidWxrc2VlZHNpbnRlcm5hdGlvbmFsLmNvbTo5MzI2YWU1ZWE2MTdkZjAx"
LOCATION = 2276  # Germany
LANGUAGE = "de"

APIFY_TOKEN = "apify_api_pn1DvsjI3OJr1klWhA3aI30xrwi0Ct1Ivlr2"
APIFY_ACTOR = "Sz8kGXrxcp7eDN4J7"


def post(endpoint, payload):
    data = json.dumps([payload]).encode()
    req = urllib.request.Request(
        BASE_URL + endpoint,
        data=data,
        headers={"Authorization": f"Basic {AUTH}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def print_table(rows, headers):
    widths = [max(len(str(r[i])) for r in [headers] + rows) for i in range(len(headers))]
    fmt = "  ".join(f"{{:<{w}}}" for w in widths)
    print(fmt.format(*headers))
    print("  ".join("-" * w for w in widths))
    for row in rows:
        print(fmt.format(*row))


def cmd_volume(keywords):
    res = post("/keywords_data/google_ads/search_volume/live", {
        "keywords": keywords,
        "location_code": LOCATION,
        "language_code": LANGUAGE,
    })
    items = res["tasks"][0]["result"] or []
    rows = [(i["keyword"], i.get("search_volume") or 0, i.get("competition", "")) for i in items]
    rows.sort(key=lambda x: -x[1])
    print_table(rows, ["Keyword", "Volume", "Competition"])


def cmd_ideas(keyword):
    res = post("/keywords_data/google_ads/keywords_for_keywords/live", {
        "keywords": [keyword],
        "location_code": LOCATION,
        "language_code": LANGUAGE,
    })
    items = res["tasks"][0]["result"] or []
    rows = [(i["keyword"], i.get("search_volume") or 0, i.get("competition", "")) for i in items]
    rows.sort(key=lambda x: -x[1])
    print_table(rows[:50], ["Keyword", "Volume", "Competition"])


def apify_request(url, payload=None):
    data = json.dumps(payload).encode() if payload else None
    method = "POST" if payload else "GET"
    req = urllib.request.Request(url, data=data, method=method,
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def cmd_ubersuggest(keyword):
    run = apify_request(
        f"https://api.apify.com/v2/acts/{APIFY_ACTOR}/runs?token={APIFY_TOKEN}&waitForFinish=120",
        {"keyword": keyword, "country": "de", "include_keywords": True},
    )
    dataset_id = run["data"]["defaultDatasetId"]
    items = apify_request(
        f"https://api.apify.com/v2/datasets/{dataset_id}/items?token={APIFY_TOKEN}&limit=200"
    )
    suggestions = items[0].get("suggestions", []) if items else []
    rows = [(s["keyword"], s.get("volume") or 0, s.get("seo_difficulty") or 0, round(s.get("cpc") or 0, 2))
            for s in suggestions]
    rows.sort(key=lambda x: -x[1])
    print_table(rows[:50], ["Keyword", "Volume", "SEO Diff", "CPC"])


def cmd_site(domain):
    res = post("/keywords_data/google_ads/keywords_for_site/live", {
        "target": domain,
        "location_code": LOCATION,
        "language_code": LANGUAGE,
    })
    items = res["tasks"][0]["result"] or []
    rows = [(i["keyword"], i.get("search_volume") or 0, i.get("competition", "")) for i in items]
    rows.sort(key=lambda x: -x[1])
    print_table(rows[:50], ["Keyword", "Volume", "Competition"])


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage:")
        print("  python kw.py volume <kw1> [kw2 ...]")
        print("  python kw.py ideas <keyword>")
        print("  python kw.py site <domain>")
        print("  python kw.py ubersuggest <keyword>")
        return

    cmd = args[0]
    if cmd == "volume" and len(args) > 1:
        cmd_volume(args[1:])
    elif cmd == "ideas" and len(args) == 2:
        cmd_ideas(args[1])
    elif cmd == "site" and len(args) == 2:
        cmd_site(args[1])
    elif cmd == "ubersuggest" and len(args) == 2:
        cmd_ubersuggest(args[1])
    else:
        print("Invalid usage. Run without args to see help.")


if __name__ == "__main__":
    main()
