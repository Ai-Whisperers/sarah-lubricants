# README — Sarah's Lubricant Business (Ai-Whisperers)

**Live site (preview):** https://sarah.paragu-ai.com
**Repo:** https://github.com/Ai-Whisperers/sarah-lubricants
**Status:** Strategy + research phase — e-commerce site NOT YET BUILT
**Last updated:** June 26, 2026 (Session 7 — research wave 2 complete)

---

## What this is

This repository is the **strategic source of truth** for Sarah Roig's intimate-wellness distribution business in Paraguay. Sarah is the operator; Ai-Whisperers (Erebus) provides strategy, research, and tooling.

The actual e-commerce site will live in the `paragu-ai-platform` monorepo when build time comes. This repo contains:

- 📊 Market research (competitor analysis, PY pricing, demand data)
- 📋 Business strategy (launch plan, budget, pricing model)
- 📝 Sarah's intake responses + our follow-up questions
- 🔬 Vendor + legal + tax research
- 🛠️ Static site build (the preview at sarah.paragu-ai.com)

---

## The business in one paragraph

Sarah Roig (RUC 4978694-6, @enkistore IG with 20K followers) is launching **Enki Store + Kinky** as an intimate-wellness brand in Paraguay, distributing **Sexitive Argentina products** (158 SKUs across lubricants, stimulants, perfumes, massage oils, candles, lingerie, kits, and games). Launch trio: **Bitchie 20ml + XXX For Her 15ml + Wet Anal 75ml**. Target margin: 100–150%. 90-day launch budget: < Gs 10M. Channels: WhatsApp Business (primary) + Instagram organic (secondary) + B2B wholesale to PY sex shops (largest lever).

---

## Brand architecture

```
ENKI STORE (parent brand)
├── Kinky (sub-brand / sección interna)
│   ├── Lubricantes
│   ├── Estimulantes
│   └── Suplementos (v2)
├── Enki Lencería (existing)
└── Enki Juguetes (Sexitive toy line — v2)
```

**Decision history:**
- June 19: Provisional name "Kinky Store" considered
- June 22: Sarah confirmed (Q3) = **"Enki Store" is the registered brand**; "Kinky" is sub-brand
- June 26: Architecture locked

See [`01_RESEARCH/brand-identity/enki-store-assessment.md`](./01_RESEARCH/brand-identity/enki-store-assessment.md).

---

## Launch trio (LOCKED June 22, 2026)

| SKU | Product | Size | DINAVISA |
|-----|---------|------|----------|
| **SEFB** | Bitchie Spray multiorgásmico | 20ml | Cosmético NSO |
| **XXX01** | XXX For Her óleo orgasmico | 15ml | Cosmético NSO |
| **WET02** | Wet Gel Lubricante Anal | 75ml | Cosmético NSO |

**Sarah's decisions (Q1–Q4, June 22):**
- Q1 (a): Drop Pink Sexy Pill from v1 (register from revenue month 3–6)
- Q2: Wet Anal (not Like a Virgin) — volume-over-differentiation trade-off
- Q3: Brand = Enki Store, Kinky = sección
- Q4: Has Distribuidor Mayorista pricing (verbal, PDF pending)

See [`01_RESEARCH/brand-identity/launch-SKU-list-3-SKUs.md`](./01_RESEARCH/brand-identity/launch-SKU-list-3-SKUs.md).

---

## Key numbers (canonical pricing v1)

| Metric | Value |
|--------|------:|
| Launch trio cost (30u each, 90 units) | Gs 2,386,200 |
| Total landed (with DINAVISA + despachante + freight) | Gs 6,265,000 |
| Recommended retail (100% margin) | Gs 125K–145K per SKU |
| Stretch retail (150% margin) | Gs 157K–218K per SKU |
| Month 3 target (80 units) | Gs 10.65M revenue / Gs 5.27M margin |
| 6-month stretch (200 units/mo) | Gs 57M+ revenue |

See [`00_STRATEGIC/financial-pricing/canonical-pricing-reference-v1.md`](./00_STRATEGIC/financial-pricing/canonical-pricing-reference-v1.md).

---

## Quick orientation

