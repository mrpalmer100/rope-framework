# ROPE-MODE-007 results — repeated surgeries do not isolate the linking number

ROPE-MODE-007 repeated the ROPE-MODE-006 unlinking test with six independent local surgeries. The family varied the surgery location, which strand moved, whether displacement was split across both strands, Gaussian width, and a transverse directional tilt. The same surrounding three-dimensional scalar-field Hamiltonian and first-four-state bound-spectrum calculation were retained.

## Surgery family

All six deformations changed the reference linking number from `-1.00225398` to numerical zero while maintaining minimum separation at or above `0.060`. The family spanned:

- center and offset surgery locations;
- motion of strand A, strand B, or both strands;
- narrow, intermediate, and broad local windows;
- untilted and tilted displacement directions;
- local curvature changes from approximately `1.22` to `10.52` in the benchmark's discrete curvature metric.

RMS displacements ranged from `0.0233` to `0.0372`. Total-length changes remained below `1.33%`, radial second-moment changes below `3%`, and normalized quadrupole changes below `2.65%`.

## Numerical controls

The spectra were recomputed at fixed spacing `h = 0.25` on box half-widths 4 and 5.

- maximum outer-shell probability: `4.52e-5`;
- worst relative excitation-gap domain drift: `9.63e-5`;
- all six surgery contrasts were stable under domain enlargement.

The measured differences are therefore not attributable to boundary leakage or finite-volume drift at the tested resolution.

## Spectral result

A nonzero linked-minus-unlinked shift was common, but its sign was not universal.

| Excited mode | Significant in surgeries | Same-sign majority | Contrast range |
|---:|---:|---:|---:|
| 1 | 6 / 6 | 5 / 6 | `-7.86e-4` to `+2.36e-3` |
| 2 | 5 / 6 | 5 / 6 | `-9.86e-4` to `+1.30e-3` |
| 3 | 5 / 6 | 5 / 6 | `-1.66e-3` to `+7.82e-4` |

The `center_B_narrow` surgery reversed the sign of all three contrasts relative to the five-surgery majority. A second center surgery that moved the other strand with a wider, tilted deformation produced the largest positive shifts. Thus the spectral response depends materially on the detailed local deformation, even though all controls have the same unlinked status.

The largest absolute Pearson correlation between a tested nuisance metric and a mode contrast was `0.848`, associated with low-order geometry measures. With only six surgeries, this cannot establish which nuisance variable is causal, but it is too large to claim independence from geometry.

## Locked bars

- topology and geometry controls: **PASS**
- boundary leakage: **PASS**
- domain convergence: **PASS**
- universal sign consistency: **FAIL**
- significance consistency: **PASS**
- domain stability: **PASS**
- weak nuisance correlations: **FAIL**

## Finding

**`REPEATED_SURGERIES_DO_NOT_ISOLATE_LINKING_NUMBER`**

The repeated experiments strengthen one limited statement: local topology-changing surgeries usually leave a measurable, converged low-mode spectral change in this Hamiltonian. They do not support the stronger statement that the shift is determined by linked versus unlinked status alone. The sign and magnitude vary with surgery details, and the tested geometric nuisance measures remain strongly correlated with parts of the response.

The most defensible interpretation is therefore:

> ROPE-MODE-006 detected a topology-sensitive candidate fingerprint, but ROPE-MODE-007 shows that the current scalar tubular potential does not yet separate the integer linking invariant from local geometric changes introduced by unlinking.

A decisive next test should use an isospectral-control strategy or a continuous constrained geometry-matching optimization that minimizes differences in the full tubular potential, curvature distribution, and low multipole moments while producing several linked and unlinked ensembles. Classification should then be performed blind to topology, using held-out geometries, rather than comparing one linked reference against hand-designed surgeries.
