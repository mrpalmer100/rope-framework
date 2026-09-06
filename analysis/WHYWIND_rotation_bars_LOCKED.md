# WHY-WINDING BRICK 2a -- MODE-RESOLVED SECTOR ROTATION: CHARTER
# (LOCKED 2026-08-28, before any kappa is computed)
# Authorized by the author 2026-08-28 (option (a) chosen from the
# brick-2 F-INSTRUMENT ledger). Supersedes the annihilated brick-2
# statistic; everything else inherited from
# analysis/WHYWIND_coupling_bars_LOCKED.md unchanged:
# objects (2c retained states, read-only), alignment (profile point i
# = arc pair states[i+1], states[i+2]), lines under test, collapse
# span, scope (4/3 vs 5/3; 3/2 out), no-salvage rule.

## THE LOCKED STATISTIC
For tangent t_i = (x_{i+2} - x_{i+1}) / ||x_{i+2} - x_{i+1}||:
    kappa_i(n, m) = RMS over quadratures of |< v(n, m; pt), t_i >|
with v the unit-norm cos/sin pattern in the pt sector as defined in
the brick-2 charter (def. 3, unchanged). No FD, no operator: this is
the state-space content of the branch's own motion on the resonant
winding pattern -- FND-152's f_dir sharpened to per-mode resolution.
NOTE the identity: sum over a complete pt-sector mode basis of
kappa^2 = f_dir-type pt share of the tangent; kappa_i(n, m) is that
share's (n, m) component. The registered f_dir provides the display
cross-check (display only, not verdict-bearing).

## LOCKED VERDICT LINES (identical structure to brick 2)
  R1  CONTRAST: median over the collapse span (last 8 profile
      tangents) of kappa(4/3; (2,6)) >= 10 x median
      kappa(5/3; max of (2,9), (3,12)).
  R2  WITHIN-CELL CONTROL: median kappa(4/3; (2,6)) >= 5 x median
      kappa(4/3; (2,7)) over the same span.
  R3  CO-MOVEMENT: Pearson r between kappa_i(4/3; (2,6)) and
      registered f_dir_i over the full profile >= 0.7; AND on 5/3
      (its 1:1 max vs its f_dir) r < 0.5 OR kappa range < 0.2 x the
      4/3 kappa range.
  SEL-CONFIRMED iff R1 and R2 and R3; any miss: SEL-OPEN, kept.
  No salvage; no post-hoc lines; th-sector and full-spectrum
  displays carry no verdict.

## COST
Inner products only; seconds. Grants reserved to the author.
