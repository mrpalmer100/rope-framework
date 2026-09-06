# COMMISSION TRIPLE-DUTY -- RESULTS (2026-09-05)
Executed under analysis/TRIPLE_DUTY_charter_LOCKED.md (locked before any
reduction was evaluated at the magic angle). Legs 0-3:
analysis/triple_duty/ (control logs, leg1_R1_symbolic.py, leg1_v2.log,
leg2_ladder.py + .json, leg3.log). s = 1/3 entered once, in Leg 3.

## VERDICT: ** TD-HALF-DEVIATOR **  (B1 passes, B2 fails)
with candidate principle P-b (Lorentz saturation) PROMOTED for Duty 3
under the charter's TD-HALF rule -- Duty 3 is a saturation at the
isotropy angle, not an identity of the anchor.

## Leg 0 -- controls (all pass)
c1 FND-130 theorem reproduced from the reused object at s = 1/3
   (f_n numeric vs analytic 0.000 pct). c2 BLOCH-L anchor reproduces
   the registered read k_f/T0_f = 9.00823, T_fibre/T0_f = 1.50137
   (deterministic, byte-identical). c3 energy_bill Leg 1 identity
   v_m^2/c^2 = 1.0000000000. v2 symbolic F_bend vs discrete gradient at
   s = 0.25 / 0.40 / 0.50: 0.0017 / 0.0030 / 0.0042 pct at converged
   discretization (at s = 0.25 the control's default N = 20000 gave
   0.027 pct because f_n ~ -0.64 is a near-cancellation of terms of
   size ~3; refining N to 80000 and 320000 converged second-order to
   0.0066 and 0.0017 pct -- the control's numerics, not the object;
   disclosed). v3 all seven ladder rungs converged (24p vs 48p drift
   0.034 pct, bar 0.5 pct). v4 clean room grep-verified.

## Leg 1 -- R1: THE DEVIATOR THEOREM (B1 PASSES)
From the FND-130 object with s, kb, R, b free:
    tau^2 - kappa^2/2 = (3s - 1) / (2 (R^2 + b^2))
    F_bend = R kb (3s - 1) / (2 (R^2 + b^2)^2)         for EVERY R, b, kb
At p = a_f: F_bend(s) = 4 pi^3 kb s^(3/2) sqrt(1 - s) (3s - 1); (3s - 1)
divides exactly (remainder 0); the cofactor 4 pi^3 kb s^(3/2) sqrt(1-s)
has no zero and no pole on (0, 1). Since E[t_z^2] - 1/3 = (3s - 1)/3 for
a uniform helix, the bending force density is the deviatoric second
moment times a positive cofactor: a filament whose tangent second
moment is isotropic exerts no bending force on itself, for every helix
radius and every kb. DUTY 2 IS A COROLLARY OF DUTY 1. Theorem, not
coincidence.

## Leg 2 -- R2: THE ANCHOR AS A FUNCTION OF s (B2 FAILS)
Seven anchor solves (registered inputs; S2, p = a_f, KT0 = 2, kb = 0;
c_T = 1, c_L^2 = 2 imposed; 1/3 not on the ladder), all converged:
   s      T_fibre/T0_f   1/(1-s)    M(s)       v_m^2/c^2 = (1-s) T
  0.20      0.47992      1.25000   -61.61 %     0.3839
  0.25      1.14906      1.33333   -13.82 %     0.8618
  0.30      1.42039      1.42857    -0.57 %     0.9943
  0.35      1.52438      1.53846    -0.91 %     0.9909
  0.40      1.54978      1.66667    -7.01 %     0.9299
  0.45      1.53609      1.81818   -15.52 %     0.8448
  0.50      1.50263      2.00000   -24.87 %     0.7513
  (1/3, registered: 1.50137, M = +0.09 %, v_m^2/c^2 = 1.0009 -- the
   FND-126 reading window)
max |M| / (1/(1-s)) = 61.6 pct vs bar 0.5 pct: B2 FAILS. T_fibre(s)
is NOT 1/(1-s) identically.

BUT the shape is the finding. M(s) <= 0 on every rung and M ~ 0 only at
the magic angle: the two curves T_fibre(s) and 1/(1-s) are TANGENT at
s ~ 1/3, not crossing. Equivalently v_m^2/c^2 = (1-s) T(s) is a HUMP
with its maximum at s = 0.323 (parabola through 0.30, 1/3, 0.35; the
1/3 point itself is the registered +0.09 pct), value 1.003 at the fit
peak and 1.0009 at the registered angle -- unity to the reading
window. The material orbital speed of the level-1 winding never exceeds
c on the ladder and reaches c only at the isotropy angle.

## Leg 3 -- candidate adjudication (s = 1/3 entered once)
P-c (second-moment isotropy as the sole condition): reproduces Duties 1
    and 2 (B1) but NOT Duty 3 as an identity (B2). Partial.
P-b (Lorentz saturation): EXHIBITED by the anchor -- v_m(s) <= c with
    equality at the magic angle. Duty 3 is re-read: not "T_fibre =
    1/(1-s) at s = 1/3" as an identity, but "the isotropy angle is
    where the dynamically anchored winding's material speed SATURATES
    c." P-b reproduces Duty 3, coincides with Duty 1, and Duty 2
    follows from Duty 1 by the deviator theorem. Zero new constants.
    PROMOTED under TD-HALF.
P-a (kinetic-energy stationarity): not separately exhibited; the
    stationarity the ladder finds is that of v_m^2 itself (P-b).
R3 (display only): E[t_z^6] = 0.1369 vs 1/7 = 0.1429; no candidate
    predicts it.

## What this settles
- Duties 1 and 2 are ONE theorem (deviator divisibility, general R,
  kb). The KNOWN_LIMITATIONS "triple duty" entry moves from "three
  accidents or one principle" to: two are one theorem; the third is a
  saturation principle exhibited numerically at the same angle.
- FND-132's c-orbital identity keeps its registered status (identity
  at s = 1/3; tripwire on T_fibre) and gains a rider: it is the
  maximum of v_m(s) over the pitch angle, equal to c at the isotropy
  angle within the reading window; off the angle v_m < c.
- The open question narrows to a sharp one: WHY does the dynamical
  anchor's v_m(s) peak at the isotropy angle? A derivation of that
  tangency from the anchor equations would make P-b a theorem and
  close the triple duty entirely. Named as the next-order.
- T_fibre = 3/2, c_L,f, kb, the share band: untouched.

## Process
Symbolic first (R1), ladder at locked rungs with 1/3 excluded (R2),
substitution once (Leg 3). One session (two budgeted). The v2 control's
discretization refinement is disclosed above; no bar was moved.
