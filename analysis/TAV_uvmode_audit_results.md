# COMMISSION TAV -- RESULTS: SCOPE-NARROWED, AND THE CONCLUSION SURVIVES BY A DIFFERENT ROUTE

*Adjudicated 2026-08-11 after bar lock
(analysis/TAV_uvmode_audit_bars_LOCKED.md). Benchmark:
benchmarks/foundations/tav_uvmode_audit.py. Chartered on an external
reviewer's UV-MODE-001 challenge, adopted with attribution.*

## The reviewer is right on the scope point, and it is a real correction

**A1.** The registry contains TWO transverse operators and they are not
the same object:

- **FND-REL-004 / FND-060** bounded the nearest-neighbour LATTICE form,
  omega^2 = (4T0/mu a^2) sin^2(ka/2) -- site-sampled, periodic in k with
  period 2pi/a, cutoff at pi/a.
- **EM-RECON-025**, the claim that actually IDENTIFIES light, registers
  the two-strand stiffness matrix [[T0 q^2 + s/a, -s/a], [-s/a,
  T0 q^2 + s/a]], whose acoustic (light) branch is omega^2 = (T0/mu) q^2
  -- **CONTINUUM in q**. The crossings enter as a COUPLING s/a that gaps
  the optical branch; they do not sample the wave. Verified symbolically:
  omega^2(q + 2pi/a) - omega^2(q) = 4 pi T0 (aq + pi)/a^2, non-zero --
  the registered light branch is NOT periodic and carries no Brillouin
  cutoff.

So FND-060's theorem is exact for the field it bounded and does NOT, on
its own, bound the registered light branch. The reviewer's diagnosis --
that the no-go may have been applied to the coarse displacement field
rather than to the physical radiation variable -- is CORRECT as stated,
and FND-060's claim text overreached in implying otherwise. Correction
pointer filed.

**A2.** No distinct primitive radiation variable is registered. The sweep
returns no gauge field, connection, or phase variable registered as the
radiating degree of freedom; EM-016's (phi, A) is a Modeled DICTIONARY
built ON the mechanical state, and EM-RECON-024 (Derived) fixes E's
direction as a fixed rotation of s. So there is no second variable to
escape into.

**A3.** Because E and B are derived FROM s by the registered dictionary,
their Fourier support is inherited: a function of a band-limited field is
band-limited in the same sense. No independent UV behaviour is available
through the dictionary.

**A4.** a is registered as CONVENTION/FORK with zero live pins
(GRV-094's provenance table) -- so the reviewer's option 7 (emergent a)
is not excluded by provenance. But it is not thereby open either: what
is pinned is the PRODUCT T0 a (the spent m_e calibration), so any
re-reading of a as a collective length must carry T0 with it and face
FND-058's arithmetic again.

## VERDICT: SCOPE-NARROWED -- but the escape it opens is already closed

The continuum q of the registered light branch is the wavevector ALONG a
strand (strands are continuous, FND-REL-002: no material points), and
that direction is genuinely unbounded. Coherence ACROSS the weave is
still carried by the crossing term s/a at spacing a. The accessible
region is therefore

    q_parallel unbounded,  |q_perp| <= pi/a

-- which is EXACTLY the slab FND-059 constructed, evaluated, and closed
on FND-REL-002's Derived isotropy (PeV photons confined to arcsecond
cones about three strand axes; accessible solid-angle fraction ~1e-9
against a 10 percent bar locked before computing), with the observed
all-sky LHAASO source distribution agreeing independently.

**Net position: the corpus's conclusion stands, but on FND-059's ground
rather than FND-060's.** The photon sector's problem is not a Nyquist
cutoff on light -- it is ANISOTROPY. That is a different and sharper
statement, and it changes what a fix must do.

## What this changes for the fix menu (stated, nothing proposed)

The demand is no longer "supply a length below 1.41e-22 m." It is:
**supply isotropy at high k.** Any escape must make the medium's
transverse sampling isotropic at PeV wavelengths -- which a finer
constituent spacing would do, but so might any structure that removes
the preferred strand directions at short wavelength. That is a strictly
wider target than the one the corpus was working against this morning,
and the reviewer's challenge is what widened it.

The corresponding inequality is unchanged in magnitude but changed in
meaning: transverse coherence must be sampled at <= 1.41e-22 m, i.e. the
constraint falls on the SPACING BETWEEN STRANDS, not on any length along
one.

## Disclosure

This commission was chartered to test a challenge that, if it landed,
would have been convenient. It landed halfway: the scope point is
conceded in full and registered against FND-060, and the escape is
nevertheless closed by an independent claim. Both halves are reported
with equal weight, per the locked bar.
