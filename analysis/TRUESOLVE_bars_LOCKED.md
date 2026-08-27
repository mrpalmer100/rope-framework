# COMMISSION TRUE-SOLVE -- THE BLOCH BENDING RE-SOLVE UNDER kappa_true -- BARS (LOCKED)

*Locked 2026-08-18 before computing. Chartered at FND-139 (named
next-order 2) and carried by the v3.27.0 handoff: the Bloch-instrument
bending re-solve under the adjudicated true curvature -- the ONLY
mover of record for the registered bound kb <= 0.079 T0_f a_f^2
(FND-126 conditional -> FND-131 bound-with-named-gap). The author
selected this job at the session desk; Sigma_wave is DEFERRED until
TRUE-STATE stage 2 and nothing in this commission touches it.*

## THE INSTRUMENT (inherited, not rebuilt)

FND-089/FND-126's supercell Bloch machinery, longitudinal build,
IMPORTED from benchmarks/foundations/blochl_longitudinal.py: the
energy form (granted rod, Kirchhoff bending strain), the neighbor
stencil, the gradient operator, the site lattice, the eigenvector
polarization identification, the m-multiplicity bundle structure, and
the anchor system (c_T,hom = c; c_L,hom = sqrt(k/T0) c at the
adjudicated k/T0 = 2). THE ONE CHANGE, and the only new physics code:
local_set's k0 is replaced by kappa_true(f1, f2) = D_s(that), the
Frenet curvature of the actual nested curve, via the operator
validated at FND-138/139 (2e-11). The per-level-sum instrument is
superseded-not-erased: the original file is untouched and remains the
record of FND-126.

Frame identity, stated on the face: the instrument's local frame and
the ANSATZ module's frame differ by e1 -> -e1, so
(t, K_reg)_bloch(f1, f2) = (tang, kcomp)_ansatz(f1, f2 + pi) EXACTLY.
The new local set therefore takes BOTH its tangent and its kappa_true
from the ANSATZ module at the shifted phase -- one parametrization,
no mixed conventions. kappa_true is memoized at the instrument's
discrete phases (exact evaluation, no interpolation; no interpolation
control needed).

## CONTROLS (all printed; halt semantics as marked)

(i)   FRAME IDENTITY: |t_ansatz(f1, f2+pi) - t_bloch(f1, f2)| < 1e-12
      at 40 random instrument phases. HALT on fail.
(ii)  OPERATOR, tangent reproduction: |D_s R - t| < 1e-8 at the
      instrument's phases. HALT on fail.
(iii) OPERATOR, Frenet property: |t . kappa_true| < 1e-6. HALT on
      fail. Display alongside: |t . K_reg| (the indictment, expected
      order one -- context, not a bar).
(iv)  LINEARITY DECOMPOSITION: the dynamical matrix assembled as
      kf*D_A + T*D_B + kb*D_C must equal the direct assembly at one
      spot-check (kf, T, kb) to < 1e-10 relative. HALT on fail.
      (Speed machinery only; no physics in it.)
(v)   STRAIGHT CONTROL: unwound medium, c_L = 3.000, c_T = sqrt(1.5),
      inherited tolerance 2e-3. HALT on fail.
(vi)  kb = 0 ANCHOR IDENTITY: at kb = 0 the bending channel is the
      ONLY consumer of k0, so the anchor solve must reproduce
      FND-126's k_f/T0_f = 9 and T_fibre/T0_f = 1.5 to the inherited
      0.02 absolute on k_f. HALT on fail -- this is the
      instrument-unchanged control.
(vii) READING WINDOW: c_L drift 24p vs 48p <= 0.5% at kb = 0 (m = 6),
      inherited bar. At the feasibility edge the window is DISPLAYED
      (the solve is anchored at 24p as FND-126's was).
(viii) MULTIPLICITY: the feasibility-relevant read at m = 2, 4, 6
      displayed; drift m=4 vs m=6 <= 1% on the ceiling or the ceiling
      registers with a multiplicity rider.
(ix)  ENSEMBLE STATISTIC: <|kappa_true|^2> over the instrument's
      local set, displayed against FND-138's grid value (0.732x
      registered) and FND-139's MC value (0.776x) -- consistency
      display, no bar (different samplings).

## THE SOLVE

Leg A -- anchor re-solve at kb = 0 (control vi above).
Leg B -- the feasibility scan: for increasing kb, solve the two
anchors for (k_f, T_fibre); the ceiling is the kb at which T_fibre
crosses zero, by bisection to 1e-4 absolute in kb. Procedure
identical to FND-126's; only k0 differs.
Leg C -- the SHIN7 worst case, value owed per FND-139: max
|kappa_true| over the instrument's phase set, registered as the
re-solved worst-case fibre curvature (bound context: SHIN7's 5.713).
Leg D -- the 17.926 disposition, BY NAME: tau_2^2 - kappa_2^2/2 is a
per-level object inside the composite build's level-2 speed; its host
state was measured off-shell (FND-139) and proven nonexistent in the
rigid family (FND-140). Its re-derivation is GATED ON TRUE-STATE
STAGE 2 and does NOT execute here. Zeroth-order energy-weighting
display only.

## CLEAN ROOM

The registered bound 0.079, the zeroth-order display 0.102, and the
KBSAT values 0.126/0.282 appear ONLY in the comparison leg, after the
bisection has converged. The build and solve legs are blind to all
four numbers. T_fibre tripwire value (v_m = c at T = 1.5) untouched
by construction at kb = 0 (control vi). Verdict prose written AFTER
the run. Bars not edited after lock.

## PRE-REGISTERED OUTCOME SHEET

- Ceiling > 0.079 (LOOSER, the display's direction): the bound of
  record moves to the new value, carrying FND-131's named
  dynamical-background gap unchanged (this re-solve corrects the
  curvature object, not that gap). KBSAT context displayed: whether
  0.126 and 0.282 fall inside or outside the new ceiling -- desk
  information only, no grant motion tonight.
- Ceiling <= 0.079 (TIGHTER, against the display): SURPRISE flagged
  by name; both values registered; the zeroth-order weighting display
  is convicted as a bad estimator and that conviction is itself
  registered.
- Anchor identity (vi) fails: INSTRUMENT-FAULT -- nothing registers,
  the discrepancy is the session's finding.
- Feasibility never closes (T > 0 at all kb searched up to 0.5):
  NO-CEILING-IN-RANGE registered with the search bound on the face.
