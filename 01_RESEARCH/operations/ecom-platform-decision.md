# E-commerce Platform Decision

**Date:** June 26, 2026
**Decision:** Make by Week 2 of launch (before public site is needed)
**Author:** Erebus
**Recommendation:** **Shopify Lite (Bsale) or Next.js custom (clone fun4me pattern)** — see matrix

---

## Platform options

| Platform | Pros | Cons | One-line fit |
|----------|------|------|--------------|
| **Shopify Lite / Bsale PY** | 1-week setup, payment integrated, host included | 2% transaction fee, monthly USD 29 | Fastest, vendor-locked |
| **WooCommerce + NIC.py domain** | Self-hosted, free, full control | Setup 2–3 weeks, security burden, manual updates | Tech-heavy, risky |
| **Next.js custom (paragu-ai pattern)** | Full control, no vendor lock, free hosting via Cloudflare | 3–4 week build, needs dev | Best long-term, slowest start |
| **WhatsApp-only (catalog + WA pay)** | Gs 0 cost, fastest, proven PY pattern | No SEO, no email capture, no analytics | Valid v1, scale blocker |
| **MercadoLibre** | Built-in traffic, payment integrated | 13–16% commission, ML restrictions on intimate | Backup channel only |
| **Tienda Nube (LATAM Nuvemshop)** | Sexitive uses it, LATAM-native, payment integrated | USD 25/mo + 2% fee | Sexitive-proven stack |

---

## Recommendation: 2-track strategy

### Track 1 — V1 launch (Week 1–4): WhatsApp-first
**Use:** WhatsApp Business catalog only
**Why:** Fastest path to revenue. Zero setup. Matches all 5 PY competitors' style.
**Add:** Paraguay-ai subdomain microsite (kinky.enki.com.py) — free, 1 week build, WA pre-filled links
**Cost:** Gs 0 + Gs 50K domain if upgrade to enkystore.com.py

### Track 2 — V2 scale (Week 5+): Tienda Nube or Next.js
**Decision:** Based on V1 learnings
- If revenue < Gs 3M/month by week 8 → stick with WA-first, defer e-com
- If revenue > Gs 3M/month → invest in proper e-com platform

**For Tienda Nube:** Sexitive already uses it → tested for LATAM adult products
**For Next.js:** Paragu-ai fleet has proven pattern (Nexa, Maskarada, Fun4Me all use Next.js 16 + Supabase + Tailwind v4)

---

## Detailed comparison matrix

| Criterion | Shopify Lite | WooCommerce | Next.js custom | Tienda Nube | WA-only |
|-----------|-------------:|------------:|---------------:|------------:|--------:|
| Setup time | 1 week | 2–3 weeks | 3–4 weeks | 1 week | Gs 0 |
| Monthly cost | USD 29 | Gs 0 (hosting extra) | Gs 0 (Cloudflare Pages) | USD 25 | Gs 0 |
| Transaction fee | 2% | 0% | 0% | 2% | 0% (bank) |
| Payment integration | ✅ Built-in | Manual | Manual | ✅ Built-in | Manual |
| SEO | Good | Good | Excellent | Good | None |
| Email capture | ✅ Built-in | ✅ Plugin | ✅ Custom | ✅ Built-in | ❌ Manual |
| Inventory mgmt | ✅ | ✅ | ✅ Custom | ✅ | ❌ Spreadsheet |
| Analytics | ✅ Built-in | ✅ Plugin | ✅ Custom | ✅ | ❌ Manual |
| Mobile UX | ✅ | ✅ | ✅ | ✅ | ✅ WA-native |
| Multi-locale | ✅ | ✅ Plugin | ✅ Easy | ✅ | ❌ |
| Vendor lock-in | 🔴 High | 🟢 None | 🟢 None | 🔴 High | 🟢 None |
| Adult content OK | ⚠️ May restrict | ✅ | ✅ | ✅ (Sexitive uses) | ✅ |
| Maintenance burden | None | High | Low (if built well) | None | None |
| Paragu-ai pattern fit | 🟡 | 🟡 | 🟢 | 🟡 | 🟢 |
| Dev cost (one-time) | Gs 0 | Gs 1–3M (hosting setup) | Gs 3–6M (Erebus internal) | Gs 0 | Gs 0 |

