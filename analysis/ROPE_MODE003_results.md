# ROPE-MODE-003 results — 3-D angular families appear, but the finite-volume gate fails

ROPE-MODE-003 moved the scalar excitation off the one-dimensional rope and into a surrounding three-dimensional field. The certified ELEC-009 linked geometry was kept fixed and represented by an embedded tubular potential. A softened central attraction supplied bound-state structure.

## Numerical setup

- Interior Cartesian grids: `23^3` and `29^3`
- Box half-width: `3.0`
- Central coupling: `alpha = 2.0`
- Central softening: `epsilon = 0.12`
- Rope-tube width: `sigma = 0.10`
- Rope coupling sweep: `beta = 0, 0.25, 0.5, 1.0`
- Lowest 18 eigenmodes computed at each grid and coupling
- Angular character classified by projection onto radial-basis times real spherical harmonics for `l=0,1,2,3`

The linked reference remained certified with `d_min = 0.06195531` and `Lk512 = -1.00225398`.

## Main result

The low spectrum did display recognizable three-dimensional angular families. At every tested coupling, the first twelve modes were classified as

`l = [0, 1, 1, 1, 0, 2, 2, 2, 2, 2, 3, 1]`.

Thus the surrounding field produced:

- one lowest `s`-like mode,
- a three-member `p`-like family,
- another `s`-like radial mode,
- five `d`-like modes.

The cubic finite box split the five `d`-like modes into approximate `3 + 2` energy clusters rather than an exact fivefold degeneracy. Mean angular projection purity was about `0.91`, and the pattern survived rope couplings through `beta = 1.0`.

The first nine excitation gaps were numerically stable: the worst `23^3 -> 29^3` change ranged from `0.752%` at `beta=0` to `1.115%` at `beta=1`.

## Failed bar

The preregistered localization bar failed. Only about `50.9%–51.1%` of the probability of the first twelve modes lay inside radius `2.2`, versus the locked requirement of `85%`. The current box and central coupling therefore do not establish that all reported excited modes are well-isolated bound states rather than finite-box states with substantial outer support.

## Interpretation

This is a materially different result from ROPE-MODE-002. A field confined to the rope did not produce atomic angular multiplicities; a surrounding 3-D field does produce recognizable `s/p/d` families.

However, the result does **not** show that the rope causes those families. The same angular structure is already present at `beta=0`, where it follows from the central three-dimensional operator. Modest rope coupling mainly preserves the structure and causes only small spectral perturbations. The present calculation therefore supports the dimensional hypothesis—three-dimensional field degrees of freedom are sufficient for orbital-like angular families—but does not yet demonstrate a rope-specific explanation of electron shells or electron spacing.

## Finding

**`SURROUNDING_3D_FIELD_GATE_NOT_YET_PASSED`**

The next controlled test should strengthen localization and isolate the rope's causal contribution by increasing the domain and/or central confinement, then comparing rope-on and rope-off spectra using converged boundary leakage, multiplet splitting, and mode-density changes.
