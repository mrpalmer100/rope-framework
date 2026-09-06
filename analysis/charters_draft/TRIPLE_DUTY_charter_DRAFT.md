# COMMISSION TRIPLE-DUTY -- CHARTER (DRAFT, NOT LOCKED)
# Drafted 2026-09-02 for the author's desk, against corpus v3.29.0 plus
# the post-release state. Locks ONLY on the author's word, and BEFORE
# any symbolic reduction is evaluated at the magic angle. Executes
# FND-130's named next-order (3) ("is there a variational statement
# under which isotropy-exactness and bending-neutrality are one
# condition"), extended to the third duty FND-132 added, and the
# KNOWN_LIMITATIONS sentence "either a variational principle unifies
# them or the corpus owns a spectacular coincidence; the question is
# named, not answered."

## THE QUESTION
One angle does three jobs, each derived from an unrelated demand:

  DUTY 1 (FND-088, isotropy): the level-1 pitch s = sin^2 psi_1 = 1/3
         (psi from the transverse plane) makes the tangent second
         moment isotropic, E[t_z^2] = 1/3, identically.
  DUTY 2 (FND-130, bending-neutrality theorem): at s = 1/3 a uniform
         helix's inward bending force density vanishes identically
         (tau^2 = kappa^2/2), so the level-1 wave speed is kb-free.
  DUTY 3 (FND-132, the c-orbital identity): the material orbital speed
         satisfies v_m^2/c^2 = (1 - s) T_fibre/T0_f = (2/3)(3/2) = 1,
         with T_fibre = 3/2 T0_f from the BLOCH-L dynamical anchor
         solve (FND-126), a computation that contains no angle demand.

Is this one selection principle or three accidents? The question is
posed so that its answer is a THEOREM or a NAMED COINCIDENCE, never a
number that happens to come out.

## THE TWO REDUCTIONS (the charter's content, stated before computing)
Written with s FREE (the target-free rule, docs/technical/
METHODOLOGY_target_free_questions.md: ask the question whose answer is
wrong wherever it lands). The value s = 1/3 is not substituted until
Leg 3.

  R1  DUTIES 1 AND 2 ARE ONE CONDITION. Hypothesis H1: for the
      registered constitutive form (the granted rod class FND-118,
      one modulus, circular section; force density as derived
      symbolically in FND-130), the bending force density of a
      uniform helix is a LINEAR FUNCTIONAL OF THE DEVIATORIC PART of
      the tangent second-moment tensor E[t (x) t]. If H1 holds, a
      filament whose tangent second moment is isotropic exerts no
      bending force on itself, for every helix radius and every kb,
      and Duty 2 is a corollary of Duty 1 rather than a coincidence.
      The sharp form: F_bend(s) / (3s - 1) must be a function with NO
      zero and no pole on s in (0, 1).

  R2  DUTY 3 IS AN IDENTITY OF THE ANCHOR. Duty 3 reads
      T_fibre/T0_f = 1/(1 - s) at s = 1/3. Hypothesis H2: the BLOCH-L
      anchor condition that produced T_fibre = 3/2 (FND-126, the
      dynamical anchor solve on FND-089's supercell, with the
      registered inputs c_L,f and the isotropy anchor), written
      symbolically as a function of s, RETURNS T_fibre(s)/T0_f =
      1/(1 - s) identically. If H2 holds, the material orbit at c is
      forced by the same isotropy that fixed the angle, and the
      tension tripwire on FND-132 becomes a theorem instead of a
      registered identity. The sharp form: the mismatch function
      M(s) = T_fibre(s)/T0_f - 1/(1 - s) must vanish identically, not
      merely at s = 1/3.

A third question rides along at display grade only:
  R3  Does any candidate principle that unifies Duties 1-3 PREDICT
      the registered sixth-moment anisotropy of the two-level tangent
      ensemble (FND-137: E[t_z^6] = 0.1369 vs 1/7)? Displayed, not
      barred; a principle that explained the angle AND the residual
      anisotropy would be worth more than one that explained the
      angle alone, and the corpus should see whether it does.

## WHAT IS GIVEN (registered inputs, verbatim; no others enter)
- The helix geometry at the derived angles: psi_1 = 35.2644 deg,
  psi_2 = 59.4444 deg (FND-088); the level-exchange symmetry (FND-090).
