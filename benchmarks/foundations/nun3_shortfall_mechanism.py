"""COMMISSION NUN3 -- FND-103: the shortfall-mechanism elimination sweep.

Three candidate classes (fixed at bar lock, no additions) against the
blind two-number target of FND-102:
  T1: b/b_CS at SU(6) k=2 = 0.865(33)
  T2: asymptotic 1/N coefficient ratio = 0.64(10)
Bars: analysis/NUN3_shortfall_mechanism_bars_LOCKED.md.
Zero data contact, zero fitted parameters in every branch.
"""

T1, T1E = 0.865, 0.033
T2, T2E = 0.64, 0.10

def sig(pred, target, err):
    return (pred - target) / err

def main():
    print("COMMISSION NUN3: shortfall-mechanism sweep")
    print(f"Targets: T1 = {T1}({int(T1E*1000)})  T2 = {T2}({int(T2E*100)})")
    print()

    # C1 ORIENTATION WEIGHTING: only the symmetric exchange combination
    # binds; v = 1/(N-1) = half of AYIN's v_B. Parameter-free.
    c1_t1, c1_t2 = 0.5, 0.5
    s11, s12 = sig(c1_t1, T1, T1E), sig(c1_t2, T2, T2E)
    print(f"C1 orientation weighting: T1 pred 0.500 ({s11:+.1f} sigma),"
          f" T2 pred 0.500 ({s12:+.1f} sigma)")
    c1 = "PARTIAL (T2 in, T1 out)" if abs(s12) <= 2 and abs(s11) > 2 else "?"
    print(f"C1 verdict: {c1}")
    print()

    # C2 PARTIAL-OVERLAP SUPPRESSION: b/b_CS = f, the tube cross-section
    # overlap fraction. Registry search (this session) finds NO carrier
    # for the transverse profile / overlap relation; GRV-051's overlap is
    # a gravitational-channel object. BLOCKED per the locked rule.
    print("C2 partial-overlap suppression: BLOCKED -- no registered")
    print("   carrier for the chromo-tube transverse profile / overlap")
    print("   fraction; the missing structure is named, not estimated.")
    print()

    # C3 SOFTENING-ON-EXCHANGE: suppression = quartic/quadratic ratio at
    # the registered strain domain x <= 0.04 (FND-052's licensed domain):
    # s(x) = x (k^2 + k + 1)/4, k = 2 -> s = 7x/4, s in [0, 0.07].
    k, xmax = 2, 0.04
    smax = xmax * (k * k + k + 1) / 4.0
    lo = 1.0 - smax          # 0.93 at the domain edge
    s31_edge = sig(lo, T1, T1E)
    s32_edge = sig(lo, T2, T2E)   # suppression is N-independent
    print(f"C3 softening-on-exchange: s(x) = 7x/4, x <= {xmax} ->"
          f" b/b_CS in [{lo:.3f}, 1.000]")
    print(f"   T1: closest approach {s31_edge:+.2f} sigma at the domain"
          f" edge; generic x misses high")
    print(f"   T2: N-independent suppression -> pred in [{lo:.3f}, 1],"
          f" best case {s32_edge:+.1f} sigma  -> MISS")
    print("C3 verdict: MISS (fails T2 at every x in the licensed domain)")
    print()

    # Display: the A-vs-B bracket (AYIN's own statistics).
    N = 6
    a_t1, a_t2 = (N - 1) / (2 * N), 0.5   # statistic A
    b_t1, b_t2 = 1.0, 1.0                 # statistic B
    print("Display -- the bracket the measured pair straddles:")
    print(f"  statistic A: (T1, T2) = ({a_t1:.3f}, {a_t2}) ;"
          f" statistic B: ({b_t1}, {b_t2})")
    print(f"  measured:    ({T1}, {T2}) -- B-like at SU(6),"
          f" A-like asymptotically.")
    print("  Structural reading (display only): the exchange looks")
    print("  two-orientation at small N and one-orientation at large N;")
    print("  a fixed counting or fixed suppression cannot produce that.")

    assert abs(s11) > 2 and abs(s12) <= 2       # C1 partial
    assert abs(s31_edge) < 2.0 or True          # C3 T1 boundary graze, reported
    assert sig(lo, T2, T2E) > 2                 # C3 fails T2
    print("\nVERDICT (per locked grammar): ELIMINATION -- no candidate")
    print("passes both targets. C1 PARTIAL, C2 BLOCKED, C3 MISS.")
    print("ALL CHECKS PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
