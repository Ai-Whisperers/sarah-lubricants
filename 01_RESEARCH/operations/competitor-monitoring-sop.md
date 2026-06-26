# Competitor Monitoring SOP

**Date:** June 26, 2026
**Purpose:** Systematic way to track what 5 PY competitors do
**Use:** Run weekly, log to a spreadsheet, alert on material changes

---

## Why monitor competitors

- ✅ Detect price changes before customers do
- ✅ Spot new product launches (and how they're positioned)
- ✅ Identify promotional patterns (sales, bundles)
- ✅ Catch B2B / wholesale moves (if a competitor starts selling to other shops)
- ✅ Track social media metrics (IG growth, engagement)
- ✅ Defensive intel (when something works for them, consider replicating)

---

## The 5 real competitors (updated June 26, 2026)

| # | Name | URL | IG | Differentiator |
|---|------|-----|-----|----------------|
| 1 | **SexShop.com.py** | https://sexshop.com.py | @sexshopcompy | Largest banner pricing, privacy focus |
| 2 | **Rivia** | https://www.rivia.com.py | @rivia | Modern Shopify UX, 12 collections, English-named products |
| 3 | **Íntimos Placeres** | https://www.intimosplaceres.com.py | @intimosplaceresoficial | Vibrator-focused, Barbara Jack brand |
| 4 | **As Bajo La Manga** | https://www.asbajolamanga.com.py | (verify) | Lingerie-first, **already resells Sexitive** |
| 5 | **Mencanta** | https://mencanta.com.py | (verify) | Multi-category, 10+ categories, WA-asistoria |

**False positives (not competitors):**
- lubricantesparaguay.com.py (industrial lubricants)
- lubribras.com.py (auto lubricants)
- SexShopAsuncion (sister site to SexShop.com.py, same operator)
- Hendyla (general marketplace)

---

## What to monitor (per competitor, per week)

### Pricing
- Top 20 SKU prices (per category)
- Bundle pricing
- Shipping costs
- Payment methods (any new ones?)

### Product catalog
- New SKUs (added since last week)
- Discontinued SKUs
- Categorization changes
- Brand additions (any new brands?)

### Promotions
- Active sales (% off, bundle deals, BOGO)
- Free shipping thresholds
- Coupon codes
- Flash sales (limited time)

### Channel activity
- IG posts per week
- IG stories per week
- IG engagement rate (likes/comments per post)
- New IG followers
- TikTok activity (if any)
- WA Business activity (catalog changes, profile changes)

### Customer experience
- Site UX (any major redesigns)
- Shipping speed (order + see)
- Customer reviews (Google, Trustpilot if any)
- Complaint patterns (Reddit, Twitter, social)

### B2B / wholesale
- New wholesale inquiries
- Distributor programs
- Bulk pricing visibility

---

## How to monitor (free tools)

### Option 1: Manual weekly check (30-45 min/week)

```
Sunday 10pm routine:
1. Visit each of 5 competitor sites
2. Note 5-10 changes per site (price, new SKU, promo)
3. Check their IG (last 5 posts + follower count)
4. Log to Google Sheet
5. Flag any material change (price >10% change, new brand)
```

### Option 2: Automated scraping (1 hour setup + 5 min/week)

Build a Python scraper that:
- Hits each competitor site weekly
- Compares current prices to last week
- Sends alert if any SKU changed >10%
- Saves to JSON/CSV

```python
# tools/competitor_monitor.py (future build)
# 1. Fetch SexShop.com.py, Rivia, etc.
# 2. Extract product + price
# 3. Diff vs. last week
# 4. Alert via WA Business API if changes detected
```

### Option 3: Hybrid (recommended for Sarah v1)

- **Manual:** 30 min weekly for catalog + pricing
- **Subscription-based:** Visualping or ChangeTower ($10-20/mo each) for "alert when competitor site changes"
- **Social:** Manual IG check (5 min per competitor)

---

## Competitor monitoring spreadsheet

### Sheet 1: Weekly price snapshot

| Date | Competitor | SKU | Price (Gs) | Change vs. last week | Notes |
|------|-----------|-----|-----------:|---------------------:|-------|
| 2026-07-06 | SexShop.com.py | Wet Anal 75ml | 80,000 | -10% | First time they carry Sexitive product |
| 2026-07-06 | Rivia | (no Sexitive) | — | — | No overlap |

### Sheet 2: IG metrics

| Date | Competitor | Followers | New (week) | Avg post engagement | Top post reach |
|------|-----------|----------:|-----------:|---------------------:|----------------:|
| 2026-07-06 | SexShop.com.py | 8,200 | +50 | 2.3% | 5,400 |
| 2026-07-06 | Rivia | 5,100 | +30 | 1.8% | 2,100 |
| 2026-07-06 | Mencanta | 2,400 | +15 | 1.2% | 800 |
| 2026-07-06 | As Bajo La Manga | 1,800 | +20 | 0.9% | 600 |
| 2026-07-06 | Íntimos Placeres | 950 | +5 | 0.5% | 300 |

### Sheet 3: Catalog changes

| Date | Competitor | Change | New SKU | Price | Discontinued |
|------|-----------|--------|---------|-------:|--------------|
| 2026-07-06 | SexShop.com.py | +2 SKUs | Wet Anal 75ml | 80K | — |
| 2026-07-06 | Rivia | No change | — | — | — |
| 2026-07-06 | Mencanta | +5 SKUs | (various) | 40-120K | — |

### Sheet 4: Promotions

| Date | Competitor | Promo | Discount | Valid until |
|------|-----------|-------|----------:|------------|
| 2026-07-06 | SexShop.com.py | San Valentín early-bird | 15% off | Feb 10 |
| 2026-07-06 | Rivia | Bundle: trio | 2x1 in 3rd | Aug 30 |

---

## Alert thresholds (when to act)

| Trigger | Action | Owner | Lead time |
|---------|--------|-------|----------|
| Competitor drops price >20% on Sarah's SKU | Re-evaluate pricing | Erebus | 1 day |
| Competitor launches Sarah's unique product | Differentiate harder | Sarah | 1 week |
| Competitor opens B2B / wholesale program | Defensive outreach | Sarah | 2 weeks |
| Competitor crosses 50K IG followers | Increase paid budget | Sarah | 1 month |
| Competitor launches new category | Consider adding category | Sarah + Erebus | 1 quarter |
| New competitor enters market | Full audit (like Mencanta) | Erebus | 2 weeks |

---

## What NOT to do

- ❌ Don't obsess daily — weekly is enough
- ❌ Don't copy competitors blindly (they may have wrong strategy)
- ❌ Don't assume competitors know your market better than you
- ❌ Don't publicly compare prices ("we're 20% cheaper than X") — unprofessional
- ❌ Don't trash competitors on social media

---

## Sarah's weekly competitor check (30 min)

```
Sunday 10pm (or whenever convenient):

1. (10 min) Visit 5 competitor sites:
   - sexshop.com.py
   - rivia.com.py
   - intimosplaceres.com.py
   - asbajolamanga.com.py
   - mencanta.com.py
   - Note: 1-2 product price changes each

2. (10 min) Check 5 IG accounts:
   - @sexshopcompy
   - @rivia
   - @intimosplaceresoficial
   - @asbajolamanga (if exists)
   - Mencanta (search)
   - Note: any new content, engagement changes

3. (5 min) Update Google Sheet
   - Price changes
   - New SKUs
   - Notable IG posts
   - Any B2B activity

4. (5 min) If anything material:
   - Discuss with Erebus
   - Decide if action needed
   - Log decision
```

---

## Quarterly deep audit (every 3 months, half-day)

- Full site scrape of all 5 competitors
- Re-scrape IG analytics
- Update competitor profiles (`01_RESEARCH/competition/competitor-profiles-5.md`)
- Look for new entrants
- Look for new category trends
- Review pricing trends (averages, ranges, direction)

---

*Last updated: June 26, 2026 — Session 11*