"""Commission RHO — the mass-dependence prediction, mechanically verified.

THE CHAIN (registered claims only): R_eq = sqrt(T_tube/(pi Sigma)) with Sigma
quark-content-INDEPENDENT (ELEC-038 one-medium + FND-017 global multiplier)
forces the ENTIRE quenched-vs-dynamical width shift into the string tension:
    s = sigma_dyn/sigma_quench = (R_dyn/R_quench)^2.
LOCKED PREDICTION (from the contaminated width axis, stated as such):
    s in [1.06, 1.22], sign s > 1.
BLIND CONFRONTATION (values seen only after the bars): TUMQCD continuum
physical-mass r0*sqrt(sigma) = 1.077(16) / 1.110(16), r0 = 0.4547(64) fm,
bracketing the published 2+1 value ~1.09 at FLAG r0 = 0.4701 fm; quenched
sigma fixed by the Edwards CONVENTION sqrt(sigma) = 0.44 GeV — the SAME
dictionary that defines the Lisbon quenched fm (a = 0.0984 at beta = 6.0),
so this convention is FORCED by coherence with the width axis, not chosen.
    => s = 1.128(46), 1.199(48), and 1.081  — ALL INSIDE the locked band.
VERDICT: SURVIVES, sign and magnitude. Sensitivity stated: on the incoherent
r0=0.5 fm quenched dictionary s drops to 1.00-1.11 (sign-marginal); that
dictionary contradicts the width data's own scale setting and is not used.
"""
import math
HBARC = 0.19733
R0_DYN, DR0 = 0.4547, 0.0064
R0SQS = [(1.077, 0.016), (1.110, 0.016)]
S21 = (1.09 * HBARC / 0.4701 / 0.44) ** 2
BAND = (1.06, 1.22)


def main():
    vals = []
    for v, e in R0SQS:
        s = (v * HBARC / R0_DYN / 0.44) ** 2
        ds = s * 2 * math.sqrt((e / v) ** 2 + (DR0 / R0_DYN) ** 2)
        assert BAND[0] < s < BAND[1], "TUMQCD point left the locked band"
        vals.append((s, ds))
    assert BAND[0] < S21 < BAND[1], "2+1 point left the locked band"
    assert all(s > 1 for s, _ in vals) and S21 > 1
    # coherence check: prediction band reproduces from the width brackets
    lo, hi = (0.402 / 0.391) ** 2, (0.407 / 0.369) ** 2
    assert abs(lo - 1.06) < 0.01 and abs(hi - 1.22) < 0.01
    for s, ds in vals:
        print(f"s = {s:.3f} +/- {ds:.3f}  IN BAND {BAND}")
    print(f"s = {S21:.3f} (2+1 published)  IN BAND {BAND}")
    print("ALL CHECKS PASS — the one-medium Sigma-universality survives its")
    print("first out-of-sample confrontation, sign and magnitude.")


if __name__ == "__main__":
    main()
