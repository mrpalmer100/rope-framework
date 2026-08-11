# COMMISSION RESH -- RESULTS: ESCAPE-FAILS-ON-ANISOTROPY; ROUTE (b) CLOSES

*Adjudicated 2026-08-11 after bar lock
(analysis/RESH_collective_cutoff_bars_LOCKED.md). Benchmark:
benchmarks/foundations/resh_collective_cutoff.py. The escape was
constructed in its strongest registered form BEFORE being judged.*

## The best case, granted in full

Strands are continuous along their own length (FND-REL-002: no material
points; no registered substructure), so the displacement field admits
arbitrarily large wavenumber ALONG a strand -- no Brillouin cutoff in
that direction. Discreteness is transverse only, at the crossing spacing
a (EM-RECON-025's stiffness matrix). This is the strongest form of
FND-058's route (b) available in registered structure, and it was granted
entirely for the test.

The accessible wavevector region is therefore a SLAB, not a sphere:
unbounded along strand axes, bounded at |k_perp| <= pi/a transverse.

## The arithmetic

At the anchor energy 1.4e15 eV, |k| = 7.095e21 m^-1.

| kappa | a [m] | pi/a [m^-1] | theta_max | accessible solid-angle fraction |
|---|---|---|---|---|
| 50 | 1.630e-17 | 1.927e17 | 2.72e-5 rad | 1.11e-9 |
| 250 | 9.533e-18 | 3.295e17 | 4.65e-5 rad | 3.24e-9 |

In familiar units: PeV photons could propagate only within about
1.6e-3 to 2.7e-3 degrees -- a few arcseconds -- of one of the three
strand axes.

Bar, locked before computing: escape succeeds iff the accessible
fraction exceeds 10 percent. The computed fractions are ~1e-9, **nine
orders below the bar.**

## VERDICT: ESCAPE-FAILS-ON-ANISOTROPY

Route (b) closes. Granting the collective mode its continuum along
strands does buy unbounded wavenumber -- but only in three measure-zero
directions, and a medium that transmits PeV photons only within
arcsecond cones of three axes is maximally anisotropic exactly where the
observations are.

**And the killing blow is the corpus's own:** FND-REL-002 (Derived)
forces the wave sector to Lorentz-invariant form -- isotropic
propagation, no preferred frame or direction. The anisotropic escape
contradicts a Derived claim. The framework is closed out here by its own
earlier success, not by an imported assumption. That is the strongest
form a negative result can take, and it is registered as such.

Observationally the same conclusion arrives independently: LHAASO's
Galactic PeV sources are distributed across the sky, not clustered on
three axes.

## What would rescue it (stated, per the locked bar)

Only a registered argument REMOVING the transverse sampling requirement
altogether -- i.e. a demonstration that the collective mode's coherence
does not need to be sampled at the crossing spacing. The commission
checked for one and found none: EM-RECON-025's own stiffness matrix is
built on crossings at spacing a, and the collective branch is defined by
the relative-displacement structure that the crossings create. Removing
the sampling removes the mode.

## Recommendation (not adopted here; route (c) is the author's)

With route (a) requiring strand substructure 8.3 orders below a MEASURED
thickness (FND-058) and route (b) now closed on the corpus's own
isotropy theorem, the honest disposition is **route (c): register the
photon sector's short-wavelength structure as UNRESOLVED in
KNOWN_LIMITATIONS at full volume**, with the three-pin contradiction,
EM-RECON-025's undischargeable cost 1, and the unpaid label gap named
there together.

This is a limitation of the registered ontology's length inventory, not
a refutation of the transverse-wave mechanics: the collective mode
exists, propagates, and carries the right state count and couplings at
accessible energies. What the corpus cannot currently do is host the
highest-energy photons that are actually observed. Stating that plainly
is the discipline working; hiding it inside an unadjudicated fork would
not be.
