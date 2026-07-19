# Hydrogen Atom — Scale & Mass Plausibility Sketch

> **STATUS: PLAUSIBILITY EXPLORATION — NOT A DERIVATION, NOT A VALIDATED CLAIM.**
> This note records that *one explicit set of assumptions* lands in the right
> ballpark for the Bohr radius and is consistent with sensible mass ratios. The
> key inputs (rope count `N`, microstructure scale `a`) are **chosen to fit, not
> derived.** It is kept as a model sketch so the assumption set and its ballpark
> behaviour are on record for future work. It is deliberately **outside** the
> validated corpus (`claims.yaml`), and nothing here should be cited as a result.
> Reproduce the numbers with `python explorations/atom_scale_plausibility.py`.

## Purpose

After viewing Gaede's atom image (an atom as a convergence of very many ropes
into a woven "star"), we asked a plausibility question, *not* a derivation
question: **does the picture land in the right ballpark for the size and mass of
a hydrogen atom, under sane assumptions?** The answer is a qualified yes, and
this note pins down exactly which assumptions are needed and what they do and do
not reach.

## The structural result this builds on (real, non-circular)

From the star-convergence geometry, a packing argument (N ropes of width `a`
fill a sphere of radius R when `N ≈ 4π(R/a)²`) gives:

    R ≈ a · √(N / 4π)

i.e. **the atomic pattern radius grows as the square root of the rope count.**
This is a genuine, non-circular structural law (no ħ, no inserted Bohr radius);
it is registered as `FND-MATTER-002` (status: Modeled). Everything below is the
*plausibility use* of this law, which is weaker than the law itself.

## The explicit assumptions (chosen, not derived)

- **A1 — microstructure scale.** `a ≈ 1×10⁻¹⁶ m`, taken at the upper end of the
  Lorentz-violation bound (`FND-REL-003`). This is the *largest* value the mesh
  scale is allowed to have; it is a **choice within a bound**, not a derived
  number (the corpus leaves the absolute scale `a` free).
- **A2 — rope count.** `N` chosen so the packing radius equals the Bohr radius:
  `N = 4π(a₀/a)² ≈ 3.5×10¹²`. This is a **tuning** — one target (`a₀`) fixes one
  free input (`N`). It is not an independent prediction of `N`.

So the concrete plausible picture is: **a hydrogen atom is ≈ 3.5×10¹² sub-nuclear
ropes converging into a woven star whose outer standing-wave pattern sits at the
Bohr radius.** A few trillion ropes is large but not absurd, and it is the single
free choice that anchors the sketch.

## What the assumption set reaches

| Observable | Result | Verdict |
|:--|:--|:--|
| Bohr radius a₀ | R = a·√(N/4π) = 5.29×10⁻¹¹ m | ✅ in the ballpark (by construction of A2, but A1/A2 inputs are sane, not absurd) |
| Mass ratio m_p/m_e = 1836 | achievable with a sensible rope-count ratio (≈1836 if mass∼N, ≈43 if mass∼N², ≈3×10⁶ if mass∼√N) | ✅ plausible — no pathological ratio required |
| Absolute hydrogen mass | requires fixing dimensionful T, κ, a | ⚠️ not checkable yet (not a failure — outside a plausibility check's reach) |

The mass-ratio check is the more meaningful one, because ratios need no absolute
scale: the picture *can* accommodate the real proton/electron ratio with an
ordinary rope-count ratio, whichever mass-vs-count law is assumed.

## Honest limits (read before using this)

1. **This is a consistency window, not a prediction.** Two free inputs (`N`, `a`)
   against one target (`a₀`) — hitting the target is easy and predicts nothing
   until `N` is fixed independently.
2. **A near-miss numerology was rejected.** `N = (1/α)⁶ ≈ 1.3×10¹³` gives a radius
   suspiciously close to `a₀`. There is **no principled reason for the exponent
   6**; it is treated as coincidence, not evidence, and must not be presented as
   a hit. (Recorded in `FND-MATTER-002`.)
3. **A correction made during the build.** An initial absolute-mass estimate used
   a wrong energy formula (`E ∼ N·T·a₀`) and produced a spurious "14 orders off"
   problem. That was an *error in the estimate*, not a model failure, and is
   retracted; absolute mass is simply not checkable at this stage.
4. **Derivation is currently BLOCKED** (`FND-MATTER-003`). Turning the radius law
   into a real derivation needs two independent inputs the model does not have:
   an absolute scale `a` (left free), and the rope count `N`. Crucially, the
   natural route "fix `N` from charge" **fails**: charge is the winding/linking
   number (= 1 for hydrogen), *not* the packing count (≈10¹²). These are two
   different quantities sharing the letter `N`; conflating them would be the
   error to avoid.

## What would turn this into a derivation

A single independent handle on **the rope count of a bound structure** — some
physics that sets `N` without reference to `a₀` — would convert `R ≈ a·√(N/4π)`
from a consistency window into an actual prediction of the atomic scale. That is
the named open problem `FND-MATTER-003`. Until then, this remains a plausibility
sketch: the model is *logically coherent and in the right ballpark*, which is all
it claims to be.
