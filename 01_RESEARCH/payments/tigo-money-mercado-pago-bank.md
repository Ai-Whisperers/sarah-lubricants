# Payments — Paraguay Landscape for Intimate-Product E-commerce

**Date:** June 19, 2026

---

## The 4 viable payment methods

### Method 1 — Bank transfer / SIPAP

| Aspect | Detail |
|--------|--------|
| **What** | Direct transfer from customer's bank to Sarah's PY bank account |
| **Customer experience** | Generate order, customer receives Sarah's bank details, customer transfers, sends receipt via WhatsApp, Sarah confirms and ships |
| **Pros** | Zero transaction fees, no processor needed, fully discreet (no card statement) |
| **Cons** | Friction (customer has to go to bank/app), not instant, manual reconciliation |
| **Best for** | First 30 days, low volume, high-discretion purchases |
| **Discreet billing** | Bank statement shows Sarah's business name (e.g., "Sarah Importaciones") — customer chooses what to tell their bank |

### Method 2 — Tigo Money

| Aspect | Detail |
|--------|--------|
| **What** | Tigo's mobile wallet, dominant in PY |
| **Customer experience** | Customer opens Tigo Money app, sends to Sarah's Tigo Money number, screenshot receipt via WA |
| **Pros** | Massive user base in PY, instant transfer, low fees (~1–2%), discreet |
| **Cons** | Limits on transfer size (verify with Tigo), not all customers have Tigo Money |
| **Best for** | Default payment method, especially for younger / unbanked customers |
| **Discreet billing** | Tigo Money statement shows "Transferencia a [Sarah's business name]" — not "Sexitive" or "lubricant" |

### Method 3 — Mercado Pago

| Aspect | Detail |
|--------|--------|
| **What** | MercadoLibre's payment processor, widely used in PY |
| **Customer experience** | Checkout on site, choose Mercado Pago, pay with card / Tigo Money / bank transfer / Mercado Credito |
| **Pros** | Familiar to most PY e-com buyers, multiple payment sub-methods, buyer protection |
| **Cons** | ~5–6% transaction fee, MercadoLibre has restrictions on adult content (checkout may work but listings get pulled), **discreet billing concern: card statement shows "MERCADO PAGO *SARAH BUSINESS"** |
| **Best for** | Customers who want buyer protection or don't have Tigo Money |
| **Discreet billing** | **⚠️ Test before relying on.** Card statement descriptor is configurable but goes through Mercado Pago's approval. |

### Method 4 — Stripe / international card processor

| Aspect | Detail |
|--------|--------|
| **What** | Stripe or similar for international card acceptance |
| **Customer experience** | Standard card checkout |
| **Pros** | International cards accepted, professional UX, dispute handling |
| **Cons** | ~4–6% + Gs 2K per transaction, **Stripe has policies on adult content (allowed but flagged)**, Payouts in USD only (Sarah needs to convert), tax complexity in PY |
| **Best for** | If Sarah later expands to UY/BO/AR customers |
| **Discreet billing** | Configurable statement descriptor — Sarah can set "Sarah Importaciones" |

---

## Recommended payment stack for launch

| Order | Method | Why |
|-------|--------|-----|
| 1 | Tigo Money | Default. Highest adoption. Lowest friction in PY. |
| 2 | Bank transfer (SIPAP) | High-discretion customers. Zero fees. |
| 3 | Mercado Pago | Customer preference (some want it). Test discreet billing before promoting. |
| 4 | Stripe (later) | Add when international traffic or larger average orders justify it. |

**Stack for launch:** Tigo Money + Bank transfer. Add Mercado Pago in month 2 after testing discreet billing.

---

## Discreet billing — what "discreet" actually means

| Layer | What shows on customer's statement | Control |
|-------|------------------------------------|---------|
| Bank transfer | "[Sarah's business name]" | Sarah controls business name (use neutral name like "Sarah Importaciones" or "LubriPY S.A.") |
| Tigo Money | "Transferencia a [Sarah's business name]" | Same as above |
| Mercado Pago | "MERCADOPAGO*[business name]" or "MERPAGO*[business name]" | Test before relying. If Mercado rejects "intimate" descriptors, fall back. |
| Stripe | "[business name] + city" | Sarah sets descriptor in dashboard. |
| Card statement (any processor) | Depends on MCC code | Sarah's business is registered as "retail cosmetics" or similar — not "adult." Use correct MCC. |

**Critical:** Sarah's business registration (RUC) should be in a neutral category ("venta de cosméticos y productos de higiene personal" or similar), NOT in any "adult entertainment" category. This affects what shows on card statements and what MCC Stripe assigns.

**See questionnaire §1.6 — RUC activity code.**

---

## Payment collection flow (recommended)

```
1. Customer adds to cart, hits "Comprar por WhatsApp"
2. Site sends pre-filled WA message to Sarah's WA Business
3. Sarah (or AI agent) replies with: order summary + total + payment options
4. Customer chooses: Tigo Money / Bank / Mercado Pago
5. Customer pays, sends receipt screenshot via WA
6. Sarah confirms receipt, asks for shipping address
7. Sarah packs, ships, sends tracking
8. Post-delivery: Sarah asks for review / repeat order
```

**No card-on-file. No saved payment methods. Maximizes discretion. Minimizes PCI scope.**

---

## What Sarah should ask her bank

1. **"¿Puedo abrir una cuenta empresa sin tener RUC todavía, o primero RUC y después cuenta?"** (In PY, RUC first.)
2. **"¿Cuál es la comisión por recibir transferencias SIPAP desde otros bancos?"** (Often 0, but verify.)
3. **"¿Puedo asociar la cuenta a Tigo Money para recibir pagos en la cuenta?"** (Usually yes.)
4. **"¿Emiten tarjetas corporativas? ¿Cuál es el costo anual?"** (For ad spend on Meta/IG later, may be needed.)
5. **"¿Tienen API o webhooks para confirmar pagos automáticamente?"** (Not needed for launch; useful later.)
