#!/usr/bin/env python3
"""Inventory reorder calculator for Enki Store.

Given current stock + sales velocity, recommend when to reorder + how much.

Run:  python3 tools/inventory_reorder_calc.py
"""
import os
from datetime import datetime

# User inputs
TIER_TRIGGER = 30  # Reorder when any SKU drops below this
TIER_OPTIMAL = 90  # Order enough to bring stock to this level

# Launch trio reference data (per canonical-pricing-reference-v1.md)
SKUS = {
    'SEFB':   {'name': 'Bitchie Spray 20ml',          'landed_cost': 66_834, 'retail': 130_000, 'weight_g': 60},
    'XXX01':  {'name': 'XXX For Her óleo 15ml',      'landed_cost': 90_610, 'retail': 145_000, 'weight_g': 50},
    'WET02':  {'name': 'Wet Gel Lubricante Anal 75ml','landed_cost': 60_425, 'retail': 125_000, 'weight_g': 90},
}

# Variable inputs (user edits)
CURRENT_STOCK = {
    'SEFB': 45,
    'XXX01': 28,
    'WET02': 15,
}

# Velocity = units sold per day (user edits)
DAILY_VELOCITY = {
    'SEFB': 0.5,    # ~15/month
    'XXX01': 0.3,   # ~9/month
    'WET02': 0.2,   # ~6/month
}

# Order constraints
MIN_ORDER_PER_SKU = 30  # Sexitive AR MOQ
LEAD_TIME_DAYS = 14     # Time from order to arrive


def days_until_stockout(stock, velocity):
    if velocity <= 0:
        return float('inf')
    return stock / velocity


def recommend_reorder(stock, velocity, sku_code, sku_name):
    """Recommend reorder if needed."""
    days_left = days_until_stockout(stock, velocity)
    reorder_eta = days_left - LEAD_TIME_DAYS
    results = {
        'sku': sku_code,
        'name': sku_name,
        'current_stock': stock,
        'daily_velocity': velocity,
        'days_until_stockout': round(days_left, 1),
        'days_until_reorder': round(reorder_eta, 1),
    }
    if stock <= TIER_TRIGGER:
        # Reorder NOW
        to_order = TIER_OPTIMAL - stock
        results['action'] = '🔴 REORDER NOW'
        results['recommend_order_qty'] = max(MIN_ORDER_PER_SKU, to_order)
        results['order_cost_gs'] = SKUS[sku_code]['landed_cost'] * results['recommend_order_qty']
        results['expected_revenue'] = SKUS[sku_code]['retail'] * results['recommend_order_qty']
    elif reorder_eta <= 7:
        # Reorder this week
        to_order = TIER_OPTIMAL - stock
        results['action'] = '🟡 REORDER THIS WEEK'
        results['recommend_order_qty'] = max(MIN_ORDER_PER_SKU, to_order)
        results['order_cost_gs'] = SKUS[sku_code]['landed_cost'] * results['recommend_order_qty']
        results['expected_revenue'] = SKUS[sku_code]['retail'] * results['recommend_order_qty']
    elif reorder_eta <= 14:
        results['action'] = '⏳ Plan reorder soon'
        results['recommend_order_qty'] = 0
        results['order_cost_gs'] = 0
        results['expected_revenue'] = 0
    else:
        results['action'] = '✅ Stock OK'
        results['recommend_order_qty'] = 0
        results['order_cost_gs'] = 0
        results['expected_revenue'] = 0
    return results


def main():
    print(f"\n=== INVENTORY REORDER CALCULATOR — {datetime.now().strftime('%Y-%m-%d')} ===\n")
    print(f"  Tier trigger: stock <= {TIER_TRIGGER} units")
    print(f"  Tier optimal: order to bring to {TIER_OPTIMAL} units")
    print(f"  Lead time: {LEAD_TIME_DAYS} days from order to arrive\n")

    total_order_cost = 0
    total_expected_revenue = 0
    items_to_reorder = []

    for sku_code, sku in SKUS.items():
        stock = CURRENT_STOCK.get(sku_code, 0)
        velocity = DAILY_VELOCITY.get(sku_code, 0)
        r = recommend_reorder(stock, velocity, sku_code, sku['name'])
        print(f"  {r['action']:<22} {sku_code:<8} {r['name']:<35}")
        print(f"      Stock: {r['current_stock']:>3} units  |  Velocity: {r['daily_velocity']:>4.1f}/day  |  Stockout in: {r['days_until_stockout']:>5.1f} days")
        if r['recommend_order_qty'] > 0:
            print(f"      → Order {r['recommend_order_qty']:>3} units = Gs {r['order_cost_gs']:>10,.0f}  (retail: Gs {r['expected_revenue']:>10,.0f})")
            total_order_cost += r['order_cost_gs']
            total_expected_revenue += r['expected_revenue']
            items_to_reorder.append(r)
        print()

    if items_to_reorder:
        print(f"=== TOTALS ===")
        print(f"  Total to order: Gs {total_order_cost:,.0f} (landed cost)")
        print(f"  Expected revenue: Gs {total_expected_revenue:,.0f}")
        print(f"  Implied margin: Gs {total_expected_revenue - total_order_cost:,.0f}  ({(total_expected_revenue - total_order_cost) / total_order_cost * 100:.0f}%)")
        print(f"\n=== NEXT STEPS ===")
        print(f"  1. Email Sexitive AR gerente with order list")
        print(f"  2. Confirm payment (transferencia)")
        print(f"  3. Wait {LEAD_TIME_DAYS} days for delivery")
        print(f"  4. Update CURRENT_STOCK values in this script when new stock arrives")
    else:
        print(f"✅ All stock levels OK. No reorder needed.")


if __name__ == '__main__':
    main()