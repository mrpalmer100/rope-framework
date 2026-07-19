# Benchmark catalogue

Every benchmark has a stable ID. **Papers cite the ID** (e.g. "see benchmark
G-002") instead of restating numbers, so a reader can trace any cited value to a
single regression-tested quantity. Generated from
`rope_solver.benchmark_catalogue`; regenerate with:

```bash
python -c "from rope_solver.benchmark_catalogue import print_catalogue; print_catalogue()"
```

## ID scheme (frozen as of 2.0)

| Prefix | Domain |
|---|---|
| `N-xxx` | Numerical primitives (solver, linking, tension) |
| `G-xxx` | Gravity / PPN |
| `EM-xxx` | Electromagnetism + light |
| `P-xxx` | Particles (charge, links, mass machinery) |
| `S-xxx` | Spectrum / fluctuation determinant |

Adding benchmarks in 2.x uses new IDs only. Renumbering or repurposing an
existing ID is a breaking change reserved for a major version, because papers
cite these IDs.

| ID | Benchmark | Expected | Verified by | Module |
|---|---|---|---|---|
| `N-001` | Laplacian on plane wave | ratio 0.991 | `test_validation` | `psi.solver` |
| `N-002` | psi ~ 1/r (boundary-corrected) | corr 0.99998 | `test_validation` | `psi.solver` |
| `N-003` | Brill-Lindquist harmonic | max 0.003 | `test_validation` | `psi.solver` |
| `N-004` | Tension force = -grad(length) | err 4e-10 | `test_validation` | `geometry.curve` |
| `N-005` | Stable ring knot | R*=0.86, m=12.1 M_Pl | `reproduce_results` | `psi.solver` |
| `N-006` | Hopf link sourced minimum | R*=0.84 | `reproduce_results` | `psi.solver` |
| `G-001` | Schwarzschild / PPN | gamma=beta=1 | `test_physics` | `gravity` |
| `G-002` | Mercury perihelion | 43.00 arcsec/cy | `test_physics` | `gravity` |
| `G-003` | Light deflection | 1.751 arcsec | `test_physics` | `gravity` |
| `G-004` | Nordtvedt eta | 0 | `test_physics` | `gravity` |
| `EM-001` | Maxwell chain | 4 eqs, d=3 | `test_electromagnetism` | `electromagnetism` |
| `EM-002` | EM constants (eps0, Z0, alpha) | Z0=376.7 ohm | `test_electromagnetism` | `electromagnetism` |
| `EM-003` | Charge quantization (q=Lk) | integer Lk | `test_electromagnetism` | `electromagnetism` |
| `EM-004` | Photon (Lk=0, non-dispersive) | omega=ck | `test_electromagnetism` | `electromagnetism.photon` |
| `EM-005` | Cosmic birefringence EB/EE | 0.0119 | `test_electromagnetism` | `electromagnetism.photon` |
| `EM-006` | Cross-sector locks | alpha, c, eps0 agree | `test_electromagnetism` | `electromagnetism` |
| `P-001` | Charge = linking number | q=Lk | `test_physics` | `particles` |
| `P-002` | Hopf relaxation conserves Lk | |Lk|=1,2,3 | `reproduce_results` | `relaxation` |
| `P-003` | Coupling kappa = alpha/2pi | 0.00116 | `test_physics` | `particles` |
| `P-004` | Lepton mass ratios (Koide phase) | 0.5% (CONJECTURE) | `test_physics` | `particles` |
| `P-005` | Chiral central charge | c=9/5 | `test_physics` | `particles` |
| `P-006` | Knot action O(1) / mass external | S_E=1 | `test_physics` | `particles` |
| `S-001` | Fluctuation determinant | Poschl-Teller validated | `test_physics` | `spectrum` |

**23 benchmarks.**