- The bending force density derivation of FND-130 (sympy leg, checked
  by discrete energy gradient to 0.005 percent), benchmarks/
  foundations/maint_equilibrium.py, reused byte-identically as the
  constitutive object; kb as a SYMBOL throughout (doubled clean room).
- The BLOCH-L anchor system (FND-126, benchmarks/foundations/
  blochl_longitudinal.py) and its inputs as registered; the
  thirteenth catch (radius convention inversion) carried in its
  corrected form.
- The c-orbital identity (FND-132, benchmarks/foundations/
  energy_bill.py, Leg 1) as the statement under test.
- FND-137's sixth- and eighth-moment numbers, for R3 display.

## WHAT IS NOT ASSUMED
No new constitutive form. No new energy functional is admitted as
"the variational principle" unless it is built from the registered
objects above with zero new constants; a candidate that needs a
coefficient to make the three duties coincide is a fit and is
reported as such. The value s = 1/3 does not appear in Legs 1-2. The
number 3/2 does not appear in Leg 2 except as the registered result
being reduced (it is the OUTPUT being explained, never an input).

## SCOPE (hard boundary)
Level-1 winding only for the bars. The level-2 helix-on-helix, the
handedness fork, and the fourth harmonic (the standing angle-family
items) are OUT except as R3/display. This commission does not
re-price kb, T_fibre, c_L,f, the share band, or any composite or
Q-SWEEP object; if H2 fails, T_fibre = 3/2 STANDS as registered and
only its "theorem vs identity" status is affected.

## DESIGN COMMITMENTS (locked at lock)
D1. SYMBOLIC FIRST. Both reductions are carried in sympy with s free,
    kb free, helix radius free, and the level-1 wavenumber free.
    Numerical evaluation is confined to Leg 3 and to controls.
D2. THE DEVIATOR TEST (R1) is a divisibility statement: compute
    F_bend(s) exactly from the FND-130 object; factor; record whether
    (3s - 1) divides it and whether the cofactor has zeros or poles
    on (0, 1). No curve-fitting, no series truncation.
D3. THE ANCHOR TEST (R2) re-runs the BLOCH-L anchor solve as a
    FUNCTION of s at the registered inputs, on a ladder of s values
    fixed at lock (s in {0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50};
    the magic value 1/3 is deliberately NOT on the ladder), each at
    the registered convergence bar (0.5 percent drift, FND-126's
    reading window). M(s) is formed at every rung. Identity is judged
    on the ladder, not at the target.
D4. CANDIDATE PRINCIPLES are enumerated and written down BEFORE Leg 3,
    each as a functional of registered objects with zero new
    constants; the list is closed at lock. Pre-registered candidates
    (the commission may find none of them is it, and says so):
      P-a  Stationarity of the level-1 wave's kinetic energy per unit
           axial length at fixed winding number (a Lagrangian in s).
      P-b  Lorentz saturation: the material speed of the medium that
           defines c cannot exceed c and saturates it (v_m = c as a
           constraint that SELECTS T_fibre given s).
      P-c  Second-moment isotropy of the tangent ensemble as the sole
           condition, with Duties 2 and 3 as corollaries (this is
           H1 and H2 together).
    A candidate that reproduces all three duties AND makes an
    additional registrable statement (R3, or the level-2 angle) is
    ranked above one that reproduces the three alone.
D5. CONTROLS. (c1) The FND-130 theorem is reproduced from the reused
    object at s = 1/3 to its registered 0.005 percent before any
    reduction is trusted. (c2) The BLOCH-L anchor solve at the
    registered geometry reproduces c_L,f = 3.00 c and T_fibre = 3/2
    at 1e-4 relative before the s-ladder runs. (c3) The energy_bill
    Leg 1 identity is reproduced to 1e-12 (its registered bar).

## VALIDATION BARS (halt-grade; every one before Leg 3)
v1. Controls c1-c3 pass.
v2. The symbolic F_bend(s) agrees with the discrete energy gradient at
    three off-target s values (from the D3 ladder) to 0.01 percent
    (the FND-130 control, applied away from the magic angle, where it
    has never been checked).
v3. The s-ladder anchor solves each meet FND-126's own convergence bar;
    a rung that does not converge is reported UNREACHED and M(s) is
    not formed there.
v4. Clean room: the strings "1/3", "0.3333", "3/2", "1.5" appear in no
    Leg 1-2 file except as the registered outputs under reduction
    (grep-verified and recorded).

