# Decision Log — Enki Store

**Date:** June 26, 2026 (rebuilt)
**Purpose:** Chronological record of every major decision made in this project
**Use:** Future sessions reference this to understand why things are the way they are

---

## Decision format

```
## [Date] — [Decision title]

**Context:** What was the question?
**Options considered:** What were the choices?
**Decision:** What was decided?
**Why:** What was the reasoning?
**Status:** ✅ Done / 🟡 In progress / 🔴 Blocked
**Owner:** Who made/owns the decision?
```

---

## 🗓️ Project timeline

### June 19, 2026 — Initial repo + 12-SKU catalog

**Context:** Sarah wants to bring Sexitive (Argentine intimate-wellness brand) to Paraguay. Initial scope.

**Decision:** Created strategy repo. Documented 12-SKU initial catalog. Built 30-question intake for Sarah.

**Why:** Get organized before deeper research. Capture assumptions explicitly.

**Status:** ✅
**Owner:** Erebus

---

### June 20, 2026 — Sarah's questionnaire response

**Context:** Sarah filled out the 30-question intake form.

**Decision:** Processed her responses. Identified 3 blockers:
1. Legal model (distributor / reseller / private label)
2. Cost basis per SKU
3. Launch SKU selection

**Why:** Need these 3 answers to make any strategic decision.

**Status:** ✅
**Owner:** Erebus

---

### June 20, 2026 — Provisional "Kinky Store" assessment

**Context:** Sarah indicated interest in "Kinky Store" as brand name.

**Decision:** Wrote Kinky Store assessment as provisional brand direction.

**Why:** Have a starting point to react to.

**Status:** 🔴 DEPRECATED June 22 — see next decision

**Note:** This file still exists at `01_RESEARCH/brand-identity/kinky-store-assessment.md` but is now archived. Do not use for current decisions.

---

### June 22, 2026 — Brand = Enki Store, Kinky = sub-brand

**Context:** Sarah's Q3 response revealed the registered brand is "Enki Store" (not "Kinky Store"). "Kinky" is a sub-brand within Enki.

**Decision:**
- Parent brand: **Enki Store** (existing @enkistore IG, 20K followers, RUC 4978694-6)
- Sub-brand: **Kinky** (intimate-wellness section inside Enki)

