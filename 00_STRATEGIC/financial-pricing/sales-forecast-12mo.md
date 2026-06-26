# Sales Forecast Model — 12-Month Detail

> ⚠️ **CRITICAL CAVEAT:** Volume projections assume 100% margin fits the PY market. Margin math is based on ESTIMATED Sexitive AR Mayorista pricing (AR retail ÷ 2). Once Q5 PDF arrives, recalculate. See `canonical-pricing-reference-v1.md` for the CRITICAL warning at the top.

**Date:** June 26, 2026
**Scope:** Per-SKU monthly unit projection + revenue + margin
**Use:** Monthly tracking + reorder decisions
**Companion to:** `cash-flow-model-12mo.md`

---

## Launch Trio (Sarah's confirmed SKU list)

| Code | Product | Size | Recommended retail (Gs) | Landed cost/unit (Gs) | Margin |
|------|---------|------|------------------------:|----------------------:|-------:|
| SEFB | Bitchie Spray | 20ml | 130,000 | 65,400 | 99% |
| XXX01 | XXX For Her óleo | 15ml | 145,000 | 73,800 | 96% |
| WET02 | Wet Anal | 75ml | 125,000 | 63,000 | 98% |

**Weighted avg retail:** Gs 130K
**Weighted avg landed:** Gs 67K (using 30u first-order math)

---

## Recommended Scenario — Monthly SKU Breakdown

### Assumptions
- DTC mix: 60% Bitchie, 30% XXX, 10% Wet Anal (initial assumption)
- Adjust as real data accumulates
- AOV target: Gs 130K+ (single SKU purchase)
- Bundle attach rate: 30%

### Month-by-month projection

| Month | Total units | Bitchie | XXX | Wet Anal | Revenue | Cost | Net |
|------:|-----------:|--------:|----:|---------:|--------:|-----:|----:|
| 1 | 20 | 12 | 6 | 2 | 2,600K | 1,340K | 1,260K |
| 2 | 30 | 18 | 9 | 3 | 3,900K | 2,010K | 1,890K |
| 3 | 50 | 30 | 15 | 5 | 6,500K | 3,350K | 3,150K |
| 4 | 70 | 42 | 21 | 7 | 9,100K | 4,690K | 4,410K |
| 5 | 90 | 54 | 27 | 9 | 11,700K | 6,030K | 5,670K |
| 6 | 110 | 66 | 33 | 11 | 14,300K | 7,370K | 6,930K |
| 7 | 130 | 78 | 39 | 13 | 16,900K | 8,710K | 8,190K |
| 8 | 150 | 90 | 45 | 15 | 19,500K | 10,050K | 9,450K |
| 9 | 170 | 102 | 51 | 17 | 22,100K | 11,390K | 10,710K |
| 10 | 190 | 114 | 57 | 19 | 24,700K | 12,730K | 11,970K |
| 11 | 210 | 126 | 63 | 21 | 27,300K | 14,070K | 13,230K |
| 12 | 230 | 138 | 69 | 23 | 29,900K | 15,410K | 14,490K |
| **Year 1** | **1,450** | **870** | **435** | **145** | **188.5M** | **97.2M** | **91.3M** |

---

## Reorder Cadence

### First order (Month 1)
- 30 units each (90 total) = Gs 2.39M landed = Gs 6.27M all-in
- Runway: 4-5 months at 20u/month volume

### Second order (Month 3)
- 50 units each (150 total) = Gs 3.98M landed = Gs 7.79M all-in
- Just-in-time for month 4-6 demand

### Third order (Month 6)
- 100 units each (300 total) = Gs 7.95M landed = Gs 12.93M all-in
- Funded from revenue (Gs 14.3M by month 6)
- Covers month 7-9 demand

### Steady-state (Month 9+)
- Order 100 units every 2-3 months
- Reorder trigger: when 30 units of any SKU remain
- Cash flow positive — can fund from monthly margin

---

## Volume Drivers (Conversion rate assumptions)

### Conversion funnel

| Stage | Assumption | Source |
|-------|-----------|--------|
| IG impressions (Month 1) | 5,000 | 20K followers × 25% reach |
| Bio link clicks | 250 (5%) | Standard IG CTR |
| WA messages | 100 (40%) | Standard click-to-msg |
| Orders | 30 (30%) | DTC sales playbook |
| Repeat (90-day) | 7 (25%) | Customer onboarding flow |

