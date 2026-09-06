# SPARSE-J COMMISSION -- MID-COMMISSION CHECKPOINT (2026-08-29)
# Under analysis/SPARSEJ_charter_LOCKED.md. Construction begun,
# C1 PASSED, three further instrument faults found in daylight, the
# solver design corrected by measurement. C2-C5 NOT RUN. Nothing
# adjudicated. Ships in the next release.

## CREDENTIAL STATUS

C1 OPERATOR IDENTITY: ** PASS ** (at the retained 144x36 member,
qsweep_stage2c states[1], A2 = 0.0046979 reproduced exactly by the
geom-route mode extraction; wres at member 9.1e-8):
  C1a: 64 random columns, colored-sparse vs direct single-column
       FD: max deviation 0.00e+00 (bit-identical -- the coloring
       is conflict-free on the measured pattern).
  C1b: 16 random unit vectors, J@v vs the dense f32 reference
       jac: max deviation 6.56e-07 vs the 5e-6 bar.
C2 ANCHOR: ** PASS ** (second half of the session, after the
BandedTorusSolver build below). From the retained member perturbed
by 1e-4 rel Gaussian noise (seed 2026), gn_sparse re-converged to
the SAME member in 10 rounds, every step accepted at fraction 1.0:
RMS 3.21e-10 (bar 1e-9); |dA2|/A2 = 1.46e-10 and |dom2|/om2 =
1.48e-07 (bars 1e-6). 11.8 min, peak RSS 2.22 GB. The first exact
f64 Newton step removed 99.91 pct of the perturbation in ONE round
(fieldRMS 7.5e-3 -> 6.6e-6) -- the snap the f32 route could not
produce.
SOLVER VERIFICATION (runbook step 1, both passed before C2):
  48x12 torus vs dense reference: rel error 3.26e-11 (bar 1e-10).
  144x36 real member, matvec residual of the damped normal solve:
  7.74e-13; factor 61 s (Python band-scatter loop -- an
  optimization candidate, annotated), solve 0.05 s, k = 41 dense
  rows, RSS 1.75 GB.
C3 (rates), C4 (144x54 memory), C5 (final annotation audit):
** ALL PASSED ** in the C3-C5 session -- see
analysis/SPARSEJ_credential_results.md (verdict SJ-CREDENTIALED;
faults 7-9 found and fixed in that march). Original runbook note (C3 needs the stage-2c
arc-step machinery replicated; do not shortcut it with re-solves).

## INSTRUMENT LEDGER (faults 4-6, continuing the spike's 1-3)

4. CHART-PATTERN MISMATCH (invalidates spike S3's fill numbers as
   a design basis): the spike's 27-nnz/row pattern came from
   G.groups()/field_residual on the 4N+3 chart. The MARCHING
   chart's wres, measured column-by-column, has 10,370 wide
   columns (~1,400-2,200 rows each; pattern nnz 18.9M). Lesson:
   measure the pattern of the residual you will actually solve.
5. THE s-DIRECTION IS SPECTRAL: probing shows W-block and Z-block
   columns couple to ALL 144 s-points at phi +-2 (144 distinct
   s-offsets), while the T block is a pure local stencil
   (s +-2, single phi). The Jacobian is block-sparse with dense
   s-lines, phi-local. (This also retroactively explains why the
   dense instrument was dense: it is not merely a memory diet.)
6. GENERIC-SPARSE NORMAL MATRIX OOM: N = J^T J on the true
   pattern has 149M nnz; forming it generically hit 3.79 GB and
   was reaped before factorization. N must never be formed as a
   global sparse matrix on this chart.

## CORRECTED EXACT-SOLVE DESIGN (daylight amendment to charter D4;
## stricter in that it forbids the global-N formation fault 6
## measured)

phi-major BLOCK-BANDED TORUS SOLVE, f64, exact:
- Variable order: slices p = 0..NP-1, each slice = [W(:,p),
  Z(:,p), T(:,p)] (3*NS vars), globals last.
- N is assembled DIRECTLY INTO banded/block storage, slice-pair
  by slice-pair: for |p_i - p_j| <= 4 (the N-graph phi halfwidth),
  N_block(i,j) = J[:,slice_i]^T @ J[:,slice_j] as a small dense
  (3*NS x 3*NS) product. Never form global N.
- Half-bandwidth ~ 4 slices + within-slice ~ (4+1)*3*NS; banded
  f64 storage ~ 540 MB at 144x36, ~ 810 MB at 144x54 (phi-major
  bandwidth does NOT grow with NP -- the route improves at the
  larger grid).
- Periodic phi wrap: the last 4 slices are the BORDER (bordered
  banded solve: factor the 32-slice core banded, dense Schur on
  the 4*3*NS border, Woodbury for pins/globals as before).
- Marquardt damping enters the block diagonal at assembly (the
  instrument's lam*d2, no scaffolding ridge).
- Estimated per-factor cost at 144x36: ~1-2 min (border
  backsolves dominate); acceptance-ladder retries reuse the
  factor across fractions as the registered solver does.

## WHAT IS BUILT AND SHIPS WITH THIS CHECKPOINT

- benchmarks/foundations/sparsej_instrument.py: pattern builder
  (empirical, per-grid, cached), conflict-free greedy coloring,
  SparseJac (colored FD, f64, C1-credentialed), gn_sparse (the
  gn_lean-verbatim loop with [SJ]-annotated kernel swaps), and
  the BorderedSolver SUPERSEDED by fault 6 (kept in-file,
  annotated, for the record).
- The 144x36 measured pattern + coloring cache
  (analysis/sparsej_pattern_144x36.pkl).

## RUNBOOK FOR THE NEXT SESSION (construction remainder + C2-C5)

1. Implement BandedTorusSolver per the corrected design (assembly
   slice-pair by slice-pair; scipy solveh_banded or LAPACK dpbtrf
   on the core; dense Schur border). Verify against lsmr on a
   small grid (agreement to 1e-10) before any credential run.
2. C2: perturb states[1] by 1e-4 rel Gaussian; gn_sparse to
   RMS <= 1e-9; A2/om2 within 1e-6 rel of registered.
3. C3: re-march two consecutive arc-rate points from the retained
   2c states; rates within 1 pct of the FND-147 profile.
4. C4: measured peak RSS of one full round at 144x54 <= 3.0 GB
   (pattern build at 54 is ~31k wres evals, ~1-2 min, cache it).
5. C5: confirm every fault 1-6 annotation sits at its code site.
6. Verdict per the charter's three forms; grants to the author.

## STANDING
C1 evidence is real and kept; the spike's METIS numbers remain
true OF THE OTHER CHART's pattern and are so labeled. Registry
untouched. Grants reserved to the author. Failures kept.
