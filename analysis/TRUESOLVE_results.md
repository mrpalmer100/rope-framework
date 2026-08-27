# COMMISSION TRUE-SOLVE -- RESULTS (2026-08-18)

Executed under analysis/TRUESOLVE_bars_LOCKED.md.
Benchmark: benchmarks/foundations/truesolve_bloch.py (imports the
FND-126 instrument and the FND-138 operator; the imported ANSATZ
module replays its halt banner before this commission's output --
cosmetic, per the standing annotation).

## VERDICT

**RE-SOLVED, LOOSER: kb <= 0.09332 T0_f a_f^2.** The Bloch-instrument
feasibility ceiling under the adjudicated true curvature replaces the
per-level-sum value as the bound of record. Direction as the
zeroth-order display predicted (LOOSER than 0.07909); magnitude
BELOW the display (0.09332 vs 0.102, ratio 0.915) -- the display
over-predicted the loosening because the anchor system re-solves
jointly: at the feasibility edge the stiffness read moves to
k_f/T0_f = 8.557, so the bending channel does not simply inherit the
kb = 0 anchors scaled by the energy-weighting ratio. The zeroth-order
weighting is a direction estimator, not a value estimator, and that
finding is registered alongside the number.

The bound carries FND-131's named dynamical-background gap UNCHANGED:
this re-solve corrected the curvature object, not that gap.

## THE INSTRUMENT-UNCHANGED PROOF (control vi)

At kb = 0 the bending channel is the only consumer of k0, and the
anchor re-solve returned k_f/T0_f = 9.00823, T_fibre/T0_f = 1.50137 --
FND-126's read to within its own inherited tolerance, with the
reading-window drift identical at 0.0343%. The instrument is the same
instrument; only the bending channel moved. Every kb = 0 object
(the additive mapping, c_L,f = 3.00 c, the k/T0 = 2 non-derive, the
material-speed identity) is untouched by construction and now by
measurement.

## CONTROLS, ALL PASS

Frame identity |t_ans(f2+pi) - t_bloch| = 6.1e-16; operator tangent
reproduction 1.6e-11; Frenet |t . kappa_true| = 6.4e-11 (the
indictment |t . K_reg| = 1.506 displayed alongside); linearity
decomposition of the dynamical matrix 4.1e-16; straight control
c_L = 2.9986/c_T = 1.2242; multiplicity m=4 vs m=6 drift on the
ceiling 0.589% (PASS at 1%; m=2 at 0.12695 displayed, coarse as
expected). Ensemble <|kappa_true|^2> = 11.90 /a_f^2 over the
instrument's sampling, consistent with FND-138's grid (0.732x
registered) and FND-139's MC (0.776x) displays. SciPy convergence
warnings near the T -> 0 boundary during the m=2 sweep are the
solver's near-singularity complaint at the edge, not a control.

## KBSAT CONTEXT (desk display only; no grant motion)

Both candidate values remain OUTSIDE the new ceiling: 0.126 and
0.282 are both infeasible under kappa_true. The KBSAT value question
at the author's desk keeps its shape; the ceiling it would confront
is now 0.09332.

## THE SHIN7 WORST CASE (value owed per FND-139, now paid)

max |kappa_true| over the phase torus (240^2 grid) = 4.4689 /a_f.
SHIN7's worst-case 5.713 was an upper bound and HOLDS with margin
1.28x; the re-solved value is now on the record.

## THE 17.926 DISPOSITION (by name)

tau_2^2 - kappa_2^2/2 is a per-level object inside the composite
build's level-2 speed. Its host state was measured off-shell
(FND-139) and proven nonexistent in the rigid family (FND-140); its
re-derivation is GATED ON TRUE-STATE STAGE 2 and no number is issued
here. energy_bill.py's two-level bracket, which consumes it, already
sits under the Sigma_wave rider chain.

## DOWNSTREAM, NAMED

Every kb-built quantity quoted from the 0.079 bound re-prices from
0.09332 on its own face at next touch: (G I_p)_f <= 4 kb/5 = 0.0747
T0_f a_f^2 (was 0.0633), lambda_strand and the Lambda_nat ceiling
move with it (arithmetic-propagation class, not run tonight). The
r_s bound inherits through kb/(T0_f r_s^2) = 9/4: r_s <= 0.2036 a_f
(was 0.187). These are stated for the ledger; their registration
rides their own claims' next sessions.
