# AGENTS.md — Sarah's Lubricant Business Strategy Repo

**Canonical location:** `/root/repos/sarah-lubricants` (NOT `/root/sarah-lubricants` — that was a stale snapshot, renamed to `sarah-lubricants.OLD` on June 26, 2026)

**Client:** Sarah (entrepreneur entering intimate-wellness distribution in Paraguay)
**Source brand:** Sexitive (Argentina) — imported and resold in PY
**Repo type:** Strategy + launch kit (read-heavy, docs + research, minimal code)
**Language:** Spanish (Paraguayan) + English for system terms

## Ground rules

- Every repo change must keep the strategy coherent and pricing-consistent.
- Do not edit client-template files under `09_TEMPLATES/` without flagging it as a content change.
- Keep product data accurate to Sexitive catalog; do not invent SKUs, prices, or product claims outside the canonical catalog at `01_RESEARCH/market/sexitive-catalog-master.md`.
- All product positioning must respect packaging claims (e.g., My Hemp explicitly says "not for genital use" — do not contradict Sexitive's own labeling).
- Intimate-wellness copy must be tasteful, sex-positive, never vulgar. Avoid clickbait, avoid objectification.

## Workflow expectations

- Read more than you produce: this repo is strategy-first. Confirm facts before changing docs.
- The questionnaire in `01_RESEARCH/legal-regulatory/validacion-cliente-sarah.md` is the source of truth for unblocking — Sarah fills it, then we build.
- Preserve section IDs, anchor headings, and pricing cross-reference blocks in every file.
- If a doc conflicts with the canonical catalog or a higher-priority index, update the doc and note where else should change.

## Quality bar

- Single source of truth for products: `01_RESEARCH/market/sexitive-catalog-master.md`
- Single source of truth for pricing: `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v1.md` (only after Sarah confirms cost basis)
- Single source of truth for unblocking decisions: `01_RESEARCH/legal-regulatory/validacion-cliente-sarah.md`
- Entry points expected to stay accurate: `README.md`, `COMPLETE-INDEX.md`, `start-here.md`, and `TODO.md`

## Boundaries

- Do not push to remote without committing staged changes in logical scopes.
- Do not add AI tool configs that require secrets.
- Do not turn this into software. If any automation would help, implement it as a script in `tools/scripts/`.
- Do not publish adult-content material as marketing assets; use Sexitive's own brand-safe product photography or commissioned alternatives only.
- Do not import regulated products (supplements, CBD topical) without DINAVISA registration on Sarah's side.

## Business model (working hypothesis — pending Sarah validation)

Sarah is bringing **Sexitive** (Argentine intimate-wellness brand) into Paraguay. Three plausible models:

1. **Authorized distributor** — formal agreement with Sexitive AR, named on their site as PY distributor.
2. **Independent importer / reseller** — buys from Sexitive AR (or local AR e-commerce), resells in PY under a PY sub-brand.
3. **Private-label rebrand** — sources from AR manufacturer, sells under entirely new PY brand.

**Model 1 is the lowest risk and highest credibility. Model 3 is the highest margin and longest path.**

The repo is structured to support any of the three — most legal/regulatory content applies to all; brand-identity content splits per model.
