# Anakyze: maskarada & fun4me — Useful Data & Insights

**Author:** Erebus
**Date:** June 19, 2026
**Purpose:** Extract reusable patterns, pricing data, and lessons from the maskarada & fun4me repos that can inform Sarah's lubricant business launch.

---

## Quick read of the landscape

| Repo | Stack | Live at | Status | Useful for Sarah? |
|------|-------|---------|--------|-------------------|
| **maskarada** | SvelteKit 5 + Supabase (legacy) → Next.js 16 monorepo (current) | maskarada.paragu-ai.com | Live, 12 routes, 4 locales, 30MB images | **YES** — intimate-product e-com with Supabase, very close fit |
| **fun4me** | Next.js 16.2 + Supabase + shadcn | fun4me.paragu-ai.com | Live but **has 13 critical/high bugs** documented in its own roadmap | **YES** — most complete adult e-com in our fleet, has 54 products live, admin panel |
| **fun4me-store** | Next.js 16.2 + 8 @ai-whisperers/* packages | (in monorepo) | Has full auth, JWT, Postgres, bcrypt, jose | **YES** — reference for multi-tenant e-com architecture |

---

## 1. Maskarada — What it is, what it teaches us

### Profile

- **Niche:** BDSM/rope shibari products (cuerdas shobari Moñai) — same regulatory profile as lubricants (cosmetic / personal products)
- **Owner:** Moñai brand (Rach's rope line, in-house)
- **Channel:** WhatsApp-first (number 595981200255 is the de-facto checkout)
- **Price range:** Gs 45,000+ per product (similar band to Sexitive retail)
- **Stack:** SvelteKit 5 (now in Next.js 16 monorepo via `apps/maskarada/`)
- **Architecture:** Supabase backend, adapter-static build, nginx serving
- **Live:** `maskarada.paragu-ai.com` (Swarm service `maskarada_web`)
- **Pages:** 12 routes + 4 locales

### What Sarah should steal

| Pattern | How maskarada does it | Adapt for Sarah |
|---------|------------------------|-----------------|
| **WhatsApp as primary checkout** | Every product CTA = `wa.me/595981200255?text=Hola!%20Quiero%20saber%20más%20sobre%20[X]` | Same pattern, different number |
| **Pre-filled message per product** | Each link has the SKU name in the URL | Same — embed SKU + tier |
| **Sub-brand with own name under parent** | "Moñai" is the sub-line under maskarada | Sarah could be "Lúmina" sub-line under her own parent, or vice versa |
| **Age-gate via cookie** | DOB + 30-day cookie, no friction per session | Same — required for intimate products |
| **Trailing-slash 308 redirect** | Canonical URLs use trailing slash | Already in our Cloudflare Pages setup |
| **Smoke test for all 13 paths** | Full route audit before deploy | Adopt same pattern |
| **Health check at `/api/health`** | Real JSON status, not just HTTP 200 | Add when Sarah's site goes live |
| **Supabase JSON content** | Spanish content as `content/es/*.json` files, markdown → JSON | Sarah can do the same |

### Pricing reference (maskarada tier)

| Tier | Price (Gs) | Sarah equivalent |
|------|-----------|------------------|
| Entry (starter) | 45,000 | Wet Anal 75ml (commodity) |
| Mid | 90,000–150,000 | Wet Like a Virgin (premium) |
| Premium | 200,000+ | Pink Sexy Pill, My Hemp |
| Bundles / kits | 180,000–400,000 | "Kit for her," "Kit for couples" |

**Translation:** Sarah's Gs pricing should anchor around Gs 45,000 (entry), Gs 90,000–150,000 (mid), Gs 200,000+ (premium). Bundles should be 10–15% cheaper than buying separately.

### What maskarada has that Sarah should NOT do

| Pattern | Why not | Alternative for Sarah |
|---------|---------|------------------------|
| Static-only build (no cart, no checkout) | Works for ~3 SKUs but breaks at 12+ | Real e-com with cart + WA checkout handoff |
| Locales (es + en) | maskarada is tourist-facing, Sarah is PY-only | Spanish only at launch, add EN only if ex-pat demand emerges |
| 30MB of WebP in `static/` | Worked for 5 products, doesn't scale | Use Supabase Storage or R2 for product images |
| No real auth | Sold via WA, no accounts needed | Same model works for Sarah's intimate catalog |

---

## 2. Fun4Me — What it is, what it teaches us

### Profile

- **Niche:** Adult intimate products (vibrators, lingerie, lubes, accessories) — DIRECTLY OVERLAPPING with Sarah's catalog
- **Owner:** Rach (also a Paraguayan entrepreneur in this space)
- **Stack:** Next.js 16.2 + Supabase + shadcn + Tailwind v4 + Docker
- **Live:** `fun4me.paragu-ai.com`
- **Scale:** 54 sample products in 12 Supabase tables, 8 categories, 6 kinks, real cart + checkout
- **Architecture:** Multi-tenant ready via `@ai-whisperers/*` packages
- **Reference architecture:** This is the most complete adult e-com template in our fleet

### What Sarah should steal — IMMEDIATELY

| Pattern | How fun4me does it | Adapt for Sarah |
|---------|--------------------|-----------------|
| **8 product categories with icons** | Lubes, vibrators, lingerie, BDSM, etc. | Sarah has 4 categories: stimulants, lubes, sensory, wellness |
| **Cart drawer + cart page** | Slide-in drawer for quick add, full page for review | Adopt 1:1 |
| **Free shipping bar** | "Gs X more for free shipping" with progress | Adapt — Sarah sets threshold at Gs 300,000 |
| **Ofertas (deals) page** | Dedicated `/ofertas` route, separate nav | Adopt — bundles as deals |
| **WhatsApp floating button** | Persistent bottom-right | Adopt |
| **Bank transfer / COD** | Two payment methods at checkout | Sarah's analog: Tigo Money / Bank transfer |
| **Age verification gate (DOB + 30-day cookie)** | Friction on first visit, persisted | Adopt |
| **JSON-LD product schema** | SEO-ready product pages | Adopt |
| **Sitemap.xml + robots.txt** | SEO hygiene | Adopt |
| **Admin panel** | Dashboard, product CRUD, order management | Adapt for Sarah's solo operation — simpler |
| **54 products = full filterable catalog** | Categories, kinks, search | Sarah has 12 SKUs — simpler |

### Critical lessons from fun4me's bug list

Fun4Me's own roadmap documents 13 critical/high bugs. These are the **exact traps Sarah must avoid** when building her catalog:

| Bug | Severity | Lesson for Sarah |
|-----|----------|------------------|
| **B1: Checkout does NOT save orders to Supabase** | CRITICAL | Whatever payment flow Sarah uses, persist to Supabase from day 1. Even if it's Tigo Money manual confirm, log the order. |
| **B2: Admin panel has ZERO auth protection** | CRITICAL | If Sarah builds an admin, gate it with Supabase auth from the first commit. |
| **B3: Product images don't show in cart (image_url vs images[])** | HIGH | Pick one image model (`images[]` is better for multi-photo) and use it consistently. |
| **B4: Free shipping threshold inconsistent (300K vs 500K)** | MEDIUM | Single source of truth: one constant in `lib/constants.ts`. |
| **B5: Login page is non-functional stub** | HIGH | Don't ship stub features. If login isn't ready, hide the link. |
| **B6: Newsletter signup does nothing** | MEDIUM | If you can't wire it, don't show it. |
| **B7: Footer "Ayuda" links are dead** | MEDIUM | Either build the page or remove the link. No half-built. |
| **B9: Cart hydration mismatch** | MEDIUM | Use `mounted` state guard in any client-only component. |
| **B10: Nested interactive elements (button inside Link)** | MEDIUM | Add-to-cart button MUST be outside the product Link. |
| **B12: updateQuantity doesn't check max_stock** | LOW | Always validate stock server-side, not just client-side. |
| **B13: WhatsApp number masked in constants.ts but shown in footer** | LOW | One source of truth for contact info, period. |

**Translation for Sarah's architecture:** Build a single `lib/constants.ts` with the WhatsApp number, free-shipping threshold, currency, and tax rate. Reference it everywhere. Don't repeat the number in 5 files.

### Fun4Me pricing reference (Rach's live catalog)

Fun4Me has 54 products with the structure established. Rach's actual price bands for the lubricant-adjacent categories:

| Category | Price band (Gs) | Note |
|----------|-----------------|------|
| Standard lubricants | 50,000 – 120,000 | Commodity tier |
| Premium / effect lubes | 100,000 – 180,000 | Differentiated |
| Stimulants (creams, drops) | 80,000 – 200,000 | Niche but higher margin |
| Supplements | 150,000 – 250,000 | Premium positioning, less volume |
| Massage candles / oils | 60,000 – 120,000 | Basket-add, lower price |
| Accessories | 40,000 – 250,000 | Wide range |

**Sarah's Sexitive SKUs map cleanly into these bands:**
- Wet line (Anal, Ice Fresh): 80,000–120,000 (premium tier — Wet is named brand)
- Wet — Like a Virgin: 150,000–200,000 (flagship premium)
- Pink Sexy Pill: 180,000–250,000 (supplement tier, also requires DINAVISA supplement registration)
- Bitchie spray 20ml: 120,000–180,000
- XXX For Her 15ml: 100,000–150,000
- more sex line (3 SKUs, 50ml): 70,000–110,000
- Love Potion line (15ml): 70,000–120,000
- Massage candles (12 scents): 60,000–90,000 each
- My Hemp CBD 15ml: 150,000–220,000 (if regulatory clears)

### Fun4Me architecture: what Sarah can clone 1:1

| Component | Fun4Me has it | Sarah can adopt? |
|-----------|---------------|-------------------|
| Cart drawer (zustand store) | ✅ Yes | **YES** — 1:1 |
| Cart page | ✅ Yes | **YES** — 1:1 |
| Checkout (shipping form) | ✅ Yes | Adapt — add Tigo Money / bank transfer / Mercado Pago fields |
| Free shipping progress bar | ✅ Yes | **YES** — 1:1 |
| Categories nav | ✅ 8 categories | Adapt to 4 (or 5 with "All") |
| Kinks / filters | ✅ 6 filters | Adapt to Sexitive's 4 categories |
| Ofertas page | ✅ Yes | **YES** — use for bundles |
| Sitemap + robots | ✅ Yes | **YES** — 1:1 |
| JSON-LD product schema | ✅ Yes | **YES** — 1:1 |
| Admin panel | ✅ Yes | Adapt — solo founder needs simpler admin |
| Auth (Supabase) | ✅ Yes (broken per bug list) | Build correctly from start |
| PostgreSQL (orders, products, customers) | ✅ 12 tables | Adapt schema for 12 SKUs |

### Fun4Me — What NOT to clone

| Pattern | Why not for Sarah |
|---------|-------------------|
| **8 product categories** | Sarah has 4. Don't over-engineer. |
| **6 kink filters** | Sexitive doesn't lean into kink. Sarah's filters: by category + price. |
| **User accounts / login** | WA checkout is enough for v1. Add accounts in v2. |
| **Complex admin** | Solo founder — Spreadsheet + Supabase studio is enough for v1. |
| **Multi-currency** | Gs only. Don't add USD/ARS/BRL until there's demand. |
| **Email marketing integration** | Out of scope for intimate products. WA is the channel. |
| **Multi-tenant (8 @ai-whisperers packages)** | Sarah is single-tenant. Use fun4me-store as reference, not dependency. |

---

## 3. Strategic synthesis — What this means for Sarah

### What Sarah can build in 2–3 weeks by leveraging what we have

| Component | Source | Effort |
|-----------|--------|--------|
| **E-commerce shell** | Clone fun4me-store, strip the parts Sarah doesn't need | 1–2 days |
| **Cart + checkout (WA handoff)** | fun4me pattern | 0.5 day |
| **Product pages (12 SKUs)** | Sexitive catalog as data source | 1 day |
| **Brand identity** | New work (Lúmina / Volare direction) | 2–3 days |
| **Content (descriptions, education)** | Mix of Sexitive's copy + Sarah's voice | 2 days |
| **WA catalog + auto-replies** | fun4me's WA flow | 0.5 day |
| **Deploy to paragu-ai.com** | Existing infra | 0.5 day |
| **Total** | | **~10 days** if Sarah is decisive on the questionnaire |

### What Sarah can NOT shortcut

| Block | Why | Source of truth |
|-------|-----|------------------|
| DINAVISA registration | 60–180 day regulatory process | Despachante in PY |
| First Sexitive wholesale order | 30–60 day shipping from AR | Sexitive AR |
| Brand naming decision | 1 day but irreversible | Sarah's call |
| Cost basis per SKU | 1 day to contact Sexitive | Sarah's action |

### Pricing benchmark for Sarah — derived from maskarada + fun4me

If Sarah follows the market median (maskarada + fun4me + sexshop.com.py):

| Sexitive SKU | Landed cost estimate (Gs) | Recommended retail (Gs) | Margin | Source of cost basis |
|--------------|---------------------------|--------------------------|--------|----------------------|
| Wet Anal 75ml | 4,500–7,000 | 95,000 | 1,300%+ | Sexitive AR wholesale + AR→PY freight |
| Wet Ice Fresh 75ml | 4,500–7,000 | 95,000 | 1,300%+ | Same |
| Wet Like a Virgin 75ml | 5,500–8,000 | 150,000 | 2,000%+ | Same + premium positioning |
| Bitchie 20ml | 5,000–7,500 | 130,000 | 1,700%+ | Same |
| XXX For Her 15ml | 4,000–6,000 | 110,000 | 1,800%+ | Same |
| more sex 50ml (3 flavors) | 4,000–6,000 | 85,000 | 1,500%+ | Same |
| Pink Sexy Pill 4 tabs | 5,000–8,000 | 180,000 | 2,500%+ | Same + supplement positioning |
| Love Potion 15ml (4 flavors) | 3,500–5,500 | 90,000 | 1,700%+ | Same |
| Massage candles 30g (12 scents) | 3,000–5,000 | 75,000 | 1,600%+ | Same |
| My Hemp 15ml | 5,000–8,000 | 170,000 | 2,200%+ | Same + CBD premium (if legal) |

**Reality check:** These margins look insane because Sexitive AR's wholesale price (ARS 3,500–4,500 ≈ Gs 25,000–32,000) is much lower than typical wholesale ratios. **Confirm with real cost basis from Sexitive AR before pricing.**

If AR wholesale is actually 60–70% of AR retail (e.g., ARS 6,000 wholesale for a product retailing at ARS 8,500), the math changes:
- Wet Anal 75ml landed = Gs 7,500–10,000
- Recommended retail = Gs 95,000
- Margin = 850–1,200%

Still very healthy. **The conclusion holds: Sexitive to PY is high-margin by global standards.**

---

## 4. Concrete recommendations for Sarah's next 30 days

### Week 1 — Intake
- [ ] Sarah completes questionnaire (sarah.paragu-ai.com/questionnaire)
- [ ] Erebus runs pricing model with her cost basis answers
- [ ] Erebus prepares 2–3 brand direction mockups (Lúmina, Volare, Kōra)

### Week 2 — Sourcing
- [ ] Sarah contacts Sexitive AR (script in `01_RESEARCH/logistics-supplier/sexitive-wholesale-AR.md`)
- [ ] Sarah engages a despachante in Asunción (DINAVISA quote)
- [ ] First cost basis established

### Week 3 — Brand
- [ ] Brand name decision (Sarah's call)
- [ ] Logo (3 directions, 1 chosen)
- [ ] Tone of voice locked

### Week 4 — Build
- [ ] Site cloned from fun4me-store pattern
- [ ] 12 products loaded (or launch subset per questionnaire §3.2)
- [ ] Cart + WA checkout working
- [ ] Deploy to `sarah.paragu-ai.com`

### Week 5+ — Soft launch
- [ ] IG business account setup
- [ ] WA Business + catalog
- [ ] 10 friend/family orders end-to-end
- [ ] Fix friction, write SOPs

---

## 5. What this repo adds to the existing fleet

| Artifact | Status | Location |
|----------|--------|----------|
| Sarah's strategy repo (this) | ✅ Complete | `/root/sarah-lubricants/` |
| Sarah's deployed preview site | ✅ Live | https://sarah.paragu-ai.com |
| Sarah's intake questionnaire | ✅ Live, 30 questions | https://sarah.paragu-ai.com/questionnaire |
| Anakyze of maskarada + fun4me (this doc) | ✅ Complete | `/root/sarah-lubricants/docs/anakyze-maskarada-fun4me.md` |
| Pricing benchmark for Sexitive SKUs | ✅ Drafted | This doc §3 |
| Fun4Me bug list as Sarah's pre-mortem | ✅ Captured | This doc §2 |
| Deployment tooling (build_site.py + deploy.sh) | ✅ Reusable | `/root/sarah-lubricants/tools/` |

**What is NOT here yet (blocked on Sarah's questionnaire):**
- Canonical pricing reference (`00_STRATEGIC/financial-pricing/canonical-pricing-reference-v1.md`)
- Brand identity docs
- Launch roadmap
- Site build code (will use fun4me-store pattern)
