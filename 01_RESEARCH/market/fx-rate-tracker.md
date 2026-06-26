# FX Rate Tracker — Argentina Wholesale Prices

**Date:** June 26, 2026 (first build)
**Purpose:** Track Gs/AR$ and Gs/USD in real-time. Flag when re-pricing is needed.
**Critical because:** Argentina wholesale inflation is 34.5% YoY (INDEC May 2026). Our 4:1 assumption will break.

---

## Why this matters

Sarah's entire pricing model assumes:
- 4 Gs/AR$ (Sarah's verbal rate, June 2026)
- 7,500 Gs/USD (PY blue rate, June 2026)

If either moves:
- **Gs/AR$ rises to 5:1** (AR$ weakens) → Sarah's cost up 25%, retail prices must rise
- **Gs/AR$ falls to 3:1** (AR$ strengthens) → Sarah's cost down 25%, can lower prices
- **Gs/USD rises to 8,500** (Gs weakens) → all USD-denominated costs (courier, freight) up
- **Gs/USD falls to 6,500** (Gs strengthens) → freight savings

**Re-pricing trigger:** When Gs/AR$ moves >10% from current baseline (4:1 = 250 Gs/100 AR$).

---

## Current rates (as of June 26, 2026)

| Pair | Rate | Change (7d) | Change (30d) | Source |
|------|-----:|------:|-------:|--------|
| **Gs/AR$** | 4.00 | TBD | TBD | Sarah's verbal |
| **Gs/USD** | 7,500 | TBD | TBD | PY blue rate estimate |

> ⚠️ These are **estimates** as of June 26, 2026. Real rates need live scraping (build below).

---

## Live data sources (free)

### Gs/AR$ (PY peso to Argentine peso)

| Source | URL | Update frequency | Notes |
|--------|-----|------------------|-------|
| **Cambios Chaco** | https://www.cambioschaco.com.py | Daily | PY bank rate |
| **Bcp.gov.py** (Banco Central del Paraguay) | https://www.bcp.gov.py | Daily | Official PY rate |
| **BCRA** (Banco Central Argentina) | https://www.bcra.gob.ar | Daily | Official AR wholesale |
| **DolarHoy** (AR) | https://dolarhoy.com | Real-time | AR blue rate |
| **CambioReal** | https://www.cambioreal.com.br | Real-time | Brazil cross-rate |

### Gs/USD (PY peso to US dollar)

| Source | URL | Notes |
|--------|-----|-------|
| **Cambios Chaco** | https://www.cambioschaco.com.py | PY bank + parallel |
| **Maxi Cambios** | https://www.maxicambios.com.py | PY Casa de Cambio |
| **BCP** | https://www.bcp.gov.py | Official |

### Argentina inflation (quarterly)

| Source | URL | Notes |
|--------|-----|-------|
| **INDEC** (AR official stats) | https://www.indec.gob.ar | IPIM, IPIB, IPP |

---

## Build a live scraper (Python, free)

Run this weekly (or daily) to update the table above.

```python
#!/usr/bin/env python3
"""FX rate tracker for Sarah's Enki Store.
Scrapes free PY + AR sources, logs to CSV, alerts on threshold breach.
"""
import urllib.request
import json
import csv
from datetime import datetime
import os

OUT_DIR = os.path.expanduser('~/sarah-fx-tracking')
os.makedirs(OUT_DIR, exist_ok=True)
CSV_FILE = os.path.join(OUT_DIR, 'fx_log.csv')

# Free APIs and pages
SOURCES = {
    'bcra_usd_oficial': 'https://api.bluelytics.com.ar/v2/latest',
    'dolarhoy_blue': 'https://dolarhoy.com/api/dolar',
    'bcp_referencial': 'https://www.bcp.gov.py/webdpc/webservice/v1/exchange_rates',
}

def fetch_json(url, timeout=10):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read())
    except Exception as e:
        return {'error': str(e)}

# Scrape
results = {
    'timestamp': datetime.now().isoformat(),
    'ars_pyg_baseline': 4.0,  # Sarah's June 26 rate
    'usd_pyg_baseline': 7500,  # PY blue estimate
}

# BCRA (AR official)
bcra = fetch_json(SOURCES['bcra_usd_oficial'])
if 'blue' in bcra:
    ars_usd = bcra['blue'].get('value_buy', 0)
    if ars_usd > 0:
        # Convert to Gs/AR$ via USD/PYG (rough — assumes USD/ARS = AR$/USD inverse)
        # In Argentina, USD is quoted as AR$/USD (e.g., 1100 AR$ per USD)
        ars_per_usd = ars_usd
        usd_pyg = 7500  # would need separate PY fetch
        results['ars_pyg_implied'] = round(usd_pyg / ars_per_usd, 2)
        results['ars_usd_blue'] = ars_per_usd
        results['ars_usd_source'] = 'bluelytics_blue'

# DolarHoy (AR blue)
dh = fetch_json(SOURCES['dolarhoy_blue'])
if isinstance(dh, dict) and not 'error' in dh:
    if 'blue' in dh:
        results['ars_usd_blue_dh'] = dh['blue'].get('venta', 0)
        results['ars_usd_source_dh'] = 'dolarhoy'

# Check thresholds and alert
alerts = []
if 'ars_pyg_implied' in results:
    delta_pct = ((results['ars_pyg_implied'] - 4.0) / 4.0) * 100
    if abs(delta_pct) > 10:
        alerts.append(f"🔴 Gs/AR$ moved {delta_pct:+.1f}% from baseline (4.0). Re-pricing needed.")

# Log to CSV
new_file = not os.path.exists(CSV_FILE)
with open(CSV_FILE, 'a', newline='') as f:
    writer = csv.writer(f)
    if new_file:
        writer.writerow(['timestamp', 'ars_pyg_baseline', 'ars_pyg_implied', 'ars_usd_blue', 'usd_pyg_baseline', 'alerts'])
    writer.writerow([
        results['timestamp'],
        results['ars_pyg_baseline'],
        results.get('ars_pyg_implied', ''),
        results.get('ars_usd_blue', ''),
        results['usd_pyg_baseline'],
        ' | '.join(alerts),
    ])

# Print
print(f"\n=== FX SNAPSHOT — {results['timestamp']} ===")
for k, v in results.items():
    print(f"  {k}: {v}")
if alerts:
    print(f"\n⚠️ ALERTS:")
    for a in alerts:
        print(f"  {a}")
print(f"\nLogged to: {CSV_FILE}")
```

**How to run:** `python3 tools/fx_tracker.py` (after Sarah has the script set up)
**Output:** CSV log of all FX snapshots, alerts when thresholds breach

---

## Manual update procedure (until script runs)

**Weekly (every Sunday):**
1. Visit https://www.cambioschaco.com.py
2. Note Gs/AR$ and Gs/USD
3. Update the table at the top of this doc
4. Check alert trigger (10% from baseline)
5. If triggered: notify Erebus to re-run pricing

---

## Re-pricing decision matrix

| Scenario | FX move | Action | Lead time |
|----------|---------|--------|-----------|
| Gs/AR$ rises < 5% | Minor | None | 1 week |
| Gs/AR$ rises 5-10% | Material | Build new pricing scenarios | 3-5 days |
| Gs/AR$ rises 10-20% | Critical | Re-price retail, update calculator | 1-2 days |
| Gs/AR$ rises > 20% | Emergency | Pause new orders, liquidate inventory, re-pricing | Same day |
| Gs/AR$ falls (AR strengthens) | Opportunity | Consider lower retail / larger orders | 1 week |
| Gs/USD rises 10%+ | Material | All freight/courier up — re-budget | 1 week |
| AR inflation > 40% YoY | Critical | Sexitive will raise prices; pre-order large | 1-2 weeks |

---

## Historical context (June 2026)

- **AR wholesale inflation (IPIM):** +34.5% YoY (INDEC May 2026)
- **AR CPI:** ~40% YoY (monthly pace slowing)
- **PY inflation (IPC):** ~3-4% YoY (much more stable)
- **AR$/USD blue:** ~1,100-1,200 (volatile)
- **Gs/USD:** ~7,500-7,800 (PY relatively stable)

**Implication:** AR peso devalues faster than PY guaraní strengthens. Gs/AR$ will tend to RISE (Sarah's cost goes up) over 12 months. Build FX buffer into retail pricing NOW.

---

## What to do with this data

### When Gs/AR$ rises (cost up):
1. Re-run `tools/pricing_calculator.py` with new FX rate
2. Update `canonical-pricing-reference-v1.md` with new numbers
3. Adjust retail prices in WA catalog (via WA Business — no website yet)
4. If price increase >15%, re-check PY market position vs. competitors
5. Consider pre-ordering inventory before next FX move

### When Gs/AR$ falls (cost down):
1. Re-run pricing calc — could be more margin
2. Consider larger next order (more stock at lower cost)
3. Consider lowering retail prices to capture more market share
4. Update cash flow model with better margins

### Always:
- **Don't lock pricing on website** (we don't have one yet — but don't change that)
- **Use WhatsApp-quoted pricing** so we can move it
- **Update Erebus monthly** with the new rate

---

## Known limitations

- ❌ Free APIs (Bluelytics, DolarHoy) sometimes go down
- ❌ PY Casa de Cambio rates not always in real-time
- ❌ BCP official rates may lag 1-2 days
- ❌ AR blue rate is unofficial; can be manipulated
- ❌ No integration with our pricing model yet (manual re-run)

**Acceptable for v1.** When monthly revenue >Gs 5M, consider paid FX rate feed (e.g., openexchangerates.org, $10/month).

---

*Last updated: June 26, 2026 — Session 11*