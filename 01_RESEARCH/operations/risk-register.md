# Risk Register — Enki Store

**Date:** June 26, 2026
**Scope:** Top 15 risks ranked by probability × impact
**Format:** Probability (1-5) × Impact (1-5) = Risk Score (1-25)

---

## Risk Matrix

| Score | Level | Action |
|------:|------:|--------|
| 18+ | 🔴 High | Address immediately, monitor weekly |
| 10-17 | 🟠 Medium | Address in next sprint, monitor monthly |
| 1-9 | 🟢 Low | Accept + monitor quarterly |

---

## Top 15 risks

### R1 — DINAVISA inspection event (regulatory shutdown)

| Field | Value |
|-------|-------|
| **Category** | Legal / regulatory |
| **Probability** | 3 (medium) |
| **Impact** | 5 (catastrophic) |
| **Score** | **15 🔴** |
| **Description** | DINAVISA inspects Enki Store and finds non-compliance (missing NSO, wrong labels, etc.) → seizure + fine + retroactive compliance |
| **Mitigation** | (1) File DINAVISA NSO immediately for 3 launch SKUs. (2) Use bilingual stickers on all Sexitive AR products. (3) Keep all documentation (Certificado de Origen, ANMAT certs, despacho papers) on file. (4) Engage despachante proactively. |
| **Owner** | Sarah + despachante |
| **Monitoring** | Quarterly DINAVISA compliance check |

### R2 — Customs seizure (modelo旅行者 detected)

| Field | Value |
|-------|-------|
| **Category** | Logistics |
| **Probability** | 3 (medium) |
| **Impact** | 4 (high) |
| **Score** | **12 🔴** |
| **Description** | Aduana PY detects pattern of personal luggage import with commercial quantities → seizure + fine + retroactive DINAVISA + criminal record possibility |
| **Mitigation** | (1) Max 1 trip/quarter. (2) Combine with personal travel (family visit). (3) Stay under 30 units/SKU per trip. (4) Switch to formal import ASAP once DINAVISA approved. (5) Never declare commercial intent. |
| **Owner** | Sarah |
| **Monitoring** | Every trip |

### R3 — Q5 PDF reveals higher costs than estimated (margin compression)

| Field | Value |
|-------|-------|
| **Category** | Financial |
| **Probability** | 4 (high) |
| **Impact** | 3 (medium) |
| **Score** | **12 🔴** |
| **Description** | Official Distribuidor Mayorista prices from Sexitive AR are higher than AR retail ÷ 2 estimate → 150% margin math doesn't work, retail prices need to rise or margin drops |
| **Mitigation** | (1) Build pricing model with 3 margin scenarios (already done in canonical-pricing-reference-v1.md). (2) Negotiate special "viajero" pricing with Sexitive AR. (3) Drop to 100% margin if needed (still beats all competitors on transparency). (4) Bundle SKUs to maintain AOV. |
| **Owner** | Sarah + Erebus |
| **Monitoring** | When Q5 PDF arrives |

### R4 — Enki's 20K IG audience doesn't convert to intimate (low engagement)

| Field | Value |
|-------|-------|
| **Category** | Marketing |
| **Probability** | 4 (high) |
| **Impact** | 3 (medium) |
| **Score** | **12 🔴** |
| **Description** | Enki's existing audience skews to general lifestyle (not intimate wellness) → low engagement on Kinky posts → slower launch |
| **Mitigation** | (1) Test small launch (10 friends/family) first to gauge response. (2) Create separate @kinky_py IG if needed. (3) Customer survey to 30 followers (already drafted in customer-survey-typeform.md). (4) Focus on B2B wholesale if DTC fails. |
| **Owner** | Sarah |
| **Monitoring** | First 30 days of launch |

### R5 — Competitor price match / undercut (Rivia, SexShop.com.py)

| Field | Value |
|-------|-------|
| **Category** | Competitive |
| **Probability** | 3 (medium) |
| **Impact** | 3 (medium) |
| **Score** | **9 🟠** |
| **Description** | Competitors detect Enki launch + match/undercut prices → Sarah loses margin advantage |
| **Mitigation** | (1) Compete on content + brand story + DINAVISA documentation (not price). (2) Build B2B wholesale channel (insulates from DTC price war). (3) Bundle pricing obscures single-SKU comparison. (4) Customer loyalty program at month 6+. |
| **Owner** | Sarah |
| **Monitoring** | Monthly competitor pricing check |

### R6 — Instagram shadowban / account suspension (intimate content)

