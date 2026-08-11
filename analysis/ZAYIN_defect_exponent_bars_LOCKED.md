# Commission ZAYIN -- the defect-exponent computation: locked bars

*Locked 2026-08-11, before any cell of the candidate table is
evaluated. This is VAV's rank-1 next brick: run the registered
defect-log machinery on the winding's energetics and test the target
exponent BLIND. The bar can be missed; a miss registers Failed-and-kept
per the V-A/GRV-096 precedent, and no scan follows.*

## The mechanism hypothesis, pre-named

The winding is a defect of the registered defect theory (E = pi K
ln(R/a_eff) + E_core, cutoff a_eff = 0.18 a and E_core = 5.448 K both
DERIVED in benchmarks/micromech/defect_cores.py). The candidate
g-mechanism: the source length is the radius at which the defect's
accumulated logarithmic energy equals a REGISTERED per-defect energy
budget B:

    g = a_eff/a x exp((B - E_core)/coef)   [cutoff convention]
    g = exp(B/coef)                        [bare convention]

with coef the registered logarithm coefficient for the defect type.

## The complete candidate table, pre-committed (no cell added later)

Budgets B (registered, non-circular -- anything containing l_q, g, A,
or hbar-through-l_q is CIRCULAR and excluded by rule):
- B1: m_e c^2 = 2 L J = 2 pi J (the defect IS the electron; VAV's
  identity)
- B2: J = T0 a/2 (the per-link locking energy, ETA)
- B3: E_core = 5.448 K (the core's own derived constant)

Coefficients (registered forms, defect-theory claims):
- K1: pi K (single 2D vortex)
- K2: 2 pi K (vortex-antivortex pair)
- K3: pi^2 K (3D line tension pi K per unit length x ropelength
  L = pi cells)

Stiffness identification: K = J (the lattice XY bond coupling is the
locking energy per link, the registered model). Table: 3 x 3 = 9
cells, all evaluated, all displayed.

## The bar, pre-committed

- HIT: any cell's exponent x = B/coef lands in [4.41, 4.68] (bare) or
  the cutoff-corrected requirement [6.13, 6.40]. A hit's precise value
  additionally SELECTS the kappa_pack reading (the bracket edges are
  the 50 and 250 readings) and predicts kappa_pack via the FND-042
  inversion; that prediction must land in [50, 250] for the hit to
  stand.
- MISS: no cell lands. The energy-budget defect-log class is EXCLUDED
  as the g-mechanism; register Failed-and-kept; compute and register
  the INVERTED DEMAND (what budget the mechanism would need, in units
  of m_e c^2 and of K) per the MATTER046 demand-grammar, as the
  specification any future rescue must meet blind.
- Look-elsewhere stated either way: 9 cells against a bar of total
  log-width ~0.5 across a candidate range ~1.5 decades; the chance
  rate is computed and displayed.

## Honesty clauses

1. No cell may be added, reweighted, or reinterpreted after any number
   is seen. The circularity rule is adjudicated per cell on the face.
2. No O(1) rescue: polarizations, degeneracy, or convention factors
   argued after the fact are refused by name (MATTER056 precedent).
3. A miss is not softened: "close in log space" is not a grade.
4. BKT-class screening lengths are out of scope: they require a
   temperature the vacuum sector does not register (noted, not
   evaluated).
5. One evaluation pass; the benchmark computes every cell in one run.
