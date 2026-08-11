"""Commission UPSILON — the additivity stress-test: two corrections and a
located wound.

B1 THE TAUTOLOGY (second in-arc correction, against FND-033(c)): in the
lattice chain n = 3 pi (R_eq/a)^2 and T0 = T_tube/n BY CONSTRUCTION, so
n T0 = T_tube is an identity; the "0.02% closure" was rounding, and bounds
nothing. Filed.

B2/B3 THE VIOLATION PARAMETER: delta = g_c E_x/(T0 a). FND-029's band
E_x/(T0 a) in [0.019, 87] cannot bound delta from above (factor 87); the
floor implies delta >= 1.9% only if the intra-tube contact prefactor
g_c >= 1, and g_c is UNREGISTERED (parallel strands could give g_c ~ 0).
Additivity is internally UNTESTED by the corpus.

B4 THE EXTERNAL DISCRIMINATOR, locked then confronted: under exact
additivity + vacuum-packing (R_tube = a sqrt(n/(3 pi))), the adjoint tube
(Casimir sigma ratio 9/4) must be WIDER: rho_R = R_adj/R_fund = 3/2.
DATA (Cardoso-Cardoso-Bicudo, PRD 81 034504 / arXiv 1010.3870, quenched
SU(3), beta = 6.2): the adjoint/fundamental ENERGY-DENSITY ratio is
CONSTANT across the transverse profile, 2.25(2) on-axis and 2.24(6) in the
mediator plane -- same profile shape, hence rho_R ~ 1.0. Deviation from
1.5: -33% -> BROKEN band (> 25%), with stated caveats (short separations
~0.3-0.6 fm; large-distance errors big; proceedings-grade).

THE WOUND, LOCATED: not additivity itself (two coincident tubes with
2.25x density is fine strand bookkeeping) but the VACUUM-PACKING
assumption inside R_tube = a sqrt(n/(3 pi)): tube strands can compress
(the adjoint packs 9/4 the density into the same radius), so the
fundamental tube's own packing factor kappa_pack >= 1 is UNMEASURED and
sits between the lattice R_eq and the vacuum Sigma. RE-SCOPING: the
pinned 3.61-3.70e35 J/m^3 stands as Sigma_eff = T_tube/(pi R_eq^2), the
DIRECTLY MEASURED tube tension density; its identification with the
VACUUM stiffness now carries Sigma_vac = Sigma_eff/kappa_pack with
kappa_pack >= 1 open. SURVIVES UNTOUCHED: MU's demotion of 5.1e35 (a
provenance result), XI/OMICRON/PI (R_eq comparisons, representation held
fixed), RHO (kappa_pack cancels in the same-representation ratio).
INHERITS THE CAVEAT: every consumer of Sigma as the vacuum's own number
(kappa_0, the fence, the M-point T0) -- re-evaluation named as next-order.
"""
import math

SIGMA_RATIO_CASIMIR = 9 / 4
RHO_R_PRED = math.sqrt(SIGMA_RATIO_CASIMIR)           # 1.5 under additivity+packing
DENSITY_RATIO_MEAS = [(2.25, 0.02), (2.24, 0.06)]     # constant across profile
RHO_R_MEAS = 1.0                                      # same-shape profiles


def main():
    assert abs(RHO_R_PRED - 1.5) < 1e-12
    for v, e in DENSITY_RATIO_MEAS:
        assert abs(v - SIGMA_RATIO_CASIMIR) < 3 * e   # Casimir scaling of density holds
    dev = RHO_R_MEAS / RHO_R_PRED - 1
    assert abs(dev) > 0.25, "confrontation left the BROKEN band"
    # tautology check: n*T0 == T_tube identically in the construction
    a, req, tt = 1e-16, 0.407e-15, 1.874e5
    n = 3 * math.pi * (req / a) ** 2
    assert abs(n * (tt / n) / tt - 1) < 1e-14
    print(f"rho_R predicted {RHO_R_PRED} vs measured ~{RHO_R_MEAS} ({dev:+.0%}) -> BROKEN")
    print("wound located at the vacuum-packing assumption; Sigma re-scoped to Sigma_eff;")
    print("kappa_pack >= 1 registered OPEN. Tautology correction filed against FND-033(c).")
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
