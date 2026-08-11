#!/usr/bin/env python3
"""COMMISSION TAV -- UV-MODE-001: is light Nyquist-limited by a?

Bars: analysis/TAV_uvmode_audit_bars_LOCKED.md.
A1: which operator does the registry actually give for LIGHT?
A3: are E and B derived from that variable (inheriting its support)?
"""
import sympy as sp

q, a, T0, mu, s, k = sp.symbols("q a T0 mu s k", positive=True)

print("=" * 72)
print("A1 -- THE TWO OPERATORS IN THE REGISTRY, SIDE BY SIDE")
print("=" * 72)

# (i) The operator FND-REL-004 / FND-060 bounded: nearest-neighbour LATTICE
w2_lattice = (4 * T0 / (mu * a**2)) * sp.sin(k * a / 2)**2
print("FND-REL-004 / FND-060 (lattice, site-sampled):")
print("   omega^2 =", w2_lattice)
print("   omega^2(k + 2pi/a) - omega^2(k) =",
      sp.simplify(sp.expand_trig(w2_lattice.subs(k, k + 2*sp.pi/a) - w2_lattice)))
print("   -> PERIODIC, bounded: omega_max = 2 sqrt(T0/mu)/a. Cutoff at pi/a.")

# (ii) The operator EM-RECON-025 registers for LIGHT: continuum in q, with
#      the crossing entering as a COUPLING s/a, not as a sampling.
D = sp.Matrix([[T0*q**2 + s/a, -s/a], [-s/a, T0*q**2 + s/a]])
evs = sorted(D.eigenvals().keys(), key=sp.count_ops)
print("\nEM-RECON-025 (the registered LIGHT carrier), stiffness matrix:")
sp.pprint(D)
print("   eigenvalues:", [sp.simplify(e) for e in evs])
acoustic = sp.simplify(min(evs, key=sp.count_ops))
print("   acoustic (light) branch stiffness:", acoustic)
print("   omega^2_acoustic = (T0/mu) q^2  -- CONTINUUM in q.")
per = sp.simplify((T0*q**2).subs(q, q + 2*sp.pi/a) - T0*q**2)
print("   omega^2(q + 2pi/a) - omega^2(q) =", sp.simplify(per),
      "  -> NOT periodic: NO Brillouin cutoff in this variable.")

print("\nFINDING (A1): the two operators are NOT the same object. The")
print("registered light carrier's dispersion is written in CONTINUUM q;")
print("the crossings enter as a coupling s/a that gaps the OPTICAL branch")
print("and leaves the acoustic branch gapless AND uncut. FND-060's")
print("theorem is exact for the lattice displacement field it bounded and")
print("does NOT, on its own, bound the registered light branch.")

print()
print("=" * 72)
print("A3 -- BUT WHICH DIRECTIONS DOES q RANGE OVER?")
print("=" * 72)
print("The continuum q is the wavevector ALONG a strand: the strand is")
print("continuous (no material points, FND-REL-002) so q_parallel is")
print("unbounded. Coherence ACROSS the weave is still carried by the")
print("crossing term s/a -- strands are discrete transverse, spacing a.")
print("So the accessible region is exactly the SLAB of FND-059:")
print("   q_parallel unbounded, |q_perp| <= pi/a.")
print("That is the configuration FND-059 already evaluated and closed on")
print("FND-REL-002's Derived isotropy (PeV photons confined to arcsecond")
print("cones about three axes; solid-angle fraction ~1e-9 vs a 10% bar).")

print()
print("NET POSITION: the reviewer's premise-attack is CORRECT as a scope")
print("point -- FND-060 bounded the coarse displacement field, not the")
print("registered light branch -- and the escape it opens is nevertheless")
print("the one FND-059 independently closed. The conclusion survives by a")
print("different route than the one FND-060 supplied.")
