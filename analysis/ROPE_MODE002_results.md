# ROPE-MODE-002 results — a central field does not generate atomic multiplets

## Question

Does adding a softened central attraction to standing waves on the certified linked rope reorganize the ordinary closed-string spectrum into robust `s`, `p`, and `d` orbital families?

## Computation actually performed

The unchanged ELEC-009 certified geometry was sampled at 128, 256, and 512 points per component. On each closed component, the benchmark solved the generalized finite-element eigenproblem for the one-dimensional rope Laplacian plus

`V(r) = -alpha / sqrt(r^2 + eps^2)`,

using `alpha = 0, 0.1, 0.3, 1, 3, 10` and fixed `eps = 0.09289362`. The first 18 eigenpairs were computed. Each eigenvector was projected, using the finite-element mass inner product, onto sampled real spherical-harmonic subspaces with `l=0,1,2`.

## Results

- The linked reference remained certified: `d_min = 0.06195531`, `Lk512 = -1.00225398`.
- The spectrum was numerically converged: the worst 256→512 relative eigenvalue change over the coupling sweep was `0.5135%`.
- At zero coupling, the familiar one-dimensional sine/cosine pairing was recovered: cluster pattern `1,2,2,2,2` through the first nine levels.
- Nonzero central coupling generally split those pairs further, producing patterns dominated by singlets and occasional doublets, not `1,3,5` multiplets.
- No tested coupling produced `1,3,5` multiplicities on either component, much less both.
- The spherical-harmonic projections did not organize as one `l=0`, three `l=1`, and five `l=2` states. Mean projection purity remained only about `0.43–0.52`.

## Locked bars

- Certified linked reference: **PASS**
- Mesh-converged central-field spectrum: **PASS**
- `1/3/5` multiplets emerge: **FAIL**
- Multiplets classify as `s/p/d`: **FAIL**
- Structure robust across coupling sweep: **FAIL**

## Finding

**`CENTRAL_FIELD_DOES_NOT_GENERATE_ATOMIC_MULTIPLETS`**

## Interpretation

The central interaction changes and splits the one-dimensional rope spectrum, but it does not create the rotational multiplet structure of a three-dimensional central-field problem. This is consistent with the dimensionality of the tested degree of freedom: a scalar field restricted to a closed curve has one periodic coordinate, whereas atomic `s/p/d` degeneracies arise from rotational symmetry over a three-dimensional configuration space.

This is a kept negative result for the proposition that a central potential alone converts standing waves on a fixed one-dimensional rope into electron shells. It is not a test of a full dynamical rope-plus-field atom, nor a proof that every higher-dimensional rope-field construction must fail.
