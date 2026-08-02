# ELEC-009 results — variational remeshing numerical gate

## Finding

**VARIATIONAL_REMESH_NUMERICAL_GATE_FAILED**

ELEC-009 implemented separate nonuniform periodic knot vectors for the two strands and a topology-certified variational remesh candidate search. The physical Poisson curve-field energy, separation floor, and linking certificates were left unchanged.

## Observed results

- Campaign start energy: `16.162510362`
- Energy immediately before the 16→20 remesh: `16.158829091`
- Energy immediately after the selected remesh: `16.245335687`
- Relative remesh energy jump: `0.00535352` (0.535352%)
- Selected smoothing parameter: `0.025`
- RMS geometry error: `0.052101`
- Hausdorff error: `0.0530855`
- Final energy after five accepted constrained steps: `16.231969041`
- Final RMS radius: `0.582224`
- Final minimum separation: `0.06195531`
- Final 512-sample linking estimate: `-1.00225398`
- Final projected-gradient / energy: `0.1508681`
- 48→64 source-quadrature relative energy difference: `0.000247783` (0.0247783%)

## Locked bars

- B1 final topology certificate: **PASS**
- B2 physical energy decreases across the campaign: **FAIL**
- B3 all accepted states certified: **PASS**
- B4 strict remesh geometry/energy fidelity: **FAIL**
- B5 source-quadrature convergence below 0.2%: **PASS**
- B6 at least five accepted steps: **PASS**
- B7 projected stationarity below 0.05: **FAIL**

## Interpretation

The source-quadrature test is already converged at the locked level, so the dominant numerical debt is not the 48-versus-64 curve-source sampling. The nonuniform-knot remesh remains topology preserving, but it is not geometry or energy neutral at the strict preregistered tolerances. Subsequent constrained descent does not recover the pre-remesh energy, and the projected residual remains large.

This result does not adjudicate whether the unchanged physical functional has a linked stationary point. It shows that the present adaptive spline transfer operator is still too disruptive to make a clean representation-independence test. The next controlled step should avoid interpolation-based remeshing entirely: optimize a fixed high-resolution direct mesh, or construct a genuine constrained closest-point/energy projection with analytic or automatic-differentiation Jacobians before changing the physical functional.
