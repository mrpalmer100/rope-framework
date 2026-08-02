# ROPE-MODE-006 results — a minimally matched topology-specific low-mode fingerprint is detected

ROPE-MODE-006 repeated the linked-versus-unlinked comparison using a local topology surgery rather than translating an entire rope component. The surgery changes the linking number while keeping the overall geometry, radial distribution, and anisotropy nearly unchanged.

## Setup

The certified ELEC-009 Hopf-linked geometry was used as the reference. At the closest approach, a broad periodic Gaussian displacement was applied to one component along the local inter-strand direction until the crossing passed through and the Gauss linking number became numerically zero. The accepted surgery used amplitude `0.123` and width `80/1024` of the loop parameter.

The surrounding-field Hamiltonian retained the ROPE-MODE-004 parameters:

- central coupling `alpha = 12.0`
- central softening `epsilon = 0.30`
- rope coupling `beta = 0.50`
- tube width `sigma = 0.16`
- fixed grid spacing `h = 0.25`
- box half-widths `4.0` and `5.0`
- first four eigenmodes

## Topology and geometry controls

| Quantity | Linked | Surgery control |
|---|---:|---:|
| Gauss linking number | `-1.00225398` | `-5.34e-6` |
| Minimum separation | `0.06195531` | `0.06084545` |

The surgery control remained closely matched to the linked geometry:

- RMS point displacement: `0.03004049`
- total-length change: `0.1152%`
- radial second-moment change: `0.0652%`
- normalized quadrupole change: `0.3879%`

All preregistered geometry-matching limits passed.

## Bound-state and domain convergence

On the larger box, the maximum outer-shell probability across the rope-off, linked, and surgery controls was `4.52e-5`, far below the locked `0.1%` ceiling.

The worst relative excitation-gap change between box half-widths 4 and 5 was `9.63e-5`, or approximately `0.0096%`, below the locked `1%` limit.

## Spectral contrast

All three excited states showed linked-minus-surgery gap contrasts exceeding three times the combined domain uncertainty. Their signs and magnitudes remained stable under the domain enlargement.

This result differs from ROPE-MODE-004 in an important way: the unlinked control no longer requires a large translation or a substantially different spatial arrangement. The spectral contrast survives after radial moments, quadrupole anisotropy, total length, separation, and overall shape are closely matched.

## Locked bars

- topology controls certified: **PASS**
- surgery geometry matched: **PASS**
- boundary leakage below threshold: **PASS**
- excitation gaps domain-converged: **PASS**
- linked-minus-surgery contrast significant in at least two excited modes: **PASS**
- contrast stable across domains: **PASS**

## Finding

**`MINIMALLY_MATCHED_TOPOLOGY_FINGERPRINT_DETECTED`**

Within this modeled scalar-field Hamiltonian, changing the rope from linked to unlinked by a small local surgery produces a measurable and converged shift in the first bound-state triplet, even though low-order geometric observables remain closely matched.

The result is evidence for a topology-sensitive spectral fingerprint in this numerical model. It is not yet proof that the effect depends only on the integer linking number: the local surgery necessarily changes higher-order geometric details near the crossing. The next decisive control is a family of multiple independent surgeries and shape-matched deformations, testing whether the spectral contrast tracks linking status rather than the exact surgery location or local curvature change.
