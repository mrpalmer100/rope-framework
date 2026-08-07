# Open Problem: The Rope Mode-Overlap Coupling (the exchange analogue)

**Status:** Open — the central unbuilt piece for ferromagnetism, chemical bond
energies, and nuclear binding magnitudes. Specified here so a derivation has a
checkable target and cannot be faked.

## Why this is the blocker

The corpus uses "mode-overlap energy" as the mechanism for three things: chemical
bonds (σ vs π), nuclear binding, and (EM-RECON-002) ferromagnetic alignment. In
every case it is **named qualitatively but never given as a formula.** Because of
that, the ferro-vs-antiferro sign cannot currently be computed — only asserted —
and the long-range field term (EM-RECON-003/004), which *is* computable, favors
antiferro or ferro depending only on geometry and does not by itself select
ferromagnetism.

## What a legitimate derivation must produce

A concrete functional **E_overlap[ψ₁, ψ₂]** giving the interaction energy of two
atoms' network mode fields ψ as a function of their separation and relative
orientation, **fixed by the strand mechanics** (not chosen to yield a desired
sign). Minimum requirements:

1. **Long-range limit:** reduces to the swirl-field strain term already computed
   (EM-RECON-003) when the mode fields barely overlap. (Consistency with a known
   result.)
2. **Scale:** at atomic separation the coupling is bond-strength, order 0.1 eV —
   the scale that beats thermal energy and matches observed exchange. (Not free:
   it must fall out, not be inserted.)
3. **Derivation, not choice:** the functional's form (hence the sign of the
   short-range coupling) must follow from the network elastic energy of two
   overlapping mode patterns, with no free parameter selecting ferro vs antiferro.

## Validation harness (independent checks a candidate must pass)

A candidate functional is only trustworthy if, using the SAME functional and no
per-case tuning, it reproduces facts it was not fitted to:

- **Chem check:** the σ > π bond-strength ordering (head-on overlap stronger than
  side-on) must emerge from the geometry dependence of E_overlap.
- **Nuclear check:** the binding-per-nucleon trend that peaks near Fe-56 (overlap
  maximized at optimal packing, then declining) must emerge.
- **Magnetism check:** for a given lattice geometry, E_overlap + field term must
  combine to give the observed order (ferro for Fe-type geometry), and the
  functional must NOT be re-tuned between the three checks.

A functional that gives the ferro/antiferro sign but fails the chem and nuclear
checks is fitted, not derived, and must be rejected. This harness is the
"everyday validation target" that the field-term work had (magnets repel) and
that the short-range coupling currently lacks.

## Until then

The ferromagnetic-alignment mechanism (EM-RECON-002) stands as *identified at the
right scale but not sign-derived*; the field term (EM-RECON-003/004) is computed
and geometry-dependent. No ferro/antiferro result should be registered from an
invented functional — doing so would be unfalsifiable. This document is the
target; the derivation is the work.
