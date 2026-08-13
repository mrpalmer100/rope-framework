# COMMISSION SHIN5 -- THE WINDING PROVENANCE DERIVATION: RESULTS

Executed 2026-08-12 under analysis/SHIN5_winding_derivation_bars_LOCKED.md.

## Verdict: D1-D4 ALL PASS. The winding is DERIVED.

D1 (hierarchy necessity, exact): a single-level helix has constant
tz = sin psi, so E[tz^4] = (E[tz^2])^2; the isotropy conditions demand
1/3 and 1/5, and (1/3)^2 = 1/9 != 1/5. NO single level can be
isotropic. Two levels are the MINIMUM. SHIN2's empirical finding is
now a one-line theorem.

D2 (existence + closed form): with sin^2(psi_1) = 1/3 (the magic
angle, 35.2644 deg) the second-moment condition holds IDENTICALLY,
and the fourth-moment condition reduces to
    35 u^2 - 30 u + 3 = 0,   u = sin^2(psi_2),
    u = (15 +- 2 sqrt 30)/35 = 0.741556 or 0.115587.
Machine-verified against the quadrature solve at 1e-8.

D3 (the Lorentz selection): the minus root gives sin(psi_eff) = 0.196
(spend 25.9x, OUTSIDE both margins); the plus root gives
sin^2(psi_eff) = u/3 = 0.247185, spend 4.05x, INSIDE both margins
(6.1x, 10.5x). The corpus's own Lorentz bound UNIQUELY SELECTS
    psi_1 = arcsin(1/sqrt 3) = 35.2644 deg
    psi_2 = arcsin(sqrt((15 + 2 sqrt 30)/35)) = 59.4444 deg.

D4 (verification): the full fourth-order orientation tensor at the
selected angles matches the isotropic tensor to 2.9e-13 (bar 1e-6);
the second-order to 8.0e-13. The homogenized transverse wave speed is
therefore direction-independent EXACTLY at these angles: FND-REL-002's
isotropy is recovered as a theorem of the derived winding at
homogenized level (Modeled; the Derived-grade full re-derivation
remains owed as stated in the bars).

## What this discharges and what remains

DISCHARGED from FND-087's debt register, item (3) in part: the
hierarchy depth (two, by theorem) and BOTH pitch angles (closed form,
selected by the registered Lorentz bound) are no longer chosen. The
grant's underived parameters drop from four to TWO: m and n_sub --
the absolute-scale class, which the corpus's standing position
(FND-MATTER-003 lineage) already marks as likely irreducible by
reasoning. STILL OWED: FND-REL-002 at Derived grade on the wound
carriers; the 3D two-polarization instrument; the bending cost.