---

## Detailed cost projection (12 months)

### WA-first approach (recommended V1)
- Setup: Gs 0
- Monthly: Gs 0
- 12-month total: **Gs 0**
- Revenue ceiling: ~Gs 5–10M/month (manual order mgmt limit)

### Tienda Nube (recommended V2)
- Setup: Gs 0 (use Sexitive's existing template as reference)
- Monthly: USD 25 × 12 = USD 300 = Gs 2.25M
- Transaction: 2% × Gs 50M annual = Gs 1M
- 12-month total: **Gs 3.25M**
- Revenue ceiling: Unlimited

### Next.js custom (V3 if scaling)
- Setup: Gs 4–6M (one-time dev, paragu-ai internal cost)
- Monthly: Gs 50K (Cloudflare Pages + Supabase free tier)
- Transaction: 0% (bank/Tigo/MP integration)
- 12-month total: **Gs 4.6–6.6M year 1, then ~Gs 600K/year**
- Revenue ceiling: Unlimited
- Bonus: Full SEO + email capture + WhatsApp pre-fill + reusable for v2/v3 SKUs

---

## Decision criteria (which to choose)

| If... | Then choose... |
|-------|----------------|
| Sarah wants revenue in 2 weeks | WA-first + paragu-ai subdomain |
| Sarah has Gs 5M+ dev budget | Next.js custom (paragu-ai pattern) |
| Sarah wants minimum ongoing cost | Next.js custom (after setup) |
| Sarah wants vendor-managed | Shopify Lite or Tienda Nube |
| Sarah plans B2B scale in 6 months | Next.js custom (B2B portal easier) |
| Sarah only plans DTC | Tienda Nube (Sexitive-proven) |

---

## Paragu-ai fleet reference

Existing Paragu-ai sites that use the Next.js pattern:
- **Nexa Paraguay** (nexa.paragu-ai.com) — 13 pages × 4 locales, Supabase JSON content
- **Maskarada** (maskarada.com.py) — 11+ pages, mature Next.js 16 + Supabase
- **Fun4Me** (fun4me.com.py) — e-commerce reference, 12 SKUs, WhatsApp pre-fill

**Pattern reusable:** Copy fun4me's product catalog + checkout flow → ~1 week for Sarah's 3 SKUs.

---

## Payment integration (per platform)

| Platform | Recommended payment stack |
|----------|----------------------------|
| Shopify Lite | Shopify Payments (card) + Tigo Money + bank transfer |
| WooCommerce | Mercado Pago + bank transfer (Tigo Money via plugin) |
| Next.js custom | Mercado Pago SDK + SIPAP bank transfer + Tigo Money (manual recon) |
| Tienda Nube | Mercado Pago + bank transfer |
| WA-first | Bank transfer (primary) + Tigo Money + MP link (manual) |

**PY payment reality check:** Mercado Pago charges 5–6% + buyer protection. Tigo Money 1–2% but requires cash loading. Bank transfer 0% but customer friction. Recommend: **bank transfer as primary, Tigo Money as secondary, Mercado Pago only as last resort.**

---

## My recommendation for Sarah

**Week 1–4 (launch):** WA-first + paragu-ai subdomain (Gs 0, immediate revenue)
**Week 5+ (decision point):** Evaluate. If revenue > Gs 3M/month, switch to Tienda Nube (Sexitive-proven). If < Gs 3M, stay WA-first.
**Month 6+ (scale):** If hitting Gs 10M+/month, invest in Next.js custom (paragu-ai pattern) for full SEO + B2B portal.

---

## Open questions

1. Does Sarah have bank account already? (needed for transfer integration)
2. Does Sarah have Tigo Money Business account? (vs personal)
3. Does Sarah have Mercado Pago cuenta negocio? (vs personal)
4. What's her expected monthly volume? (drives platform ROI)

---

*Last updated: 2026-06-26 | Revisit Week 5 of launch*