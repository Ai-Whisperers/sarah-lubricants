# Paraguay Tax + Legal Compliance Roadmap

**Date:** June 26, 2026
**Author:** Erebus (research only — Sarah needs a contador for filing)
**Scope:** Full PY legal/tax stack for intimate-wellness e-commerce importing AR cosmetics
**Sources:** Web research on DINAVISA, MIC, SET, Ley 4868/13, Ley 7.593/2025

> ⚠️ **This is research, not legal advice.** Sarah must engage a contador + despachante for actual filings. Estimated costs and timelines are based on industry-standard ranges as of June 2026.

---

## 1. DINAVISA — Cosmetics registration (launch blocker)

**Authority:** Dirección Nacional de Vigilancia Sanitaria (DINAVISA), Ministerio de Salud Pública y Bienestar Social

### Process for Cosmético NSO (Notificación Sanitaria Obligatoria)

| Step | Detail | Time | Cost (Gs) |
|------|--------|-----:|----------:|
| 1. Gather ANMAT paperwork from Sexitive AR | Certificado de Libre Venta + formulation + label artwork | 7–14 days | 0 |
| 2. Hire despachante | PY-licensed customs broker | 3–7 days | 0 (or Gs 1–2M retainer) |
| 3. Submit NSO application | Online via DINAVISA portal | 1 day | Gs 500K–800K |
| 4. DINAVISA review | Technical + labeling check | 15–30 days | 0 |
| 5. NSO approval | Receive NSO number per SKU | — | 0 |

**Total time:** 25–45 days for first SKU; subsequent SKUs in parallel = 15–30 days
**Total cost:** Gs 500–800K per SKU + Gs 1–2M despachante retainer

### Per-category requirements

| Category | Process | Time | Cost |
|----------|---------|-----:|-----:|
| Cosmético NSO | Notification only | 15–30d | Gs 500–800K |
| Suplemento Dietario | Full registration + clinical data | 90–180d | Gs 4–8M |
| Juguete sexual | No DINAVISA (regulated by MIC) | 0 | 0 |
| Lencería | No DINAVISA | 0 | 0 |
| CBD tópico | **Zona gris** — no clear pathway | — | N/A (avoid) |

---

## 2. MERCOSUR — Certificado de Origen

**What it is:** Document certifying product is manufactured in Argentina. Issued by Sexitive AR or their Cámara de Comercio.

**Why it matters:** Without it, PY charges 14–18% DI (Derecho de Importación) on the import. With it, intra-MERCOSUR trade = 0% DI.

**Process:**
1. Ask Sexitive AR manager for Certificado de Origen MERCOSUR
2. They issue via Argentine Chamber of Commerce
3. Cost: ~AR$ 50,000–100,000 per shipment (paid to AR Cámara)
4. Saves: 14–18% × product cost

**For 90-unit launch (Gs 2.4M product):**
- Without cert: +Gs 340–430K DI
- With cert: Gs 0 DI

**Recommendation:** Always request. Sarah should confirm with Sexitive AR gerente in next conversation.

---

## 3. IVA Importación

**Rate:** 10% on product cost (cosmetics)
**Calculation:** IVA = product_cost × 0.10
**Paid to:** Aduana Nacional (customs)

**For 90-unit launch:** Gs 2,386,200 × 0.10 = **Gs 238,620**

**Note:** Modelo viajero (personal luggage) avoids this. Formal imports always pay.

---

## 4. RUC actividad codes

**Sarah's RUC:** 4978694-6
**Current actividad:** "venta de productos por internet" (generic)

**Required codes for Sexitive business:**

| Código | Descripción | Cubre lo que Sarah hace? |
|--------|-------------|--------------------------|
| 47190 | Venta al por menor de otros productos en comercios no especializados | ✅ General retail |
| 47910 | Venta al por menor por correo y por internet | ✅ E-com |
| 46101 | Venta al por mayor a cambio de una retribución o por contrata | ✅ B2B wholesale |
| 46491 | Venta al por mayor de productos cosméticos, de tocador y de perfumería | ✅ Specific — RECOMMENDED |
| 47730 | Venta al por menor de productos farmacéuticos, cosméticos, de tocador y artículos de perfumería | ✅ Specific — RECOMMENDED |
| 52290 | Otras actividades de apoyo al transporte | ✅ If Sarah handles own logistics |

