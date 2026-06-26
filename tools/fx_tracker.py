#!/usr/bin/env python3
"""FX rate tracker for Sarah's Enki Store.

Scrapes free PY + AR sources, logs to CSV, alerts on threshold breach.

Run weekly:  python3 tools/fx_tracker.py
Run daily:   python3 tools/fx_tracker.py --quick   (just print rates, no log)
"""
import urllib.request
import urllib.parse
import json
import csv
import sys
import re
from datetime import datetime
import os

OUT_DIR = os.path.expanduser('~/sarah-fx-tracking')
os.makedirs(OUT_DIR, exist_ok=True)
CSV_FILE = os.path.join(OUT_DIR, 'fx_log.csv')

# Sarah's baseline (June 26, 2026 verbal)
BASELINE_ARS_PYG = 4.0
BASELINE_USD_PYG = 7500

# Re-pricing trigger
REPRICE_THRESHOLD_PCT = 10.0


def fetch(url, timeout=12, headers=None):
    """Fetch URL with timeout, return (status, body)."""
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/json,*/*',
        'Accept-Language': 'es-PY,es;q=0.9',
    }
    if headers:
        default_headers.update(headers)
    try:
        req = urllib.request.Request(url, headers=default_headers)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return None, str(e)


def fetch_json(url, timeout=10):
    """Fetch JSON API, return dict or {error: str}."""
    status, body = fetch(url, timeout=timeout, headers={'Accept': 'application/json'})
    if status != 200:
        return {'error': f'HTTP {status}: {body[:200]}'}
    try:
        return json.loads(body)
    except Exception as e:
        return {'error': f'JSON parse: {e}'}


def get_bcra_blue():
    """Argentina USD/ARS blue rate from bluelytics."""
    url = 'https://api.bluelytics.com.ar/v2/latest'
    data = fetch_json(url)
    if 'error' in data:
        return None
    try:
        return float(data['blue']['value_sell'])
    except (KeyError, TypeError, ValueError):
        return None


def get_dolarhoy_blue():
    """AR USD/ARS blue from dolarhoy."""
    url = 'https://dolarhoy.com/api/dolar'
    data = fetch_json(url)
    if 'error' in data:
        return None
    try:
        return float(data['blue']['venta'])
    except (KeyError, TypeError, ValueError):
        return None


def get_bcp_referencial_usd():
    """PY USD/PYG from BCP API."""
    url = 'https://www.bcp.gov.py/webdpc/webservice/v1/exchange_rates'
    data = fetch_json(url)
    if 'error' in data or not isinstance(data, list):
        return None
    for entry in data:
        try:
            if 'referencial' in str(entry).lower() or 'dolar' in str(entry).lower():
                # BCP API structure varies; try common field names
                for k in ['venta', 'compra', 'cotizacion', 'value']:
                    if k in entry:
                        return float(entry[k])
        except (TypeError, ValueError):
            continue
    return None


def get_cambioschaco_html():
    """PY exchange rates from Cambios Chaco website (HTML, parsed)."""
    url = 'https://www.cambioschaco.com.py'
    status, body = fetch(url, timeout=15)
    if status != 200:
        return None
    # Find Gs/USD and Gs/AR$ in HTML
    # Pattern: number followed by currency or "Guaraníes"
    usd_pyg = None
    ars_pyg = None
    # Try common formats
    for m in re.finditer(r'(\d{1,3}(?:\.\d{3})*(?:,\d+)?)\s*(?:Gs\.?|Gs|Guaran(?:í|ié))?[\s/]?(?:x?\s*USD|\$)', body, re.IGNORECASE):
        val = m.group(1).replace('.', '').replace(',', '.')
        try:
            n = float(val)
            if 5000 < n < 15000:
                usd_pyg = n
                break
        except ValueError:
            pass
    for m in re.finditer(r'(\d{1,3}(?:\.\d{3})*)\s*(?:Gs\.?|Gs|Guaran(?:í|ié))?[\s/]?(?:x?\s*AR\$|AR\$|ARS)', body, re.IGNORECASE):
        val = m.group(1).replace('.', '').replace(',', '.')
        try:
            n = float(val)
            if 1 < n < 20:
                ars_pyg = n
                break
        except ValueError:
            pass
    return {'usd_pyg': usd_pyg, 'ars_pyg': ars_pyg}


def main():
    quick_mode = '--quick' in sys.argv

    results = {
        'timestamp': datetime.now().isoformat(timespec='minutes'),
        'baseline_ars_pyg': BASELINE_ARS_PYG,
        'baseline_usd_pyg': BASELINE_USD_PYG,
    }

    # AR USD/ARS
    ars_usd_blue = get_bcra_blue() or get_dolarhoy_blue()
    if ars_usd_blue:
        results['ars_usd_blue'] = ars_usd_blue

    # PY USD/PYG (try multiple sources)
    usd_pyg = get_cambioschaco_html().get('usd_pyg') if get_cambioschaco_html() else None
    if not usd_pyg:
        usd_pyg = get_bcp_referencial_usd()
    if usd_pyg:
        results['usd_pyg'] = usd_pyg

    # Compute Gs/AR$ implied
    if ars_usd_blue and usd_pyg:
        ars_pyg_implied = usd_pyg / ars_usd_blue
        results['ars_pyg_implied'] = round(ars_pyg_implied, 2)

    # Cross-check with cambioschaco ars_pyg
    chaco = get_cambioschaco_html()
    if chaco and chaco.get('ars_pyg'):
        results['ars_pyg_chaco'] = chaco['ars_pyg']

    # Use the most reliable Gs/AR$ (prefer cambioschaco direct, then implied)
    ars_pyg_final = results.get('ars_pyg_chaco') or results.get('ars_pyg_implied') or BASELINE_ARS_PYG
    results['ars_pyg_used'] = ars_pyg_final

    # Alerts
    alerts = []
    if ars_pyg_final:
        delta_pct = ((ars_pyg_final - BASELINE_ARS_PYG) / BASELINE_ARS_PYG) * 100
        if abs(delta_pct) > REPRICE_THRESHOLD_PCT:
            direction = "AR$ weakened (cost up)" if delta_pct > 0 else "AR$ strengthened (cost down)"
            alerts.append(
                f"🔴 Gs/AR$ moved {delta_pct:+.1f}% from baseline {BASELINE_ARS_PYG}. "
                f"New rate: {ars_pyg_final}. {direction}. RE-PRICING NEEDED."
            )
    if usd_pyg and (usd_pyg / BASELINE_USD_PYG - 1) * 100 > REPRICE_THRESHOLD_PCT:
        alerts.append(
            f"🟡 Gs/USD moved {(usd_pyg / BASELINE_USD_PYG - 1) * 100:+.1f}%. "
            f"Freight/courier costs up."
        )

    results['alerts'] = ' | '.join(alerts) if alerts else 'None'

    # Print
    print(f"\n=== FX SNAPSHOT — {results['timestamp']} ===")
    print(f"  Baseline Gs/AR$: {BASELINE_ARS_PYG}  |  Baseline Gs/USD: {BASELINE_USD_PYG}")
    for k, v in results.items():
        if k not in ('timestamp', 'baseline_ars_pyg', 'baseline_usd_pyg'):
            print(f"  {k}: {v}")
    if alerts:
        print(f"\n⚠️  ALERTS:")
        for a in alerts:
            print(f"  {a}")
    else:
        print(f"\n✅ No re-pricing needed (within {REPRICE_THRESHOLD_PCT}% of baseline)")

    # Log
    if not quick_mode:
        new_file = not os.path.exists(CSV_FILE)
        with open(CSV_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            if new_file:
                writer.writerow([
                    'timestamp', 'ars_usd_blue', 'usd_pyg', 'ars_pyg_implied',
                    'ars_pyg_chaco', 'ars_pyg_used', 'alerts'
                ])
            writer.writerow([
                results['timestamp'],
                results.get('ars_usd_blue', ''),
                results.get('usd_pyg', ''),
                results.get('ars_pyg_implied', ''),
                results.get('ars_pyg_chaco', ''),
                results.get('ars_pyg_used', ''),
                results.get('alerts', ''),
            ])
        print(f"\nLogged to: {CSV_FILE}")


if __name__ == '__main__':
    main()