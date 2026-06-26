# Customer Onboarding Flow — 5 Stages

**Date:** June 26, 2026
**Scope:** From first awareness to repeat customer
**Goal:** Map every customer touchpoint + automate what can be automated

---

## Stage 1: AWARENESS (Day 0)

**Customer state:** Doesn't know Enki Store exists.

**Channels:**
- Instagram organic posts (@enkistore)
- Instagram stories
- Instagram hashtags discovery
- TikTok (Month 3+)
- Google search (SEO content)
- Word of mouth (referrals)

**Sarah's actions:**
- Publish content (per `instagram-launch-calendar-30d.md`)
- Engage with comments + DMs
- Use hashtags (per `keyword-demand-py.md`)
- Collaborate with micro-influencers (Month 3+)

**Customer signals to track:**
- New follower on @enkistore
- Profile visits (IG analytics)
- Hashtag impressions

**Automation:**
- None (organic only)

---

## Stage 2: INTEREST (Day 0–3)

**Customer state:** Has seen Enki posts, considering a product.

**Channels:**
- IG profile visit (looks at bio link)
- Clicks to paragu-ai subdomain
- Sends DM asking about products
- Saves post for later
- Tags a friend

**Sarah's actions:**
- IG bio links to `wa.me/595XXXXXXXX` (click-to-chat)
- Subdomain (`kinky.enki.com.py`) shows product cards + WA CTA
- Replied to DMs within 4h with intro + catalog link

**Customer signals to track:**
- Bio link clicks (UTM tagged)
- DM messages received
- Subdomain pageviews

**Automation:**
- IG DM auto-reply (optional, with care)
- WA auto-reply outside hours

---

## Stage 3: CONSIDERATION (Day 1–7)

**Customer state:** Engaged in WA conversation, evaluating product.

**Touchpoints:**
- WA conversation with Sarah (Q&A, objection handling)
- Price comparison (mentally)
- Possibly asks partner for opinion
- Reads reviews / social proof

**Sarah's actions:**
- WA Business: respond within 1h business hours
- Use scripts from `04_SALES/dtc-sales-playbook.md`
- Send product photos / details
- Send battle cards objections (per `competitor-battle-cards.md`)
- Offer bundles if appropriate
- Send Nudges if customer goes quiet (Day 3)

**Customer signals to track:**
- WA messages exchanged
- Time to first message after click
- Objection types raised
- Nudge responses

**Automation:**
- Quick replies for common questions
- Day 3 nudge (if quiet): "¿Te decidiste? Tengo stock"
- Day 7 follow-up: offer discount code

---

## Stage 4: PURCHASE (Day 1–14)

**Customer state:** Ready to buy.

**Touchpoints:**
- Order confirmation message
- Payment instructions
- Payment confirmation
- Order status updates

**Sarah's actions:**
- Send order confirmation (template from `customer-messages.md`)
- Send payment instructions
- Confirm payment receipt
- Add customer to Google Sheet / CRM
- Pack order
- Ship via AEX/Mirtrans
- Send tracking number

**Customer signals to track:**
- Order value
- Payment time (instant vs delayed)
- Repeat purchase within 30 days

**Automation:**
- Payment receipt confirmation (manual but fast)
- WhatsApp Business catalog (visual product cards)
- Shipping notification template

---

## Stage 5: RETENTION (Day 14+)

**Customer state:** Purchased, evaluating experience.

**Touchpoints:**
- Delivery confirmation
- Day 3 post-delivery check-in
- Day 14 cross-sell
- Day 30 review request
- Day 60 reorder reminder
- Day 90 re-engagement (if inactive)
- Birthday email (annual)

**Sarah's actions:**
- Send delivery follow-up
- Request review / UGC
- Cross-sell related product
- Remind reorder cadence
- Reactivate if gone cold

**Customer signals to track:**
- Repeat purchase rate (30 / 60 / 90 days)
- Average order value growth
- Referral rate
- NPS proxy (would recommend)

**Automation (Brevo email automation):**
- Day 3 post-delivery: "¿Te llegó?"
- Day 14: cross-sell email
- Day 30: review request
- Day 60: reorder reminder + 5% off
- Day 90 (if inactive): re-engagement with VOLVER10 code
- Birthday: 15% off with CUMPLE15

---

## Customer journey visualization

