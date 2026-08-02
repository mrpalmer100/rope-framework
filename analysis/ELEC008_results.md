# ELEC-008 results — adaptive direct periodic-spline representation

## Executed change

ELEC-008 replaced the global K=8 Fourier chart with direct periodic cubic-spline control points. The run began with 16 controls per component, performed four certified constrained descent steps, adaptively redistributed/refined to 20 controls using a monitor based on local curvature and inter-strand proximity, and performed four further steps. The Poisson curve-field physical energy was unchanged. Every proposed path retained hard 128-point separation/linking checks, and accepted endpoints were certified at 128/256/512 points.

## Observed numbers

- Initial physical energy: `16.162510362`
- Energy before remesh, after four 16-control steps: `16.153451059`
- Energy immediately after 16→20 remesh: `16.248388289`
- Relative remesh energy jump: `0.005877` (0.588%)
- Final physical energy: `16.228949267`
- Accepted constrained steps: `8`
- Final RMS radius: `0.614388`
- Final minimum separation: `0.06407244`
- Final 512-point linking estimate: `-1.00271866`
- Final projected physical-gradient / energy: `0.1452795`

## Locked-bar adjudication

- B1 final multiresolution topology certificate: **PASS**
- B2 final physical energy below campaign start: **FAIL**
- B3 every accepted state certified: **PASS**
- B4 remeshing topology/energy fidelity: **PASS**
- B5 at least eight accepted steps: **PASS**
- B6 projected stationarity below 0.05: **FAIL**

## Finding

`ADAPTIVE_DIRECT_METHOD_FAILED`

The direct representation itself supports topology-certified descent within each fixed mesh stage. However, the adaptive 16→20 control-point remesh changes the discretized physical energy enough that the final campaign energy is above the original 16-control start, even though the remesh jump remains below the preregistered 1.5% fidelity limit. More importantly, the final projected residual is `0.1453`, almost three times the stationarity ceiling.

This run therefore does **not** establish a representation-independent constrained stationary linked soliton. It also exposes a new numerical debt: remeshing is topology-safe but not sufficiently energy-neutral for cross-mesh energy comparisons at the present spline interpolation and 64-sample energy quadrature. A stronger next test should use nonuniform periodic knots or a variational spline projection chosen to minimize geometric/energy mismatch during remeshing, followed by mesh-converged energy quadrature. No new stabilizing physics should be added until that discretization debt is resolved.