| If you want... | Read this |
|----------------|-----------|
| Understand the whole project | [`start-here.md`](./start-here.md) |
| See all docs (file-by-file) | [`COMPLETE-INDEX.md`](./COMPLETE-INDEX.md) |
| Check what's done / what's next | [`TODO.md`](./TODO.md) |
| Understand the launch math | [`00_STRATEGIC/financial-pricing/launch-budget-under-10M.md`](./00_STRATEGIC/financial-pricing/launch-budget-under-10M.md) |
| See the master product catalog (158 SKUs) | [`01_RESEARCH/market/sexitive-catalog-master.md`](./01_RESEARCH/market/sexitive-catalog-master.md) |
| See scraped competitor data | [`01_RESEARCH/competition/competitor-pricing-scraped.md`](./01_RESEARCH/competition/competitor-pricing-scraped.md) |
| See B2B wholesale targets | [`01_RESEARCH/market/py-sex-shop-directory.md`](./01_RESEARCH/market/py-sex-shop-directory.md) |
| Brand architecture decision | [`01_RESEARCH/brand-identity/enki-store-assessment.md`](./01_RESEARCH/brand-identity/enki-store-assessment.md) |
| Compliance roadmap (DINAVISA + SET + tax) | [`01_RESEARCH/legal-regulatory/py-compliance-roadmap.md`](./01_RESEARCH/legal-regulatory/py-compliance-roadmap.md) |
| Sales channels ranked (15) | [`01_RESEARCH/marketing/sales-channels-matrix.md`](./01_RESEARCH/marketing/sales-channels-matrix.md) |
| Sales scripts + objection handling | [`01_RESEARCH/marketing/competitor-battle-cards.md`](./01_RESEARCH/marketing/competitor-battle-cards.md) |
| 30-day IG launch calendar | [`06_MARKETING/instagram-launch-calendar-30d.md`](./06_MARKETING/instagram-launch-calendar-30d.md) |
| SEO content pillar (38 blog posts) | [`06_MARKETING/seo-content-pillar.md`](./06_MARKETING/seo-content-pillar.md) |
| Customer survey (Typeform) | [`01_RESEARCH/market/customer-survey-typeform.md`](./01_RESEARCH/market/customer-survey-typeform.md) |
| E-commerce platform decision | [`01_RESEARCH/operations/ecom-platform-decision.md`](./01_RESEARCH/operations/ecom-platform-decision.md) |
| Email platform decision (Brevo) | [`01_RESEARCH/operations/email-platform-decision.md`](./01_RESEARCH/operations/email-platform-decision.md) |
| Fulfillment + courier options | [`01_RESEARCH/logistics-supplier/py-fulfillment-options.md`](./01_RESEARCH/logistics-supplier/py-fulfillment-options.md) |
| PY packaging suppliers (6 imprentas) | [`01_RESEARCH/logistics-supplier/py-packaging-suppliers.md`](./01_RESEARCH/logistics-supplier/py-packaging-suppliers.md) |
| Keyword research + Google Trends PY | [`01_RESEARCH/marketing/keyword-demand-py.md`](./01_RESEARCH/marketing/keyword-demand-py.md) |
| PY micro-influencer list (50 creators) | [`01_RESEARCH/marketing/py-micro-influencer-list.md`](./01_RESEARCH/marketing/py-micro-influencer-list.md) |
| LatAm competitive landscape | [`01_RESEARCH/market/latam-intimate-competitive-landscape.md`](./01_RESEARCH/market/latam-intimate-competitive-landscape.md) |
| Modelo viajero strategy | [`01_RESEARCH/operations/modelo-viajero-strategy.md`](./01_RESEARCH/operations/modelo-viajero-strategy.md) |
| WhatsApp Business setup guide | [`08_WHATSAPP/whatsapp-business-setup.md`](./08_WHATSAPP/whatsapp-business-setup.md) |
| WhatsApp catalog content (trio) | [`08_WHATSAPP/whatsapp-catalog-launch-trio.md`](./08_WHATSAPP/whatsapp-catalog-launch-trio.md) |
| Customer message templates | [`09_TEMPLATES/customer-messages.md`](./09_TEMPLATES/customer-messages.md) |
| Executive summary (Ivan/Kiki) | [`docs/executive-summary.md`](./docs/executive-summary.md) |
| Glossary (Sexitive/PY terms) | [`docs/glossary.md`](./docs/glossary.md) |
| Sarah's intake form | [`01_RESEARCH/legal-regulatory/validacion-cliente-sarah.md`](./01_RESEARCH/legal-regulatory/validacion-cliente-sarah.md) |
| Sarah's questionnaire response | [`02_MEETINGS/2026-06-20-questionnaire-response.md`](./02_MEETINGS/2026-06-20-questionnaire-response.md) |
| 21 Round 2 questions (A-F) | [`02_MEETINGS/2026-06-22-round-2-questions.md`](./02_MEETINGS/2026-06-22-round-2-questions.md) |
| | Audio prompt pack for Sarah | [`02_MEETINGS/2026-06-22-audio-prompt-pack.md`](./02_MEETINGS/2026-06-22-audio-prompt-pack.md) |
| | Sarah's action checklist (this week) | [`01_RESEARCH/operations/this-week-for-sarah.md`](./01_RESEARCH/operations/this-week-for-sarah.md) |
| | What we KNOW vs ASSUMED | [`01_RESEARCH/operations/validation-status.md`](./01_RESEARCH/operations/validation-status.md) |
| | What we DON'T know | [`01_RESEARCH/operations/gaps-and-unknowns.md`](./01_RESEARCH/operations/gaps-and-unknowns.md) |
| | Decisions made (chronological) | [`01_RESEARCH/operations/decision-log.md`](./01_RESEARCH/operations/decision-log.md) |
| | Sarah's daily/weekly/monthly work | [`05_OPERATIONS/daily-checklist.md`](./05_OPERATIONS/daily-checklist.md) |
| | 1-page launch roadmap (print) | [`03_LAUNCH/launch-roadmap-1page.md`](./03_LAUNCH/launch-roadmap-1page.md) |
| | Repo audit + critique | [`01_RESEARCH/operations/repo-audit-roast-jun26.md`](./01_RESEARCH/operations/repo-audit-roast-jun26.md) |
| | 5 questions SENT to Sarah (June 20) | [`02_MEETINGS/2026-06-20-clarifying-questions-asked.md`](./02_MEETINGS/2026-06-20-clarifying-questions-asked.md) |
| | 5 questions ANSWERED by Sarah (June 22) | [`02_MEETINGS/2026-06-22-clarifying-questions-answered.md`](./02_MEETINGS/2026-06-22-clarifying-questions-answered.md) |
| | Pricing calculator (Python tool) | [`tools/pricing_calculator.py`](./tools/pricing_calculator.py) |
| | TikTok PY audit | [`06_MARKETING/tiktok-py-audit.md`](./06_MARKETING/tiktok-py-audit.md) |
| | Customer onboarding flow | [`04_SALES/customer-onboarding-flow.md`](./04_SALES/customer-onboarding-flow.md) |
| | 90-day KPI dashboard | [`03_LAUNCH/90-day-kpi-dashboard.md`](./03_LAUNCH/90-day-kpi-dashboard.md) |

