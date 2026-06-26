#!/usr/bin/env python3
"""Sexitive AR catalog re-scraper.

Pulls shop.sexitive.com sitemap + product pages, extracts SKUs + prices,
outputs a TSV ready to replace the existing catalog.

Run monthly (or after Sexitive announces new SKUs):
    python3 tools/sexitive_catalog_sync.py
"""
import urllib.request
import re
import json
import os
import csv
from datetime import datetime

OUT_DIR = os.path.expanduser('~/sarah-catalog-sync')
os.makedirs(OUT_DIR, exist_ok=True)
OUT_TSV = os.path.join(OUT_DIR, f'sexitive_ar_{datetime.now().strftime("%Y%m%d")}.tsv')


def fetch(url, timeout=15):
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'Accept-Language': 'es-PY,es;q=0.9',
            'Accept': 'text/html,application/xml',
        })
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return None, str(e)


def get_sitemap_urls(sitemap_url):
    """Extract product URLs from sitemap.xml."""
    status, body = fetch(sitemap_url)
    if status != 200:
        return []
    urls = re.findall(r'<loc>(https://shop\.sexitive\.com/productos/[^<]+)</loc>', body)
    return urls


def extract_product_info(url):
    """Extract SKU, title, price from a Sexitive product page."""
    status, body = fetch(url)
    if status != 200:
        return None
    # Try JSON-LD first
    jsonld_blocks = re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', body, re.DOTALL)
    for block in jsonld_blocks:
        try:
            d = json.loads(block)
            items = d if isinstance(d, list) else [d]
            for item in items:
                if isinstance(item, dict) and item.get('@type') == 'Product':
                    sku = item.get('sku', '') or ''
                    title = item.get('name', '') or ''
                    offers = item.get('offers', {})
                    if isinstance(offers, list):
                        offers = offers[0] if offers else {}
                    price = offers.get('price', '') if isinstance(offers, dict) else ''
                    return {
                        'sku': sku,
                        'title': title[:120],
                        'price_ars': price,
                        'url': url,
                    }
        except (json.JSONDecodeError, KeyError, IndexError, TypeError):
            continue
    # Fallback: try HTML
    title_m = re.search(r'<h1[^>]*>(.*?)</h1>', body, re.DOTALL)
    title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else ''
    price_m = re.search(r'"price"\s*:\s*"?([\d.,]+)"?', body)
    price = price_m.group(1) if price_m else ''
    sku_m = re.search(r'"sku"\s*:\s*"([^"]+)"', body)
    sku = sku_m.group(1) if sku_m else ''
    if title or price:
        return {
            'sku': sku,
            'title': title[:120],
            'price_ars': price,
            'url': url,
        }
    return None


def main():
    print(f"\n=== SEXITIVE AR CATALOG SYNC — {datetime.now().strftime('%Y-%m-%d')} ===\n")
    print("Fetching sitemap...")
    urls = get_sitemap_urls('https://shop.sexitive.com/sitemap.xml')
    if not urls:
        # Try product sitemap
        urls = get_sitemap_urls('https://shop.sexitive.com/product-sitemap.xml')
    if not urls:
        # Try direct listing page
        print("Sitemap not found, trying robots.txt for hints...")
        status, body = fetch('https://shop.sexitive.com/robots.txt')
        if status == 200:
            print(body[:500])
        return
    print(f"Found {len(urls)} product URLs in sitemap")
    print("Scraping product pages (this takes ~30 seconds)...")
    products = []
    for i, url in enumerate(urls, 1):
        if i % 20 == 0:
            print(f"  Progress: {i}/{len(urls)}")
        info = extract_product_info(url)
        if info:
            products.append(info)
    print(f"Successfully extracted {len(products)} products")
    # Write TSV
    with open(OUT_TSV, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['SKU', 'Title', 'Price_AR$', 'Price_Gs_est_4to1', 'URL', 'Scrape_date'])
        for p in products:
            try:
                price_ars = float(p['price_ars'].replace(',', '.')) if p['price_ars'] else 0
                price_gs = int(price_ars * 4) if price_ars else 0
                writer.writerow([
                    p['sku'],
                    p['title'],
                    price_ars,
                    price_gs,
                    p['url'],
                    datetime.now().strftime('%Y-%m-%d'),
                ])
            except ValueError:
                writer.writerow([
                    p['sku'],
                    p['title'],
                    p['price_ars'],
                    '',
                    p['url'],
                    datetime.now().strftime('%Y-%m-%d'),
                ])
    print(f"\nSaved to: {OUT_TSV}")
    print(f"Total products: {len(products)}")
    if products:
        with_prices = [p for p in products if p['price_ars']]
        print(f"With prices: {len(with_prices)}")
        if with_prices:
            print(f"Sample first 5:")
            for p in with_prices[:5]:
                print(f"  [{p['sku']:<10}] {p['title'][:50]:<50} AR$ {p['price_ars']}")


if __name__ == '__main__':
    main()