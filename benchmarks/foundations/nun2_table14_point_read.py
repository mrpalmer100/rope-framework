"""COMMISSION NUN2 -- FND-102: the FND-092 kill clause fires at point level.

Apply FND-092's pre-registered SU(6) k=2 decision grammar, verbatim,
to the Table 14 continuum point of Athenodorou-Teper 2021
(arXiv:2106.00364): sigma_2/sigma_f = 1.654(13) (NG and l->infinity
columns identical; SU(6) is in the safe-volume group, no correction).
Bars: analysis/NUN2_table14_point_read_bars_LOCKED.md, locked before
the table was read.
"""

# Datum (Table 14, transcribed verbatim).
X, E = 1.654, 0.013
TABLE14 = {  # N: (measured ratio, err) -- l->infinity column
    4: (1.381, 0.014), 5: (1.551, 0.011), 6: (1.654, 0.013),
    8: (1.794, 0.028), 10: (1.796, 0.029), 12: (1.857, 0.029),
}

# FND-092 pre-registered grammar (2026-08-11, blind to this data).
BAND_LO, BAND_TOP = 1.5904, 1.5981   # softened-Casimir band
CASIMIR, SINE = 1.6000, 3 ** 0.5     # exact laws at SU(6) k=2

def main():
    kill_thr = BAND_TOP + 3 * E
    kill = X >= kill_thr
    select = (BAND_LO - E <= X <= BAND_TOP + E) and (X <= SINE - 3 * E)
    print("COMMISSION NUN2: FND-092 point-level adjudication, SU(6) k=2")
    print(f"P1: x = {X}({int(E*1000)}) vs kill threshold {kill_thr:.4f}"
          f" -> KILL {'FIRES' if kill else 'does not fire'};"
          f" SELECT {'fires' if select else 'does not fire'}")
    print(f"    {(X-BAND_TOP)/E:.1f} sigma above softened band top")
    print(f"P2: {(X-CASIMIR)/E:.2f} sigma above exact Casimir {CASIMIR}")
    print(f"P3: {(SINE-X)/E:.2f} sigma below sine {SINE:.4f}")
    print()
    print("Display: binding fraction b = (2 - ratio)/2 vs Casimir b:")
    for N, (m, err) in TABLE14.items():
        cas = 2 * (N - 2) / (N - 1)
        b, bc = (2 - m) / 2, (2 - cas) / 2
        print(f"  SU({N:2d}): b = {b:.4f} vs {bc:.4f}"
              f"  ratio {b/bc:.3f}  ({(m-cas)/err:+.1f} sigma from CS)")

    assert kill and not select
    assert abs((X - BAND_TOP) / E - 4.30) < 0.02
    assert abs((X - CASIMIR) / E - 4.15) < 0.02
    assert abs((SINE - X) / E - 6.00) < 0.02
    print("\nVERDICT (per locked grammar): KILL -- Failed-and-kept.")
    print("ALL CHECKS PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