## THE LEGS
Leg 0  Controls v1-v4.
Leg 1  R1, symbolic: F_bend(s) from the FND-130 object; factorization;
       cofactor analysis; the deviator statement proved or refuted.
Leg 2  R2, the anchor as a function of s: the s-ladder solves; M(s) at
       every converged rung; the fit-free question "is M identically
       zero" answered by the ladder's max |M(s)| against bar B2.
Leg 3  Substitution and candidate adjudication: s = 1/3 entered once;
       each pre-registered candidate principle checked against all
       three duties; R3 display (does the winning candidate, if any,
       predict E[t_z^6] = 0.1369).
Leg 4  Results doc and, on the author's grant, the draft registration.

## PRE-REGISTERED INTERPRETATION RULES (locked before results; anything
## else is NO CALL)
  B1 (R1 passes): (3s - 1) divides F_bend(s) exactly and the cofactor
     has no zero and no pole on (0, 1).
  B2 (R2 passes): max over converged rungs of |M(s)| / (1/(1 - s))
     < 0.5 percent (FND-126's own reading tolerance), with at least
     five converged rungs spanning both sides of 1/3.

  TD-THEOREM: B1 and B2 both pass. The three duties are ONE selection
      principle: second-moment isotropy of the tangent ensemble
      forces the angle, the angle forces bending-neutrality by the
      deviator theorem, and the anchor forces T_fibre = 1/(1 - s)
      identically, hence the material orbit at c. Registrable at
      Derived grade on the symbolic leg; FND-132's tension tripwire
      is re-labelled from identity to theorem-consequence (it still
      fires on any re-pricing; only its status changes). The
      KNOWN_LIMITATIONS "triple duty" entry moves to RESOLVED.
  TD-HALF-DEVIATOR: B1 passes, B2 fails. Duties 1 and 2 are one
      theorem; Duty 3 remains a registered numerical identity of the
      anchor at s = 1/3, with M(s) displayed. The open question
      narrows to: why does the dynamical anchor return 1/(1 - s) at
      the magic angle and not elsewhere.
  TD-HALF-ANCHOR: B2 passes, B1 fails. Duties 1 and 3 are one
      condition (isotropy fixes both the angle and the tension);
      bending-neutrality stays a separate theorem coincident at
      s = 1/3, with the cofactor's structure displayed.
  TD-COINCIDENCE: B1 and B2 both fail, all controls green. The three
      duties are three separate conditions that share a root. The
      corpus registers the coincidence at its measured size: the
      cofactor's nearest zero to 1/3 and the value of M(1/3)'s slope
      are the two numbers that say how special the root is. Kept at
      full weight; no candidate principle is granted.
  TD-OPEN: a control fails, or fewer than five ladder rungs converge,
      or the FND-130 object cannot be carried symbolically at free s.
      NO CALL; report and stop.

The candidate adjudication (Leg 3) can only PROMOTE a principle when
the verdict is TD-THEOREM or a TD-HALF; under TD-COINCIDENCE the
candidates are reported as failed and kept.

## NO-RESCUE RULE
No new candidate principle after Leg 3 has begun. No change to the
s-ladder, the convergence bar, or the deviator statement after a
number exists. No coefficient may be introduced to make a candidate
fit; a candidate that needs one is reported as a fit and fails. The
value s = 1/3 is entered exactly once.

## SCHEDULING (budgets, not bars)
Legs 0-1 are symbolic and reading: one session. Leg 2 is seven
BLOCH-L anchor solves on the FND-089 supercell at the registered
grid (each is the FND-126 computation re-run at a different angle):
laptop-class, likely one session. Leg 3 is an afternoon. No
SPARSE-J solves, no torus continuation. Durable state to
analysis/triple_duty_ckpt.pkl; results to
analysis/TRIPLE_DUTY_results.md; this text to
analysis/TRIPLE_DUTY_charter_LOCKED.md on the author's lock.

## STANDING
Registered claims untouched until the author grants. Grants reserved
to the author. No claim is drafted before Leg 3 has run ONCE. Adjacent
commission disclosed in advance: CASIMIR-PLATE (F3) consumes the
level-1 wave state and T_fibre as inputs and is unaffected by this
commission's verdict in every form except TD-THEOREM's relabelling,
which touches status only, not values. The two may run in either
order.

DRAFT, NOT LOCKED. Lock line and amendments, if any, go below this line
with their reasons.
