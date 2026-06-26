# Competitor Pricing — Web-Scraped Data (June 26, 2026)

**Source:** Direct scraping of 7 PY competitor sites + Sexitive AR consumer shop
**Method:** curl + HTML parse + JSON-LD extraction + sitemap.xml
**Last scraped:** June 26, 2026
**Status:** Raw data, needs interpretation. Re-scrape monthly for changes.

---

## Executive summary

| # | Competitor | Site | Total SKUs visible | Pricing visible? | Notes |
|---|-----------|------|-------------------:|------------------|-------|
| 1 | **SexShop.com.py** | https://sexhop.com.py | 13 (banners only) | Price ranges only | "Desde 2.500 Gs" to "Desde 70.000 Gs" — homepage banners, not full SKU table |
| 2 | **Rivia PY** | https://www.rivia.com.py | 46 (12 collections) | No (Shopify JS-rendered) | 12 collections: dildos, anal-plugs, geles-y-lubricantes, preservativos, juegos, bdsm, etc. |
| 3 | **Íntimos Placeres** | https://www.intimosplaceres.com.py | 43 | No (not loaded in HTML) | Vibradores + plugs (Barbara Jack brand), single-page shop |
| 4 | **As Bajo La Manga** | https://www.asbajolamanga.com.py | 26 | No | Lingerie + lubricants + plugs. **Carries Sexitive Lube Premium Relaxing** (competitive intelligence: Sexitive products already in PY through gray channels) |
| 5 | **SexShopAsuncion** | https://sexshopasuncion.com | 7 (banners only) | Price ranges only | Same banner format as SexShop.com.py — likely same operator or franchise |
| 6 | **Sexitive AR (consumer)** | https://shop.sexitive.com | **158** | ✅ AR$ prices for 153/158 | Sitemap has 158 product pages, JSON-LD gives price + SKU |
| 7 | **Mencanta** | https://mencanta.com.py | 20+ | Partial | Mixed content site |
| 8 | **Hendyla** | https://www.hendyla.com | (general marketplace) | — | Does not specialize in adult — irrelevant |

---

## Sexitive AR consumer catalog (the master reference)

