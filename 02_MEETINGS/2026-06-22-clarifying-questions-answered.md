# 2026-06-22 — Sarah's Answers to Round 1 Questions

**Channel:** WhatsApp from Sarah → Erebus
**Status:** 🟡 4 of 5 answered, Q5 (cost PDF) still missing + 3 new follow-ups (Q6, Q7, Q8)
**Last updated:** June 22, 2026

> **Note:** This file is Sarah's RESPONSES. For the original questions sent, see [`2026-06-20-clarifying-questions-asked.md`](2026-06-20-clarifying-questions-asked.md).

---

## Sarah's answers table

| # | Question | Sarah's answer | Status | Action |
|---|----------|----------------|--------|--------|
| **Q1** | Pink Sexy Pill — ¿drop / ANMAT / capital extra? | **(a) drop** | ✅ Confirmed | Drop PSP from v1 launch. Re-evaluate months 3–6 from revenue. |
| **Q2** | ¿Sumamos lubricante? ¿Cuál? | **"Sumamos lubricante anal"** (Wet — Anal 75ml, code WET02) | ✅ Confirmed | Lock trio: Bitchie 20ml + XXX For Her 15ml + **Wet Anal 75ml** (NOT Like a Virgin as I had recommended). |
| **Q3** | "Kinky Store" — ¿final? | **NO.** La marca registrada es **"Enki Store"**. "Kinky" es submarca / sección dentro de Enki. | ✅ Confirmed — changes brand doc entirely | Rewrite `kinky-store-assessment.md` → `enki-store-assessment.md`. Verify DINAPI for "Enki" + "Kinky" separately. |
| **Q4** | Sexitive AR manager — ¿ya le preguntaste? | **Sí, ya tengo el precio mayorista** | ✅ Confirmed (but no PDF received) | Need Q5 (PDF) to plug real numbers into pricing model. Verbal answer alone is not auditable. |
| **Q5** | Cotización mayorista — ¿me mandás el PDF? | ❓ **No enviada aún** | 🔴 Still pending | This is the single biggest unblock. Pricing model waits on this. |

---

## What changed in our plan because of Q2 (anal, not Like-a-Virgin)

| Dimension | Old plan (my rec) | New plan (Sarah's choice) |
|-----------|-------------------|---------------------------|
| Trio | Bitchie + XXX + **Wet — Like a Virgin** | Bitchie + XXX + **Wet Anal** |
| Differentiation | Strongest (unique PY formulation) | Weakest (commodity, all 5 competitors sell it) |
| Margin room | Higher (no direct comparison) | Tighter (must beat Rivia/SexShop.com.py on price) |
| Strategic value | Establishes premium category | Volume driver, lower margin per unit |

**Impact:** Wet Anal is a strategic downgrade from a differentiation standpoint. Sarah is choosing volume-over-differentiation. Acceptable if her goal is "validar el mercado rápido" (matches her 0–6 month time horizon). Flag for review at month 3.

## What changed in our plan because of Q3 (Enki, not Kinky)

| Document | Old state | New state |
|----------|-----------|-----------|
| `01_RESEARCH/brand-identity/kinky-store-assessment.md` | Kinky Store as main brand | **NOW ARCHIVED** (see `kinky-store-assessment.md` deprecated notice). Replaced by `enki-store-assessment.md`. |
| `01_RESEARCH/brand-identity/naming-options.md` | Recommended Lúmina/Volare | Update to recommend **Enki** with Kinky as vertical |
| `01_RESEARCH/brand-identity/launch-SKU-list-3-SKUs.md` | Kinky Store as the brand | Update to Enki Store as the brand |
| `TODO.md`, `README.md`, `COMPLETE-INDEX.md` | All reference Kinky Store | Need search-replace to update |

## What changed in our plan because of Q4 (precio mayorista confirmed)

Q4 confirms that **Sarah's cost basis = Distribuidor Mayorista** column. We have verbal confirmation but not the PDF. The pricing model can be built on these numbers as estimates, with a "verify with PDF" note.

**Key pricing intelligence from this confirmation:**
- Sarah buys at Distribuidor Mayorista (AR$ 5,515–8,270 per SKU, 60–67% of Publico)
- This is consistent with a "named reseller, not formal distributor" model
- Confirms the choice of **Model 2 (Independent Reseller)** — not Model 1 (Authorized Distributor)
- MERCOSUR origin certificate question (Q4c) is still open — affects whether 0% DI applies

## New follow-up questions to add (Q6, Q7, Q8)

### Q6 — DINAPI verification for "Enki" + "Kinky"
- 6a) ¿Me mandás screenshot del registro DINAPI de "Enki Store" con número, titular y clases?
- 6b) ¿"Kinky" tiene registro separado o es solo una sección dentro de Enki?
- 6c) ¿Qué clases tenés cubiertas? (3 = cosméticos, 5 = lubricantes/farmacia, 35 = retail — necesitamos al menos 3+35)

### Q7 — RUC actividad code (contador confirmation)
- ¿Tu contador ya confirmó que la actividad actual "venta de productos por internet" cubre la importación de cosméticos DINAVISA-regulados, o hay que ampliar el RUC?
- Si hay que ampliar: ¿cuánto cuesta y cuánto tarda?

### Q8 — MERCOSUR origin certificate from Sexitive AR
- ¿Ya le preguntaste al gerente de Sexitive AR si emite Certificado de Origen MERCOSUR para los envíos a PY?
- ¿O ya tenés respuesta? (Si dice que no → +14–18% DI, encarece el landed cost)

## Mathematical constraint discovered (June 22, 2026)

While preparing the pricing model, I ran the landed-cost math with the confirmed Distribuidor Mayorista prices:

| Order size | Total landed (Gs) | Fits < Gs 10M? | 150% margin retail feasible? |
|------------|-------------------|----------------|------------------------------|
| 3 SKUs × 30u (90u total) | 5.8M | ✅ Yes | ❌ No — Bitchie Gs 187K, XXX Gs 255K (above market ceiling Gs 180K) |
| 3 SKUs × 50u (150u) | 7.8M | ✅ Yes | ❌ No — XXX Gs 163K, Bitchie Gs 120K (tight) |
| 3 SKUs × 100u (300u) | 12.9M | ❌ No (+Gs 2.9M) | ✅ ✅ all 3 in market range |
| 10 SKUs × 30u (300u) | 14.5M | ❌ No (+Gs 4.5M) | ⚠️ Tight — depends on SKU mix |

**Decision needed from Kiki/Erebus:** either drop to 100% margin (NOT 150%), increase order size (raise capital), or expand SKU count to spread DINAVISA/despachante fixed costs. The 150% target doesn't fit the Gs 10M constraint at 3-SKU scale.

**Resolution:** Drop to 100% margin (decided June 26). Updated in `canonical-pricing-reference-v1.md`.

---

*Last updated: June 26, 2026 — Session 10 (split for clarity)*