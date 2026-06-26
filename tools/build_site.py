#!/usr/bin/env python3
"""Render every Sarah repo .md into build/<path>/index.html and also create short URL slugs."""
import os, re, pathlib, html, markdown, shutil

ROOT = pathlib.Path("/root/repos/sarah-lubricants")
OUT  = ROOT / "build"

SLUGS = {
    "sarah": "sarah-questionnaire-hub",
    "questionnaire": "01_RESEARCH/legal-regulatory/validacion-cliente-sarah",
    "catalog":       "01_RESEARCH/market/sexitive-catalog-master",
    "market":        "01_RESEARCH/market/paraguay-market-snapshot",
    "legal":         "01_RESEARCH/legal-regulatory/dinavisa-import-requirements",
    "mercosur":      "01_RESEARCH/legal-regulatory/mercosur-argentina-paraguay-tariffs",
    "models":        "00_STRATEGIC/strategic-context/three-models-comparison",
    "supplier":      "01_RESEARCH/logistics-supplier/sexitive-wholesale-AR",
    "freight":       "01_RESEARCH/logistics-supplier/ar-py-freight-options",
    "competition":   "01_RESEARCH/competition/competitor-profiles-5",
    "payments":      "01_RESEARCH/payments/tigo-money-mercado-pago-bank",
    "brand":         "01_RESEARCH/brand-identity/naming-options",
    "operations":    "01_RESEARCH/operations/fulfillment-returns-customer-service",
    "anakyze":       "docs/anakyze-maskarada-fun4me",
}

PAGE_CSS = """
:root{--bg:#0e0d12;--panel:#1a1820;--line:#2a2730;--text:#f0eef5;--muted:#a09cae;--accent:#e8a4c5;--accent2:#a4c5e8;--warn:#e8c5a4;--ok:#a4e8b8}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--text);line-height:1.7;padding:0 0 80px}
.wrap{max-width:880px;margin:0 auto;padding:40px 24px}
.topbar{background:var(--panel);border-bottom:1px solid var(--line);padding:14px 24px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:10;backdrop-filter:blur(8px)}
.topbar a{color:var(--muted);text-decoration:none;font-size:13px}
.topbar a:hover{color:var(--accent)}
.topbar .home{font-weight:600;color:var(--accent)}
.content{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:40px 48px;margin-top:24px}
.content h1{font-size:30px;margin:0 0 8px;letter-spacing:-.5px;border-bottom:2px solid var(--accent);padding-bottom:12px}
.content h2{font-size:22px;margin:32px 0 12px;padding-bottom:8px;border-bottom:1px solid var(--line)}
.content h3{font-size:17px;margin:24px 0 8px;color:var(--accent)}
.content p{margin:12px 0;font-size:15px}
.content a{color:var(--accent2);text-decoration:none;border-bottom:1px solid rgba(164,197,232,.3)}
.content a:hover{border-bottom-color:var(--accent2)}
.content ul,.content ol{margin:12px 0;padding-left:24px}
.content li{margin:6px 0;font-size:15px}
.content code{background:rgba(255,255,255,.06);padding:2px 6px;border-radius:4px;font-size:13px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;color:var(--warn)}
.content pre{background:#0a0910;border:1px solid var(--line);border-radius:8px;padding:16px;overflow-x:auto;margin:16px 0}
.content pre code{background:transparent;padding:0;color:var(--text)}
.content blockquote{border-left:3px solid var(--accent);background:rgba(232,164,197,.05);padding:12px 16px;margin:16px 0;border-radius:0 6px 6px 0}
.content blockquote p{color:var(--muted);font-style:italic;margin:0}
.content table{width:100%;border-collapse:collapse;margin:16px 0;font-size:14px}
.content th{background:#0a0910;text-align:left;padding:10px 12px;border-bottom:2px solid var(--line);color:var(--accent);font-weight:600}
.content td{padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}
.content tr:hover td{background:rgba(232,164,197,.04)}
.content hr{border:0;border-top:1px solid var(--line);margin:24px 0}
.content strong{color:var(--text);font-weight:700}
.content em{color:var(--muted)}
.path{font-size:11px;color:var(--muted);font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;margin-top:4px}
.checkbox-item{padding:10px 14px;background:#0a0910;border:1px solid var(--line);border-radius:6px;margin:8px 0;display:flex;align-items:flex-start;gap:10px}
.checkbox-item .box{width:18px;height:18px;border:2px solid var(--accent);border-radius:4px;flex-shrink:0;margin-top:2px}
.checkbox-item .label{flex:1;font-size:15px}
.checkbox-item .label strong{color:var(--accent)}
.section-num{display:inline-block;background:var(--accent);color:#0e0d12;padding:2px 10px;border-radius:99px;font-size:12px;font-weight:700;margin-right:8px}
@media(max-width:600px){.content{padding:24px 20px}.wrap{padding:20px 16px}.content h1{font-size:24px}}
"""

