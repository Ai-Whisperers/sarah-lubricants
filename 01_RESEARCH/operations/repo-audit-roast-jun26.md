# Repo Audit & Roast — June 26, 2026

**This is not a roast to be cruel. It's a roast to be useful. Every repo gets bloated when built fast. The question is: what's signal, what's noise, what's missing.**

**Method:** I read every key file. I ran quality metrics across all 84 docs. I checked what's actually load-bearing vs. decorative. Then I built the upgrade list.

---

## What the repo actually IS

**A 6-session research binge that produced 84 markdown files, 100K words, 15K lines, 98 HTML pages.**

It's:
- ✅ Strategy-heavy (correct)
- ✅ Spanish-first (correct for PY market)
- ✅ Single source of truth for products/pricing/brand (correct)
- ❌ Bloated — multiple docs say similar things
- ❌ Lacking actual *data* — most numbers are estimates
- ❌ No real vendor quotes (just templates)
- ❌ Index rot — COMPLETE-INDEX and README drift from each other
- ❌ Decision-fatigue for Sarah — too many docs to read
- ❌ Sarah's actual decisions are buried

---

## 🔥 THE ROAST

### Roast 1 — Sarah can't read this
84 docs. 100K words. That's a 6-hour read minimum.

**The most important document for Sarah** (the operator) is `start-here.md`. **It's 4 months stale** — it still says "Sexitive has 12 SKUs" (we have 158). It still says "Sarah needs to answer 3 questions" (she already did). It still says the trio is "to be confirmed" (it's locked).

A new visitor to this repo would conclude the project is at the *very beginning*. The actual state is "we have everything except vendor quotes, a logo, and Sarah's actual data."

**Sarah would land on `start-here.md` and not understand what's already been done or what's still needed.**

### Roast 2 — The pricing math is wrong
We modeled at **4 Gs/AR$** when:
- Argentina wholesale inflation is **34.5% YoY** (INDEC May 2026)
- Sarah's verbal June 17 trip prices (Bitchie Gs 19,700) are *already below* our "Mayorista ÷ 2" estimate
- We have **zero confirmed Sexitive AR Mayorista pricing**
- The 4:1 FX assumption will likely be 5:1 or 6:1 within 12 months

**The entire pricing model is built on top of an unvalidated estimate, with a known-moving FX rate, against a supplier whose prices we haven't seen.**

This isn't unique to us — every startup does this — but we should be screaming about it louder. The "AUDIT DISCLAIMER" at the top of `canonical-pricing-reference-v1.md` is too quiet for the stakes.

### Roast 3 — We over-engineered and under-validated
84 docs. 10 of them are blog posts. 5 of them are 1-line templates. We have:
- **30+ SKU battle cards** but **0 customer interviews**
- **6 marketing channels** but **0 customers acquired**
- **3 payment options documented** but **0 payments processed**
- **4 B2B pricing tiers designed** but **0 B2B meetings held**
- **4 influencer outreach templates** but **0 influencers contacted**

**Documentation is not validation.** We have a beautiful strategy repo. Sarah still has to do the actual work.

### Roast 4 — The "Sarah has 20K followers" assumption is unverified
We assume Enki's existing IG audience will convert to Kinky (intimate wellness). **Never validated.** Could be:
- 20K lifestyle followers who reject intimate content
- 20K followers with 1% engagement (= 200 real people)
- 20K followers mostly outside Paraguay
- 20K bot followers

**This single assumption underlies every revenue projection.** If it's wrong by 50%, our cash flow model is wrong by 50%.

### Roast 5 — Documentation drift
- README's quick-link table has 24 entries; COMPLETE-INDEX has different organization
- `start-here.md` contradicts current state
- `kinky-store-assessment.md` still exists as deprecated, confusing readers
- `enki-store-assessment.md` doesn't link to it explicitly
- Date stamps are inconsistent ("June 26, 2026" everywhere, no time, no author)

### Roast 6 — The launch roadmap is too long
The 90-day launch roadmap is 262 lines. Sarah's day-to-day reality will be:
- Respond to WhatsApp
- Pack orders
- Post 1 IG story
- Maybe write a thank-you card

**The roadmap should be 1 page Sarah prints and sticks on the wall.** Not a long-form doc.

### Roast 7 — We have no customer voice
Out of 100K words:
- 0 customer testimonials
- 0 customer quotes
- 0 customer pain points articulated in their words
- 0 user research beyond the questionnaire Sarah filled out

The blog posts are educated guesswork. The "competitor battle cards" are inferences. **Nothing has been tested against a real person.**

### Roast 8 — The 158-SKU catalog is bloat
**Sarah is launching with 3 SKUs.** The 158-SKU catalog master is reference material. But it's been treated as a marketing deliverable. It includes products Sarah will never sell (Pink Pill = 90-180 day DINAVISA, My Hemp = zona gris, supplements Sarah can't launch yet).

For the actual launch, what Sarah needs is **a 3-SKU launch catalog** + **a "future SKUs" roadmap**. Not a 158-row table.

### Roast 9 — The risk register is theoretical
"R8 — Sarah burnout" is rated 16/25 (highest). But it has **no mitigation that's actionable today**. "Hire part-time helper at month 2" — but no job description, no cost, no time to hire.

Compare to **R3 — Q5 PDF higher costs (score 12)** — mitigation says "negotiate special viajero pricing with Sexitive AR." But we don't know if Sexitive will agree. There's no backup for "what if they don't."

The risk register reads like an academic exercise, not an operational tool.

