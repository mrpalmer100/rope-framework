# BRICK 2 -- RESONANT COUPLING MATRIX ELEMENTS (CHARTER, LOCKED
# 2026-09-01; authorized by the author: "let's now charter brick 2")

## Question
Does the resonant COUPLING STRENGTH -- not line geometry -- order
the four cells' verdicts? (The registered dispersion doc's brick-2
proposal; the sole surviving mechanism after the re-pricing.)

## Locked definition (fixed before any number is computed)
For each cell, at its DEEPEST GATED 144x36 member x*:
  M(cell) = max over the nearest-line mode pair of
            |v^T J(x*) t| / (||v|| ||J(x*) t||)
where J(x*) is the credentialed instrument's f64 Jacobian at x*,
t is the branch tangent at x* (deep-pair difference, normalized),
and v ranges over the two real Fourier vectors (cos, sin) of the
pt-sector mode with phi-winding n and s-harmonic m of the cell's
nearest lattice line at the REGISTERED anchor (3/2: n=4,m=8;
4/3: n=2,m=6; 5/3: n=3,m=12; 5/4: n=4,m=10). M is the fraction of
the linearized response along the branch that projects onto the
resonant mode -- dimensionless, in [0,1].
Also computed, same formula, for each cell's nearest j=n line mode
where different (5/3: n=6 pair; 5/4: n=2 pair) -- reported, not
scored.

## Locked scoring (rank-based; no thresholds)
n(B2) = does M rank the FLAT cell (5/3) LOWEST of the four?
Separation s = min(M collapse cells) / M(5/3).

## Verdict forms (LOCKED)
B2-CONFIRM: flat lowest AND s >= 3   -> coupling suppression is the
  mechanism; successor interpretation claim drafted for grant.
B2-PARTIAL: flat lowest AND s < 3    -> right ordering, weak
  separation; rider only; 54-grid replication prioritized.
B2-REFUTE:  flat not lowest          -> the last line-based
  mechanism falls; the mechanism question returns to open; the
  54-grid profile replication becomes the standing experiment.
B2-OPEN: any M ill-conditioned (||J t|| ~ 0) -- recorded, no force.

## Inputs (all registered/gated; no new solves)
Deepest members: 3/2, 4/3, 5/3 from the registered stage-2 ckpts;
5/4 = profile s11 (with s10 for t). Tangents from each cell's
registered deep pair. J via the SJ-CREDENTIALED instrument's
pattern machinery at each cell's own (grid, mode, n2) key.

## Deliverables
The M table (one script, logged), verdict per the forms, drafts
for grant, analysis/BRICK2_results.md.

## AMENDMENT A1 (pre-computation, 2026-09-01): the 3/2 deep pair is
not present in this release's analysis stores (predates the export;
only SVD diagnostics survive). B2 computes on the three cells with
registered gated states here (4/3, 5/3, 5/4); the rank test reads
"flat lowest of the available cells," separation over the available
collapse cells. The 3/2 entry is a pure later addition under the
same locked formula if the author supplies an earlier archive.
Implementation note, fixed now: v ranges over the four real vectors
(cos/sin x both winding signs) of the (m, n) mode; M takes the max.

## AMENDMENT A2 (pre-verdict, 2026-09-01, disclosed): the A1/v1
definition (raw-Fourier projection of the pt-sector Jacobian
response) is structurally null -- M(4/3) = 0.0000 with the response
living on carrier sidebands (m ~ 33-42, n = 1-3; diagnostic logged)
-- raw Fourier is the wrong basis for a carrier-mediated coupling
(drafter's physics error, caught by the zero; no cross-cell
comparison existed). Superseding definition, in the theory's OWN
mode convention (q1 modes()): with w(x) the physical field from
geom(), Dw = w(deep) - w(prev) over the registered deep pair,
  M = max over winding sign of |<e_line, Dw>| / (||e_line|| ||Dw||)
  e_line[s,p] = exp(-i K_line s) exp(+/- i n phi),
  K_line = m_line * 2pi / LCELL.
Calibration anchor computed alongside: the same quantity for the
cell's level-2 mode (E2s, one phi winding) -- expected large.
Scoring and verdict forms unchanged.
