# COMMISSION CASIMIR-PLATE (F3) -- CHARTER (DRAFT, NOT LOCKED)
# Drafted 2026-09-02 for the author's desk, against corpus v3.29.0 plus
# the post-release state (S3R, Q54, REPRICE, BRICK2, GR54 in progress).
# Locks ONLY on the author's word, and BEFORE any boundary-modified
# spectrum is computed. Executes STRATEGIC_TARGETS.md section F3 (17 Aug
# 2026: "highest external value, one commission"), recorded in the
# CHANGELOG at v3.26.77 as "Casimir deliberately NOT added (uncomputed)".

## NAMING (binding, per docs/NAME_REGISTRY.md)
"Casimir" in this charter means the PLATE FORCE between two conductors.
It is NOT the adjoint Casimir-SCALING ratio of the k-string sector
(FND-046/047/106, docs/ADJOINT_CS_MEASUREMENT_SPEC.md). Every text this
commission produces writes CASIMIR-PLATE; the scaling ratio keeps its
registered name. Third naming-collision risk flagged before it collides
(EM-020 / Sigma_wave precedent).

## THE QUESTION
FND-132 gave zero-point energy a mechanical identity: it IS the fine
winding's rotation, with the dynamical share of the vacuum budget at
[0.615, 0.779] (Prediction 32). If that identity is physical, the
force between two conductors in this medium becomes computable from
the corpus's own machinery: the transverse-mode spectrum of the wound
vector medium (the FND-089 instrument) between two plates, versus the
same medium unbounded. The question, in the order it must be answered:

  Q1  Does the wound medium, with the plate condition READ OFF the
      registered field-tensor dictionary, produce a plate force that
      falls as d^-4 at all?
  Q2  If so, is the dimensionless coefficient the two-polarization
      number, or does a third channel (the longitudinal carrier,
      c_L/c = sqrt(k/T0) coarse, c_L,f = 3.00 c fine) contribute?
  Q3  What per-mode ACTION does the coefficient require, and can any
      registered fine-level object supply it inside the a_f ceiling?

Q1 and Q2 are zero-input structural questions with kill outcomes. Q3
is where the corpus's one mesoscopic unknown (what sets g, FND-044) is
expected to reappear; the charter names that in advance so that its
reappearance is a finding and not a surprise.

## WHAT IS GIVEN (registered inputs; no others enter a build leg)
- The wound vector medium at the derived angles psi_1 = 35.2644 deg,
  psi_2 = 59.4444 deg, no free angles; its 18-neighbour stencil and
  two transverse bands (FND-088/089, benchmarks/foundations/
  shin6_3d_bloch.py). Reused byte-identically (SPARSE-J D1 precedent).
- The field-tensor dictionary (EM-016/017 Derived; phi's channel
  longitudinal by elimination, EM-018; the inertial term EM-019; the
  calibration constant EM-021).
- The zero-point cutoff convention (FND-109, ZP-CONV): carried modes
  only; THE LATTICE IS THE REGULATOR. No zeta regularization, no
  analytic continuation, no continuum subtraction by hand.
- The wave state: level-1 wave speed sqrt(3/2) c, material orbit at
  c, R_1 = 0.22508 a_f, T_fibre = 3/2 T0_f (FND-130/131/132).
- The a_f CEILING and the (m, n_sub) suspension (FND-110; GRV-128;
  FND-122). a_f enters every build leg as a SYMBOL.
- The registered hbar relation, for the consequence leg only:
  hbar = T0 [l_q^2/(4 pi alpha)]/c (PRED-003 lineage; GRV-093).
- The weave bath, for reading (iii) only: FND-STRAND-007/008 (gapped
  bath; temperature a symbol).

## WHAT IS NOT ASSUMED (the circularity ban, verbatim from the one-fence
## directive)
No hbar, no hbar-omega/2 per mode, no quantized occupancy in any build
leg. The measured plate-force coefficient, pi^2/240, and every
experimental number are TARGETS and stay out of the room until Leg 5.
The doubled clean room of COMMISSION MAINT is honoured: energy scales
attach as symbols in Legs 1-4 and as numbers in Leg 5 only.

