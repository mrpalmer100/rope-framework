# ROPE-MODE-004 results — a candidate low-mode fingerprint appears, but the full convergence gate fails

ROPE-MODE-004 asked whether the certified Hopf-linked rope leaves a spectral effect that cannot be explained merely by adding the same amount of tubular potential in an unlinked or spherically averaged arrangement.

## Setup

The certified ELEC-009 linked geometry was held fixed. A second control was constructed by translating one component without changing either component's shape or length until its Gauss linking number was numerically zero. A third control used the spherical radial average of the linked tubular profile, normalized to the same integrated perturbation strength.

The surrounding field Hamiltonian used a softened central attraction plus the selected rope control. The calculation kept the grid spacing fixed at `h = 0.25` while increasing the box half-width from `3.0` to `4.0`, so the comparison tests finite-volume rather than resolution effects.

- linked reference: `d_min = 0.06195531`, `Lk = -1.00225398`
- unlinked control: `Lk = -0.00000010`
- central coupling: `alpha = 12.0`
- central softening: `epsilon = 0.30`
- rope coupling: `beta = 0.50`
- tube width: `sigma = 0.16`
- grids: `23^3` and `31^3`

## Measurable low-mode signal

The rope perturbation was numerically measurable. On the larger box, the linked rope shifted the first three excited gaps relative to rope-off by approximately:

- mode 1: `+0.10320`
- mode 2: `+0.11915`
- mode 3: `+0.13572`

The corresponding linked-minus-unlinked contrasts were:

- mode 1: `+0.03540`
- mode 2: `+0.01538`
- mode 3: `+0.02121`

For those three modes, the contrast exceeded three times the estimated finite-domain uncertainty. The sign and approximate magnitude also survived the box enlargement. These modes were tightly localized on the larger box: their outer-shell probabilities were approximately `5.7e-5` to `6.0e-5` for the linked case.

The spherical control is also informative. It produced an unsplit shift of about `0.11915` across the first triplet. The linked geometry instead produced three distinct shifts around that value. This indicates that anisotropic rope geometry splits an otherwise degenerate low multiplet. The present control does not yet prove that the splitting is uniquely caused by *linking topology*, because the matched unlinked geometry differs spatially as well as topologically.

## Failed full-spectrum gates

The preregistered benchmark reported the first twelve modes, and the higher modes were not sufficiently isolated from the finite boundary.

- maximum outer-shell probability on the larger box: `0.135819`
- worst relative excitation-gap drift from box 3 to box 4: `0.0619842`

Therefore:

- topology controls certified: **PASS**
- all reported modes bound by the boundary-leakage gate: **FAIL**
- all reported gaps domain-converged: **FAIL**
- rope perturbation measurable: **PASS**
- linked-unlinked contrast above numerical uncertainty: **PASS**
- contrast stable across domains: **PASS**

## Finding

**`NO_CONVERGED_TOPOLOGY_SPECIFIC_FINGERPRINT`**

The calculation provides evidence for a **candidate low-mode geometry/topology-sensitive fingerprint**, especially in the first triplet, but it does not yet establish a converged topology-specific fingerprint across the preregistered spectrum.

The decisive next test should focus on the first four bound states, enlarge the domain to at least half-width `5`, and replace the translated unlinked control with an isospectral-geometry or topology-surgery control that more closely matches the linked rope's radial and angular density. This is necessary to separate genuine linking-number dependence from ordinary anisotropic geometry.