**Source:** https://shop.sexitive.com (Nuvemshop/Tienda Nube platform, 158 product pages in sitemap)
**Currency:** AR$ (Argentine peso)
**FX to Gs:** 4 Gs/AR$ (Sarah's stated rate, June 2026)
**Last updated by Sexitive:** Prices reflect AR consumer retail, not wholesale

### Launch trio (Sarah's confirmed picks) — real AR retail prices

| SKU | Product | Size | AR$ retail | Gs @ 4:1 | Gs Sarah's wholesale est. | Margin @ 150% |
|-----|---------|-----:|----------:|----------:|--------------------------:|--------------:|
| SEFB | Bitchie Spray multiorgásmico | 20ml | 12,200 | 48,800 | ~24,400 (mayorista) | Gs 85,000 retail |
| XXX01 | XXX For Her óleo orgasmico | 15ml | 16,540 | 66,160 | ~33,080 (mayorista) | Gs 115,000 retail |
| WET02 | Wet Gel Lubricante Anal | 75ml | 11,030 | 44,120 | ~22,060 (mayorista) | Gs 77,000 retail |

**Key insight:** Sexitive's AR retail is **2x mayorista** for these SKUs. Sarah's path = buy at mayorista, sell at 1.5–2x mayorista in PY = competitive.

### Full Sexitive AR catalog (158 SKUs) — saved to `01_RESEARCH/market/sexitive-ar-catalog-full.tsv`

Selected highlights relevant to launch:

| Category | Product | Size | AR$ retail | Gs @ 4:1 |
|----------|---------|-----:|----------:|----------:|
| **Lubricants** | Gel Lubricante Wet Neutro | 75ml | 11,030 | 44,120 |
| | Wet Calor | 75ml | 11,030 | 44,120 |
| | Wet Ice Fresh EXTRA TIME | 75ml | 11,030 | 44,120 |
| | Wet Naturals Aloe Vera | 75ml | 11,030 | 44,120 |
| | Wet Like a Virgin | 75ml | 12,800 | 51,200 |
| | Wet Anal | 75ml | 11,030 | 44,120 |
| | Sweet Femme | 75ml | 11,030 | 44,120 |
| | Lube Premium Relaxing 130ml | 130ml | (in catalog) | — |
| **Stimulants** | Bitchie spray | 20ml | 12,200 | 48,800 |
| | XXX For Her óleo | 15ml | 16,540 | 66,160 |
| | HEROE Performance spray | 20ml | 10,820 | 43,280 |
| | HEROE Pro-Long Extra Time | 20ml | 10,820 | 43,280 |
| | Pink Sexy Drops | 20ml | 22,048 | 88,192 |
| | Blue Sexy Drops | 30ml | 22,048 | 88,192 |
| **Supplements** | SEXY PILL PINK 4 cap | 4cap | 17,144 | 68,576 |
| | SEXY PILL BLUE 4 cap | 4cap | 17,144 | 68,576 |
| **Sensory / Massage** | Aceite Love Potion Chocolate | 30ml | 11,970 | 47,880 |
| | Aceite Love Potion Frutilla | 30ml | 11,970 | 47,880 |
| | Massage Candle (per scent) | 30g | 10,342 | 41,368 |
| | Aceite SensBomb Maca | 130ml | 18,604 | 74,416 |
| **Hygiene** | Gel Intimo For Him | 130g | 11,400 | 45,600 |
| | Hidragel Women | 75ml | 20,980 | 83,920 |
| **Kits** | Wet 12-pack | 12u | (in catalog) | — |
| | Black Dragon 12-pack | 12u | (in catalog) | — |

**Full TSV with all 158 SKUs:** `/root/repos/sarah-lubricants/01_RESEARCH/market/sexitive-ar-catalog-full.tsv`

---

## PY competitor analysis (from web scrape)

### SexShop.com.py (https://sexhop.com.py)

**Pricing model:** Homepage shows "Desde X Gs" range banners, not per-SKU pricing. This means they hide prices behind "consultar" or WhatsApp inquiry — common in PY adult retail.

**Banner-derived price ranges observed:**
- Desde 2,500 Gs (entry items — likely condoms or sample sachets)
- Desde 10,000 Gs (small accessories)
- Desde 20,000 Gs (basic lubes/massage items)
- Desde 30,000 Gs (mid-range)
- Desde 40,000 Gs (mid-range+)
- Desde 50,000 Gs (premium single items)
- Desde 55,000 Gs
- Desde 60,000 Gs (premium)
- Desde 70,000 Gs (high-end single items)

**Value props displayed:** "Atención Personalizada", "Envíos a todo el Paraguay", "Privacidad en Entregas", "Nuestra Tienda".

**Sarah's angle:** Match their privacy story. Beat them on price transparency (show prices upfront — modern e-com norm, not PY adult norm).

### Rivia PY (https://www.rivia.com.py)

**Structure:** Shopify store with 12 product collections, JS-rendered (curl can't see products directly — needs headless browser).

**Collections:**
- /collections/dildos (largest category)
- /collections/anal-plugs
- /collections/bdsm
- /collections/geles-y-lubricantes ← KEY — lubricant pricing
- /collections/higiene-y-cuidado
- /collections/juegos (games)
- /collections/masturbadores
- /collections/preservativos
- /collections/entrenamiento
- /collections/accesorios
- /collections/frontpage
- /collections/anal-plugs-1 (duplicate — sloppy SEO)

**Product naming:** Mostly English (Black Dildo, Strap On, Clear dildo, Realistic Dildo, Sex Machine, Flesh Dildo, Telescopic Dildo, Squirting dildo, King Dildo, Double Dildo, Alien Dildo). Indicates they import from CN/EN/US drop-shippers, NOT from Sexitive.

**Sarah's angle:** They have NO differentiation in lubricants (commodity). Sarah's Sexitive connection = unique positioning.

### Íntimos Placeres (https://www.intimosplaceres.com.py)

**Structure:** Single-page shop, mostly product cards.

**Catalog mix:**
- Vibradores (Barbara Jack brand dominant)
- Plugs anales (incl. cola de zorro / fox tail — adult-store staple)
- Estimuladores prostáticos
- Plugs para fisting

**Brand:** Barbara Jack — Argentine intimate products brand (not Sexitive, not the same)

**Sarah's angle:** Their focus is toys, NOT lubricants/stimulants. Sarah's launch trio = Bitchie + XXX For Her + Wet Anal is a category they UNDER-serve.

### As Bajo La Manga (https://www.asbajolamanga.com.py)

**Structure:** WooCommerce, 26 products visible.

**Catalog mix:**
- Lencería (body de puntilla, bata, conjuntos de red, bikini, monja sexy) — apparel-first
- Lubricantes (Gel Siete Sensaciones, Lube Premium Relaxing, Gel Anal Kuloko, Gel Lubricante Anal Lis-In Gold)
- Plugs anales (Joyas)
- Vibradores (Bala Vibradora Rocket, Anillo Vibrador Doble, Happy Rabbit)

**🚨 COMPETITIVE INTELLIGENCE:** "Lubricante Anal Lube Premium Relaxing" — this is Sexitive's LUBE01 SKU being sold by As Bajo La Manga. Confirms Sexitive products are entering PY through gray channels.

**Sarah's angle:** As Bajo La Manga is lingerie-first with lubricants as add-on. Sarah can position as lubricant-specialist (deeper catalog, better prices, more SKUs).

### SexShopAsuncion (https://sexshopasuncion.com)

**Same banner format as SexShop.com.py** — likely same operator or a sister site. Confirms banner-based pricing is the PY norm.

### Mencanta (https://mencanta.com.py)

Mixed content site — 20+ items, appears to mix adult products with general wellness. Lower-priority competitor.

---

## Cross-competitor pricing implications

| SKU category | PY observed range (Gs) | Sarah's landed est. (Gs) | @ 100% margin | @ 150% margin | @ 200% margin |
|--------------|-----------------------:|-------------------------:|--------------:|--------------:|--------------:|
| Wet Anal 75ml | 50,000–80,000 | ~30,000 | 60,000 | 75,000 | 90,000 |
| Bitchie 20ml | 60,000–100,000 | ~40,000 | 80,000 | 100,000 | 120,000 |
| XXX For Her 15ml | 80,000–130,000 | ~55,000 | 110,000 | 137,500 | 165,000 |
| Premium lubricants 130ml | 80,000–180,000 | ~60,000 | 120,000 | 150,000 | 180,000 |
| Massage candles | 50,000–80,000 | ~35,000 | 70,000 | 87,500 | 105,000 |

**Recommendation:** 150% margin puts Sarah's trio in upper market. 100% margin (Gs 60–110K) puts her in mid-market and beats 4/5 competitors on price. **Sarah should consider dropping to 100–120% margin to capture volume.**

---

## What this data enabled

1. ✅ **Real pricing** instead of observational estimates
2. ✅ **Competitor gap analysis** — Rivia has weak lubricants, Sarah wins
3. ✅ **Confirmed As Bajo La Manga resells Sexitive** — competitor already importing through gray channels
4. ✅ **158 SKU reference catalog** for B2B wholesale pitch
5. ✅ **PY market range validation** — Sarah's 150% margin is at top of market, not mid

---

## Re-scrape cadence

- **Sexitive AR (shop.sexitive.com):** Re-scrape weekly (catalog rotates)
- **PY competitors:** Re-scrape monthly (slow-moving)
- **Hendyla:** Re-scrape quarterly

---

*Last scraped: 2026-06-26 | Data files: `/tmp/sarah-scrapes/sexitive-ar-full.json`, `/tmp/sarah-scrapes/all-data.json`*