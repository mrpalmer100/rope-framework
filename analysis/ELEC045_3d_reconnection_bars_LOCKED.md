# ELEC-045 — The 3D two-strand reconnection action: locked bars (before computation)

## Commission
ELEC-044's surviving cell (D = w, n_t = 111 -> 0.885 hbar) rests on an UNDERIVED
identification: that the reconnection barrier's width is the inter-strand gap w
rather than the core diameter d_c. This computation derives the barrier from the
framework's registered strand physics (tension T, wave speed exactly c, hard core
d_c, medium spacing w with weave pinning) instead of assuming a 1D cosine.

## Model (declared before running)
Two elastic strands in 3D, each pinned at both ends (weave crossings) over span
l_pin, resting separation w, energy = T x total length + hard-core exclusion at
d_c (d_c/w = 3.2e-3, registered). Reaction coordinate: constrained center-pair
separation s from w down to d_c. V(s) = E_min(s) - E_min(w) is the DERIVED
barrier profile. Effective inertia mu(s) from the constrained deformation mode's
kinetic integral with linear density T/c^2 (transverse speed exactly c, ELEC-043).
Separatrix action at threshold: W = integral_{d_c}^{w} sqrt(2 mu(s) (E_b - V(s))) ds.

## Locked bars
B1 (instrument). E_min(s) monotone decreasing in s toward rest; mesh convergence:
   N=41 vs N=81 nodes changes W by < 2%. FAIL voids everything downstream.

B2 (the analytic check). The numerical V(s) at small deflection matches the
   triangle-mode prediction V ~ 2 T (w-s)^2 / l_pin to within 20% in the
   quadratic coefficient. Anchors the numerics to known elasticity.

B3 (THE DECIDER — length independence). Run l_pin/w = 2, 4, 8 at fixed w.
   Fit W ~ l_pin^p. PASS if |p| < 0.15 (the action is set by w alone, pinning
   cancels, D = w is DERIVED). FAIL if |p| >= 0.15: the action depends on the
   embedding and no universal quantum exists at this scale — record and keep.

B4 (scale law). Run w' = 0.5w and 2w at fixed l_pin/w. PASS if W ~ w^q with
   q in [1.85, 2.15] (the T w^2/c form). FAIL kept otherwise.

B5 (the prefactor). Report kappa_3D = W / (T w^2 / c). No pass band locked —
   whatever it is, it replaces 1.80 in the ELEC-044 grid, and the D=w x n_t=111
   cell must be RE-EVALUATED at kappa_3D. If the cell moves outside a factor 3
   of hbar, the reconciliation candidate is killed by its own requested
   derivation and that verdict is filed without softening.

B6 (scope). The computation resolves the APPROACH barrier; the topology-change
   moment at contact is below the model's resolution (the core is a hard wall,
   not dynamics). The strand-crossing cost at scale d_c is an additive term
   bounded by kappa T d_c^2/c = 1e-5 x the w-scale action (negligible if B4
   holds) — state this bound explicitly in the output.

## Kill condition
B1 fail => Failed-and-kept, no downstream numbers quoted.