def make_input_form_html(md_path: pathlib.Path, content_html: str) -> str:
    """Wrap question/option lines in pretty checkbox boxes so Sarah can use it as a fillable sheet."""
    lines = content_html.split('\n')
    out = []
    in_question = False
    for line in lines:
        if re.match(r'^\s*-\s*\(\s*\)\s*\*\*', line) or re.match(r'^\s*<li>\s*\(\s*\)\s*\*\*', line):
            out.append('<div class="checkbox-item"><div class="box"></div><div class="label">' + re.sub(r'^\s*<li>\s*|\s*</li>\s*$|^\s*-\s*', '', line) + '</div></div>')
            in_question = True
        elif line.strip().startswith('( ) **') or re.match(r'^\s*<li>\s*\(\s*\)\s*', line):
            out.append('<div class="checkbox-item"><div class="box"></div><div class="label">' + re.sub(r'^\s*<li>\s*|\s*</li>\s*$|^\s*-\s*', '', line) + '</div></div>')
        else:
            out.append(line)
    return '\n'.join(out)

def render(md_path: pathlib.Path) -> None:
    raw = md_path.read_text(encoding="utf-8")
    is_questionnaire = "validacion-cliente-sarah" in str(md_path) or "sarah-questionnaire-hub" in str(md_path)

    md = markdown.Markdown(extensions=["extra", "sane_lists", "tables", "fenced_code", "toc"])
    rendered = md.convert(raw)

    if is_questionnaire:
        rendered = make_input_form_html(md_path, rendered)

    rel = md_path.relative_to(ROOT)
    breadcrumb_parts = []
    for p in rel.parts[:-1]:
        breadcrumb_parts.append(f'<a href="/index">{p}</a> /')
    breadcrumb = ' / '.join(breadcrumb_parts) if breadcrumb_parts else ''

    title_match = re.search(r'^#\s+(.+)$', raw, re.MULTILINE)
    page_title = title_match.group(1).strip() if title_match else md_path.stem

    html_doc = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(page_title)} — Sarah's Lubricant Business</title>
<style>{PAGE_CSS}</style>
</head>
<body>
<div class="topbar">
<a href="/sarah-questionnaire-hub" class="home">✨ Sarah's Hub</a>
<div>
<a href="/sarah-questionnaire-hub" style="margin-right:14px">📋 Questionnaire</a>
<a href="/start-here" style="margin-right:14px">📚 Repo</a>
<a href="/index">Index</a>
</div>
</div>
<div class="wrap">
<div class="content">
<div class="path">{rel}</div>
{rendered}
</div>
</div>
</body>
</html>"""

    rel_no_ext = md_path.relative_to(ROOT).with_suffix("")
    out_path = OUT / rel_no_ext / "index.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html_doc, encoding="utf-8")
    print(f"  {md_path.relative_to(ROOT)} -> {out_path.relative_to(OUT)}")

def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    md_files = sorted(ROOT.rglob("*.md"))
    md_files = [f for f in md_files if "node_modules" not in f.parts and ".git" not in f.parts and "build" not in f.parts]
    print(f"Found {len(md_files)} markdown files\n")
    for f in md_files:
        render(f)

    print(f"\nBuilt {len(md_files)} HTML pages in {OUT}\n")

    rendered = {}
    for f in md_files:
        rel_no_ext = f.relative_to(ROOT).with_suffix("")
        rendered[str(rel_no_ext).replace("\\","/")] = OUT / rel_no_ext / "index.html"

    for slug, target in SLUGS.items():
        if target in rendered:
            slug_dir = OUT / slug
            slug_dir.mkdir(exist_ok=True)
            shutil.copy2(rendered[target], slug_dir / "index.html")
            print(f"  Short URL /{slug} -> {target}/")
        else:
            print(f"  WARNING: slug {slug} -> {target} not found in rendered files")

    for top in ["README", "start-here", "COMPLETE-INDEX", "AGENTS", "TODO", "sarah-questionnaire-hub"]:
        if top in rendered:
            src_html = rendered[top]
            slug_dir = OUT / top
            if not slug_dir.exists():
                slug_dir.mkdir()
                shutil.copy2(src_html, slug_dir / "index.html")
                print(f"  Short URL /{top} -> {top}/")
            else:
                print(f"  Short URL /{top} -> {top}/ (already exists)")

if __name__ == "__main__":
    main()