---

## Build / deploy

This repo has a static site generator at `tools/build_site.py` that compiles the markdown to HTML at `build/`. The site is deployed to Cloudflare Pages at `sarah.paragu-ai.com` (preview only — NOT customer-facing).

```bash
cd /root/repos/sarah-lubricants
python3 tools/build_site.py    # Build HTML
bash tools/deploy.sh           # Deploy to Cloudflare
```

---

## Repo structure

```
sarah-lubricants/
├── 00_STRATEGIC/         # Strategy + financial planning
├── 01_RESEARCH/          # Market, competitor, legal, brand, operations, payments, marketing research
├── 02_MEETINGS/          # All conversation logs with Sarah
├── 03_LAUNCH/            # Launch roadmap + checklists (TBD)
├── 04_SALES/             # Sales scripts, objection handling (TBD)
├── 05_OPERATIONS/        # Pack-ship SOPs, inventory (TBD)
├── 06_MARKETING/         # IG strategy, content calendar
├── 07_DESIGN/            # Brand assets, logo (TBD)
├── 08_WHATSAPP/          # WA Business setup, broadcasts (TBD)
├── 09_TEMPLATES/         # Customer-facing templates (TBD)
├── docs/                 # Anakyze of fleet, glossary, references
├── tools/                # Static site builder + deploy scripts
├── content/              # (TBD) Source content for static site
└── build/                # Auto-generated HTML output
```

---

## Active blockers

1. 🔴 **Q5 PDF from Sexitive AR** — Sarah hasn't sent the official wholesale price list
2. 🔴 **DINAPI Enki classes verified** — Sarah hasn't confirmed classes 3, 5, 35
3. 🔴 **Contador engaged** — RUC + tax compliance unverified
4. 🔴 **Despachante engaged** — DINAVISA + import process not started

When blockers clear, launch is feasible in 3–4 weeks.

---

## Repository rules (AGENTS.md)

- Every session doc persists to `/02_MEETINGS/` with date stamp
- Decisions go to `/00_STRATEGIC/` or topic-specific `/01_RESEARCH/`
- TBD docs are placeholder index entries — fill or remove
- Never invent SKUs not in Sexitive catalog
- Sarah's responses always quoted verbatim from WhatsApp

---

*Last updated: 2026-06-26 — 90 markdown docs (was 84), 5 Python scripts, 100+ HTML build files, **repo audit + upgrade complete (Session 10)**