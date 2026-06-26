# Returns + Complaint Handling SOP

**Date:** June 26, 2026
**Scope:** Standard Operating Procedures for returns, complaints, and edge cases
**Reference:** `01_RESEARCH/legal-regulatory/py-compliance-roadmap.md` (Ley de Defensa del Consumidor)

---

## Policy summary

| Situation | Action | Cost to Sarah |
|-----------|--------|---------------|
| Product defect / manufacturing issue | Full replacement + return shipping refund | Gs 5K (product) + Gs 30K (return ship) |
| Wrong product shipped | Full replacement + apology gift | Gs 5K (correct product) + Gs 5K (sample) |
| Customer changed mind, product unopened | 7-day exchange (different SKU) | Customer pays return shipping |
| Customer changed mind, product opened | No return (DINAVISA + biosecurity) | 0 |
| Shipping damage | Full replacement + investigation | Gs 5K (product) + investigation time |
| Lost in transit | Reship + file claim with courier | Gs 5K (product) + Gs 30K (ship) |
| Late delivery (>7 days Asunción, >10 days interior) | Discount next purchase + apology | Gs 5K discount |
| Allergic reaction | Stop use + refer to doctor + record incident | 0 + regulatory doc |

---

## Returns decision tree

```
Customer initiates return/refund
│
├─ Product opened?
│   ├─ YES (intimate product) → No return. Apologize + offer discount next time.
│   └─ NO (sealed) → Continue ↓
│
├─ Defective / wrong / damaged?
│   ├─ YES → Full replacement. Return shipping refunded.
│   └─ NO → Continue ↓
│
├─ Within 7 days of delivery?
│   ├─ YES → Exchange (different SKU) OK. Customer pays return shipping.
│   └─ NO → Polite decline (past return window).
│
└─ Damaged in shipping?
    ├─ YES → File claim with courier + reship product.
    └─ NO → Refer to "Customer changed mind" branch.
```

---

## Complaint response SLAs

| Severity | Response time | Resolution time | Owner |
|----------|---------------|-----------------|-------|
| 🔴 Critical (allergic reaction, legal threat) | < 30 min | < 24h | Sarah + Escalate to Erebus |
| 🟠 High (defective product, wrong shipment) | < 2h | < 48h | Sarah |
| 🟡 Medium (late delivery, packaging issue) | < 4h | < 5 days | Sarah |
| 🟢 Low (general question, minor feedback) | < 24h | < 7 days | Sarah |

---

## Scripts by situation

### 1. Defective product

```
¡Hola [nombre]! Lamento mucho el problema. 😔

Para resolverlo rápido:
1. ¿Podés mandarme una foto del producto defectuoso?
2. ¿Tenés el lote / fecha de vencimiento?

Apenas confirme, te envío un reemplazo SIN COSTO 
+ un detalle de disculpa. 

El envío de retorno te lo reembolsamos.

Disculpá las molestias. Esto no refleja nuestra calidad.
```

### 2. Wrong product shipped

```
¡Hola [nombre]! Tenés toda la razón, te equivocamos. 😔

Te envío el producto correcto HOY sin costo. 
Cuando recibas, devolvé el equivocado en el mismo 
paquete (te paso una guía prepaga).

Te incluyo también un mini aceite de regalo como 
disculpa por el error.

¡Gracias por tu paciencia!
```

### 3. Customer changed mind (opened product)

```
¡Hola [nombre]! Gracias por escribirnos.

Lamentablemente, por bioseguridad y regulación DINAVISA, 
no podemos aceptar devoluciones de productos íntimos 
abiertos. Esto aplica a todas las tiendas en Paraguay.

Lo que sí puedo ofrecerte:
- 15% de descuento en tu próxima compra (código VOLVER15)
- Cambio por otro producto equivalente (sellado)

¿Te interesa alguna de estas opciones?
```

### 4. Customer changed mind (sealed, within 7 days)

```
¡Hola [nombre]! Sin problema.

¿Querés cambiar por otro producto de la misma categoría 
o hacer devolución?

Si es cambio: me decís qué querés y te envío hoy.
Si es devolución: me pasás tus datos y te paso 
instrucciones de envío (a tu costo).

Una vez recibido y verificado, te reembolso.
```

### 5. Allergic reaction / safety incident (CRITICAL)

```
[Nombre], lamento mucho que hayas tenido esta reacción.
Lo más importante: dejá de usar el producto inmediatamente 
y consultá a tu médico si los síntomas persisten.

Para registrar el incidente (regulatorio):
1. ¿Cuándo empezaste a usar el producto?
2. ¿Qué síntomas tuviste exactamente?
3. ¿Tenés fotos del producto + zona afectada?

Vamos a investigar el lote y, si es necesario, vamos 
a suspenderlo preventivamente. Tu seguridad es prioridad.

Te voy a hacer un seguimiento personal en 24h. ¿Te parece?
```

