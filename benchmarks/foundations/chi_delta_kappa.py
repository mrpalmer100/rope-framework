"""Commission CHI — delta(kappa) derived, confronted, and KILLED (Failed-and-kept).

READING B (the chartered model): adjoint tube = strands of k = 2 fundamental
tubes plus pairwise contact binding, sigma_D/sigma_f = k + c k(k-1),
c = 0.125 calibrated on PHI's adjoint point. LOCKED DISCRIMINATOR: all k = 2
representations degenerate -> sextet ratio predicted 2.25.
BLIND DATA (Bali hep-lat/0006022, continuum-extrapolated; Deldar
independent): Casimir scaling holds across eight representations with
violations excluded above 5% up to 1 fm (continuum central ~1%; Deldar
5-15% with coarser systematics) -> sextet ratio = C_6/C_3 = 2.50.
Reading B misses by 10% against a <= 5% bound at its cleanest point, and
degrades further up the ladder (decuplet: B 3.75 vs 4.50, -17%; 27-plet:
B 5.5 vs 6.0, -8%; 15-sym: B 3.75 vs 7.0, -46%). KILLED.

READING A survives (retained, NOT confirmed -- it fits by construction):
exact strand additivity with recruitment n_D proportional to C_D. The
mainstream literature independently carries this picture as the Lund "rope
model" -- overlapping strings form a rope with tension proportional to the
Casimir -- a naming the corpus registers with a straight face.

Consequences: PHI's (2.25, +0.125) point is RE-READ as string k-counting vs
Casimir counting, not strand super-additivity; the E_x channel returns to
unmeasured-in-tubes; UPSILON's kappa_rel = 2.25 compression stands (a
measured density ratio, explanation-independent); kappa_fund and Sigma_vac
remain open. NEW BOUND: across seven non-fundamental representations the
additivity-plus-recruitment PACKAGE closes to <= 5% (continuum ~1%) -- the
first multi-point constraint on within-tube tension bookkeeping, degenerate
between delta_strand and recruitment deviations, stated as the package.
"""
CASIMIR = {"6": 10/4, "8": 9/4, "10": 9/2, "15a": 4.0, "27": 6.0, "15s": 7.0}
K = {"6": 2, "8": 2, "10": 3, "15a": 3, "27": 4, "15s": 3}
C_CAL = 0.125
CS_BOUND = 0.05


def reading_b(k):
    return k + C_CAL * k * (k - 1)


def main():
    assert abs(reading_b(2) - CASIMIR["8"]) < 1e-12          # calibration point
    dev6 = abs(reading_b(K["6"]) / CASIMIR["6"] - 1)
    assert dev6 > CS_BOUND, "sextet no longer kills Reading B"
    kills = sum(abs(reading_b(K[r]) / CASIMIR[r] - 1) > CS_BOUND
                for r in CASIMIR if r != "8")
    assert kills >= 4
    print(f"sextet: B predicts {reading_b(2)} vs Casimir {CASIMIR['6']} "
          f"({dev6:+.0%} vs <=5% bound) -> READING B KILLED")
    print(f"{kills}/5 non-calibration representations exceed the bound")
    print("Reading A retained (not confirmed); additivity+recruitment package")
    print("bounded at <=5% (continuum ~1%) across seven representations.")
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
