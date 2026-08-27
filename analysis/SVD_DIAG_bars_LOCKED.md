# SVD-DIAG bars -- LOCKED 2026-08-21 BEFORE COMPUTING

The smallest-singular-value diagnostic along the aligned branch
(external review step 3, adopted after FND-145). PURPOSE: separate an
A2-chart degeneracy (fold-in-A2 / bad continuation coordinate) from an
approaching GENUINE degeneracy (fold, resonance, gauge degeneration)
using the Jacobian's bottom spectrum and its singular vectors. This is
a DIAGNOSTIC: it grades the chart and the branch geometry; it does not
adjudicate the reach-or-asymptote binary and no interpretive grant is
taken here.

## STATES (measured in this order; per-state checkpoint after each)

  S0  96x36 member 0        A2 = 0.0018792   (baseline, mild)
  S1  96x36 member 1        A2 = 0.0046979
  S2  96x36 march-head x2   A2 ~= 0.0063277  (tangent pair x1,x2 aboard)
  S3  96x36 PROBE-94 landed A2 = 0.0094647
  S4  112x42 adjudicated FND-145 state (n = 14114)

Each state's field RMS is reported first. A state at RMS >= 1e-8 is
measured but FLAGGED and excluded from the interpretation rules
(rate/geometry statements cite full-bar states only, the standing house
rule).

## MATRICES

J = T.jac(x, 'a2', A2_measured(x), PW = 50, float32) -- the Jacobian
the solver actually sees, forward-difference, pin weight 50, each
state pinned at its OWN measured |c2| so the pin row sits at zero.
J_free = J with the continuation pin row (row m-3) deleted. All
sigma comparisons are WITHIN this identical construction; PW-
and chart-dependence is acknowledged; cross-grid sigma comparisons
(S0-S3 vs S4) are NOT registered -- S4 is reported for the record and
interpreted only against itself.

## MEASUREMENTS (per state)

  1. Full singular spectrum of J (LAPACK, values only, float32).
     Report sigma_max, sigma_min, sigma_min/sigma_max, and the bottom
     ten sigmas (gap structure).
  2. Full singular spectrum of J_free. Report sigma_1 (null
     candidate), sigma_2, sigma_2/sigma_max, bottom ten.
  3. Right singular vectors by shifted inverse iteration (CG on
     (J^T J + mu I) matvecs): v_min of J; v_1 and (deflated) v_2 of
     J_free. Vector anatomy: norm fractions in the th / pt / T blocks
     and the (om1, om2) tail; dominant s-mode and phi-mode of the th
     and pt parts; alignment |<v, t_hat>| with the finite-difference
     branch tangent where the pair exists (S2).

## INSTRUMENT BARS (halt-grade; failure of any = STOP, no
## interpretation registered)

  (i)  NULL VALIDATION at S2: sigma_1(J_free)/sigma_max < 1e-4 AND
       |<v_1(J_free), t_hat>| > 0.99, where t_hat = (x2 - x1)
       normalized. The free system's null direction IS the branch
       tangent at a regular point; if the instrument cannot see that,
       it cannot see anything.
  (ii) CROSS-CHECK on every state: inverse-iteration sigma_min(J)
       within 5% relative of the LAPACK value. Vectors are trusted
       only where values agree.
  (iii) INSTRUMENT FLOOR: the forward-difference J carries ~1e-7
       relative error and the store is float32. Any sigma/sigma_max
       below 1e-6 is reported as "< floor", not as a value.

## INTERPRETATION RULES (registered BEFORE results; anything not
## matching a rule is NO CALL and stays open)

Baseline ratios at S0: Ra2 = sigma_min(J)/sigma_max and
R2 = sigma_2(J_free)/sigma_max. Trajectory read across S0 -> S3
(same grid, same construction):

  RULE A (A2-CHART DEGENERACY): Ra2 declines by >= 10x from S0 to S3
       while R2 stays within 3x of its S0 value. Registered reading:
       the chart, not the branch -- fold-in-A2 or exhausted
       parameterization; supports the queued Om2-parameterized
       continuation (review step 4). No branch pathology claimed.
  RULE B (APPROACHING GENUINE DEGENERACY): R2 ALSO declines by
       >= 10x from S0 to S3. Registered reading: a second direction
       is softening. Subclassify by v_2 anatomy at S3:
         B-res  : (om1, om2) fraction >= 0.3, or the dominant field
                  content sits in the m2-sector -- resonance-type
                  (the W0-margin-below-one suspect).
         B-gauge: T-block fraction >= 0.5 -- tension/gauge-type.
         B-open : neither -- UNCLASSIFIED, registered open.
  RULE C (HEALTHY): neither declines by 10x. Registered reading: the
       bottom spectrum does not explain the dA2/ds collapse; the
       asymptote-vs-chart question stays open and the q-sensitivity
       probe (review step 2) is promoted.

