#!/usr/bin/env python3
"""Pricing calculator for Enki Store.

Run: python3 tools/pricing_calculator.py

Outputs landed cost, margin scenarios, and break-even for the launch trio.
Reads from canonical pricing reference (currently estimates until Q5 PDF).
"""
import sys
import json
from datetime import datetime

# === INPUT PARAMETERS (edit these) ===
PARAMS = {
    # Cost basis (use AR retail ÷ 2 as estimate until Q5 PDF lands)
    "bitchie_ar_mayorista": 6100,    # AR$ per unit (Distribuidor Mayorista est)
    "xxx_ar_mayorista": 8270,
    "wet_anal_ar_mayorista": 5515,

    # FX rate
    "ars_to_pyg": 4,                  # 4 Gs per AR$
    "usd_to_pyg": 7500,              # ~blue rate June 2026

    # Per-shipment fixed costs (Gs)
    "freight_kg_per_usd": 6,          # USD per kg
    "freight_kg_total": 10,           # kg total
    "iva_import_pct": 10,            # % on product cost
    "despachante_per_shipment": 1_200_000,  # Gs
    "dinavisa_per_sku": 500_000,     # Gs per SKU (one-time)
    "dinavisa_skus_count": 3,         # number of SKUs
    "packaging_per_unit": 5_000,      # Gs per unit
    "marketing_per_month": 500_000,   # Gs per month (post-launch)
    "contabilidad_per_month": 400_000, # Gs per month
    "buffer_pct": 5,                  # % buffer for unexpected costs

    # Retail prices (Gs)
    "bitchie_retail": 130_000,
    "xxx_retail": 145_000,
    "wet_anal_retail": 125_000,

    # Volume scenarios
    "scenarios": [
        {"name": "First order (30u each)", "units_per_sku": 30},
        {"name": "Second order (50u each)", "units_per_sku": 50},
        {"name": "Third order (100u each)", "units_per_sku": 100},
    ],
}


def calculate_scenario(units_per_sku, params):
    """Calculate landed cost + per-unit cost + margins for a given order size."""
    # Product cost (per SKU in Gs)
    products = {
        "Bitchie 20ml": params["bitchie_ar_mayorista"] * params["ars_to_pyg"],
        "XXX For Her 15ml": params["xxx_ar_mayorista"] * params["ars_to_pyg"],
        "Wet Anal 75ml": params["wet_anal_ar_mayorista"] * params["ars_to_pyg"],
    }
    product_cost_per_sku = {sku: cost for sku, cost in products.items()}
    total_product_cost = sum(cost * units_per_sku for cost in product_cost_per_sku.values())

    # Freight (proportional to kg; scales with units)
    freight_total = params["freight_kg_per_usd"] * params["freight_kg_total"] * params["usd_to_pyg"]
    # Scale freight with order size
    freight_total = freight_total * (units_per_sku / 30.0)  # 30u is baseline

    # IVA import (10% on product)
    iva_import = total_product_cost * params["iva_import_pct"] / 100

    # Despachante (fixed per shipment)
    despachante = params["despachante_per_shipment"]

    # DINAVISA (fixed per shipment, all SKUs in one)
    dinavisa = params["dinavisa_per_sku"] * params["dinavisa_skus_count"]

    # Packaging
    packaging = params["packaging_per_unit"] * units_per_sku * 3  # 3 SKUs

    # Buffer
    buffer = (total_product_cost + freight_total + iva_import + despachante + dinavisa + packaging) * params["buffer_pct"] / 100

    # Total landed
    total_landed = total_product_cost + freight_total + iva_import + despachante + dinavisa + packaging + buffer

    # Per-unit landed (weighted average across 3 SKUs)
    total_units = units_per_sku * 3
    per_unit_landed = total_landed / total_units

    # Per-SKU landed
    per_sku_landed = {}
    for sku, cost in product_cost_per_sku.items():
        sku_product = cost * units_per_sku
        sku_share = total_landed * (sku_product / total_product_cost)
        per_sku_landed[sku] = sku_share / units_per_sku

    # Margins
    retail = {
        "Bitchie 20ml": params["bitchie_retail"],
        "XXX For Her 15ml": params["xxx_retail"],
        "Wet Anal 75ml": params["wet_anal_retail"],
    }
    margins = {}
    for sku, landed in per_sku_landed.items():
        r = retail[sku]
        margin = (r - landed) / landed * 100
        margins[sku] = {"retail": r, "landed": landed, "margin_pct": margin}

    return {
        "scenario": f"{units_per_sku} units each (90u / 150u / 300u total)",
        "product_cost": total_product_cost,
        "freight": freight_total,
        "iva_import": iva_import,
        "despachante": despachante,
        "dinavisa": dinavisa,
        "packaging": packaging,
        "buffer": buffer,
        "total_landed": total_landed,
        "per_unit_landed": per_unit_landed,
        "per_sku_landed": per_sku_landed,
        "margins": margins,
        "total_units": total_units,
    }


