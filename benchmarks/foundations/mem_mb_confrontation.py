"""COMMISSION MEM -- the m_b(n) confrontation.

Bars: analysis/MEM_mb_confrontation_bars_LOCKED.md (locked first).
Registered models m_b(n) in {1, sqrt(n), n^(2/3), n}; identities
I-CONST (TAV windows) and I-TUBE (QGATE-004 census); survival chain
per FND-029/EM-RECON-030; at-threshold pin per QOPH's displayed
convergence (conditional tier).
"""

import math

RAW = 29.0                       # FND-029 raw bundle ratio e_b/(T0 a)
BAND = (0.395, 0.460)            # EM-RECON-030 survival band
L1 = 3.0                         # displayed band factor; headline L1 = 1

MODELS = {
    "single-pair": lambda n: 1.0,
    "surface-line": lambda n: math.sqrt(n),
    "contact-patch": lambda n: n ** (2.0 / 3.0),
    "full-section": lambda n: float(n),
}
INV = {   # m -> n per model
    "surface-line": lambda m: m * m,
    "contact-patch": lambda m: m ** 1.5,
    "full-section": lambda m: m,
}
WINDOWS = {
    "I-CONST (k50, f_c)": (5, 9),
    "I-CONST (k50 hex / k250 f_c)": (14, 27),
    "I-CONST (k250, hex)": (40, 81),
    "I-TUBE census": (47, 198),
}
PIN = (RAW / BAND[1], RAW / BAND[0])     # m_b at threshold, L1 = 1


def verdict(m):
    r = RAW / m
    if r > BAND[1]:
        return f"ratio {r:7.2f}  SURVIVES (above band)"
    if r >= BAND[0]:
        return f"ratio {r:7.2f}  AT THRESHOLD (inside band)"
    return f"ratio {r:7.2f}  FAILS (below band)"


def main():
    print(f"survival band {BAND}; at-threshold pin m_b in "
          f"[{PIN[0]:.1f}, {PIN[1]:.1f}] at L1 = 1 "
          f"(L1 factor-3 band: [{PIN[0]/L1:.1f}, {PIN[1]*L1:.1f}])\n")

    print("Q1 -- survival matrix (per-pair ratio at window edges, L1 = 1):")
    for wname, (lo, hi) in WINDOWS.items():
        print(f"  {wname}: n = {lo}..{hi}")
        for mname, f in MODELS.items():
            mlo, mhi = f(lo), f(hi)
            print(f"    {mname:13s} m_b = {mlo:6.1f}..{mhi:6.1f}   "
                  f"low: {verdict(mlo)}   high: {verdict(mhi)}")
        print()

    print("Q2 -- the at-threshold pin, inverted per model (n demanded):")
    hits = []
    for mname, g in INV.items():
        nlo, nhi = g(PIN[0]), g(PIN[1])
        print(f"  {mname:13s} demands n in [{nlo:7.1f}, {nhi:7.1f}]")
        for wname, (lo, hi) in WINDOWS.items():
            ilo, ihi = max(nlo, lo), min(nhi, hi)
            if ilo <= ihi:
                hits.append((mname, wname, ilo, ihi))
                print(f"      INTERSECTS {wname}: n in [{ilo:.1f}, {ihi:.1f}]")
    print()

    print("Q3 -- discrimination statement (conditional, nothing adopted):")
    if hits:
        for mname, wname, ilo, ihi in hits:
            print(f"  IF at-threshold AND {mname} contact AND identity {wname}:")
            print(f"     the count is pinned to n in [{ilo:.0f}, {ihi:.0f}]")
        print("\nVERDICT (pre-committed grammar): PINNED-CONDITIONAL")
    else:
        print("  no registered window intersects the pin")
        print("\nVERDICT: SURVIVES-UNPINNED or EXCLUDED (inspect Q1)")


if __name__ == "__main__":
    main()