## SCOPE (hard boundary)
Parallel conducting plates, zero temperature of the LABORATORY (the
weave's own bath is reading (iii), inside scope), separations
d >> a_f, d >> the winding period. Sphere-plate geometry, finite
conductivity (Drude/plasma), roughness, and the lab-temperature
correction are OUT: the confrontation in Leg 5 is against the
parallel-plate coefficient the experimental literature itself reports
after those corrections, and the charter says so on the face.
This commission does NOT re-adjudicate the share band (Prediction 32),
Sigma_wave, the composite build, or any Q-SWEEP/GR54 object; the
composite amplitude question enters only as the named home of the
level-2 contribution, which is bracketed, not used.

## DESIGN COMMITMENTS (locked at lock)
D1. INSTRUMENT. The FND-089 supercell (shin6_3d_bloch.py: derived
    tangent field, 18-neighbour dynamical matrix, both transverse
    bands) in a PISTON geometry: a slab of height L along the plate
    normal, a plate at z = 0 and z = L, and a movable plate at z = d,
    periodic in-plane. The Casimir energy per area is
      E(d) = [E_slab(d) + E_slab(L - d)] - [E_slab(L/2) + E_slab(L/2)]
    computed at fixed lattice regulator. The piston form is chosen
    BEFORE any number because it cancels the surface and bulk terms
    identically on a lattice and leaves no subtraction to choose.
D2. THE PLATE. The boundary condition is DERIVED from the dictionary
    in Leg 1, not chosen: a perfect conductor has zero tangential E,
    and the dictionary maps E to a mechanical displacement/strain
    component; the condition imposed at the plate sites is whatever
    that mapping says, written down and recorded before Leg 2 runs.
    If the dictionary does not fix the plate condition uniquely for
    every registered channel, the commission HALTS at Leg 1 with
    verdict CAS-BC-OPEN and no plate-force number is produced.
D3. THE CHANNEL CENSUS. Leg 1 also records, per registered mechanical
    channel (transverse band 1, transverse band 2, the longitudinal
    carrier), whether the derived plate condition constrains it. A
    channel the plate does not constrain contributes nothing to the
    piston energy by construction; a channel it does constrain is
    summed. The census is a derived object, displayed, not tuned.
D4. THREE PER-MODE ENERGY READINGS, all computed, none adopted. Each
    reading assigns an energy to a boundary-modified mode of
    frequency omega; the d-dependence follows from the same spectrum:
      (i)   COHERENT-WINDING: the dynamical share sits in the winding
            wave itself (one mode family at the winding wavenumber,
            amplitude R_1); the piston energy is the change in that
            state's energy under the plate condition.
      (ii)  STANDING-WAVE ACTION: E_mode = S omega with the registered
            form S = pi T A^2/(2c) (HBAR sector; "the length cancels
            identically, what selects the amplitude remains open"),
            S carried as a SYMBOL.
      (iii) WARM-WEAVE EQUIPARTITION: the registered gapped bath
            (FND-STRAND-007/008) at temperature T_w (symbol),
            classical occupation.
    The exponent p and coefficient K are extracted separately for
    each reading. No fourth reading is admitted after numbers exist.
D5. THE LADDER. Plate separation d = 8, 16, 32, 64 lattice units
    (winding-period-commensurate rounding recorded), piston height
    L = 4 d_max, in-plane Bloch reduction over a k_par grid converged
    per bar v4. The exponent p is the log-log slope over the top three
    rungs; the coefficient is Richardson-extrapolated in 1/d and its
    last two extrapolants must agree to 1 percent (bar v5).
D6. ANISOTROPY DISPLAY. The plate normal along the weave z-axis and
    along (111) (FND-137's sixth-moment anisotropy is the named
    input). The coefficient's orientation spread is DISPLAYED; it is
    not barred, because a laboratory plate averages over weave
    orientations the corpus has not registered.
D7. LEVEL-2 CONTENT. The level-2 winding's contribution to reading (i)
    is BRACKETED using the registered two-level bracket (path factor
    2.409, kb <= 0.07909), not solved; the exact number is the
    composite build's property (FND-134/135) and is not chased here.

## VALIDATION BARS (halt-grade; every one before any Casimir number)
v1. INSTRUMENT REPRODUCTION: the unbounded FND-089 supercell reproduces
    the registered SHIN6 numbers (min group speed 0.791; phase spread;
    both polarizations, thirteen directions) to 1e-6 relative.
v2. CONTROL A, SCALAR DIRICHLET: the straight (unwound) medium reduced
    to a single scalar band with Dirichlet plates, in the same piston
    instrument, must give p = 4.00 +/- 0.05 and a coefficient
    converging to the lattice-free value for one Dirichlet
    polarization, pi^2/1440 per unit S, within 1 percent at the top
    rung. This is the mathematics of a linear-dispersion scalar on a
    lattice, not a physical target; it calibrates the piston, the
    ladder and the extrapolation. (The number is permitted in the
    control leg because it is a property of the mode sum, independent
    of any value of S.)
v3. CONTROL B, SCALAR NEUMANN: same, with the Neumann plate; sign and
    magnitude of the parallel-plate scalar result reproduced.
v4. IN-PLANE CONVERGENCE: E(d) at the top rung changes by < 1e-4
    relative when the k_par grid is doubled.
v5. PISTON INDEPENDENCE: E_slab(d) + E_slab(L - d) is independent of L
    to 1e-4 relative at fixed d over L in {3, 4, 6} d_max.
v6. CLEAN ROOM: hbar, pi^2/240, and every experimental value appear in
    NO file executed in Legs 0-4 (grep-verified and recorded, MAINT
    precedent).

## THE LEGS
Leg 0  Controls v1-v6.
Leg 1  THE PLATE, DERIVED. Reading only; no solves. Output: the plate
       condition on the displacement field per channel, and the
       channel census (D2/D3). Halt on CAS-BC-OPEN.
Leg 2  THE BOUNDARY-MODIFIED SPECTRUM on the piston ladder, wound
       medium at the derived angles, every channel the census admits.
       Output: mode frequencies per rung, per k_par, per orientation.
Leg 3  THE THREE READINGS. From Leg 2's spectrum, E(d) under (i), (ii),
       (iii); exponent p and coefficient K in symbol units for each;
       the transverse-only and total K recorded separately.
Leg 4  ANISOTROPY DISPLAY (D6).
Leg 5  CONSEQUENCE LEG -- numbers attach. Targets loaded ONCE:
       the parallel-plate force law F/A = -(pi^2/240) hbar c / d^4,
       the exponent as measured (Lamoreaux 1997; Mohideen and Roy 1998;
       Bressi et al. 2002, parallel plates; Decca et al. 2005/2007,
       the 1-percent class at 160-750 nm after the literature's own
       conductivity and thermal corrections; citations fixed at lock).
       Then, under reading (ii): the per-mode action S_req that the
       measured coefficient demands, and its confrontation with
         (a) the registered hbar relation (GRV-093) -- an identity
             check, not a result, recorded as such; and
         (b) the fine winding's own single-mode action
             S_1(a_f) = pi T_fibre R_1^2/(2c) evaluated at the a_f
             CEILING, reported as the ratio S_1(ceiling)/S_req.
       Under reading (iii): the bound on k_B T_w that the sub-micron
       data impose on any d^-3 term, against the registered bath.

## PRE-REGISTERED INTERPRETATION RULES (locked before results; anything
## else is NO CALL)
Let p be the converged exponent and K the coefficient in the form
F/A = -K S_eff c / d^4, with S_eff the per-mode action of the reading.
Let K_2 be the two-polarization transverse-only value and K_tot the
census-total value. The exponent window is p in [3.9, 4.1] at the top
rung with v5 passed; outside it, p is "not 4".

  CAS-BC-OPEN: Leg 1 cannot fix the plate condition from the
      dictionary for some channel. HALT. Registered as a named debt on
      EM-016's face (a conductor is not yet a dictionary object); no
      plate-force number exists.

  CAS-SHAPE-FAIL: p is not 4 under EVERY reading the census admits.
      The wound medium with the derived plate condition does not
      produce the Casimir law. FND-132's mechanical identity (zero-
      point energy = the winding's rotation) is REFUTED AS THE CASIMIR
      SOURCE; registered Failed and kept. Prediction 32 (the share
      band) is untouched: the energy bill is an accounting result and
      survives on its own evidence. This is STRATEGIC_TARGETS F3's
      pre-named failure mode, firing.

  CAS-CHANNEL-KILL: p = 4 for the transverse readings, but the census
      forces the longitudinal carrier to meet the plate condition and
      K_tot / K_2 - 1 > 0.03 (threshold fixed from the 1-percent
      datasets with a 3x safety margin). The superluminal channel is
      NOT hidden from conductors at the Casimir surface; the
      registered Lorentz-hiding machinery has a falsifier fired on it.
      Kept. (For orientation, not for the bar: a longitudinal channel
      at c_L = 3c with a Dirichlet-class condition would add of order
      1.5x the transverse value; at c_L = sqrt(2) c, of order 0.7x.
      The bar is the measured K_tot/K_2, not these estimates.)

  CAS-FORM: p = 4 and K_2 = pi^2/240 within the ladder's own
      convergence (1 percent) under reading (ii). The FORM of the
      Casimir law DERIVES from the wound medium and the dictionary,
      and its coefficient is reduced to ONE per-mode action S_eff.
      Sub-verdicts, exactly one:
        CAS-PIN:  S_1(a_f) = S_req at some a_f INSIDE the registered
                  ceiling. The fine scale a_f is PINNED by the plate
                  force. This spends the programme's one permitted
                  calibration (declared here, in advance: the
                  measurement spent is the Casimir coefficient); the
                  frame-dragging amplitude (GRV-128 chain) and the PeV
                  rotation quantum (F2) become PREDICTIONS at the
                  pinned a_f and are re-priced on their own claims.
        CAS-GAP:  S_1(ceiling) < S_req by a factor R (recorded). The
                  winding's single-mode action cannot supply the
                  Casimir action anywhere inside the ceiling; the
                  coefficient waits on the collective/mesoscopic
                  mechanism the corpus already names as its one
                  unknown (FND-044: what sets g). The form result
                  stands; the mechanical identity is BRACKETED (the
                  winding is the zero-point ENERGY; the Casimir
                  ACTION is collective), not refuted.
        CAS-OVER: S_1(ceiling) > S_req. The ceiling is too generous by
                  the recorded factor; a_f gains a Casimir-derived
                  UPPER bound tighter than FND-110's, registered as a
                  bound (a bound is not a pin; no exposure clause arms).

  CAS-THERMAL (runs alongside any of the above): reading (iii) yields
      a d^-3 term whose coefficient, against the sub-micron data,
      bounds k_B T_w. If a bath temperature is registered anywhere in
      the corpus and exceeds the bound, the warm-weave grant's
      tripwire fires and is recorded; otherwise the bound is filed on
      FND-STRAND-007's face as a constraint.

  Anything else (unconverged ladder, a control failing after Leg 2
  began, a reading whose p lands in neither window): NO CALL; report
  and stop.

## NO-RESCUE RULE
No re-derivation of the plate condition, no change of reading, no
change of piston geometry, ladder or extrapolation order, and no new
per-mode energy assignment after a Leg 2 number exists. The three
readings are all computed and all reported whichever one flatters.
Failures kept on the record at full weight.

## SCHEDULING (budgets, not bars)
With in-plane Bloch reduction the per-k_par problem is a 1D chain of
d x (winding period)^2 sites, three components each: at d = 64 and
period 6 this is ~7k unknowns, dense-diagonalizable on the laptop;
the k_par grid multiplies the count but not the size. Expected cost:
one session for Legs 0-1, one for Legs 2-4, one for Leg 5 and the
results doc. No SPARSE-J solves are required; the instrument is the
FND-089 eigen-instrument, not the torus solver. Durable state to
analysis/casimir_plate_ckpt.pkl at every close-out; results to
analysis/CASIMIR_PLATE_results.md; bars to
analysis/CASIMIR_PLATE_charter_LOCKED.md on the author's lock.

## STANDING
Registered claims untouched by this commission until the author
grants. Grants reserved to the author. No claim is drafted before the
verdict step has run ONCE. This charter ships with its results in the
release that carries them.

DRAFT, NOT LOCKED. Lock line and amendments, if any, go below this line
with their reasons.

LOCKED 2026-09-05 on the author's word ("execute the next brick on the
queue"), before any Casimir number exists. Notes at lock: FINE-GATE
(FND-167) names this commission's per-mode action as the relation that
would give the a_f gate its first closing pair; PEV-IDENT (FND-166)
means the "PeV rotation quantum re-priced at a pinned a_f" consequence
under CAS-PIN is the ceiling relation times 2 sqrt2, not an independent
prediction. Neither touches the bars.

## AMENDMENT A1 (Leg 0 calibration, 2026-09-05; before Leg 1 and before
## any wound number): two properties of the piston as chartered, found by
## the scalar controls and fixed as calibration, not rescue:
(a) The piston E_slab(d) + E_slab(L-d) - 2 E_slab(L/2) does not cancel
    the FAR slab's own d^-3 term; for any d^-3 law it carries the exact
    geometric factor g(d, L) = 1 + (d/(L-d))^3 - 2 (2d/L)^3 (0.787 at
    d = 64, L = 256). The Casimir energy is read as piston(d)/g(d, L).
    v5 (L-independence) is read on the normalized piston.
(b) The plate's EFFECTIVE POSITION is a lattice fact: a Dirichlet-class
    condition at fixed sites 0 and n+1 gives d_eff = d + 1; a Neumann-
    class (free-end) condition gives d_eff = d. The ladder's d is the
    effective separation; Leg 1 must state d_eff for the derived plate
    condition before Leg 2 runs.
With (a) and (b): control A (scalar Dirichlet) p_F = 4.002, K ->
pi^2/1440 to 0.01 pct at both Richardson extrapolants; control B
(scalar Neumann) p_F = 4.002, K = pi^2/1440 to 0.00 pct; v4 in-plane
convergence 3e-6 at W = 1024 -> 2048 (a 64 x 64 in-plane grid was
found non-convergent at the 74 pct level and rejected); v5 spreads
1.2e-3 (D, at fixed d_eff bookkeeping) and 2.4e-5 (N). Recorded in
analysis/casimir/.

## AMENDMENT A2 (2026-09-05): Leg 1 resolved by E-RECON (analysis/
## ERECON_results.md, RECON-IDENTICAL). Plate condition, recorded before
## Leg 2: tangential collective displacement PINNED at plate sites
## (Dirichlet, both transverse bands), d_eff = d + 1; tension field phi
## level along the plate (longitudinal carrier constrained at k_par != 0).
## CAS-BC-OPEN is lifted; Legs 2-5 licensed.

## AMENDMENT A3 (pre-Leg-2, 2026-09-05): implementation choices fixed before any
## wound number. Ladder d = 10, 20, 30, 40 (P = 5 commensurate rounding of the
## chartered 8/16/32/64; recorded), L = 120 = 3 d_max, effective separations d + 1.
## In-plane quadrature: polar, radial Gauss-Legendre on k = k_c t^3 (k_c = pi/5,
## N_r = 16), 16 angles; shown on the scalar control to match a 1024^2 grid to the
## lattice-correction level. Readings from one spectrum: (ii) E = (1/2) S sum omega
## (the charter's K_2 = pi^2/240 force coefficient is the 1/2-quantum convention,
## S_eff the hbar-analogue); (iii) F = k_B T_w sum ln omega; (i) the k_par = 0 slice
## (the coherent winding is the zero in-plane wavenumber family). Plate normal along
## z only; the (111) display (D6) is deferred as UNREACHED with reason (a (111) slab
## is not layer-commensurate with the cubic cell at P = 5).

## AMENDMENT A4 (pre-Leg-3, 2026-09-05, computational budget): the local
## ladder runs at N_r = 12, N_t = 8 with the k <-> -k (time-reversal)
## reduction (49 k-points incl. the k = 0 slice), divide-and-conquer
## eigensolver, threaded BLAS. The 16 x 16 grid cost 630 s per k-point
## (~45 h). The scalar control converged at 16 x 8; v4 (in-plane
## convergence at the top rung, finer grid) is OWED as a follow-up run
## and the verdict will carry it as a caveat until it lands. No bar moved.
