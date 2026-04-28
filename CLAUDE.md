# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Lead generation website for Dachdecker / Zimmerei (roofer & carpentry) in Germany. Core model: customer makes ONE inquiry → receives up to THREE quotes from vetted local roofers → chooses freely. Revenue via pay-per-lead.

Brand: **hausbau.pro** — Lead-Generierung für Dachdecker und Zimmereien in Deutschland.

---

## Website Structure (Actual)

```
/                           Homepage (index.html)
/dachdecker/{city}/         City pages (Köln, Dortmund, München live)
/dachsanierung/{city}/
/zimmermann/{city}/
/dachausbau/{city}/
/dachfenster/{city}/
/flachdach/{city}/
/blog/
/css/style.css
/js/main.js
```

**Active city pages (14 per service × 6 services):**
- `dachdecker/` — München, Köln, Hamburg, Stuttgart, Dortmund, Düsseldorf, Leipzig, Freiburg, Berlin, Frankfurt, Nürnberg, Hannover, Bremen, Mannheim
- `dachsanierung/`, `zimmermann/`, `dachausbau/`, `dachfenster/`, `flachdach/` — same 14 cities each
- `dachdecker-preisvergleich/` — separate section with its own 8 city pages

**Other sections:**
- `blog/` — 9 articles on roofing topics
- `glossar/` — 16 glossary terms (bitumenbahn, daemmung, dachformen, etc.)

---

## Tech Stack

- Plain HTML/CSS/JS — no framework
- Form backend: Formspree (placeholder `YOUR_FORM_ID` in all HTML files — user will provide real ID)
- Fonts: Inter via Google Fonts

---

## CRITICAL Content Rules

### 1. City pages must be LOCALLY AUTHENTIC — no doorwaypages
Per memory rule. Every city page must feel written for exactly that place.

- ❌ NOT just "Stadtname ersetzen" in a template
- ✅ Individual PLZ ranges, neighborhood names, local architecture (e.g. "Satteldächer in Köln-Ehrenfeld", "Plattformdächer in München-Pasing")
- ✅ Unique H2/H3 headings per city ("Warum ein Dachdecker aus Köln-Mülheim?")
- ✅ Testimonials with real-feeling names + cities
- ✅ Regional keywords that only make sense for that city

### 2. Content must sound HUMAN-WRITTEN
Per memory rule. Google and users detect AI-patterns.

- ❌ No em-dashes (—), no "darüber hinaus", "in Bezug auf", "letztlich", "es ist wichtig zu erwähnen"
- ❌ No sterile lists like "Wir bieten folgende Leistungen an:"
- ✅ Short, direct sentences. Talk like a tradesperson or local business owner.
- ✅ Natural German. Filler words and colloquialisms are fine where authentic.
- ✅ Every page should feel written by a real human for that specific place.

### 3. Do NOT hallucinate city-specific content
When generating or editing city pages, only use verified local data:

- ✅ Use actual neighborhood names from the city's real data in `gen_service_pages.py`
- ✅ Use actual PLZ ranges, architecture descriptions, landmarks that exist
- ❌ Do NOT invent neighborhood names, streets, landmarks, or local facts
- ❌ Do NOT guess architecture types — if unsure, leave generic or research first
- When adding new cities: verify neighborhoods and landmarks via web search before generating

The city data in `CITIES` dict (gen_service_pages.py) is the authoritative source. Do not contradict it.

---

## Deployment

GitHub Actions deploys to Cloudflare Pages on push to `main`:
```yaml
# .github/workflows/deploy.yml
wrangler pages deploy . --project-name=hausbau-pro
```
Requires `CLOUDFLARE_API_TOKEN` secret. Manual deploy: `wrangler pages deploy . --project-name=hausbau-pro`

---

## Generating Pages

**`gen_service_pages.py`** — generates all 84 service/city pages (6 services × 14 cities). Uses the rich dachdecker/muenchen template for all pages. Run with `python gen_service_pages.py`.

**`gen_pages.py`** — generates `dachdecker-preisvergleich/{city}/index.html` for 8 cities. Run with `python gen_pages.py`.

---

## Git Workflow

- Branch: `main` — auto-deploys to Cloudflare Pages
- Commit messages should be descriptive but concise

---

## Keyword Research Tools

Scripts use DataForSEO API v3 (Germany location code 2276, language "de").

**`kw.py`** — single-query CLI:
```
python kw.py volume <kw1> [kw2 ...]
python kw.py ideas <keyword>
python kw.py site <domain>
python kw.py ubersuggest <keyword>
```

**`kw_research.py`** — batch research across 7 cities × services:
- Regions: Köln, Düsseldorf, Stuttgart, München, Hamburg, Freiburg, Leipzig
- Outputs `kw_results.csv` sorted by search volume
- Results: 270 keywords with volume > 0 (out of 3260 checked)

**API credentials** (in `kw-api.txt` — DO NOT COMMIT):
- DataForSEO Base64 auth header (from kw-api.txt)
- Apify Ubersuggest actor: `Sz8kGXrxcp7eDN4J7`
- Apify token (from kw-api.txt)

---

## User Preferences

- Direct execution, no fluff
- Practical business advice
- Save non-obvious rules to `~/.claude/memory/` with frontmatter
- Check memory files when working on city pages or content
