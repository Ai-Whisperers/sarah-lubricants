# WhatsApp Business Setup Guide

**Date:** June 26, 2026
**Audience:** Sarah Roig
**Goal:** Configure WhatsApp Business for Enki Store in <30 minutes
**Reference:** Meta WhatsApp Business API + standard WA Business app setup

---

## Step 1: Download WhatsApp Business app (NOT regular WhatsApp)

- iOS: https://apps.apple.com/app/whatsapp-business/id1386412985
- Android: https://play.google.com/store/apps/details?id=com.whatsapp.w4b

**Why separate:** Personal number stays personal, business number is for customers.

**Decision needed:** Does Sarah want to use her existing +595 number, or get a new dedicated number?
- **Existing:** No transition cost, but mixes personal + business contacts
- **New number:** Clean separation, requires new SIM (~Gs 50K from Tigo/Claro/Personal)

**Recommendation:** Use existing number for launch. Migrate to new number if volume warrants.

---

## Step 2: Business Profile setup

### Profile fields

| Field | Value |
|-------|-------|
| **Business name** | Enki Store |
| **Category** | Health/Beauty (or Retail) |
| **Profile photo** | Enki logo (circular crop) |
| **Description** | "Bienestar íntimo, con privacidad 💕 Envíos a todo Paraguay 🇵🇾" |

### About section

```
Enki Store es la primera distribuidora oficial de Sexitive 
Argentina en Paraguay. Ofrecemos lubricantes, estimulantes, 
aceites y velas de masaje con registro DINAVISA.

🛒 Comprá por WhatsApp: este chat
📦 Envíos discretos en 24-72h a todo el país
🔒 Privacidad garantizada — packaging genérico
```

### Address
- **Use:** Skip physical address for privacy (or use depósito address if Sarah has a commercial dirección)
- **Coordinates:** Optional, helps customers find pickup point

### Business hours

| Day | Hours |
|-----|-------|
| Lunes a Viernes | 9:00 – 21:00 |
| Sábado | 9:00 – 18:00 |
| Domingo | Cerrado (auto-reply on) |

---

## Step 3: Catalog setup (WA Business native)

### Upload 3 product cards (launch trio)

**Card 1: Bitchie 20ml**
- Photo: Sexitive product shot (high-res)
- Name: "Bitchie Spray multiorgásmico — 20ml"
- Price: Gs 130,000
- Description: "Spray de Sexitive Argentina con L-Arginina + ácido láctico. Efecto calor + sensibilidad aumentada. Rinde 30-40 aplicaciones."
- Link: https://kinky.enki.com.py/producto/bitchie
- Code: SEFB

**Card 2: XXX For Her 15ml**
- Photo: Sexitive product shot
- Name: "XXX For Her óleo orgasmico — 15ml"
- Price: Gs 145,000
- Description: "Óleo cosmético para ella. 1-2 gotas, efecto hasta 45 min. Sensibilidad aumentada + orgasmos más intensos."
- Link: https://kinky.enki.com.py/producto/xxx-for-her
- Code: XXX01

**Card 3: Wet Anal 75ml**
- Photo: Sexitive product shot
- Name: "Wet Gel Lubricante Anal — 75ml"
- Price: Gs 125,000
- Description: "Lubricante anal base agua, 75ml. No mancha, no irrita, larga duración. Cosmético certificado."
- Link: https://kinky.enki.com.py/producto/wet-anal
- Code: WET02

### How to add catalog items
1. Open WA Business → Settings → Business Tools → Catalog
2. Tap "+" to add new item
3. Add photo, name, price, description, link, code
4. Save
5. Repeat for each product

---

## Step 4: Quick Replies (saved responses)

### How to set up
1. Settings → Business Tools → Quick Replies
2. Tap "+" to add
3. Set shortcut (e.g. "hola")
4. Set message (full response)
5. Save

### 10 essential quick replies