### Roast 10 — `kinky-store-assessment.md` still exists
This deprecated file contradicts current state. **First-time visitors will hit it.** Confusing.

### Roast 11 — `tools/deploy.sh` still hardcoded path
Wait — actually fixed in Session 8. Good. But the `tools/build_site.py` *output* structure changed (per-folder index.html) and the new structure isn't documented anywhere. A new Erebus session would have to reverse-engineer it.

### Roast 12 — `02_MEETINGS/2026-06-20-clarifying-questions.md` mixes questions and answers
Document title says "clarifying questions" but it contains both the questions AND Sarah's answers. Confusing. Should be split: `2026-06-20-clarifying-questions-asked.md` and `2026-06-22-clarifying-questions-answered.md`.

### Roast 13 — The "Sexitive has 12 SKUs" zombie data
- `start-here.md` still says 12
- `validacion-cliente-sarah.md` (the questionnaire) says 12
- These were correct in June but wrong by June 26
- No note that the questionnaire is "stale, see sexitive-catalog-master.md for current"

### Roast 14 — No "what's unblocking you right now" page
The most actionable question — "what does Sarah need to do this week to unblock launch?" — is buried across 4 different files. Should be 1 page.

---

## 📊 Quantitative Audit

### Quality metrics (84 docs)

| Metric | Count | % |
|--------|------:|--:|
| Have H1 heading | 84 | 100% ✅ |
| Have date stamp | 50 | 60% |
| Have "Last updated" footer | 46 | 55% |
| Have internal links | 1 | **1% ❌** |
| Have tables | 80 | 95% ✅ |
| Have checkboxes | 11 | 13% |
| Have code blocks | 30 | 36% |
| >10 headings (deep structure) | 60 | 71% |
| <100 lines (shallow) | 16 | 19% |
| >500 lines (bloated) | 0 | 0% ✅ |

### Biggest issues by impact

| Issue | Severity | Fix effort |
|-------|---------:|----------:|
| `start-here.md` contradicts current state | 🔴 Critical | 1h |
| Pricing math built on FX guess + unverified estimates | 🔴 Critical | 4h |
| No customer voice / research validation | 🟠 High | 8h |
| Internal link graph missing (1% have internal links) | 🟠 High | 4h |
| Multiple deprecated/zombie files | 🟠 High | 1h |
| Doc drift between README / COMPLETE-INDEX | 🟡 Medium | 2h |
| Risk register mitigations not actionable | 🟡 Medium | 4h |
| Launch roadmap too long | 🟡 Medium | 1h |
| 158-SKU catalog not pruned to launch trio | 🟡 Medium | 1h |
| No "this week for Sarah" action page | 🔴 Critical | 1h |

**Total upgrade effort:** ~28 hours

---

## ✅ What actually IS good (don't touch)

These are well-built. Don't refactor for the sake of it:

- ✅ `sexitive-catalog-master.md` — accurate 158-SKU reference
- ✅ `competitor-pricing-scraped.md` — real scraped data
- ✅ `py-compliance-roadmap.md` — comprehensive + accurate
- ✅ `risk-register.md` — comprehensive, just needs actionable mitigations
- ✅ `business-model-canvas.md` — solid Osterwalder
- ✅ `cash-flow-model-12mo.md` — good scenario modeling (if estimates are right)
- ✅ `customer-messages.md` — 12 ready-to-paste templates
- ✅ `glossary.md` — necessary reference
- ✅ The 10 SEO blog posts — quality content

---

## 🎯 THE UPGRADE PLAN (in priority order)

| # | Upgrade | Why | Effort |
|---|---------|-----|-------:|
| 1 | **Rewrite `start-here.md`** | Sarah's first read, contradicts state | 1h |
| 2 | **Create `this-week-for-sarah.md`** | Action page, replaces 4-doc hunt | 1h |
| 3 | **Prune `sexitive-catalog-master.md`** to launch-focused | Drop what's not in launch | 1h |
| 4 | **Add WARNING banner to pricing math** | FX + estimate reality | 0.5h |
| 5 | **Fix `kinky-store-assessment.md`** → archived with redirect | Zombie file | 0.5h |
| 6 | **Split clarifying questions doc** | Title vs content mismatch | 0.5h |
| 7 | **Add internal link graph** (one-pass) | 1% internal links = 99% orphan | 4h |
| 8 | **Make risk mitigations actionable** (owner + due date) | Risk register usability | 4h |
| 9 | **Compress launch roadmap to 1 page** | Print-and-stick version | 1h |
| 10 | **Sync README + COMPLETE-INDEX** | Single source for index | 2h |
| 11 | **Add decision log** (chronological decisions made) | Historical context | 2h |
| 12 | **Add "what we don't know" page** | Honest gaps | 1h |
| 13 | **Add validation status doc** (what's tested vs. assumed) | Critical for risk awareness | 2h |
| 14 | **Write 1-page "Day 1" operational checklist** | Sarah's actual daily work | 1h |
| 15 | **Add "Sarah's roadmap to launch"** (decision tree) | Help Sarah decide | 1h |

**Total:** ~21 hours

---

## 🚀 EXECUTING UPGRADE NOW

I'll do these in order of value. Starting with the critical ones (Sarah's read + action), then structural (link graph + drift fix), then quick wins.

Skipping: blog post production (we have 10 of 38, that's enough for v1).

Continuing to: **what data we still need to validate** (separate doc).

Let me know if you want any specific upgrades prioritized differently.