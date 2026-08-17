# Release Notes -- v3.26.55 (16 Aug 2026): CI Fix -- EM-RECON-034 Benchmark

Benchmark-only. The 2D profile closure benchmark timed out on GitHub
CI (300 s). Replaced its scalar adaptive integrator with kink-aligned
Gauss-Legendre quadrature -- equivalence established against the
original integrator BEFORE the rewrite (<= 5e-5 on d0 at both window
edges), every registered number reproduced (bottom edge 1.6975),
runtime 2.5 s. Performance-only; no physics, no claims touched.
