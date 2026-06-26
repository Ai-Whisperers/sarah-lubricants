# Sexitive Dropship vs. Hybrid Import — Analysis

**Date:** June 26, 2026
**Question:** Should Sarah use Sexitive's dropship program (SexShopMayorista.com), formal import, or the hybrid (modelo旅行者 + formal)?
**Verdict:** Hybrid wins. Dropship as backup. Formal as primary.

---

## The 3 paths analyzed

### Path 1: Pure Dropship (SexShopMayorista.com)

**What it is:** SexShopMayorista.com (operated by Sexitive AR) ships directly to Sarah's customers. No inventory in PY. No DINAVISA paperwork (Sexitive handles).

**Pros:**
- ✅ Zero inventory risk
- ✅ No capital tied up in stock
- ✅ No DINAVISA paperwork (Sexitive handles)
- ✅ No freight / courier coordination
- ✅ Fast to start (no SKU selection needed beyond catalog)
- ✅ Test products without buying

**Cons:**
- ❌ Lower margin (Sexitive keeps ~20-30% margin for dropship service)
- ❌ No DINAVISA pathway in Sarah's name (no brand value)
- ❌ Customers see Sexitive branding (privacy concern)
- ❌ Sarah can't customize packaging
- ❌ No B2B wholesale (dropship is DTC-only)
- ❌ No control over delivery time
- ❌ Not eligible for Sexitive's full wholesale pricing

**Margin math (estimate):**
- Sexitive AR retail: AR$ 12,200 (Bitchie)
- Sexitive dropship price to Sarah: ~AR$ 7,000-8,000 (est. ~30-40% off retail)
- Sarah's sell price: Gs 130,000 (~AR$ 32,500 at 4:1)
- Sarah's revenue: Gs 32,500 - Gs 7,500 (dropship cost) - Gs 0 (no freight/DINAVISA) = Gs 25,000 net
- **Margin: ~25,000 / 32,500 = 77%** (vs. ~100% on direct)

---

### Path 2: Pure Formal Import (current plan)

**What it is:** Sarah buys from Sexitive AR Distribuidor Mayorista, imports formally via DINAVISA + despachante, holds inventory in PY.

**Pros:**
- ✅ Highest margin (Mayorista = ~50% of AR retail)
- ✅ Full DINAVISA documentation in Sarah's name (brand value)
- ✅ B2B wholesale possible (key lever)
- ✅ Custom packaging (discretion + branding)
- ✅ 6-month fixed price contract possible
- ✅ Tax deductible (IVA crédito fiscal on inputs)

**Cons:**
- ❌ Capital tied up in inventory (Gs 2-4M first order)
- ❌ DINAVISA NSO process (15-30 days, Gs 500K per SKU)
- ❌ Despachante fees (Gs 1.2M per shipment)
- ❌ IVA import (10% on product cost)
- ❌ Storage required
- ❌ Customs risk (if not done correctly)
- ❌ Slower to start (3-4 weeks before first shipment)

**Margin math (estimated, per `canonical-pricing-reference-v1.md`):**
- Mayorista cost: ~AR$ 6,100 (Bitchie) = Gs 24,400
- Landed cost per unit (at 30u order): ~Gs 66,800
- Sarah's sell price: Gs 130,000
- **Margin: ~63,200 / 130,000 = 49% net (after DINAVISA amortization, freight, IVA)**

**Wait — that doesn't match the 100% margin we said in canonical pricing. Let me clarify:**

The 100% margin in `canonical-pricing-reference-v1.md` is calculated as:
- **Per-unit landed cost** (Gs 66,800) vs. **per-unit retail** (Gs 130,000)
- That's 49% net margin per unit sold.

The 100% comes from `(retail - landed) / landed` = (130K - 66.8K) / 66.8K ≈ 95% markup. So "100% margin" in our docs really means "doubled the cost" which is closer to a 50% net margin. **This is terminology drift that confuses the math. See "Terminology note" below.**

---

### Path 3: Hybrid (modelo旅行者 + formal)

**What it is:** First 2-3 shipments use modelo旅行者 (personal luggage, no DINAVISA). Then transition to formal once DINAVISA NSO is approved.

**Pros:**
- ✅ Saves Gs 1.7-2M per shipment (28-32% of landed cost)
- ✅ Fast to market (no DINAVISA wait)
- ✅ Validates demand before committing to formal
- ✅ Same DINAVISA-approved product line (just personal import)
- ✅ Hybrid flexibility: choose path per shipment

**Cons:**
- ❌ Limited to ~1 trip/quarter (customs personal effects limit)
- ❌ Limited to ~30 units/SKU per trip (avoid commercial pattern detection)
- ❌ Personal risk for Sarah (luggage weight, customs interaction)
- ❌ No scalability (can only do ~4 trips/year = max 120 units/SKU/year)
- ❌ For formal sales, eventually need DINAVISA anyway

