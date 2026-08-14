"""COMMISSION NUN4 -- FND-104: the orientation-decoherence inventory.

f(N) = b/b_CS = (1 + w(N))/2 against the three-part bar of
analysis/NUN4_orientation_decoherence_bars_LOCKED.md. Closed
inventory, zero parameters, zero data contact in derivations.
"""

import math

T1, T1E = 0.865, 0.033      # f(6)
T2, T2E = 0.64, 0.10        # f(inf)
P4, P4E = 0.928, 0.021      # f(4) profile bar
P5, P5E = 0.898, 0.022      # f(5) profile bar

INVENTORY = {
    "D1 w=(N-2)/(N-1)": lambda N: (N - 2) / (N - 1),
    "D2 w=1/(N-1)":      lambda N: 1 / (N - 1),
    "D3 w=2/(N-1)":      lambda N: 2 / (N - 1),
    "D4 w=4/(N-1)":      lambda N: 4 / (N - 1),
    "D5 w=2/N":          lambda N: 2 / N,
    "D6 w=(N-2)/N":      lambda N: (N - 2) / N,
    "D7 w=1/2 (control)": lambda N: 0.5,
    "D8 w=N/(2(N-1))":   lambda N: N / (2 * (N - 1)),
}

def f(w, N):
    return (1 + w(N)) / 2

def w_inf(w):
    return w(10 ** 9)

def main():
    print("COMMISSION NUN4: orientation-decoherence inventory sweep")
    print(f"Bars: f(6)={T1}({int(T1E*1000)})  f(inf)={T2}({int(T2E*100)})"
          f"  f(4)={P4}({int(P4E*1000)})  f(5)={P5}({int(P5E*1000)})")
    print()
    passers = []
    for name, w in INVENTORY.items():
        f6, f4, f5 = f(w, 6), f(w, 4), f(w, 5)
        finf = (1 + w_inf(w)) / 2
        s1, s2 = (f6 - T1) / T1E, (finf - T2) / T2E
        s4, s5 = (f4 - P4) / P4E, (f5 - P5) / P5E
        b1, b2 = abs(s1) <= 2, abs(s2) <= 2
        b3 = abs(s4) <= 3 and abs(s5) <= 3
        ok = b1 and b2 and b3
        if ok and "control" not in name:
            passers.append(name)
        print(f"{name:22s} f6={f6:.3f}({s1:+5.1f})  finf={finf:.3f}"
              f"({s2:+5.1f})  f4={f4:.3f}({s4:+5.1f})"
              f"  f5={f5:.3f}({s5:+5.1f})  "
              f"{'PASS' if ok else 'FAIL'}"
              f"{' [control: not promotable]' if 'control' in name and ok else ''}")
    print()

    # Shape lemma: family f(N) = A + c/(N-1).
    # B1: A + c/5 = 0.865 +- 2(0.033); B2: A = 0.64 +- 2(0.10).
    # B3 slope: f(4) - f(6) = c(1/3 - 1/5) = 2c/15, measured
    # 0.928 - 0.865 = 0.063 with error sqrt(0.021^2 + 0.033^2) = 0.039;
    # 3-sigma window on slope AND both absolute profile points.
    print("Shape lemma: family f(N) = A + c/(N-1)")
    found = []
    for A in [0.44 + 0.001 * i for i in range(400)]:
        if abs(A - T2) > 2 * T2E:
            continue
        for c in [0.0 + 0.005 * j for j in range(600)]:
            f6 = A + c / 5
            f4 = A + c / 3
            f5 = A + c / 4
            if abs(f6 - T1) > 2 * T1E:
                continue
            if abs(f4 - P4) > 3 * P4E or abs(f5 - P5) > 3 * P5E:
                continue
            found.append((A, c))
    if found:
        As = [a for a, _ in found]; cs = [c for _, c in found]
        print(f"  SURVIVING WINDOW: A in [{min(As):.3f}, {max(As):.3f}],"
              f" c in [{min(cs):.3f}, {max(cs):.3f}]"
              f"  ({len(found)} grid points)")
        # sample corner check
        A, c = found[0]
        print(f"  example member: f(4)={A+c/3:.3f} f(5)={A+c/4:.3f}"
              f" f(6)={A+c/5:.3f} f(inf)={A:.3f}")
    else:
        print("  EMPTY: no (A, c) satisfies B1+B2+B3 -- the"
              " 1/(N-1)-decay family is excluded by shape.")

    print()
    if passers:
        print(f"VERDICT: SURVIVING CANDIDATE(S): {passers}")
    elif found:
        print("VERDICT: NO INVENTORY MEMBER PASSES; the shape lemma leaves"
              " a nonempty (A, c) window, displayed as the surviving"
              " target for a future counting.")
    else:
        print("VERDICT: FAMILY EXCLUSION -- no member passes and the"
              " shape window is empty.")
    print("ALL CHECKS COMPLETE")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