## SCHEDULING (budgets, not bars)

Detached, MEMORY-EXCLUSIVE while live. Per-state checkpoint to
/tmp/svd_diag_ckpt.pkl. Calibration on synthetic matrices only,
performed before this lock: values-only f32 SVD ~160 s at n = 10370,
~400 s at n = 14114; total budget ~45 min. Caps are budgets; a budget
exit is resumable and adjudicates nothing.

LOCKED before any corpus matrix was built. Zero amendments at lock
time; any later amendment is recorded below this line with its reason.

## AMENDMENT 1 (2026-08-21, recorded before any interpretation)

WHAT WAS FOUND: the first S0 spectrum shows a dense bottom CLUSTER
(sigma 2.5e-6 .. 3.8e-6 and continuing, ratio ~3e-9 against
smax = 955) far below the registered floor. The chart projects out
the mean and s-Nyquist modes in recon() (TGrid.null), so state
components living in those modes are structurally invisible to the
residual: the cluster is the expected image of GENUINE null
directions at the FD/f32 noise scale, not branch physics. The locked
measurement read sigma_min raw, which would have measured this
cluster identically at every state and adjudicated nothing; the
locked inverse iteration also chases the cluster and its CG stalls
against the nine-decade spectrum (killed at 14 min on S0).

WHAT CHANGES (measurement mechanics only; thresholds, rule structure,
states, and the halt-grade character of the bars are unchanged):
  1. FLOOR-COUNT AND EFFECTIVE SIGMAS. floor_abs = 1e-6 * smax per
     state. k0 = count of sigmas below floor_abs is REPORTED. The
     diagnostic quantities become sigma_eff = smallest sigma ABOVE
     the floor, for J and for J_free; Ra2 and R2 in the rules are
     redefined onto these effective ratios. The bottom-ten report
     becomes the ten sigmas immediately above the floor, plus the
     cluster's range.
  2. VECTORS from the SAME LAPACK factorization (full SVD with
     vectors, economy mode) on the 96 x 36 states: a cluster sample
     vector (its anatomy CERTIFIES or REFUTES the structural-null
     reading; if its dominant modes are not the projected mean or
     s-Nyquist families, the cluster's nature is reported as OPEN and
     rules are not applied), the sigma_eff vector of J, and of
     J_free. S4 (112 x 42) stays values-only with targeted shifted
     inverse iteration at the LAPACK sigma for its vectors (CG capped;
     used only if the self-consistency check passes).
  3. BAR (i) restated for the cluster: at S2 the branch tangent must
     lie in the NEAR-NULL SPACE of J_free -- projection of t_hat onto
     the span of the below-floor right singular vectors of J_free
     > 0.99 in norm. (The tangent is a genuine null direction and
     therefore lives inside the cluster; asking v_1 alone to be the
     tangent was wrong as locked.)
  4. BAR (ii) restated: on 96-grid states, self-consistency
     ||J v_eff|| within 5% of sigma_eff from the factorization; on
     S4, iterative-vs-LAPACK at the targeted sigma as locked.

WHY THIS IS AN AMENDMENT AND NOT A NEW LOCK: the question, the
states, the rule thresholds (10x / 3x / 0.3 / 0.5), and the
interpretations attached to rules A, B, C are untouched. What
changed is which sigma is read, forced by a structural property of
the chart discovered on first contact -- and discovered BEFORE any
along-branch comparison existed to bias the choice.

## AMENDMENT 2 (2026-08-22, recorded before any rule application)

WHAT WAS FOUND: bar (ii) as amended in amendment 1 computes the
self-consistency check ||J v_eff|| through the STORED float32 matrix
with float32 BLAS accumulation. That arithmetic carries an absolute
noise floor ~ eps32 * ||J|| * sqrt(n) ~ 1e-4, a sizeable fraction of
sigma_eff ~ 1e-3. The check therefore measures storage arithmetic,
not factorization quality: at S2 the SAME matrix passed at 0.24% on
J and failed at 11.83% on J_free (one row deleted), a spread that
doublet mixing (~0.2% split) cannot produce. The 11.83% is a noise
draw, but per the house rules a failed halt-grade bar is not argued
past -- it is repaired and re-measured.