**Why:** Use the existing brand asset (Enki's audience + DINAPI + history) for Kinky launch.

**Status:** ✅ Locked
**Owner:** Sarah + Erebus

---

### June 22, 2026 — Launch trio = Bitchie + XXX + Wet Anal

**Context:** Sarah picked which SKUs to launch with.

**Decision:**
- ✅ **Bitchie 20ml** (multiorgasmic spray, Sexitive bestseller)
- ✅ **XXX For Her 15ml** (female orgasmic oil)
- ✅ **Wet Anal 75ml** (commodity lubricant)
- ❌ Pink Sexy Pill (deferred — supplement registration = 90-180 days, 4-8M Gs)
- ❌ My Hemp CBD (deferred — zona gris, no DINAVISA pathway)

**Why:** Sarah chose Q1=(a) drop PSP + Q2="lubricante anal". Volume-over-differentiation strategy.

**Status:** ✅ Locked
**Owner:** Sarah

---

### June 22, 2026 — Pricing math: 100% margin recommended

**Context:** At 150% margin + Gs 10M + 3 SKUs × 30u, math doesn't fit.

**Decision:** **Recommend 100% margin** (not 150%):
- Bitchie Gs 130K
- XXX For Her Gs 145K
- Wet Anal Gs 125K

**Why:** 150% margin puts Sarah above PY market range. 100% beats 5/5 PY competitors on price transparency.

**Status:** 🟡 Provisional until Q5 PDF validates cost basis
**Owner:** Erebus

---

### June 26, 2026 — Modelo旅行者 strategy approved

**Context:** Sarah's June 17 trip brought goods as personal luggage, saving ~Gs 1.7M per shipment.

**Decision:** Document modelo旅行者 strategy. Recommend first 2 shipments use it. Switch to formal import by shipment 3 (once DINAVISA approved).

**Why:** 28-32% landed cost savings. Personal luggage legal path is well-defined.

**Status:** 🟡 Pending Sarah's confirmation (decision tree in `this-week-for-sarah.md`)
**Owner:** Sarah + Erebus

---

### June 26, 2026 — Email platform = Brevo

**Context:** Compared Mailchimp vs Brevo vs ActiveCampaign vs Mailrelay for PY market.

**Decision:** **Brevo** for email (free tier 9K emails/month; best LATAM deliverability; Spanish UI).

**Why:** Best deliverability for PY ISPs, free tier covers Month 1-3, Spanish support.

**Status:** ✅
**Owner:** Erebus

---

### June 26, 2026 — E-commerce platform = WA-first

**Context:** Shopify vs Woo vs Next.js vs Tienda Nube vs WA-only.

**Decision:** **WA-first for launch.** Migrate to Tienda Nube or Next.js in Month 5+ if revenue justifies.

**Why:** PY norm is WhatsApp. Zero setup cost. Personal service. All 5 PY competitors use this.

**Status:** ✅
**Owner:** Sarah + Erebus

---

### June 26, 2026 — Logo direction = Playful Pop

**Context:** 3 visual directions considered (Playful Pop / Premium Kink / Minimal Naughty).

**Decision:** **Direction 1: Playful Pop** (rose palette, rounded typography, friendly).

**Why:** Matches Enki's existing warmth, fits wellness/sensual positioning, ages well.

**Status:** 🟡 Recommended, not yet produced (designer not yet engaged)
**Owner:** Sarah + designer (when engaged)

---

### June 26, 2026 — Wait for Q5 PDF before locking pricing

**Context:** All current pricing math is based on estimates (AR retail ÷ 2).

**Decision:** Don't lock retail prices publicly until Q5 PDF received. Keep pricing on WhatsApp (movable).

**Why:** FX risk + cost estimate uncertainty. Web pricing is harder to change than WhatsApp quotes.

**Status:** 🔴 Waiting on Q5 PDF
**Owner:** Sarah (delivers Q5), Erebus (recalculates)

---

### June 26, 2026 — B2B wholesale = top revenue priority

**Context:** Identified 23 PY sex shops as B2B wholesale targets. Top 10 priority list built.

**Decision:** B2B wholesale is the **highest single revenue lever** — bigger per-buyer than DTC. Prioritize:
1. As Bajo La Manga (already importing Sexitive — high conversion likelihood)
2. SexShop.com.py (largest banner pricing — high volume)
3. Rivia (modern UX — structured buyer)
4. Íntimos Placeres (under-served on lubricants)
5. Mencanta (mixed content)

**Why:** Single B2B buyer = Gs 5-20M/month potential. 5 B2B buyers > 100 DTC customers.

**Status:** 🟡 Top of B2B outreach list ready, not yet contacted
**Owner:** Sarah (visits)

---

### June 26, 2026 — AR inflation risk acknowledged

**Context:** Argentina wholesale inflation 34.5% YoY (INDEC May 2026). Our 4:1 FX assumption may break.

**Decision:** Build FX buffer into retail (don't publish on website, keep on WhatsApp). Lock 6-month pricing with Sexitive AR when Q5 arrives.

**Why:** Pricing flexibility protects margin. Website pricing is hard to change.

**Status:** 🟡 FX tracking doc recommended (TBD)
**Owner:** Sarah + Erebus

---

## Pending decisions (waiting on data)

| Decision | Waiting on | Priority |
|----------|-----------|----------|
| Lock launch retail prices | Q5 PDF | 🔴 Critical |
| Lock launch budget actual | Vendor quotes (3 despachantes + 3 contadores + 3 imprentas) | 🔴 Critical |
| Confirm modelo旅行者 for first shipment | Sarah's risk tolerance | 🟠 High |
| Choose despachante | Quotes received | 🟠 High |
| Choose contador | Quotes received | 🟠 High |
| Choose imprentas | Quotes received | 🟠 High |
| Engage designer for logo | Sarah's brand direction confirmation | 🟡 Medium |
| Launch Date | All above complete | 🟠 High |
| TikTok @kinky_py launch | After IG engagement audit | 🟡 Medium |
| MercadoLibre PY test | After IG engagement confirms organic works | 🟡 Medium |
| LatAm expansion | After PY stable | ⚪ Future |

---

*Last updated: June 26, 2026 — Session 10 Repo Upgrade*
*Format adapted from decision-log patterns in tech orgs*