**Recommended:** Add 46491 + 47730 to RUC.
**Process:** Contador files RUC amendment via SET portal.
**Cost:** Gs 500K–1.5M (contador fee).
**Time:** 30–60 days.

---

## 5. SET — Tax obligations

**IVA (monthly):**
- 10% on sales
- 10% on import (already counted above as IVA import)
- Credit for IVA paid on inputs (DINAVISA fees, despachante, freight, stock)
- File: Monthly declaration via SET portal (Marangatu)

**IRP (Impuesto a la Renta Personal) — if Sarah persona física:**
- Progressive rate 8–10% on net income
- File: Annually via IRP system
- Threshold: Gs 50M annual exempt

**IRE (Impuesto a la Renta Empresarial) — if becomes SA/SAS:**
- 10% on net income
- Quarterly advance payments + annual return
- Recommended once Sarah hits Gs 100M+ annual revenue

**Recommendation for v1:** Stay persona física with RUC. Switch to SAS only at Gs 100M+ annual revenue.

---

## 6. Ley 4868/13 — Comercio Electrónico

**PY law regulating e-commerce.**

**Required disclosures on e-com site:**

| Disclosure | Required? |
|-----------|-----------|
| Nombre del proveedor | ✅ Yes |
| RUC | ✅ Yes |
| Dirección física | ✅ Yes |
| Teléfono / email | ✅ Yes |
| Características del producto | ✅ Yes |
| Precio total (incluye IVA) | ✅ Yes |
| Costos de envío | ✅ Yes |
| Política de devolución | ✅ Yes |
| Plazo de entrega | ✅ Yes |
| Derecho de arrepentimiento (5 días) | ✅ Yes |

**Implementation:** Even for WA-first model, Sarah should have a 1-page "Términos y Condiciones" she can share via WA link. Paragu-ai subdomain microsite should include footer with all disclosures.

---

## 7. Ley 7.593/2025 — Protección de Datos Personales

**PY data privacy law.**

**Key requirements for Sarah:**

| Requirement | Implementation |
|-------------|----------------|
| Consentimiento explícito | "Acepto recibir comunicaciones de Enki" checkbox in WA/IG |
| Finalidad明确 | "Tus datos se usan solo para procesar tu pedido" |
| Derecho de acceso | Customer can request their data |
| Derecho de supresión | Customer can request deletion |
| Seguridad razonable | Don't store customer data in plain spreadsheets |
| No transferencia sin consentimiento | Don't share customer list with third parties |

**Practical implementation for Sarah:**
- Use a CRM (HubSpot Free, Pipedrive, or Google Contacts) with password protection
- Don't share customer lists with Sexitive AR or anyone else
- Add privacy policy line in every WA greeting message

---

## 8. Habilitación Municipal (Asunción)

**Required:** Yes, for any commercial operation in Asunción
**Process:** Municipalidad de Asunción habilitación commercial
**Cost:** Gs 200K–500K/year (varies by categoría + tamaño)
**Time:** 30–60 days
**Applies to:** Online retail with PY domicile

**Action:** Sarah needs to verify if her current RUC dirección already has habilitación. If she's operating from home (no commercial address), may need to register.

---

## 9. Defensa del Consumidor — Returns policy

**Required disclosures on returns:**

| Element | Disclosure |
|---------|-----------|
| Derecho de cambio | "5 días desde la entrega" |
| Productos excluidos | "Productos íntimos abiertos no se cambian" |
| Productos defectuosos | "Cambio inmediato o devolución" |
| Costo de envío devolución | "A cargo del cliente (salvo defecto nuestro)" |
| Plazo de resolución | "5 días hábiles" |

**Sarah's recommendation:**
- No returns on opened intimate products (industry standard, DINAVISA-aligned)
- 7-day exchange on sealed products
- Full replacement on defective / wrong-shipped
- Customer pays return shipping