WHAT CHANGES (mechanics only; the 5% threshold and the halt-grade
character are unchanged):
  1. BAR (ii) is verified against the TRUE operator: a float64
     directional finite difference of wres itself,
     ||(wres(x + h v) - wres(x)) / h|| vs sigma, h = 1e-7. This is
     float32-independent and simultaneously adjudicates the deeper
     worry that float32 STORAGE could corrupt the bottom spectrum:
     if it does, this check fails honestly and the halt is correct.
     For J_free the pin row's contribution is removed from the f64
     residual difference before the norm.
  2. The same f64-FD norm is reported for the cluster sample vector
     (certifying below-floor-ness against the true operator, not the
     store).
  3. v_eff vectors are checkpointed alongside the scalars so the
     check is re-runnable post hoc.
All states are re-measured from a wiped checkpoint under the amended
check; no result computed under the amendment-1 check is interpreted.

WHY THIS IS AN AMENDMENT AND NOT A NEW LOCK: states, thresholds,
rules, and interpretations untouched; only the arithmetic by which
bar (ii) is evaluated changes, and in the direction of a STRICTER,
storage-independent verification.

## AMENDMENT 3 (2026-08-22, recorded before any rule application)

WHAT WAS FOUND: the amendment-2 f64-FD true-operator check FAILED at
S2/Jfree at 11.96% -- the same magnitude as the amendment-1 failure,
so the original noise diagnosis was WRONG and the mismatch is real.
The measured ||J_true v_eff|| = 1.171e-3 equals the THIRD above-floor
sigma: the float32-stored factorization's bottom VECTOR at S2/Jfree
is mixed with a neighboring singular direction. Mechanism: vector
rotation under a store perturbation scales as ||dJ|| / gap, and at
S2/Jfree the gap between sigma_eff (1.046e-3) and the 118-dim
cluster edge (9.6e-4) is ~8%; where gaps are comfortable (J at all
states, Jfree at S0/S1) the same check passes at 0.18-0.37%.
INSTRUMENT LESSON KEPT: float32-J VALUES are sound at the bottom;
float32-J VECTORS are not trustworthy at small gaps. (This does not
touch the solver's use of the f32 J, whose steps are accepted by an
f64 residual test.)

WHAT CHANGES (measurement arithmetic only; states, thresholds,
rules, the f64-FD arbiter and its 5% threshold all unchanged):
  1. 96 x 36 states are measured in FLOAT64 via the normal matrix:
     J built f64 (T.jac dtype=float64, ~0.9 GB, affordable at
     n = 10370 -- the f32 choice was inherited from the 112 x 42
     memory constraint, which does not bind here), JtJ accumulated
     by blocked dsyrk, J freed, and the bottom eigenpairs taken with
     scipy.linalg.eigh subset (syevr). sigma = sqrt(eig). At the
     bottom the normal matrix CONDITIONS VECTORS BETTER, not worse:
     absolute eigengaps ~1e-7 against a backward error ~1e-10 give
     rotations ~1e-3 even at the pinched S2 gap. smax by power
     iteration on JtJ. k0, cluster range, sigma_eff, and the
     ten-above-floor all read from the subset (extended if the
     cluster approaches the subset edge).
  2. The amendment-2 f64-FD true-operator check REMAINS THE ARBITER
     for (sigma_eff, v_eff) and for the cluster sample, threshold 5%
     unchanged. If the f64 vectors fail it, the halt stands and the
     instrument is declared unfit at that state.
  3. S4 (112 x 42) stays values-only as registered: JtJ accumulated
     in f64 from a blocked f32 J (the gn_exact_f32j precision
     argument), eigenVALUES only from the subset; no vector claims
     at S4.
All states re-measured from a wiped checkpoint; nothing computed
under amendments 1-2 is interpreted, though their logs are kept.

## IMPLEMENTATION NOTE (2026-08-22, after the first rules-stage halt)

The rules block halted on "cluster anatomy does not certify
structural nulls": it was still coded against the AMENDMENT-1
anatomy heuristic (dominant th/pt mode index >= NS/2 - 1), which
reads pt_mode (46, -4) at S0 and misses the cutoff by one index even
though the vector is ~70-80% T-block at near-Nyquist s-modes.
Amendment 2 item 2 already superseded that heuristic with the
operator-level certification -- ||J_true v_cluster|| below the floor
by f64 finite difference of wres -- which is stricter, objective,
and PASSED at every vector state and both matrices (5.2-6.9e-5
against floors ~1.0-1.2e-3). The rules block is brought into line
with the amended bars: certification = cluster_true < floor at all
vector states. No bar, threshold, or rule changes; the anatomy
readings stay on the record. This failure mode was predicted and the
repair path stated in the session record BEFORE the halt fired.



