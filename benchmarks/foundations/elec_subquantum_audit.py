"""ELEC-056 -- THE SUB-QUANTUM PROGRAMME AUDITED AFTER THE ANCHOR'S LOSS:
A DEPENDENCY AND DIMENSIONALITY AUDIT, MACHINE-CHECKED.

Bars locked in analysis/ELEC056_subquantum_audit_bars_LOCKED.md BEFORE this ran.
"""
import os
import re
import numpy as np
import yaml

HBAR = 1.054571817e-34
C = 2.99792458e8
FM = 1e-15
BOHR = 5.29177e-11
R_NUC = 5 * FM
L_OLD = np.sqrt(HBAR * C / 1.70e3)
L_NEW = np.sqrt(2 * np.pi * HBAR * C / 1.70e3)
TARGETS = [f"QGATE-{n:03d}" for n in range(11, 18)]
ANCHORS = {"HBAR-005", "HBAR-006"}
ROOT = os.path.join(os.path.dirname(__file__), "..", "..")


def load():
    d = yaml.safe_load(open(os.path.join(ROOT, "claims.yaml")))
    c = d["claims"] if isinstance(d, dict) else d
    return {x["id"]: x for x in c}


def closure(claims, cid, seen=None):
    seen = seen or set()
    for dep in claims.get(cid, {}).get("depends_on", []) or []:
        if dep not in seen:
            seen.add(dep)
            closure(claims, dep, seen)
    return seen


def main():
    claims = load()

    # B1 dependency audit
    print("B1 DEPENDENCY AUDIT (transitive closure vs the anchors):")
    hits = {}
    for cid in TARGETS:
        cl = closure(claims, cid)
        hit = cl & ANCHORS
        hits[cid] = hit
        print(f"   {cid}: {len(cl):3d} ancestors, anchor dependence: "
              f"{sorted(hit) if hit else 'NONE'}")
    assert not any(hits.values()), "an anchor dependence exists; verdict must change"
    print("   RESULT: NO claim in the pilot-wave programme depends on HBAR-005/006,")
    print("   directly or transitively. The anchor was PROSE ADJACENCY, not lineage.")

    # B2 dimensionality audit
    print("\nB2 DIMENSIONALITY AUDIT (dimensionful constants in the executable code):")
    pat = re.compile(r"(1\.05457|6\.626e|2\.998e|2\.99792|9\.109e|1\.602e|"
                     r"=\s*[\d.]+\s*\*\s*FM|\bfm\b\s*=|BOHR|1\.6605e)")
    clean = True
    for cid in TARGETS:
        p = os.path.join(ROOT, claims[cid]["benchmark"])
        code = open(p).read()
        body = "\n".join(l for l in code.splitlines() if not l.strip().startswith("#"))
        found = sorted(set(m.group(0) for m in pat.finditer(body)))
        clean &= not found
        print(f"   {os.path.basename(p):38s} {'scale-free' if not found else found}")
    assert clean
    print("   RESULT: the guidance flow, the singlet Bell run, and every relaxation")
    print("   and transport benchmark are SCALE-FREE -- box units, hbar_eff = 1, mode")
    print("   indices. No length enters the mechanism anywhere.")

    # B3 what was lost
    print("\nB3 WHAT THE ANCHOR WAS ACTUALLY CARRYING (HBAR-006's two conclusions):")
    for tag, L in (("old anchor 4.31 fm", L_OLD), ("corrected >= 10.81 fm", L_NEW)):
        print(f"   {tag:24s} atom cells = {(BOHR/L)**3:.2e} | "
              f"nucleus (5 fm) cells = {(R_NUC/L)**3:.3f}")
    print("   (a) BORN EXACTNESS AT ATOMIC SCALES SURVIVES: an atom still spans ~1e11")
    print("       cells; the conclusion needed only 'very many', and it still holds.")
    print("   (b) THE NUCLEAR NON-BORN PREDICTION DOES NOT: it moves from 1.56 cells")
    print("       (a testable boundary) to 0.10 (deep sub-quantum), which ELEC-055")
    print("       showed is excluded by nuclear data with no parameter freedom left.")
    print("   The anchor was carrying ONE of the two, and it was the falsifiable one.")

    # B4 verdict
    print("\nB4 VERDICT: SURVIVES UNANCHORED.")
    print("   The programme loses no foundation -- it never had one from this quarter;")
    print("   the flow's uniqueness, the CHSH violation, the relaxation family and the")
    print("   transport predictors are all dimensionless results that stand exactly as")
    print("   registered. What it loses is its ONLY BRIDGE TO OBSERVATION: HBAR-006")
    print("   was the single claim converting the sub-quantum layer into a length, and")
    print("   through it a nuclear prediction. Without it the layer is a working")
    print("   mechanism with no scale, hence NO CURRENT EMPIRICAL CONTENT of its own.")
    print("   Registered plainly: this does not weaken the mathematics and does not")
    print("   rescue the physics -- the corpus's distinctive-prediction deficit")
    print("   (NUCQ-001's own conclusion) is now the pilot-wave branch's deficit too.")

    # B5 hygiene
    print("\nB5 HYGIENE: hbar_constancy_and_scale.py's 4.31 fm assert is ARITHMETICALLY")
    print("   CORRECT (sqrt(hbar c/T) is that length); only its identification as the")
    print("   admissible coherent segment was wrong. Supersession banner added; the")
    print("   assert and all locked bars left untouched per the no-silent-edit rule.")
    print("PASS: the audit is structural and machine-checked, not editorial.")


if __name__ == "__main__":
    main()
