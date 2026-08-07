# Release v3.1.0 — The electron line, the constraint census, and two tooling repairs (1 August 2026)

**402 registered claims (104 Derived, 246 Modeled, 4 EFT-constrained, 3
Conjecture, 5 Open, 23 Failed-and-kept); 384 code-backed, all passing.**

A minor version rather than a major one: v3.0.0's retirements changed what the
corpus claims, and this release adds a completed line of work, a document
designed to outlive the model, and repairs to the machinery that checks it.

---

## The electron line: fourteen claims from conjecture to a clean negative

Prompted by the observation that the corpus's electron had always been treated
as a **static geometry**, and that its strongest no-go (ELEC-057) silently used
`r_e ∝ a`, a proportionality that follows from staticness rather than from
physics.

**What was built.** Matter couples to the medium's longitudinal sector through a
cubic vertex whose coefficient *grows* in the inextensible limit that experiment
independently forces (ELEC-067). In that limit the sector becomes an
instantaneous constraint sourced by |∇ψ|², with an attractive back-reaction —
the shape of a guidance structure. Derrick scaling then gave no static soliton in
1+1 but a stable dynamical branch with `L* = c/ω` (ELEC-068), a result that did
**not** survive to three dimensions (ELEC-070) and was retracted, replaced by a
structural stabiliser: the strain expansion's own sixth-order term, positive
whenever `k > 2T₀`, which the registered stiffness ratio exceeds by eight orders.

**What was solved.** The 3-D radial Euler–Lagrange equation turned out exactly
soluble via a first integral. The sixth-order truncation gave a cusped profile;
solved to **all orders**, the true object is **hollow with a hard core at finite
radius** (ELEC-074). The scaling relations survived the correction exactly —
size linear in the field excursion, energy cubic — with only coefficients moving.
*A truncation can be right about exponents and wrong about shapes.*

**What was decided.** Sized to the scattering bound, the object is **2.0e37 times
too light**; massed to the electron, it is **1.7 microns across** (ELEC-075). The
obstruction is structural: `E ~ T₀Δ³` with a hadronically fixed T₀ leaves no
freedom, and no profile refinement changes an exponent. The hard core sits at
1.7% of a strand spacing — the continuum failing, not physical structure.

**Four challenges survived.** Parametrization (ELEC-071: the quartic's sign is
parametrization-dependent and FND-REL-002 selects the attractive one),
functional selection (ELEC-077: the framework's denial of material points forbids
an elastic energy in longitudinal displacement), conservation law (ELEC-079:
strand-length conservation is GLOBAL, and ELEC-078 applied it locally), and
premise (ELEC-080: the reservoir is not an electron-line assumption — without it
a closed medium absorbs transverse displacement at zero cost and **light cannot
propagate**, so the optics sector has relied on it since the first transverse
wave).

**The verdict.** The medium admits a stable localized finite-energy solution.
It is not the electron.

## The foundations reduction: one free parameter, not two

`T₀ = Σa²/3` follows from ELEC-053's invariance theorem, and inverting returns
the Lorentz bound to 0.1% for both registered scale sets. So "what sets T₀" was
never a separate question — the framework has **one free scale**, Σ (FND-017).

And "why doesn't a tensioned ground state relax?" dissolves: in an inextensible
medium the tension is a **Lagrange multiplier**, which stores no energy and does
work only when the configuration changes. A useful no-go falls out — **no local
derivation of T₀ can exist**, since a multiplier is fixed by state and boundary
conditions.

## Σ: the arbiter does not arbitrate, and the route is a calculation

Specifying the polarimetry experiment honestly showed it **cannot decide Σ's
value** (QGATE-018): discriminating the two candidates needs sensitivity 4.8e8
beyond VMB@CERN's design goal. Three things had been travelling under one
heading — a threshold test on Σ's branch (already passed), a genuine near-term
test of the **electron's internal class**, and a measurement of Σ that does not
exist.

But the two candidates differ as an internal consistency argument versus a
*computation* on published lattice data, so the route is a better calculation.
Redone with an independent estimator — fitting the paper's own profile and
integrating analytically rather than trapezoid-with-truncation — **0.407 fm
survives to 1.3%** (ELEC-081), with a bootstrap error of 0.3% and a sech-family
model spread of 2.2%. The 28% tension is not an artifact of the method. The
corpus **leans** to the lattice value without claiming it.

## Two tooling repairs, both from real failures

**The forward check** (`tools/forward_check.py`, FND-019). GRV-049 used a
luminosity law GRV-047 had revised three claims earlier under a title announcing
the revision — a **63-order** error (GRV-053). The corpus's guards all looked
*downstream* of changed claims; nothing looked *forward* from a claim being
relied on. The new tool lists later claims that name, depend on, or share a
sector with revision language, and it was **validated against both** of the day's
failures. The corpus-wide audit shows 292 of 402 claims have later claims naming
them.

**The predictions paper**, corrected twice: a reader's note now states the
discrimination audit up front (nineteen predictions, **one** discriminator), and
the withdrawn whisper figures were replaced with the channel-saturated
description.

## The constraint census, written to outlive the model

`docs/CONSTRAINTS_FOR_ANY_OBJECT_ONTOLOGY.md` (FND-018) collects what this corpus
paid to learn, in a form that applies to **any** successor starting from objects:
five non-negotiable constraints, four results worth stealing, six failure modes
priced by what they cost here.

*Nothing in it requires strands — only objects with a scale, a tension, and a
signal speed.*

---

## Where the corpus stands

- **One free parameter:** Σ, two candidates 28% apart, no experiment in reach,
  a calculation that leans lattice-ward.
- **One discriminating prediction:** the α–G drift ratio, confronted at 1.74σ,
  with a named weak point already at 2.06σ and a decision expected **2027–2030**.
- **Twenty-three registered failures**, kept with their reasoning.
- **A reconstruction that is untouched:** optics, electricity, magnetism, local
  gravity, and the nuclear mass table from C-12 to U-238 on one calibrated
  constant.

*The failures are the point. A framework that recorded only its successes would
have a longer list of predictions and no way to tell which of them meant
anything.*
