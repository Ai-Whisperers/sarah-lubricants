# Sarah's Lubricant Business — Strategy & Launch Kit

**Last updated:** June 19, 2026

---

## 🌐 Live (preview)

🔗 **https://sarah.paragu-ai.com** — read-only strategy & questionnaire site (deployed to Cloudflare Pages).

| Section | URL |
|---------|-----|
| Home (navigation hub) | https://sarah.paragu-ai.com/ |
| **Questionnaire (Sarah's homework)** | https://sarah.paragu-ai.com/questionnaire |
| Start here (5 min) | https://sarah.paragu-ai.com/start-here |
| Product catalog (12 SKUs) | https://sarah.paragu-ai.com/catalog |
| Market snapshot | https://sarah.paragu-ai.com/market |
| DINAVISA legal | https://sarah.paragu-ai.com/legal |
| MERCOSUR tariffs | https://sarah.paragu-ai.com/mercosur |
| 3 business models | https://sarah.paragu-ai.com/models |
| Sexitive AR contact | https://sarah.paragu-ai.com/supplier |
| Freight AR→PY | https://sarah.paragu-ai.com/freight |
| 5 competitors | https://sarah.paragu-ai.com/competition |
| Payments (Tigo, bank, MP) | https://sarah.paragu-ai.com/payments |
| Brand names | https://sarah.paragu-ai.com/brand |
| Operations SOP | https://sarah.paragu-ai.com/operations |
| Full index | https://sarah.paragu-ai.com/COMPLETE-INDEX |

**Local source repo:** `/root/sarah-lubricants/` (this is the strategy + content source of truth)
**Build output:** `build/` (auto-rendered to HTML from all `.md` files)
**Deploy:** `tools/deploy.sh` → Cloudflare Pages project `sarah-lubricants`

This is the **strategic source of truth** for launching Sarah's intimate-wellness distribution business in Paraguay. It is **not** the runtime code — when we get to that point, the website will live in `Ai-Whisperers/paragu-ai-platform` (or a fresh repo if Sarah prefers full white-label).

**Source product:** Sexitive (Argentina) — 12 SKUs across 4 categories: stimulants, lubricants, sensory/ambiance, wellness.

**Working hypothesis:** Sarah imports Sexitive products from Buenos Aires and resells in Paraguay, either as authorized distributor, independent reseller, or private-label rebrand (decision pending — see `01_RESEARCH/legal-regulatory/validacion-cliente-sarah.md` Section 2).

---

## Why this repo exists

1. **Single source of truth** — the Sexitive catalog is real but spans 12 SKUs in 4 regulatory categories. If we don't centralize the product data, we'll misclassify something at the customs or DINAVISA stage and lose money.
2. **Intake before build** — intimate-wellness import is a regulated business. We cannot write code before Sarah answers ~30 questions on legal model, costs, brand, and ops. The questionnaire is in `01_RESEARCH/legal-regulatory/validacion-cliente-sarah.md`.
3. **Pre-mortem before launch** — the PY market has at least 5 established sex-shop retailers (sexshop.com.py, Rivia, Intimos Placeres, As Bajo La Manga, Sex Shop Paraguay). The strategy must differentiate or Sarah competes on price against incumbents.

---

## Quick Start

1. **START HERE:** `start-here.md` (5 min)
2. **Questionnaire for Sarah:** `01_RESEARCH/legal-regulatory/validacion-cliente-sarah.md` (Sarah's homework, ~30 min)
3. **Product catalog:** `01_RESEARCH/market/sexitive-catalog-master.md` (Sexitive's 12 SKUs)
4. **Market snapshot:** `01_RESEARCH/market/paraguay-market-snapshot.md` (competition + sizing)
5. **Legal roadmap:** `01_RESEARCH/legal-regulatory/dinavisa-import-requirements.md` (DINAVISA + customs)

---

## Project Summary

Sarah is bringing Sexitive (Argentine intimate-wellness brand) to Paraguay. The catalog has 12 SKUs across 4 categories. The business is feasible but has 3 hard dependencies before any code:

1. **Legal model** — authorized distributor, independent reseller, or private label.
2. **Cost basis** — what Sarah actually pays for each SKU at her tier (wholesale? direct from Sexitive? via MercadoLibre AR arbitrage?).
3. **Regulatory** — DINAVISA classification per SKU, import permits, supplement registration for Pink Sexy Pill, CBD handling for My Hemp.

If those three are answered, the rest (brand, web, marketing, ops) is execution. If they're not, we build on sand.

---

## Directory Structure

| Folder | Content |
|--------|---------|
| `00_STRATEGIC/` | Strategic, financials, positioning |
| `01_RESEARCH/` | Market, legal, competition, supplier, payments, brand |
| `02_MEETINGS/` | Sarah sessions, intake prep, archives |
| `03_LAUNCH/` | Roadmap, sales playbooks, website |
| `04_SALES/` | Sales scripts, pricing strategy |
| `05_OPERATIONS/` | Fulfillment, returns, customer service |
| `06_MARKETING/` | Digital presence, content calendar |
| `07_DESIGN/` | Brand + website |
| `08_WHATSAPP/` | WhatsApp catalog + automation |
| `09_TEMPLATES/` | Client / customer templates |
| `docs/` | Planning, indexes, executive summary |
| Root MD | README, TODO, start-here, agents |

---

## Entry Points

| Doc | Purpose |
|-----|---------|
| `start-here.md` | Project overview + option summary |
| `docs/executive-summary.md` | Current status and next block |
| `TODO.md` | Phase tracker (P0–P5) |
| `docs/REPO-WORK-PLAN.md` | Phased execution plan |
| `01_RESEARCH/legal-regulatory/validacion-cliente-sarah.md` | **Sarah's homework — 30 questions, 6 sections** |

---

## Status legend

- ✅ Complete
- 🟡 In progress
- 🔴 Blocked (waiting on Sarah or external)
- ⚪ Not started