**Margin math (per `modelo-viajero-strategy.md`):**
- Per-shipment savings: Gs 1.7-2M
- Over 4 shipments/year: Gs 6.8-8M total savings
- Could fund 1-2 months of fixed costs

---

## Detailed comparison

| Dimension | Pure Dropship | Pure Formal | Hybrid |
|-----------|--------------:|-------------:|-------:|
| **Margin per unit (Bitchie)** | 77% net | 49% net | 49% net (after switch) |
| **Capital required to start** | ~Gs 0 | Gs 5-7M | Gs 0-1M (modelo) → Gs 5-7M (formal) |
| **Time to first sale** | 1 week | 4-6 weeks | 2-3 weeks |
| **DINAVISA in Sarah's name** | ❌ No | ✅ Yes | ✅ Yes (after switch) |
| **B2B wholesale possible** | ❌ No | ✅ Yes | ✅ Yes (after switch) |
| **Custom packaging** | ❌ No | ✅ Yes | ✅ Yes (after switch) |
| **Inventory risk** | ✅ Zero | ❌ Capital tied up | 🟡 Partial (modelo) |
| **Customer privacy (discretion)** | ❌ Sexitive branding | ✅ Sarah's branding | ✅ Sarah's branding |
| **Scale potential** | ❌ Limited to 1× per order | ✅ Unlimited | ✅ Unlimited (after switch) |
| **Regulatory risk** | 🟢 Low | 🟠 Medium (DINAVISA inspection) | 🟠 Medium (modelo detection) |

---

## Recommendation: **Hybrid (Path 3)**

**Phase 1 (Months 1-2):** Modelo旅行者
- 2 shipments (90-180 units total)
- Total cost: ~Gs 4M (vs. Gs 7M formal)
- Validates: demand, pricing, customer feedback
- Risk: Gs 0 capital at risk if no sales (vs. Gs 4M stuck in formal inventory)

**Phase 2 (Month 3+):** Formal import
- DINAVISA NSO approved (process started Month 1)
- Switch to formal for inventory replenishment
- Begin B2B wholesale (key revenue lever)
- Lock 6-month fixed price with Sexitive AR gerente

**Backup (if Sexitive AR breaks relationship):** Dropship
- Switch to SexShopMayorista.com dropship
- Accept lower margin in exchange for continuity
- Time to find new supplier (3-6 months)

---

## Decision tree for Sarah

```
Can you travel to AR in next 60 days?
├── YES → Start with modelo旅行者 (Phase 1)
│   ├── After 2-3 trips, switch to formal (Phase 2)
│   └── Dropship as backup only
└── NO → Start with formal import (Phase 2 only)
    ├── First shipment: small (60-90 units)
    ├── Use modelo旅行者 if you can coordinate with a friend/family trip
    └── Dropship as bridge if formal takes too long
```

---

## Action items for Sarah

### This week
- [ ] Decide: Can you travel to AR in next 60 days?
- [ ] If YES: Plan 1st modelo旅行者 trip (July or August 2026)
- [ ] If NO: Get formal import quotes from despachante
- [ ] Either way: Start DINAVISA NSO process NOW (15-30 days)

### Month 1-2
- [ ] First shipment (modelo or formal)
- [ ] Track actual vs. estimated costs in a spreadsheet
- [ ] Re-run `tools/pricing_calculator.py` with real numbers
- [ ] Update `canonical-pricing-reference-v1.md` with confirmed costs

### Month 3
- [ ] If modelo旅行者 worked: Switch to formal
- [ ] Lock 6-month fixed price contract with Sexitive AR gerente
- [ ] Begin B2B wholesale outreach

### If things break
- [ ] Contact SexShopMayorista.com for dropship rate sheet
- [ ] Compare to formal import rates
- [ ] Decide: dropship bridge vs. find new supplier

---

## Terminology note (DRIFT ALERT)

Our pricing docs use "X% margin" inconsistently. Let me clarify:

| Term | Meaning | Example |
|------|---------|---------|
| **Markup** | (Retail - Cost) / Cost | Bitchie: (130K - 66.8K) / 66.8K = 95% |
| **Gross margin** | (Retail - Cost) / Retail | Bitchie: (130K - 66.8K) / 130K = 49% |
| **Net margin** | After all expenses (DINAVISA amortization, returns, fees) | Likely 30-40% net |

**In our docs, "100% margin" really means "100% markup" (i.e., doubled the cost).** This is industry standard for retail but creates confusion.

**Recommendation:** Use "gross margin %" in all future pricing docs to be unambiguous. Update `canonical-pricing-reference-v1.md` to specify "100% markup = 50% gross margin."

---

*Last updated: June 26, 2026 — Session 11*