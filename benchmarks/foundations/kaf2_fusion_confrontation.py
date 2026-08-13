"""COMMISSION KAF2 -- the fusion confrontation.

Bars: analysis/KAF2_fusion_confrontation_bars_LOCKED.md (locked first).
Q1 identity audit; Q2 three-reading confrontation; Q3 discriminator
verdict. KAF's registered law imported unmodified.
"""

import math

C_RATIO = 9.0 / 4.0          # C_A/C_F
RHO_R = 1.0                  # PHI, within errors
DELTA_MEAS = 0.125           # PHI: sigma_adj = 1.125 x 2 sigma_f
X_REG = 0.04                 # FND-040 dominance clause
L1 = 3.0


def e_soft(x):
    return x / 2 - x * x / 8


def e_stiff(x):
    return x / 2 + x * x / 8


def E(f, k, x, e):
    return f * e(k * k * x) + k * (1 - f) * e(x)


def q1_identity():
    kappa_rel = C_RATIO / RHO_R ** 2
    delta_from_kappa = kappa_rel / 2.0 - 1.0
    return kappa_rel, delta_from_kappa, abs(delta_from_kappa - DELTA_MEAS)


def q2_readings():
    out = {}
    # R-FREE: minimize over f (KAF's family, both signs)
    for name, e in (("soft", e_soft), ("stiff", e_stiff)):
        n = 100001
        fmin = min(range(n), key=lambda i: E(i / (n - 1), 2, X_REG, e)) / (n - 1)
        delta = E(fmin, 2, X_REG, e) / (2 * e(X_REG)) - 1.0
        out[f"R-FREE ({name})"] = delta
    # R-COHERENT: f = 1 forced
    for name, e in (("soft", e_soft), ("stiff", e_stiff)):
        out[f"R-COHERENT ({name})"] = e(4 * X_REG) / (2 * e(X_REG)) - 1.0
    # R-RECRUIT: charge-level, strain-free, n_b-free
    out["R-RECRUIT"] = C_RATIO / 2.0 - 1.0
    return out


def main():
    print("Q1 -- identity audit:")
    kr, dk, resid = q1_identity()
    ident = resid < 1e-12
    print(f"  kappa_rel = {kr:.4f}; kappa_rel/2 - 1 = {dk:.4f} vs measured "
          f"delta {DELTA_MEAS} (residual {resid:.1e}) -> "
          f"{'IDENTITY CONFIRMED: one measurement, two coordinates' if ident else 'identity fails'}")

    print("\nQ2 -- three-reading confrontation (measured delta = +0.125):")
    readings = q2_readings()
    survivors = []
    for name, d in readings.items():
        if d <= 0:
            verdict = "EXCLUDED (wrong sign / null vs +12.5 percent)"
        else:
            fac = max(d / DELTA_MEAS, DELTA_MEAS / d)
            verdict = ("HITS (exact)" if fac < 1.001 else
                       f"{'within' if fac <= L1 else 'EXCLUDED beyond'} L1 (x{fac:.2f})")
        if "HITS" in verdict or "within" in verdict:
            survivors.append(name)
        print(f"  {name}: delta = {d:+.4f} -> {verdict}")

    print("\nQ3 -- discriminator verdict:")
    nb_free = [s for s in survivors if s == "R-RECRUIT"]
    print(f"  survivors: {survivors}")
    print("  n_b appears in NO surviving reading (R-RECRUIT is charge-level;")
    print("  the strain readings that carry configuration structure are excluded).")
    if ident and nb_free and survivors == nb_free:
        print("\nVERDICT (pre-committed grammar): POINT-CONSUMED")
        print("  - the point is one degree of freedom (Q1) and it is consumed by")
        print("    the registered n_b-free recruitment law (RETRODICTION, per G2);")
        print("  - FND-077's named decider route is adjudicated EMPTY;")
        print("  - R-COHERENT is EXCLUDED as the adjoint mechanism (registered);")
        print("  - R-FREE's null is excluded by the same point.")
    else:
        print("\nVERDICT: DISCRIMINATOR-LIVE or ALL-MISS (inspect above)")


if __name__ == "__main__":
    main()
