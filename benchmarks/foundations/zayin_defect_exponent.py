"""Commission ZAYIN -- the defect-exponent computation.
Bars locked BEFORE any cell was evaluated
(analysis/ZAYIN_defect_exponent_bars_LOCKED.md): the 3x3 candidate table
is closed, the bar brackets are fixed, a miss registers Failed-and-kept
with the inverted demand, and no O(1) rescue is permitted.
"""
import math

L_RING = math.pi          # ropelength in cells
E_CORE = 5.448            # derived core constant (units of K)
A_EFF = 0.18              # derived cutoff (units of a)
BAR_BARE = (4.41, 4.68)   # required exponent, bare convention
BAR_CUT = (6.13, 6.40)    # required exponent, derived-cutoff convention
G_TARGET = (82.6, 108.0)

# Budgets in units of J (= K, the lattice bond coupling = locking energy)
BUDGETS = {"B1 m_e c^2 = 2 pi J": 2 * math.pi,
           "B2 J (per-link locking)": 1.0,
           "B3 E_core = 5.448 K": E_CORE}
# Log coefficients in units of K
COEFS = {"K1 pi K (single vortex)": math.pi,
         "K2 2 pi K (pair)": 2 * math.pi,
         "K3 pi^2 K (3D line x L)": math.pi ** 2}


def main():
    print("THE TABLE (exponent x = B/coef; bar bare [4.41, 4.68], "
          "cutoff [6.13, 6.40]):")
    hits, cells = [], []
    for bn, B in BUDGETS.items():
        for cn, coef in COEFS.items():
            x = B / coef
            g_bare = math.exp(x)
            g_cut = A_EFF * math.exp(x)
            in_bar = (BAR_BARE[0] <= x <= BAR_BARE[1]
                      or BAR_CUT[0] <= x <= BAR_CUT[1])
            cells.append(x)
            if in_bar:
                hits.append((bn, cn, x))
            print(f"  {bn} / {cn}: x = {x:.3f} -> g = {g_bare:.2f} (bare) / "
                  f"{g_cut:.2f} (cutoff)  [{'HIT' if in_bar else 'miss'}]")
    print(f"  cells evaluated: {len(cells)}; hits: {len(hits)}")
    assert len(cells) == 9

    if not hits:
        xmax = max(cells)
        print("VERDICT: MISS -- the energy-budget defect-log class is")
        print(f"  EXCLUDED. Largest exponent delivered: {xmax:.2f}")
        print(f"  (B = m_e c^2 with the single-vortex pi K), a factor")
        print(f"  {BAR_BARE[0]/xmax:.2f}-{BAR_CUT[1]/xmax:.2f} short of the bar;")
        print(f"  in g: best {math.exp(xmax):.1f} (bare) vs target "
              f"{G_TARGET[0]}-{G_TARGET[1]} -- short by "
              f"{G_TARGET[0]/math.exp(xmax):.0f}-"
              f"{G_TARGET[1]/(A_EFF*math.exp(xmax)):.0f}x. Registered")
        print("  Failed-and-kept per the locked bar; no rescue attempted.")

        # The inverted demand (MATTER046 grammar)
        for name, coef in COEFS.items():
            b_bare = (BAR_BARE[0] * coef, BAR_BARE[1] * coef)
            b_cut = (BAR_CUT[0] * coef, BAR_CUT[1] * coef)
            print(f"  DEMAND under {name}: B = {b_bare[0]:.1f}-{b_bare[1]:.1f} K"
                  f" (bare) = {b_bare[0]/(2*math.pi):.2f}-"
                  f"{b_bare[1]/(2*math.pi):.2f} m_e c^2;"
                  f"  {b_cut[0]:.1f}-{b_cut[1]:.1f} K (cutoff) = "
                  f"{b_cut[0]/(2*math.pi):.2f}-{b_cut[1]/(2*math.pi):.2f} m_e c^2")
        print("  THE DEMAND IN ONE LINE: the winding's log budget must be")
        print("  2.2-3.2 electron rest energies (single-vortex reading) --")
        print("  no registered energy is that; any future rescue must derive")
        print("  one blind.")

    # Look-elsewhere, stated either way: 9 cells spanning x in [0.10, 2.0]
    # against bar segments of total width 0.27 + 0.27 = 0.54 located at
    # 4.4-6.4 -- the bar sits ENTIRELY ABOVE the candidate range, so the
    # chance rate for this table was ZERO and the exclusion is maximally
    # clean (no cell could have hit by luck; none did by physics).
    lo, hi = min(cells), max(cells)
    assert hi < BAR_BARE[0]
    print(f"LOOK-ELSEWHERE: table range x in [{lo:.2f}, {hi:.2f}] lies")
    print("  entirely BELOW both bar segments -- chance hit rate exactly 0;")
    print("  the class does not merely miss, it CANNOT reach: registered")
    print("  budgets top out at m_e c^2 = 2 pi K while the bar starts at")
    print("  4.41 pi K. The exclusion is structural, not numerical.")
    print("ALL BARS ADJUDICATED (verdict: Failed-and-kept)")


if __name__ == "__main__":
    main()
