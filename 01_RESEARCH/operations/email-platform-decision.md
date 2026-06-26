# Email + Subscription Platform Decision

**Date:** June 26, 2026
**Scope:** Email marketing + subscription billing for Enki Store
**Use:** P4 (Month 2+) — email list, lead nurturing, future subscription box

---

## Email platform comparison (4 options)

| Platform | Plan free | Plan pago | LatAm deliverability | Spanish UI | SMS | WhatsApp | CRM | Best for |
|----------|----------:|----------:|---------------------:|-----------|-----|----------|-----|----------|
| **Brevo (ex Sendinblue)** | ✅ 300 emails/day | USD 25/mo (20K emails) | ✅ Excellent (SMTP regional) | ✅ | ✅ Add-on | ⚠️ Limited | ✅ Basic | **PY/LATAM businesses** |
| **Mailchimp** | ✅ 500 contacts | USD 13/mo (Essentials) | ⚠️ Known issues some ISPs | ⚠️ Limited | ⚠️ Add-on (US only) | ❌ | ✅ Basic | Brand recognition, simple use |
| **ActiveCampaign** | ❌ | USD 29/mo (Lite) | ✅ Good | ⚠️ Limited | ⚠️ Add-on | ❌ | ✅ Advanced | Automation-heavy |
| **Mailrelay** | ✅ 80K emails/mo (!) | EUR 10/mo | ⚠️ EU-focused | ⚠️ Limited | ❌ | ❌ | ❌ | EU-style, big free tier |

---

## 🏆 Recommendation: **Brevo** (ex Sendinblue)

**Why Brevo wins for Sarah:**

1. **Best LATAM deliverability** — SMTP servers optimized for region, known to avoid Mailchimp's deliverability issues with Paraguayan ISPs
2. **Pago en moneda local** en varios países LATAM (can pay in Gs equivalent via credit card or local payment)
3. **Spanish soporte** + Spanish UI
4. **Generous free tier** — 300 emails/day = 9,000/month = enough for first 6 months of Enki
5. **Email + SMS + WhatsApp + CRM** in one platform (won't need to add pieces later)
6. **Cheap paid plan** — USD 25/mo includes 20,000 emails, basic CRM, landing pages

**For Sarah's needs:**
- Launch (Month 1–3): Free tier (9K emails/mo)
- Growth (Month 4–12): Lite plan USD 25/mo (20K emails)
- Scale (Year 2): Standard plan USD 65/mo (unlimited sends + advanced automation)

---

## Email strategy for Sarah

### Phase 1 (Month 1–3): List building
- Lead magnet: "10 Consejos para Mejorar tu Bienestar Íntimo" (free PDF)
- Capture: IG bio link → Typeform → email
- Welcome sequence: 5 emails over 14 days (product intro, education, soft pitch)

### Phase 2 (Month 4–6): Nurture + conversion
- Weekly newsletter: educational content + new arrivals
- Segmented lists: by interest (lubricants vs. stimulants vs. wellness)
- Abandoned cart recovery (when e-com launches)
- Win-back campaigns (90-day inactive)

### Phase 3 (Month 7+): Retention + LTV
- VIP segment (top 10% customers) → early access + exclusive bundles
- Subscription box waitlist (when launched)
- Birthday emails (10% off)
- Reorder reminders (60 days post-purchase)

---

## Email automation recipes (Brevo)

### Welcome flow (5 emails, 14 days)

| Day | Subject | Goal |
|-----|---------|------|
| 0 | "¡Bienvenida a Enki! 💕 Tu guía gratis" | Deliver lead magnet + introduce brand |
| 2 | "5 cosas que no sabías sobre lubricantes" | Educate, build trust |
| 5 | "Cómo Sarah empezó Enki (mi historia)" | Personal connection |
| 8 | "Conocé el bestseller: Bitchie 20ml" | Soft product pitch |
| 14 | "15% off en tu primera compra — código BIENVENIDA15" | Conversion |

### Abandoned cart flow (3 emails, 7 days)

| Hour | Subject | Goal |
|------|---------|------|
| 1 | "¿Olvidaste algo? Tu carrito te espera" | Reminder |
| 24 | "Tu carrito sigue disponible — te lo dejamos reservado" | Urgency |
| 168 (7d) | "Última oportunidad: 10% off con código VOLVER10" | Discount |

### Post-purchase flow (3 emails, 30 days)

| Day | Subject | Goal |
|-----|---------|------|
| 3 | "¿Te llegó tu pedido? Contanos" | Check-in + soft review ask |
| 14 | "Probá algo nuevo: tu guía de productos" | Cross-sell |
| 30 | "Reorder reminder + 5% off" | Repeat purchase |

---

## Subscription billing (for future subscription box)

**When to activate:** Month 6+ (once regular monthly orders are stable)

### Platform options

| Platform | Cost | Notes |
|----------|------|-------|
| **Stripe Billing** | 2.9% + Gs 250/tx | Best for international. Requires Stripe Atlas (foreign entity) for PY |
| **Mercado Pago Suscripciones** | 4–6% + Gs variable | PY-native, recurring billing built-in |
| **Brevo Payments** | Included with Brevo paid | Add-on for email platform |
| **Manual WhatsApp subscription** | Gs 0 | Sarah tracks + bills monthly via MP link |

**Recommendation:** Start with **manual WhatsApp subscription** (Month 6–9) → migrate to **Mercado Pago Suscripciones** once 50+ active subscribers.

---

## Subscription box model (for Month 6+)

### Tier 1: Discovery Box (Gs 89,000/month)
- 1 lubricant (Wet line)
- 1 sample sachet
- 1 Love Potion mini (15ml)
- 1 thank-you card
- Surprise item (candle / game)

### Tier 2: Enamorado Box (Gs 149,000/month)
- 2 products (lubricant + massage oil)
- 1 sachet
- 1 candle
- 1 special gift (kit / lingerie sample)

### Tier 3: Wellness Box (Gs 249,000/quarter)
- Quarterly box with 3–5 products
- Exclusive Kinky merchandise
- Discount code for full-size purchases

---

## Email content calendar (Month 1)

| Week | Email topic | Segment |
|------|-------------|---------|
| W1 | Welcome + lead magnet delivery | New subscribers |
| W2 | "How Sarah started Enki" | All |
| W3 | "Top 3 lubricants and how to use them" | All |
| W4 | "Behind the scenes: packing your order" | All |

---

## KPIs to track

| Metric | Target |
|--------|-------:|
| Open rate | > 25% |
| Click rate | > 3% |
| Conversion (email → sale) | > 2% |
| List growth | +100/month |
| Unsubscribe rate | < 0.5%/send |
| Spam complaint | < 0.1% |

---

## Implementation timeline

| Week | Action |
|------|--------|
| W1 (launch) | Create Brevo account (free), import IG followers as subscribers (with consent) |
| W2 | Build welcome flow (5 emails) |
| W3 | Build lead magnet PDF "10 Consejos para Bienestar Íntimo" |
| W4 | First newsletter send |
| Month 2 | Abandoned cart flow (when e-com launches) |
| Month 3 | Segmented lists by interest |
| Month 6 | Subscription box beta (manual WhatsApp) |
| Month 9 | Migrate to Mercado Pago Suscripciones |

---

*Last updated: 2026-06-26 | Decision: Brevo*