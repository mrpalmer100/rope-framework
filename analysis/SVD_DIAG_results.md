# SVD-DIAG results -- 2026-08-22

Bars: analysis/SVD_DIAG_bars_LOCKED.md (locked; three amendments and
one implementation note, all recorded in daylight, all in the
stricter direction). Benchmark:
benchmarks/foundations/svd_diagnostic.py. State + v_eff vectors:
analysis/svd_diag_ckpt.pkl.

## VERDICT (mechanical, from the registered rules)

RULE C: HEALTHY BOTTOM SPECTRUM. Ra2(eff) S0 1.068e-6 -> S3
1.219e-6 (drop 0.9x against the registered 10x threshold); R2(eff)
identical. The Jacobian's bottom spectrum DOES NOT explain the
eightfold dA2/ds collapse: no fold signature, no resonance approach,
no gauge degeneration anywhere on the measured branch. Per the rule
as locked, the q-sensitivity probe (external review step 2) is
PROMOTED.

## THE TRAJECTORY (f64 normal-matrix measurement, all bars passed)

  state  A2         sigma_eff(J)  eff-ratio   k0   softest direction
  S0     0.0018792  1.0199e-3     1.068e-6    115  99.98% T, (0,14)
  S1     0.0046979  1.0701e-3     1.072e-6    117  99.98% T, (0,13)
  S2     0.0063277  1.0465e-3     1.004e-6    117  96% T, near-Nyq mix
  S3     0.0094647  1.4207e-3     1.219e-6    124  95% T, mixed
  S4*    0.0093937  1.5680e-3     1.003e-6    178  (112x42, values only)

  *S4 reported for the record per the lock; cross-grid sigma
   comparisons not registered. Its eff-ratio sits at the same scale
   as every 96 x 36 state.

Jfree tracks J to four digits at every state. The branch tangent is
an exact null of the downdated free system and bar (i) measured its
projection into the near-null space at 0.99999.

## BARS RECORD

  (i)   tangent-in-null-space: PASS 0.99999 (three independent runs).
  (ii)  f64-FD true-operator check, 8 of 8 at S0-S3: 0.10-0.14%
        against the 5% halt threshold. S4: values only, no vector
        claims (registered).
  (iii) cluster certification, operator-level: ||J_true v_cluster||
        = 5.2-6.9e-5 against floors 1.0-1.2e-3 at every vector
        state and both matrices -- below-floor CERTIFIED.

## INSTRUMENT LESSONS KEPT

  1. THE CHART CARRIES STRUCTURAL NULLS: recon() projects the mean
     and s-Nyquist families, giving a genuine null cluster (k0 = 115
     at 96 x 36 scaling to 178 at 112 x 42). Raw sigma_min of this
     chart is meaningless; the effective sigma above a certified
     floor is the physical quantity. (Amendment 1.)
  2. FLOAT32-J VECTORS ARE NOT TRUSTWORTHY AT SMALL GAPS. The
     f32-stored factorization's bottom vector at S2/Jfree was mixed
     with a neighbor (gap ~8% to the cluster edge); the f64
     true-operator check caught it TWICE (11.83%, 11.96%) before
     the diagnosis was accepted -- the first diagnosis (accumulation
     noise) was WRONG and the record says so. Values were sound
     throughout. Does not touch the solver's use of f32 J, whose
     steps are accepted by an f64 residual test. (Amendments 2-3.)
  3. The f64 normal-matrix route (blocked dsyrk, dsymv power
     iteration, syevr subset, exact dsyr pin downdate) is BOTH more
     accurate and 2.5x faster than the f32 dense SVD it replaced
     (208 s vs 519 s per 96-grid state), at ~1 GB steady.
  4. Container scheduling: two further silent OOM reaps mapped and
     fixed at their sites (the 1.6 GB eigh copy at n = 14114; the
     rebind-before-free rebuild holding 3.9 GB). Detached runs
     survive tool-call boundaries but NOT long user-idle gaps;
     per-state checkpointing carried the run across four kills with
     zero lost states.

## WHAT THIS MEANS (granted as FND-146, 2026-08-22, with the author's scope-tightening amendment)

The step-3 diagnostic was built to separate a chart artifact from an
approaching singularity. It found NEITHER softening: the bottom
spectrum is flat to ~20% along the whole measured branch while
dA2/ds collapses eightfold. The W0-margin-below-one resonance
suspect takes a direct hit: nothing softens in the omega tail at any
state (om-fractions ~1e-11 or below in every measured vector). The
rate collapse is therefore a property of the branch's DIRECTION
FIELD -- how the tangent rotates away from A2 -- or of the
rationalized cell itself, not of any approaching degeneracy. That is
exactly the question Q-SWEEP was chartered to test, and RULE C
promotes its first stage, the q-sensitivity probe around 3/2.