| Shortcut | Full message |
|----------|--------------|
| `hola` | ¡Hola! 👋 Soy Sarah de Enki Store. ¿En qué te puedo ayudar? |
| `catalogo` | Te paso nuestro catálogo: https://kinky.enki.com.py. ¿Qué producto te interesa? |
| `precios` | Los precios son: Bitchie Gs 130,000 · XXX For Her Gs 145,000 · Wet Anal Gs 125,000. Envío gratis en Asunción. |
| `envio` | Envío gratis en Asunción (24-48h). Interior: Gs 25-50K según destino (3-5 días). |
| `pago` | Aceptamos transferencia bancaria (Bancard, Itaú, Continental), Tigo Money o Mercado Pago. ¿Cuál te queda mejor? |
| `trio` | El trio completo (Bitchie + XXX + Wet Anal) sale Gs 350,000 con envío gratis. ¡Ahorrás Gs 50,000! |
| `gracias` | ¡Gracias por tu compra! 🙌 Te confirmo el envío apenas despache. |
| `privacidad` | Tu privacidad es prioridad. Empaque genérico, sin logos, sin marca visible. Nadie sabe qué es. |
| `mayorista` | Hola! Sí, hacemos ventas mayoristas a tiendas. ¿Me pasás tu WhatsApp y te contacto con el catálogo B2B? |
| `horario` | Nuestro horario: Lun-Vie 9-21h, Sáb 9-18h. Domingo cerrado. Te respondo en cuanto pueda. |

### Auto-reply outside hours

**Message:**
```
¡Hola! Gracias por escribir a Enki Store 🌙

Nuestro horario de atención es Lun-Vie 9-21h y Sáb 9-18h. 
Te respondemos mañana en horario comercial.

Si tenés una consulta urgente, escribinos a 
+595 [número] con el mensaje "URGENTE" y te respondemos 
lo antes posible.

¡Gracias por tu paciencia! 💕
```

### How to enable
Settings → Business Tools → Away Message → Enable
- Schedule: Outside business hours
- Recipients: All

---

## Step 5: Labels (organize customers)

### How to set up
1. Settings → Business Tools → Labels
2. Create custom labels
3. Apply to chats

### 8 labels to create

| Label | Color | When to use |
|-------|-------|-------------|
| `Nuevo` | Blue | First-time customer |
| `Compró` | Green | Confirmed order, awaiting payment |
| `Pagó` | Yellow | Payment received, ready to ship |
| `Enviado` | Orange | Order shipped |
| `VIP` | Red | Top customer (3+ orders) |
| `Mayorista` | Purple | B2B buyer |
| `Consulta` | Gray | Just asking questions |
| `Pendiente` | Brown | Waiting on customer response |

---

## Step 6: Catalog link in Instagram bio

**Update IG bio to:**
```
Enki Store 💕
Bienestar íntimo · Envíos a todo 🇵🇾
📲 Pedí por WhatsApp: wa.me/595XXXXXXXX
📦 Catálogo: linktr.ee/enkipy
```

**Use Linktree (free) to centralize:**
- WhatsApp link
- Catalog page
- Instagram
- Email signup

---

## Step 7: Click-to-WhatsApp ads (optional, P3+)

WA Business allows running ads that open a chat directly.

**Setup:** https://business.facebook.com/wa/click-to-whatsapp-ads

**Use case:** IG Story ad → "Pedí ya" → opens WA chat with pre-filled message

**Cost:** USD 0.10–0.50 per message received (vs. Gs 50–200 per organic message)

**Recommendation:** Activate when launch metrics justify (Month 2+).

---

## Step 8: Backup + privacy

### Auto-backup
- Settings → Chats → Chat backup → Daily to Google Drive
- Includes photos, voice notes, contacts

### Two-step verification
- Settings → Account → Two-step verification → Enable PIN
- Prevents account takeover

### Privacy settings
- Profile photo: My contacts
- Last seen: My contacts
- About: Public (for branding)
- Status: My contacts

---

## Setup checklist (Week 1)

- [ ] Download WA Business app
- [ ] Verify phone number (Sarah's existing or new)
- [ ] Set business profile (name, photo, description)
- [ ] Upload 3 launch SKUs to catalog
- [ ] Create 10 quick replies
- [ ] Set away message (outside hours)
- [ ] Create 8 labels
- [ ] Enable auto-backup to Google Drive
- [ ] Enable two-step verification
- [ ] Update IG bio with WA link
- [ ] Set up Linktree (or similar) for centralized links

**Total time:** 30 minutes

---

## What NOT to do

- ❌ Don't use personal WhatsApp for business (mixed contacts)
- ❌ Don't broadcast without consent (will get banned)
- ❌ Don't auto-send "Hola, te interesa..." cold messages
- ❌ Don't share customer data with anyone
- ❌ Don't take payments outside WA (loses audit trail)
- ❌ Don't use WA status for promotions (use IG for that)

---

*Last updated: 2026-06-26 — Sarah: complete setup before launch*