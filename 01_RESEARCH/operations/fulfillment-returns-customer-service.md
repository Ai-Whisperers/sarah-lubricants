# Operations — Fulfillment, Returns, Customer Service

**Date:** June 19, 2026
**Purpose:** Document the operational model for the launch.

---

## Fulfillment options

### Option 1 — Self-fulfilled from home (recommended for launch)

| Aspect | Detail |
|--------|--------|
| **Setup** | Sarah's spare room / garage. Shelving. Picking area. |
| **Capacity** | Up to ~30 orders/day solo |
| **Cost** | Gs 0 (existing space) + Gs 200K–500K initial packaging supplies |
| **Pros** | Zero fixed cost, full control, easy to start |
| **Cons** | Not scalable past ~50 orders/day, no business address, harder to insure |
| **Best for** | Months 0–6 |

### Option 2 — 3PL warehouse in Asunción

| Aspect | Detail |
|--------|--------|
| **Setup** | Contract with 3PL provider |
| **Capacity** | Unlimited (within 3PL's space) |
| **Cost** | Gs 300K–1M/month base + Gs 5K–10K per pick-pack |
| **Pros** | Scalable, business address, professional image, easier insurance |
| **Cons** | Higher fixed cost, less control, 3PL may not specialize in discreet handling |
| **Best for** | Months 6+ when revenue justifies |

### Option 3 — MercadoLibre fulfillment (FULL)

| Aspect | Detail |
|--------|--------|
| **Setup** | List on MercadoLibre PY, opt into Mercado Envíos |
| **Capacity** | MercadoLibre's warehouses |
| **Cost** | Commission (~15%) + fulfillment fee |
| **Pros** | Built-in traffic, trust, logistics |
| **Cons** | MercadoLibre restricts adult content; products may be delisted; less brand control |
| **Best for** | Not recommended for intimate products |

---

## Pack-ship SOP (recommended for self-fulfilled)

```
1. Receive order via WhatsApp (with payment receipt)
2. Confirm receipt in writing ("Recibido, te llega en 2-3 días")
3. Pick from shelf (FIFO — first in, first out)
4. Inspect product (no damage, no leaks, within expiration)
5. Place product in plain outer carton (no Sexitive branding visible)
6. Add thank-you card (small, brand-stamped, with WA QR for reorder)
7. Add any free samples (if running a sampling program)
8. Seal with branded tape (or plain if no branded tape yet)
9. Print shipping label (recipient name + address only, no product description)
10. Hand off to carrier
11. Send tracking number to customer via WhatsApp
```

**Total time per order: 5–10 minutes once practiced.**

---

## Returns policy — intimate products

| Principle | Application |
|-----------|-------------|
| **No returns on opened products** (hygiene) | Standard across all competitors |
| **Sealed products can be exchanged** | Within 7 days, customer pays return shipping |
| **Damaged in transit** | Full replacement or refund, Sarah pays shipping |
| **Wrong SKU shipped** | Full replacement + Sarah pays return shipping |
| **Customer changed mind (sealed)** | Store credit, customer pays return shipping |
| **Customer changed mind (opened)** | No return |

**Document the policy on the site footer + WhatsApp auto-reply.**

---

## Customer service via WhatsApp

| Channel | Hours | Response time SLA |
|---------|-------|-------------------|
| **WhatsApp Business** | Mon–Sat 9:00–20:00 PY | < 1 hour during hours, < 12 hours outside |
| **Instagram DM** | Same hours | < 4 hours |
| **Email** (later) | 24/7 | < 24 hours |

**First 90 days: Sarah handles all WA directly. After that, consider an AI agent for first-line triage (product questions, order status, hours).**

---

## Inventory tracking

For the first 6 months, a Google Sheet is enough. Schema:

| SKU | Name | On hand | Reorder point | Last restock | Unit cost | Sale price |
|-----|------|---------|---------------|--------------|-----------|------------|
| WET04 | Wet Ice Fresh 75ml | 25 | 10 | 2026-06-15 | Gs X | Gs Y |
| ... | ... | ... | ... | ... | ... | ... |

**When monthly revenue crosses Gs 10M, migrate to a real tool (Sortly, inFlow, or a simple Notion database).**

---

## Privacy / data handling (Ley 7.593/2025)

Sarah will collect:
- Customer name (required for shipping)
- Customer phone (required for WhatsApp / shipping)
- Customer address (required for shipping)
- Optional: email, birthday (for promotions)

**Required:**
- Privacy policy on site (template in `09_TEMPLATES/`)
- Customer data stored securely (encrypted sheet or proper DB)
- Customer can request data deletion at any time
- Customer data not shared with third parties (except shipping carrier, which needs name + address)

**Sarah's AI agent (if deployed) must:**
- Not log customer data to training
- Not retain conversations longer than X days
- Honor data deletion requests
