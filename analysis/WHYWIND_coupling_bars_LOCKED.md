# WHY-WINDING BRICK 2 -- RESONANT COUPLING MATRIX ELEMENTS: CHARTER
# (LOCKED 2026-08-28, before any coupling number is computed)
# Authorized by the author 2026-08-28 ("let's charter brick 2").
# Predecessor: WHYWIND_dispersion (RES-OPEN, failure kept). Under test:
# the j = n selection rule -- the leading refinement noted, not
# granted, in WHYWIND_dispersion_results.md.

## THE QUESTION
Brick 1 showed proximity cannot discriminate: q = 5/3 sits CLOSER to
its 1:1 line than q = 3/2 sits to its firing line, yet stays flat. The
refined hypothesis: the resonant COUPLING is large on j = n
(self-degenerate) lines and suppressed on j != n lines. Brick 2
measures the coupling directly on the retained states.

## OBJECTS (all pre-existing; nothing re-solved)
- States: analysis/qsweep_stage2c_ckpt.pkl, prof-4/3 and prof-5/3,
  14 retained full-bar states each (credentialed this session: gates
  reproduce on load). The 3/2 cell is OUT OF SCOPE (no retained
  profile states); the chartered contrast is the FND-152/153 pair.
- Instrument: QTGrid(144, 36, N1, N2) and its residual F(x) exactly
  as in benchmarks/foundations/qsweep_stage1.py. No operator changes.

## LOCKED DEFINITIONS
1. Branch tangent at retained state i: t_i = (x_{i+1} - x_i) /
   ||x_{i+1} - x_i||, consecutive retained states in A2 order.
2. Directional derivative J(x_i) t_i by CENTRAL finite difference,
   step h = 1e-6 * (1 + ||x_i||_inf), on the full residual F.
3. Probe vector v(n, m; sector, quadrature): the field pattern
   cos/sin(n * pgrid + 2 pi m * sgrid / LCELL) placed in ONE sector
   of the state layout (pt = winding sector primary; th recorded as
   display only), zeros elsewhere, normalized to unit 2-norm. Both
   quadratures computed; a line's coupling uses their RMS.
4. NORMALIZED COUPLING at state i to line (n, m):
       kappa_i(n, m) = RMS_quadratures |< v(n,m; pt), J(x_i) t_i >|
                        / || J(x_i) t_i ||
   -- the fraction of the branch's linear response landing on the
   resonant winding pattern. Dimensionless, in [0, 1].
5. Lines under test (from the brick-1 lattice, fixed here):
   - q = 4/3 FIRING line (j = n class):      (n=2, m=6)   [Om1/2]
   - q = 4/3 off-resonant control:           (n=2, m=7)   [non-harmonic k]
   - q = 5/3 1:1 routes (j != n class):      (n=2, m=9) and (n=3, m=12);
     a cell's 1:1 coupling is the MAX of its two routes.
   - q = 5/3 off-resonant control:           (n=2, m=10)
6. Collapse span: profile points 5-12 of the 4/3 profile (the cliff
   and after, per the registered stage-2c table) and the
   amplitude-matched points of the 5/3 profile.

## LOCKED VERDICT LINES (all three required for SEL-CONFIRMED)
  R1  CONTRAST: median over the collapse span of
      kappa(4/3; (2,6))  >=  10 x  median kappa(5/3; 1:1 max).
  R2  WITHIN-CELL CONTROL: median kappa(4/3; (2,6))
      >=  5 x  median kappa(4/3; (2,7)).
      (Guards against "everything couples to everything".)
  R3  CO-MOVEMENT: Pearson r between kappa_i(4/3; (2,6)) and the
      registered f_dir_i over the full 4/3 profile >= 0.7; AND the
      same statistic on 5/3 (its 1:1 max vs its f_dir) < 0.5 OR its
      kappa range < 0.2 x the 4/3 kappa range.
  Any miss: SEL-OPEN, registered, kept. No salvage clause; no
  post-hoc line additions. th-sector displays carry no verdict.

## COST AND EXECUTION
Two residual evaluations per tangent (central FD) plus inner
products: ~26 evaluations per cell, minutes at n = 15554. Runs
in-session on the author's go. Deliverables: results doc with the
full kappa tables, verdict block mechanical, draft registration
AWAITING THE AUTHOR; state untouched (read-only on the ckpt).

Grants reserved to the author. Failures kept.
