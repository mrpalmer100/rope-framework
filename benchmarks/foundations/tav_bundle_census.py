"""COMMISSION TAV -- the bundle census.

Bars: analysis/TAV_bundle_census_bars_LOCKED.md (locked first).
Question: is the tube constituent a bundle of n_b vacuum strands?
Censuses: B1 geometry (integer windows), B2 solidity, B3 the count
confrontation over the four locked cells, with the declared natural
cell (axial share, hex packing) fixed at lock.
"""

import math

W_C = (0.0395e-15, 0.0565e-15)          # ELEC-050 lattice band, m
A_LIVE = {"kappa50": 1.63e-17, "kappa250": 0.953e-17}   # FND-040 pairs
WOA = 0.6272                             # FND-068 / EM-RECON-030
F_C = 0.309                              # FND-MATTER-038
PHI = {"phi_fc": F_C, "phi_hex": math.pi / (2 * math.sqrt(3))}
R_BAND = (0.35e-15, 0.5e-15)             # lattice tube radius, m
L1 = 3.0
GAP_SOLID = 1.5                          # FND-STRAND-004 crossover


def b1_windows():
    out = {}
    for fl, a in A_LIVE.items():
        wv = WOA * a
        for pn, phi in PHI.items():
            lo = phi * (W_C[0] / wv) ** 2
            hi = phi * (W_C[1] / wv) ** 2
            ints = (math.ceil(lo), math.floor(hi))
            out[(fl, pn)] = (lo, hi, ints)
    return out


def b2_solidity():
    return {pn: (1 / math.sqrt(phi) - 1) for pn, phi in PHI.items()}


def b3_ratio(count, phi):
    """ratio = n_struct_variant / (n_t * n_b), R and floor cancel:
    n_t*n_b = f_c*phi*(2R/w_vac)^2 = 4 f_c phi (R/w_vac)^2
    all-family: 3 pi (R/a)^2 -> ratio = (3pi/4)(w_vac/a)^2/(f_c phi)
    axial:      pi (R/a)^2  -> ratio = (pi/4)(w_vac/a)^2/(f_c phi)"""
    fam = 3.0 if count == "all" else 1.0
    return (fam * math.pi / 4.0) * WOA ** 2 / (F_C * phi)


def g1_cancellation_check():
    """FND-068 convention: (pi/4)(w_vac/a)^2 = f_c exactly?"""
    lhs = (math.pi / 4.0) * WOA ** 2
    return lhs, F_C, abs(lhs / F_C - 1.0)


def main():
    print("B1 geometry -- integer n_b windows:")
    b1 = b1_windows()
    b1_pass = {}
    for (fl, pn), (lo, hi, ints) in b1.items():
        ok = ints[1] >= max(2, ints[0])
        b1_pass.setdefault(pn, []).append(ok)
        print(f"  {fl} {pn}: n_b in [{lo:.2f}, {hi:.2f}] -> integers "
              f"{ints[0]}..{ints[1]} {'PASS' if ok else 'EMPTY'}")
    b1_ok = any(all(v) for v in b1_pass.values())

    print("\nB2 solidity -- internal gap in units of sigma:")
    b2 = b2_solidity()
    for pn, g in b2.items():
        print(f"  {pn}: gap = {g:.3f} sigma vs crossover {GAP_SOLID} -> "
              f"{'SOLID' if g <= GAP_SOLID else 'NOT SOLID'}")
    b2_ok = all(g <= GAP_SOLID for g in b2.values())

    print("\nG1 cancellation check:")
    lhs, fc, rel = g1_cancellation_check()
    conf = rel < 1e-3
    print(f"  (pi/4)(w_vac/a)^2 = {lhs:.5f} vs f_c = {fc:.5f} "
          f"(rel {rel:.1e}) -> cancellation {'CONFIRMED' if conf else 'NOT CONFIRMED'}")
    if conf:
        print("  => B3 ratio reduces to (families)/phi identically; "
              "FND-067 demotion applies as pre-committed.")

    print("\nB3 count confrontation (ratio n_struct_variant / n_hier, "
          "R- and floor-independent):")
    natural = None
    cells = {}
    for count in ("all", "axial"):
        for pn, phi in PHI.items():
            r = b3_ratio(count, phi)
            cells[(count, pn)] = r
            tag = " <= DECLARED NATURAL CELL" if (count, pn) == ("axial", "phi_hex") else ""
            print(f"  ({count}-family, {pn}): ratio = {r:.3f} "
                  f"{'CONSISTENT (within L1)' if 1/L1 <= r <= L1 else 'BEYOND L1'}{tag}")
    natural = cells[("axial", "phi_hex")]
    b3_ok = 1 / L1 <= natural <= L1

    print()
    if b1_ok and b2_ok and b3_ok:
        v = "BUNDLE-CONSISTENT" + (" (with the G1 demotion)" if conf else "")
    elif (not b1_ok) and (not b2_ok) and all(not (1/L1 <= r <= L1) for r in cells.values()):
        v = "BUNDLE-EXCLUDED"
    else:
        v = "BUNDLE-UNDERDETERMINED"
    print(f"VERDICT (pre-committed grammar): {v}")


if __name__ == "__main__":
    main()
