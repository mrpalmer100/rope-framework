# SPARSE-J SPIKE RESULTS (S1-S3 of the locked charter; 2026-08-29)
# Executed under analysis/SPARSEJ_charter_LOCKED.md. Engineering
# measurements only; adjudicates nothing. Ships in the NEXT release.

## S1 -- MEASURED DEPENDENCY PATTERN (real retained 144x36 member,
## qsweep_stage2c_ckpt.pkl, read-only)

The field-residual pattern from the corpus's OWN existing sparse
machinery (G.groups(), already used by truestate_stage2.gamma_solve):
  shape (20736, 20739); nnz 539,136; nnz/row 16-34, median 27.
Stencil decoded (offset analysis, node = s*NP + phi):
  s: +-1..+-4 (9-point), phi: +-1..+-2 (5-point), 4 dof/node.
THREE DENSE BORDER COLUMNS confirmed (20736..20738; column nnz
20736 / 10368 / 15552): the global parameters couple to every row.
These are the Woodbury border of charter D4 -- the border is
COLUMNS as well as pin rows.

## S2 -- COLORING COUNT

69 groups: one sparse Jacobian assembly costs 69 residual sweeps
vs 15,554 dense column probes (225x fewer evaluations).

## S3 -- FACTORIZATION FILL AND MEMORY (synthetic values on the
## TRUE pattern per the charter's fill-only allowance; core =
## local columns, border split off)

Ordering ladder, all measured on the core normal matrix
(f64, SymmetricMode, diag_pivot_thresh = 0):
  144x36  COLAMD (scipy default)      670 MB fill   RSS 2.0 GB
  144x36  MMD_AT_PLUS_A               OOM-killed (with the dense
          border columns left in: the first, failed attempt)
  144x36  RCM + NATURAL               646 MB        RSS 2.0 GB
          (bandwidth 2427; the periodic wrap defeats RCM)
  144x36  hand ND, J-halfwidths       844-904 MB    (BUG, kept:
          separators sized to J's stencil do not separate the
          NORMAL matrix's graph -- N doubles the halfwidths)
  144x36  hand ND, N-halfwidths(8,4)  547 MB        RSS 1.7 GB
  144x54  hand ND, N-halfwidths       1068 MB       RSS 3.1 GB
  144x36  METIS ND (pymetis)          366 MB        RSS 1.2 GB
  144x54  METIS ND (pymetis)        ** 736 MB       RSS 2.29 GB **

HEADLINE: the 144x54 core factorization fits this container class
at 2.29 GB peak -- under the charter's C4 bar (3.0 GB for a full
round) with ~0.7 GB of daylight for the colored-FD sweeps and
solver state. The dense instrument's normal matrix ALONE at the
same grid is 4.3 GB. 144x72 extrapolates to ~3.2 GB peak:
borderline, unpromised.

## INSTRUMENT LEDGER (faults found in the spike, kept)
1. Dense-column poisoning: factoring with the 3 global columns in
   the sparse core explodes fill (first OOM). Border them.
2. Separator-width bug: ND separators must be sized to the normal
   matrix's doubled stencil (s: 8, phi: 4), not the Jacobian's.
3. SuperLU partial pivoting destroys a supplied ordering; the
   no-pivot symmetric mode (ridge-stabilized) is required. The
   ridge is spike scaffolding only -- the real instrument's
   damping (lam) plays this role natively in the LM normal
   equations.

## NEW DEPENDENCY
pymetis (pip). To be added to requirements with a note at the
instrument site.

## STANDING
Charter bars C1-C5 untouched and unrun: construction and
credential are the commission's next work. Grants reserved to the
author. Failures kept.