### 6. Late delivery

```
¡Hola [nombre]! Lamento la demora. 

Déjame revisar el estado con [AEX/Mirtrans]. 
Te confirmo en 2 horas.

Independientemente de la demora, te quiero compensar 
con un cupón de Gs 15K para tu próxima compra 
(código DISCULPA15).

¡Gracias por tu paciencia!
```

### 7. Lost in transit

```
[Nombre], lamento mucho. El paquete se perdió en 
transporte. Esto es responsabilidad del courier, 
no tuyo.

Vamos a:
1. Abrir reclamo con [AEX/Mirtrans] (tarda 7-15 días)
2. Reenviarte el producto HOY sin costo
3. Compensarte con un detalle extra

Cuando recibas el nuevo, mantené el empaque por 
si el courier necesita ver algo.

¡Gracias por tu comprensión!
```

### 8. Refund request (generic)

```
¡Hola [nombre]! Gracias por escribir.

Para procesar un reembolso, necesito que me cuentes:
1. ¿Cuál es el motivo?
2. ¿El producto está abierto o sellado?
3. ¿Cuándo lo recibiste?

Con esa info te confirmo si corresponde reembolso 
o cambio.

[After their response, follow the decision tree]
```

---

## Tracking

**Tool:** Google Sheet "Returns & Complaints" with columns:

| Date | Customer | Order # | SKU | Reason | Resolution | Refund Gs | Notes |
|------|----------|---------|-----|--------|------------|----------:|-------|
| 2026-07-15 | María | 0042 | SEFB | Defectuoso | Cambio enviado | 0 | Lote XXXX vencido |
| 2026-07-18 | Juan | 0035 | XXX01 | Demora | Cupón Gs 15K | 15,000 | AEX 7 días |

---

## Returns by month target

| Month | Returns expected | % of orders |
|------|-----------------:|------------:|
| 1 | 1–2 | 10% |
| 2 | 2–3 | 8% |
| 3 | 2–4 | 5% |
| 4+ | 3–5 | 4% |

**Healthy return rate:** <5% of orders. >10% = investigate product quality or packaging.

---

## Common complaint patterns (to watch for)

| Pattern | Action |
|---------|--------|
| Multiple complaints about same SKU | Investigate batch (Sexitive AR) |
| Multiple complaints about same shipping region | Switch courier or add insurance |
| Multiple complaints about packaging | Redesign (imprentas) |
| Customer complaint escalates to social media | Crisis protocol (see below) |
| Threatens legal action | Escalate to Erebus + contador immediately |

---

## Crisis protocol (social media escalation)

If a customer posts a public complaint on IG / TikTok / Twitter:

1. **Within 1h:** Respond publicly with apology + private message ask
2. **Within 4h:** Resolve privately (refund/replacement)
3. **Within 24h:** Follow up publicly with resolution
4. **Document:** Save the original complaint + resolution in `docs/incidents/`

**Template public response:**
```
[Nombre], lamentamos mucho tu experiencia. Esto no 
refleja nuestra calidad habitual. Te enviamos mensaje 
privado para resolver en minutos.
```

---

## Compliance documentation

Per Ley de Defensa del Consumidor (PY):
- Returns policy must be displayed on website + WA profile
- 5-day "derecho de arrepentimiento" for online purchases (BUT intimate products excluded per biosecurity)
- Customer data must be deleted upon request (Ley 7.593/2025)

**Sarah's policy display:**

```
POLÍTICA DE DEVOLUCIONES — Enki Store

• Cambio dentro de 7 días si el producto está sellado
• No se aceptan devoluciones de productos íntimos abiertos 
  (bioseguridad, DINAVISA)
• Producto defectuoso: cambio sin costo + envío de retorno 
  reembolsado
• Pérdida en envío: reship sin costo (responsabilidad del courier)
• Dirección de devoluciones: [dirección de Sarah]
• Consultas: +595 [número] o @enkistore

Última actualización: 2026-06-26
```

---

## What NOT to do

- ❌ Don't promise refunds without verifying (some claims are invalid)
- ❌ Don't ignore complaints (they escalate)
- ❌ Don't accept returns of opened intimate products (DINAVISA + biosecurity)
- ❌ Don't ship replacement without confirming defect (waste)
- ❌ Don't engage publicly with hostile complaints (move to DM)
- ❌ Don't admit fault if unsure (investigate first)
- ❌ Don't give refunds in cash (use original payment method)

---

*Last updated: 2026-06-26 | Sarah: print this and reference before responding to complaints*