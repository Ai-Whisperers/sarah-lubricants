#!/usr/bin/env python3
"""Competitor monitor — weekly price scrape for 5 PY competitor sites.

Detects price changes >10% and flags them. Logs to CSV.

Run weekly:  python3 tools/competitor_monitor.py

LIMITATIONS:
- Competitor sites use JavaScript-rendered prices (Shopify/WooCommerce).
  Plain HTTP scraping extracts very few prices.
- For full coverage, run in a browser context (Selenium/Playwright).
  This script works best on server-rendered pages.
- DNS resolution required (some VPS environments block external domains).
"""
import urllib.request
import re
import json
import csv
import os
import sys
from datetime import datetime
from html.parser import HTMLParser

OUT_DIR = os.path.expanduser('~/sarah-competitor-tracking')
os.makedirs(OUT_DIR, exist_ok=True)
CSV_FILE = os.path.join(OUT_DIR, 'competitor_prices.csv')

# 5 competitors
COMPETITORS = [
    {
        'name': 'SexShop.com.py',
        'url': 'https://sexhop.com.py',
        'currency': 'Gs',
    },
    {
        'name': 'Rivia',
        'url': 'https://www.rivia.com.py',
        'currency': 'Gs',
    },
    {
        'name': 'Íntimos Placeres',
        'url': 'https://www.intimosplaceres.com.py',
        'currency': 'Gs',
    },
    {
        'name': 'As Bajo La Manga',
        'url': 'https://www.asbajolamanga.com.py',
        'currency': 'Gs',
    },
    {
        'name': 'Mencanta',
        'url': 'https://mencanta.com.py',
        'currency': 'Gs',
    },
]

PRICE_CHANGE_THRESHOLD_PCT = 10.0


class ProductExtractor(HTMLParser):
    """Extract product names + prices from HTML."""
    def __init__(self):
        super().__init__()
        self.products = []
        self.current_text = ''
        self.in_price = False
        self.in_product = False
        self.last_price = ''

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        # Common product patterns
        if tag in ('h2', 'h3') and 'product' in attrs_dict.get('class', '').lower():
            self.in_product = True
            self.current_text = ''
        elif tag in ('span', 'div') and 'price' in attrs_dict.get('class', '').lower():
            self.in_price = True
            self.current_text = ''

    def handle_endtag(self, tag):
        if self.in_product and tag in ('h2', 'h3'):
            product_name = self.current_text.strip()
            self.in_product = False
            if product_name:
                self.last_product = product_name
        if self.in_price and tag in ('span', 'div'):
            price_text = self.current_text.strip()
            self.in_price = False
            # Extract numeric
            m = re.search(r'[\d.,]+', price_text.replace('.', '').replace(',', '.'))
            if m and self.last_product:
                try:
                    price = float(m.group())
                    if 1000 < price < 1_000_000:  # reasonable price
                        self.products.append({
                            'name': self.last_product[:100],
                            'price': price,
                        })
                        self.last_product = ''
                except ValueError:
                    pass

    def handle_data(self, data):
        self.current_text += data


def fetch(url, timeout=15):
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'Accept-Language': 'es-PY,es;q=0.9',
            'Accept': 'text/html',
        })
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return None, str(e)


def extract_products_from_html(html):
    """Try multiple extraction strategies."""
    products = []
    # Strategy 1: HTMLParser
    try:
        parser = ProductExtractor()
        parser.feed(html)
        products = parser.products
    except Exception:
        pass

    # Strategy 2: regex for common price patterns
    if not products:
        for m in re.finditer(r'>([A-Z][a-zA-Záéíóúñ\s]{5,50}?)<.*?Gs\.?\s*([\d.,]+)', html):
            try:
                price = float(m.group(2).replace('.', '').replace(',', '.'))
                if 5000 < price < 1_000_000:
                    products.append({'name': m.group(1).strip()[:100], 'price': price})
            except (ValueError, IndexError):
                pass
    return products


def main():
    today = datetime.now().strftime('%Y-%m-%d')
    all_rows = []

    print(f"\n=== COMPETITOR PRICE MONITOR — {today} ===\n")

    # Load existing CSV (if any) for diff
    existing = {}
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = (row['date'], row['competitor'], row['product'])
                existing[key] = row

    new_rows = []

    for comp in COMPETITORS:
        print(f"  Scraping {comp['name']}...")
        status, body = fetch(comp['url'])
        if status != 200:
            print(f"    ❌ {status} — {str(body)[:80]}")
            continue
        products = extract_products_from_html(body)
        print(f"    Found {len(products)} products")

        for prod in products[:30]:  # cap at 30 per competitor
            row = {
                'date': today,
                'competitor': comp['name'],
                'product': prod['name'],
                'price_gs': int(prod['price']),
                'currency': comp['currency'],
            }
            new_rows.append(row)
            all_rows.append(row)

    # Diff against last week
    print(f"\n=== PRICE CHANGES vs. LAST RUN ===")
    changes = []
    last_week = today
    # Find last date in existing
    if existing:
        dates = sorted(set(k[0] for k in existing.keys()))
        if len(dates) > 1:
            last_week = dates[-1]

    for new_row in new_rows:
        key = (new_row['date'], new_row['competitor'], new_row['product'])
        prev_key = (last_week, new_row['competitor'], new_row['product'])
        if prev_key in existing:
            try:
                old_price = int(existing[prev_key]['price_gs'])
                new_price = new_row['price_gs']
                if old_price > 0:
                    pct = ((new_price - old_price) / old_price) * 100
                    if abs(pct) >= PRICE_CHANGE_THRESHOLD_PCT:
                        changes.append({
                            'date': today,
                            'competitor': new_row['competitor'],
                            'product': new_row['product'],
                            'old': old_price,
                            'new': new_price,
                            'pct': pct,
                        })
            except (KeyError, ValueError):
                pass

    if changes:
        for c in changes:
            emoji = "🔴" if c['pct'] > 0 else "🟢"
            print(f"  {emoji} {c['competitor']:<25} {c['product'][:40]:<40} {c['old']:>7} → {c['new']:>7} ({c['pct']:+.1f}%)")
    else:
        print(f"  ✅ No price changes >{PRICE_CHANGE_THRESHOLD_PCT}% vs. last run")

    # Log
    new_file = not os.path.exists(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['date', 'competitor', 'product', 'price_gs', 'currency'])
        if new_file:
            writer.writeheader()
        for row in new_rows:
            writer.writerow(row)
    print(f"\nLogged {len(new_rows)} price points to: {CSV_FILE}")


if __name__ == '__main__':
    main()