---

## 10. Etiquetado requerido (DINAVISA)

**Required on consumer-facing labels (Spanish):**

| Element | Required |
|---------|----------|
| Nombre del producto | ✅ |
| Ingredientes (INCI) | ✅ |
| Contenido neto | ✅ |
| Lote + fecha de vencimiento | ✅ |
| Nombre del importador | ✅ (Sarah's RUC) |
| Dirección del importador | ✅ |
| País de origen | ✅ |
| Condiciones de almacenamiento | ⚠️ If applicable |
| Modo de uso / advertencias | ✅ For stimulants/lubricants |
| "Uso externo" warning | ✅ For topical products |

**Implementation:** Use Sexitive AR labels + add Spanish-language sticker overlay (Sarah prints in PY).

---

## 11. Insurance — Product liability

**Recommended:** Póliza de responsabilidad civil para productos
**Cost:** Gs 500K–1.5M/year for small business
**Coverage:** Up to Gs 50–100M per claim
**Provider:** Aseguradora del Este, La Paraguaya, orMapfre PY

**Recommendation:** Defer to month 3+ (when revenue justifies). For now, mitigate via clear product warnings + returns policy.

---

## 12. Despachante + Contador shortlist criteria

### Despachante (customs broker)

**Look for:**
- ✅ Experience with cosmetics import (not general imports)
- ✅ DINAVISA registration experience
- ✅ MERCOSUR origin certificate processing
- ✅ Bilingual (Spanish + Portuguese/English helpful)
- ✅ References from other cosmetics importers
- ✅ Per-shipment fee structure (not % of value)

**Questions to ask:**
1. ¿Cuántos embarques de cosméticos AR→PY ha procesado en los últimos 12 meses?
2. ¿Cuál es su fee por embarque + por SKU?
3. ¿Manejan el Certificado de Origen MERCOSUR?
4. ¿Pueden referirme con otro importador de cosméticos?
5. ¿Cuánto tarda el trámite DINAVISA NSO en su experiencia?

### Contador (accountant)

**Look for:**
- ✅ Experience with e-commerce businesses
- ✅ Familiar with RUC amendments for cosmetics
- ✅ IVA + IRP filing experience
- ✅ Monthly fee structure (not per-filing)

**Questions to ask:**
1. ¿Cuántos clientes de e-commerce con RUC tenés?
2. ¿Has manejado RUC amendments para agregar actividad de cosméticos?
3. ¿Cuál es tu fee mensual por liquidación de IVA + IRP?
4. ¿Podés ayudarme con la habilitación municipal?

---

## Compliance timeline for launch

| Week | Action | Owner |
|------|--------|-------|
| W1 | Confirm DINAPI Enki + Kinky | Sarah |
| W1 | Engage contador (RUC check) | Sarah |
| W2 | Engage despachante (quote) | Sarah |
| W2 | Order Sexitive AR + ask for Certificado de Origen | Sarah |
| W3 | Submit DINAVISA NSO for 3 SKUs | Despachante |
| W4 | Receive NSO approvals | DINAVISA |
| W5 | Customs clearance + IVA payment | Despachante |
| W6 | First stock arrives | Sarah |
| W6 | Apply bilingual stickers + ship to launch | Sarah |

---

## Compliance cost summary (Year 1)

| Item | Cost (Gs) |
|------|----------:|
| DINAVISA NSO × 3 SKUs | 1,500,000–2,400,000 |
| Despachante fees (3–4 shipments) | 3,600,000–6,000,000 |
| Contador (monthly × 12) | 2,400,000–4,800,000 |
| Habilitación municipal (Asunción) | 200,000–500,000 |
| RUC amendment (actividad codes) | 500,000–1,500,000 |
| Liability insurance (optional v1) | 0 (defer) |
| **TOTAL compliance cost Year 1** | **Gs 8.2–15.2M** |

**This is the BIG hidden cost** beyond launch budget. Sarah should budget Gs 10–15M for full Year 1 compliance, not just launch.

---

*Last updated: 2026-06-26 | Author: Erebus research, not legal advice*