### Volume multipliers

| Multiplier | Effect | When active |
|-----------|--------|-------------|
| Micro-influencer collabs | +50% reach per post | Month 3+ |
| TikTok @kinky_py | +30% discovery | Month 3+ |
| Email automation | +15% repeat rate | Month 2+ |
| B2B wholesale | +Gs 5M/mo per buyer | Month 4+ |
| MercadoLibre | +20% reach (if approved) | Month 4+ |
| Bundle attach | +30% AOV | Month 1+ |

---

## Break-Even Analysis

### Fixed costs (monthly)
- Contador: Gs 400K
- Marketing (post-launch): Gs 500K
- Brevo paid (Month 4+): Gs 250K
- Misc (cloud, domain): Gs 100K
- **Total fixed:** Gs 1.25M/month

### Variable cost per unit (avg)
- Landed cost: Gs 67K
- Packaging: Gs 5K
- Courier: Gs 30K
- **Total variable:** Gs 102K/unit

### Revenue per unit
- Avg retail: Gs 130K

### Contribution margin per unit
- 130K − 102K = **Gs 28K per unit**

### Break-even units per month
- 1,250K / 28K = **~45 units/month**

### Break-even timeline (Recommended scenario)
- Month 3: 50 units (just past break-even)
- Month 4: 70 units (clearly profitable)
- **Break-even achieved in Month 3**

---

## Pricing Variants Sensitivity

### If Sarah drops to 100% margin
- Bitchie retail: 130K → 131K (no real change)
- XXX retail: 145K → 148K (slightly higher)
- Net effect: marginal, but more competitive vs Rivia/SexShop

### If Sarah goes to 150% margin
- Bitchie retail: 130K → 163K (+25%)
- XXX retail: 145K → 185K (+28%)
- Net effect: above market, risk of low conversion

### If Sarah goes to 200% margin
- Bitchie retail: 130K → 196K (+51%)
- XXX retail: 145K → 221K (+52%)
- Net effect: well above market, ~30% conversion drop

**Recommendation:** Stay at 100% margin for launch. Test 125% at month 3.

---

## Mix Optimization (over time)

### Initial mix (Month 1–3)
- Bitchie: 60% (Sarah's flagship)
- XXX: 30% (premium SKU, lower volume)
- Wet Anal: 10% (commodity)

### Mature mix (Month 6+)
- Bitchie: 40% (mature market)
- XXX: 25%
- Wet Anal: 15%
- New SKUs (added Month 2+): 20% (Pink Pill, Like a Virgin, etc.)

---

## Risk-Adjusted Forecast

| Scenario | Probability | Year 1 units | Year 1 revenue | Year 1 net |
|----------|------------:|-------------:|---------------:|-----------:|
| 🟢 Optimistic (viral + B2B scales) | 15% | 2,900 | 377M | 169.8M |
| 🟡 Recommended | 60% | 1,450 | 188.5M | 72.7M |
| 🟠 Conservative | 20% | 450 | 58.5M | 5.7M |
| 🔴 Failure (DINAVISA blocks + audience mismatch) | 5% | <100 | <13M | <-20M |

**Probability-weighted forecast:**
- Expected units: 1,485
- Expected revenue: Gs 192.8M
- Expected net: Gs 73.2M

---

## Monthly tracking spreadsheet

Sarah should track (Google Sheet):

| Month | Units sold | Revenue | COGS | Marketing | Ops | Net | Cum cash | vs Forecast |
|------:|----------:|--------:|-----:|----------:|----:|-----:|----------:|-----------:|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| ... | | | | | | | | |

**Variance threshold:** If actual is <50% of forecast for 2 consecutive months → escalate (cut costs, revise strategy).

---

## Trigger events for forecast revision

| Event | Action |
|-------|--------|
| Q5 PDF arrives with different prices | Re-do pricing math |
| Month 1 actuals <10 units | Switch to Conservative forecast |
| Month 3 actuals >100 units | Switch to Stretch forecast |
| B2B buyer signs | Add their volume to forecast |
| DINAVISA inspection event | Pause expansion, focus on existing |
| Competitor launches similar product | Adjust pricing / add differentiator |

---

*Last updated: 2026-06-26 | Sarah: update monthly with actuals*