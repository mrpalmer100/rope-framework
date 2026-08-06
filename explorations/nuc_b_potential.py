import numpy as np
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "explorations"))
sys.path.insert(0, str(ROOT / "benchmarks" / "em"))
import nuc_a_asymmetry as na
from atomic_mass_predictor import structure_constants, calibrate_aV

X0 = 1.36
AA_KIN = 16.6

def eta_healing_tail(x0=X0):
    return x0 / (x0 + 1.0)

def a_pot(eta, epsbar, accounting="quartet"):
    if accounting == "quartet":
        return 6.0 * epsbar * (1.0 - eta) / (3.0 + eta)
    return 6.0 * epsbar * (1.0 - eta) / (1.0 + eta)

def main():
    aSaV, aC = structure_constants()
    aV = calibrate_aV(aSaV, aC)
    epsbar = aV / 6.0
    eta = eta_healing_tail()
    print(f"epsbar = a_V/6 = {epsbar:.4f} MeV; eta = x0/(x0+1) = {eta:.4f}\n")
    cands = {
        "B1 primary (linear, quartet)": a_pot(eta, epsbar, "quartet"),
        "B2 (quadratic overlap)":       a_pot(eta**2, epsbar, "quartet"),
        "B3 (label-blind)":             a_pot(eta, epsbar, "blind"),
    }
    print("== CANDIDATES vs band; combined vs 19-23 ==")
    for lab, ap in cands.items():
        tot = AA_KIN + ap
        print(f"  {lab}: a_pot={ap:.2f} ({'IN' if 1.5<=ap<=4 else 'OUT'}); combined={tot:.2f} ({'IN 19-23' if 19<=tot<=23 else 'out'})")
    print()
    nucs = na.load_table()
    print("  reference kinetic alone (16.6):")
    na.s1_table_closure(AA_KIN, "kin", nucs, aV, aSaV, aC)
    na.s2_valley(AA_KIN, "kin", aV, aSaV, aC)
    print()
    for lab, ap in cands.items():
        tot = AA_KIN + ap
        na.s1_table_closure(tot, lab, nucs, aV, aSaV, aC)
        na.s2_valley(tot, lab, aV, aSaV, aC)
        print()

main()