def print_scenario(scenario):
    """Print a scenario's results."""
    print(f"\n{'='*70}")
    print(f"SCENARIO: {scenario['scenario']}")
    print(f"{'='*70}")
    print(f"\nTotal units: {scenario['total_units']}")
    print(f"\n--- Cost breakdown ---")
    print(f"  Product cost:  Gs {scenario['product_cost']:>15,.0f}")
    print(f"  Freight:       Gs {scenario['freight']:>15,.0f}")
    print(f"  IVA import:    Gs {scenario['iva_import']:>15,.0f}")
    print(f"  Despachante:   Gs {scenario['despachante']:>15,.0f}")
    print(f"  DINAVISA:      Gs {scenario['dinavisa']:>15,.0f}")
    print(f"  Packaging:     Gs {scenario['packaging']:>15,.0f}")
    print(f"  Buffer:        Gs {scenario['buffer']:>15,.0f}")
    print(f"  ---")
    print(f"  TOTAL LANDED:  Gs {scenario['total_landed']:>15,.0f}")
    print(f"\n--- Per-unit landed ---")
    for sku, landed in scenario["per_sku_landed"].items():
        print(f"  {sku:<25} Gs {landed:>10,.0f}/unit")
    print(f"\n--- Margins ---")
    for sku, m in scenario["margins"].items():
        margin_str = f"{m['margin_pct']:>6.1f}%"
        print(f"  {sku:<25} Landed Gs {m['landed']:>9,.0f} | Retail Gs {m['retail']:>9,.0f} | Margin {margin_str}")


def calculate_break_even(fixed_costs, contribution_margin):
    """Calculate break-even units per month."""
    if contribution_margin <= 0:
        return float("inf")
    return fixed_costs / contribution_margin


def print_break_even(params):
    """Print break-even analysis."""
    print(f"\n{'='*70}")
    print("BREAK-EVEN ANALYSIS")
    print(f"{'='*70}")

    # Fixed costs (monthly)
    fixed_costs = params["marketing_per_month"] + params["contabilidad_per_month"]

    # Avg contribution margin per unit
    # Take 30u scenario's avg margin per unit
    scenario_30u = calculate_scenario(30, params)
    avg_retail = sum(m["retail"] for m in scenario_30u["margins"].values()) / 3
    avg_landed = sum(m["landed"] for m in scenario_30u["margins"].values()) / 3
    contribution_margin = avg_retail - avg_landed

    be_units = calculate_break_even(fixed_costs, contribution_margin)
    be_revenue = be_units * avg_retail

    print(f"\nFixed costs (monthly): Gs {fixed_costs:,.0f}")
    print(f"  Marketing:    Gs {params['marketing_per_month']:,.0f}")
    print(f"  Contabilidad: Gs {params['contabilidad_per_month']:,.0f}")
    print(f"\nAvg contribution margin per unit: Gs {contribution_margin:,.0f}")
    print(f"  (avg retail {avg_retail:,.0f} - avg landed {avg_landed:,.0f})")
    print(f"\nBreak-even units/month: {be_units:.0f}")
    print(f"Break-even revenue/month: Gs {be_revenue:,.0f}")


def main():
    print("=" * 70)
    print("ENKI STORE — PRICING CALCULATOR")
    print(f"Generated: {datetime.now().isoformat()}")
    print("=" * 70)
    print(f"\nFX assumptions:")
    print(f"  AR$ → PYG: {PARAMS['ars_to_pyg']}:1")
    print(f"  USD → PYG: {PARAMS['usd_to_pyg']}:1")

    print(f"\n⚠️  Cost basis is ESTIMATE (AR retail ÷ 2)")
    print(f"   Replace with Sexitive AR Distribuidor Mayorista actual prices")
    print(f"   when Q5 PDF is received.")

    # Run scenarios
    for s in PARAMS["scenarios"]:
        scenario = calculate_scenario(s["units_per_sku"], PARAMS)
        print_scenario(scenario)

    # Break-even
    print_break_even(PARAMS)

    # JSON output for programmatic use
    if "--json" in sys.argv:
        all_scenarios = [calculate_scenario(s["units_per_sku"], PARAMS) for s in PARAMS["scenarios"]]
        print(f"\n{'='*70}")
        print("JSON OUTPUT (machine-readable)")
        print(f"{'='*70}")
        print(json.dumps({
            "params": PARAMS,
            "scenarios": all_scenarios,
            "generated": datetime.now().isoformat(),
        }, indent=2))


if __name__ == "__main__":
    main()