```
AWARENESS          INTEREST         CONSIDERATION      PURCHASE         RETENTION
   │                  │                  │                │                 │
   ▼                  ▼                  ▼                ▼                 ▼
IG post          IG bio click        WA Q&A          Order confirm      Delivery check
TikTok (M3+)     WA DM click        Price compare    Payment info       Review request
SEO (M2+)        Subdomain          Battle cards     Tracking #         Cross-sell
Referral         save/tag           Nudge D3          Pack + ship       Reorder D60
                                   Nudge D7                           Re-engage D90
                                                                       Birthday
```

---

## Conversion funnel targets

| Stage | Conversion target |
|-------|------------------:|
| Awareness → Interest | 5% (of IG impressions → bio clicks) |
| Interest → Consideration | 40% (of bio clicks → WA messages) |
| Consideration → Purchase | 30% (of WA messages → orders) |
| Purchase → Repeat (90 days) | 25% |

**Net funnel:** 10K IG impressions → 500 bio clicks → 200 WA messages → 60 orders → 15 repeat customers.

---

## Time to first sale (TTFS)

| Customer segment | Expected TTFS |
|------------------|----------------:|
| Existing Enki follower (warm) | 1–3 days |
| IG discovery (cold) | 3–7 days |
| TikTok (cold, M3+) | 1–5 days |
| Referral | <1 day (immediate) |
| B2B wholesale buyer | 7–30 days |

---

## Cohort analysis framework

**Track per cohort (monthly):**
- Orders / customer
- Average order value
- Repeat purchase rate
- Time between purchases
- Channel attribution

**Tool:** Google Sheets (free) or Pipedrive CRM (free tier)

---

## Customer segmentation

| Segment | Definition | Strategy |
|---------|-----------|----------|
| **Loyalist** | 3+ orders, 90-day window | VIP perks, early access, referral ask |
| **Repeat** | 2 orders, 90-day window | Cross-sell, bundle offers |
| **New** | 1 order, 30-day window | Onboarding sequence, review ask |
| **Inactive** | 1 order, 90+ days ago | Win-back campaign with discount |
| **Window shopper** | WA message, no order | Nudge sequence, social proof |
| **Cold lead** | IG follow, no engagement | Retarget via WA broadcast (consent only) |

---

## 12-touch nurture sequence (full journey example)

| Touch # | Day | Channel | Content |
|---------|-----|---------|---------|
| 1 | 0 | IG post | Educational post (e.g., "qué es un lubricante") |
| 2 | 0 | IG story | Daily story with product mention |
| 3 | 1 | Bio click | Subdomain visit (UTM tagged) |
| 4 | 1 | WA message | First Q&A |
| 5 | 2 | WA reply | Battle card objection handled |
| 6 | 3 | WA nudge | "¿Te decidiste?" |
| 7 | 4 | WA message | Order confirmation |
| 8 | 5 | WA message | Payment confirmation |
| 9 | 6 | WA message | Tracking # + shipping notification |
| 10 | 10 | WA follow-up | "¿Te llegó? ¿Cómo te fue?" |
| 11 | 14 | Email | Cross-sell + review request |
| 12 | 30 | Email | Reorder reminder + 5% off |

**Total: 12 touches over 30 days per customer journey.**

---

## Retention metrics (KPIs)

| Metric | Target | Tool |
|--------|-------:|------|
| Repeat purchase rate (90d) | >25% | Google Sheets |
| Average order value | Gs 130K+ | Manual log |
| Customer LTV (12-month) | Gs 500K | Manual calculation |
| NPS (would recommend) | >40 | Quarterly survey |
| Email open rate | >25% | Brevo |
| WA response rate | >70% | Manual |
| Unboxing post rate | >5% | IG tracking |

---

## Onboarding checklist (for Sarah to print)

- [ ] WA Business profile + photo + description
- [ ] WA catalog uploaded (3 SKUs)
- [ ] WA quick replies set (10 minimum)
- [ ] WA labels created (8 minimum)
- [ ] IG bio link updated to wa.me link
- [ ] IG story highlight "Trio" created
- [ ] Subdomain live (kinky.enki.com.py via paragu-ai)
- [ ] First 9 IG posts queued
- [ ] First 9 stories queued
- [ ] Brevo account created (free tier)
- [ ] First email lead magnet PDF created ("10 Consejos para Bienestar Íntimo")
- [ ] Email welcome flow (5 emails) configured in Brevo
- [ ] Google Sheet for customer tracking set up

**Time to complete:** 2-3 hours

---

*Last updated: 2026-06-26 | Launch Week 1 deliverable*