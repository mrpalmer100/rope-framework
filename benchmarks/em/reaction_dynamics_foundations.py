"""CHEM-DYN-001 (Modeled; parts Derived): reaction dynamics from mode-capacity
mechanics. Bars pre-committed in a prior session; all four faced.
(a) BARRIER EXISTENCE derived in BOTH sharing limits: coherent (eigenvalue,
    E = -2 sqrt(t1^2+t2^2) + cores): barrier = (1/4)e^(-2 d0/xi) De = 0.0142 De,
    entirely the THIRD-BODY CONTACT (the frustration term bottoms at exactly
    -1 De at x* = ln sqrt2 -- analytic); incoherent (capacity partition,
    E = -2 max(t1,t2) + cores): 0.50 De. Frustration (strict sub-additivity)
    + third-body contact: consequences, not assumptions.
(b) BARRIER << BOND, parameter-free BRACKET: 0.0142 < measured H+H2 ratio
    0.0885 < 0.50. Log-midpoint 0.084 (within 5% of measured) recorded as
    OBSERVATION ONLY; deriving the coherence fraction is next-order.
(c) HAMMOND derived in-model: heteronuclear surface (De2 = 0.6 De1) puts the
    saddle with the forming strong bond long (x = 2.0) and the breaking weak
    bond barely stretched (x = 0.01): early TS for the exothermic direction.
(d) CATALYSIS = CAPACITY DONATION (Modeled toy): relaxing n1+n2 <= 1+kappa
    lowers the symmetric-cut frustration barrier monotonically
    (0.875 -> 0.500 De for kappa 0 -> 1), catalyst returned unchanged.
Corpus anchors only: De = 4.747 eV, d0 = 0.741 A, xi from the H2 vibration.
"""
import numpy as np

De, d0 = 4.747, 0.741
xi = np.sqrt(2*De/35.57)
XS = np.linspace(-0.4, 2.5, 581)


def E_coh(x1, x2):
    return (-2*np.sqrt(np.exp(-2*x1)+np.exp(-2*x2)) + np.exp(-2*x1) + np.exp(-2*x2)
            + np.exp(-2*(x1+x2+d0/xi)))


def E_inc(x1, x2):
    return (-2*max(np.exp(-x1), np.exp(-x2)) + np.exp(-2*x1) + np.exp(-2*x2)
            + np.exp(-2*(x1+x2+d0/xi)))


def minimax(Efn):
    barrier = -np.inf
    for u in np.linspace(-2.0, 2.0, 161):
        vals = [Efn(x, x-u) for x in XS if (x-u) > -0.4]
        barrier = max(barrier, min(vals))
    return barrier - (-1.0)


def hammond_saddle(rr=0.6):
    def E(x1, x2):
        return (-2*np.sqrt(np.exp(-2*x1)+(rr*np.exp(-x2))**2) + np.exp(-2*x1)
                + rr*np.exp(-2*x2) + np.exp(-2*(x1+x2+d0/xi)))
    best = None
    for u in np.linspace(-2.0, 2.0, 321):
        m = min((E(x, x-u), x, x-u) for x in XS if (x-u) > -0.4)
        if best is None or m[0] > best[0]:
            best = m
    return best[1], best[2]


def catalysis_barrier(kappa):
    return min(-(1+kappa)*np.exp(-x) + 2*np.exp(-2*x) for x in XS) + 1.0


def test():
    b_coh_num, b_inc = minimax(E_coh), minimax(E_inc)
    b_coh = 0.25*np.exp(-2*d0/xi)
    assert b_coh_num > 0 and b_inc > 0, "bar (a): barrier > 0 in both limits"
    assert abs(b_coh_num - b_coh) < 0.005, "coherent numeric matches analytic third-body form"
    meas = 0.42/De
    assert b_coh < meas < b_inc, "bar (b): the parameter-free bracket contains the measured ratio"
    assert b_coh < 0.05, "coherent limit: barrier << bond"
    xf, xb = hammond_saddle()
    assert xf > xb + 0.5, "bar (c): early TS for the exothermic direction (Hammond emerges)"
    bars = [catalysis_barrier(k) for k in (0.0, 0.25, 0.5, 1.0)]
    assert all(np.diff(bars) < 0) and bars[-1] < 0.6*bars[0], "bar (d): monotone capacity-donation relief"
    print(f"barriers: coherent {b_coh:.4f} De (0.067 eV) / incoherent {b_inc:.3f} De; measured 0.0885")
    print(f"bracket holds; log-midpoint {np.sqrt(b_coh*0.5):.3f} (observation only)")
    print(f"Hammond: forming x {xf:.2f} vs breaking x {xb:.2f} (early TS); catalysis {bars[0]:.3f}->{bars[-1]:.3f} De")
    print("PASS: barriers, Hammond, and catalysis all emerge from capacity mechanics; nothing assumed.")


if __name__ == "__main__":
    test()