| Field | Value |
|-------|-------|
| **Category** | Platform |
| **Probability** | 4 (high) |
| **Impact** | 3 (medium) |
| **Score** | **12 🔴** |
| **Description** | Meta (IG) flags intimate product content as adult → shadowban or account suspension → lose primary channel |
| **Mitigation** | (1) Avoid explicit words in captions/hashtags. (2) Use "wellness" / "cuidado personal" framing. (3) Build email list + TikTok as backups (different moderation). (4) Never use nudity in photos. (5) Have backup IG account ready. |
| **Owner** | Sarah |
| **Monitoring** | Daily IG analytics + reach monitoring |

### R7 — Mercado Pago account blocked (high-risk category)

| Field | Value |
|-------|-------|
| **Category** | Payment |
| **Probability** | 3 (medium) |
| **Impact** | 3 (medium) |
| **Score** | **9 🟠** |
| **Description** | Mercado Pago flags intimate product sales as high-risk → freezes account + funds |
| **Mitigation** | (1) Push bank transfer as primary payment (no MP fees, no MP risk). (2) Tigo Money as secondary. (3) MP only as last resort. (4) Keep MP funds moving (don't let balance accumulate). |
| **Owner** | Sarah |
| **Monitoring** | Weekly MP account health check |

### R8 — Sarah burnout / time constraint (sole operator)

| Field | Value |
|-------|-------|
| **Category** | Operational |
| **Probability** | 4 (high) |
| **Impact** | 4 (high) |
| **Score** | **16 🔴** |
| **Description** | Sarah operates alone (or with minimal help) → hours exceed capacity → orders delayed, customer service suffers, growth stalls |
| **Mitigation** | (1) Hire part-time helper at month 2 (pack + ship = 10h/week minimum). (2) Document SOPs early (this repo + whatsapp-business-setup.md). (3) Set WA auto-reply outside hours. (4) Use templates (customer-messages.md). (5) Mom or family as backup packer. |
| **Owner** | Sarah |
| **Monitoring** | Weekly time audit |

### R9 — Counterfeit Sexitive products enter PY (brand erosion)

| Field | Value |
|-------|-------|
| **Category** | Brand |
| **Probability** | 2 (low) |
| **Impact** | 4 (high) |
| **Score** | **8 🟠** |
| **Description** | Counterfeit Sexitive products from CN or elsewhere enter PY market at lower price → erodes brand value + confuses customers |
| **Mitigation** | (1) Use unique Enki stickers on all products (visual proof of legit). (2) Marketing emphasizes "importado directo de Sexitive AR." (3) DINAVISA paperwork as proof. (4) Report counterfeits to Sexitive AR + DINAPI. |
| **Owner** | Sarah + Erebus |
| **Monitoring** | Quarterly competitor audit |

### R10 — FX rate shock (Gs/AR$ moves from 4:1 to 5:1)

| Field | Value |
|-------|-------|
| **Category** | Financial |
| **Probability** | 3 (medium) |
| **Impact** | 4 (high) |
| **Score** | **12 🔴** |
| **Description** | Argentine peso devalues further against Guaraní → all input costs rise 25% → margin collapses if retail prices stay fixed |
| **Mitigation** | (1) Build 10-15% FX buffer into retail prices. (2) Order larger batches when FX is favorable. (3) Renegotiate retail prices quarterly based on FX. (4) Consider USD-denominated contracts with Sexitive AR. |
| **Owner** | Sarah |
| **Monitoring** | Weekly FX rate check |

### R11 — Competitor reports Enki to Meta/DINAVISA (malicious complaint)

| Field | Value |
|-------|-------|
| **Category** | Competitive / platform |
| **Probability** | 2 (low) |
| **Impact** | 4 (high) |
| **Score** | **8 🟠** |
| **Description** | PY competitor reports Enki IG to Meta for "adult content" → shadowban; or reports to DINAVISA for non-compliance |
| **Mitigation** | (1) Keep DINAVISA documentation on file (full compliance). (2) Use "wellness" framing in IG content. (3) If shadowban: appeal to Meta + have backup account. (4) If DINAVISA complaint: respond with full documentation. |
| **Owner** | Sarah |
| **Monitoring** | Monthly IG reach + DINAVISA status |

### R12 — Sexitive AR raises prices (supplier moves)

| Field | Value |
|-------|-------|
| **Category** | Supplier |
| **Probability** | 2 (low) |
| **Impact** | 4 (high) |
| **Score** | **8 🟠** |
| **Description** | Sexitive AR raises Distribuidor Mayorista prices 10-20% → Sarah's margin compressed |
| **Mitigation** | (1) Lock pricing for 6 months (contract). (2) Diversify suppliers (Bezzi AR, Brazilian brands). (3) Pass through to retail. (4) Build private-label SKU as alternative. |
| **Owner** | Sarah |
| **Monitoring** | Per order |

### R13 — Contador + despachante don't exist (no qualified vendors)

| Field | Value |
|-------|-------|
| **Category** | Vendor |
| **Probability** | 1 (very low) |
| **Impact** | 4 (high) |
| **Score** | **4 🟢** |
| **Description** | Cannot find PY contador + despachante with cosmetics experience → regulatory blocked |
| **Mitigation** | (1) Multiple outreach (5 candidates each, per py-vendor-shortlist.md). (2) Backup: generalist contador + accept higher uncertainty. (3) Long-term: train someone. |
| **Owner** | Sarah |
| **Monitoring** | Week 1 of P1 phase |

### R14 — Customer allergic reaction (product safety)

| Field | Value |
|-------|-------|
| **Category** | Product safety |
| **Probability** | 2 (low) |
| **Impact** | 5 (catastrophic) |
| **Score** | **10 🟠** |
| **Description** | Customer has allergic reaction to Sexitive product → injury claim + reputational damage + potential lawsuit |
| **Mitigation** | (1) Clear warning labels (Spanish, ingredient list). (2) Sample sachet for first-time buyers (lower risk). (3) Record all ingredients per SKU. (4) Liability insurance at month 6+ (Gs 500K-1.5M/year). (5) Document all incidents (return SOP). |
| **Owner** | Sarah |
| **Monitoring** | Per incident |

### R15 — Cash flow crisis (negative cumulative > Gs 10M)

| Field | Value |
|-------|-------|
| **Category** | Financial |
| **Probability** | 2 (low) |
| **Impact** | 5 (catastrophic) |
| **Score** | **10 🟠** |
| **Description** | Cumulative cash burn exceeds Gs 10M (Sarah's full capital) → business can't continue |
| **Mitigation** | (1) Track monthly cash flow (per cash-flow-model-12mo.md). (2) If trending negative at month 3-4: pause modelo旅行者, cut discretionary costs. (3) Secure bridge capital (loan from family/Gaston) by month 4 if needed. (4) Worst case: pause B2B outreach, focus DTC. |
| **Owner** | Sarah |
| **Monitoring** | Monthly cash flow review |

---

## Risk score summary

| Risk | Score | Level |
|------|------:|-------|
| R8 — Sarah burnout | 16 | 🔴 |
| R1 — DINAVISA inspection | 15 | 🔴 |
| R2 — Customs seizure | 12 | 🔴 |
| R3 — Q5 PDF higher costs | 12 | 🔴 |
| R4 — IG audience mismatch | 12 | 🔴 |
| R6 — IG shadowban | 12 | 🔴 |
| R10 — FX rate shock | 12 | 🔴 |
| R14 — Allergic reaction | 10 | 🟠 |
| R15 — Cash flow crisis | 10 | 🟠 |
| R5 — Competitor price match | 9 | 🟠 |
| R7 — MP account blocked | 9 | 🟠 |
| R9 — Counterfeit products | 8 | 🟠 |
| R11 — Malicious competitor report | 8 | 🟠 |
| R12 — Sexitive price raise | 8 | 🟠 |
| R13 — No qualified vendors | 4 | 🟢 |

**Total risk score:** 137 (out of 375 max for 15 risks)
**Average risk:** 9.1 (medium)

---

## Top 3 risks to address in Week 1

1. **R8 (burnout)** — Document SOPs now (this repo). Hire part-time by month 2.
2. **R1 (DINAVISA)** — Engage despachante Week 1, file NSOs Week 2.
3. **R4 (IG audience)** — Run customer survey to 30 followers BEFORE launch to validate.

---

## Top 5 risks to monitor monthly

- R3 (Q5 PDF costs) — when PDF arrives
- R6 (IG shadowban) — daily analytics
- R10 (FX rate) — weekly check
- R14 (allergic reactions) — per incident
- R15 (cash flow) — monthly review

---

## Quarterly review

Every quarter (Sept, Dec, Mar, Jun), review:
- All 15 risks with new probability/impact scores
- New risks identified
- Mitigation effectiveness
- Update this register

---

*Last updated: 2026-06-26 | Review quarterly*