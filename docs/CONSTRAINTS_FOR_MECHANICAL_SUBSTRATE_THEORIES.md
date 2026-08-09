# Constraints and Disciplines for Finite-Scale Mechanical Substrate Theories

*With rope-specific findings separated out. Distilled from the Rope Hypothesis
corpus, 1 August 2026 — 402 registered claims in total, of which 384 are
code-backed and 23 are classified Failed-and-kept (21 of those 23 are themselves
code-backed).*

**Scope, stated first because an earlier edition got it wrong.** This document
was originally titled *"What an Object-Based Ontology of Spacetime Must
Satisfy"* and presented a single undifferentiated list. An external reviewer
correctly objected that it conflated three different kinds of content and
asserted as universal several things that hold only for a particular class of
substrate. That edition is archived at
`_superseded/CONSTRAINTS_v1_overbroad_2026-08-01.md`.

The reviewer's summary of what this corpus can honestly claim is adopted here:

> a transferable methodological framework and a detailed constraint census for
> **finite-scale mechanical substrate theories**, together with rope-specific
> examples of how such theories succeed, fail, and mislead their builders.

The three tiers below are kept explicitly separate. **Part A** applies to any
research programme. **Part B** applies to theories with a finite microscopic
scale and mechanically propagating disturbances — not to every ontology that
"starts with objects." **Part C** is rope-specific and transfers only as
example.

---

# Part A — Universal programme disciplines

These are about how to run an investigation. They are independent of ontology.

### A1. Source before instrument

**Before building machinery to detect a quantity: name the claim that sources
it, state the magnitude it predicts, and check that the predicted value is not
in the instrument's null space.**

The corpus's cleanest example is also its most expensive. Five sessions built a
validated 3-D lattice-gauge solver, correct to 1e-13 on every gauge and symmetry
check. One session of reading then found that nothing in the framework sources a
flux — and worse, that the only phase the framework does derive is 2πN, which is
*exactly* what a 2π-periodic instrument cannot see. The instrument worked. The
audit came last. The three parts of the rule are separable and all three are
needed.

### A2. Sweep free scales; do not select a convenient one

When a bound gives only a ceiling, the honest procedure is to sweep the allowed
interval and ask whether independent requirements **overlap**. Selecting a value
that makes one sector work proves nothing about the others.

Here the sweep was decisive in a way no single-point check could have been: two
sectors' requirements passed 5.2 decades apart, and one of them needed a scale
*larger* than the framework's own bound permitted — an internal contradiction
found without consulting any experiment.

### A3. Distinguish *distinctive* from *derived*

Deriving a number that competitors fit is intellectually meaningful and does
**not** discriminate between theories. This corpus believed it had eight
distinctive predictions; a census against four criteria — quantitative,
distinctive **in observable outcome**, checkable, live — left one.

The demotion kinds are worth learning, because a successor will meet all of them:

- **Confirmed but shared** — the observable matches, and so does a rival's.
- **Conditional on an unestablished population** — needs objects nobody has found.
- **Awaiting an unbuilt component** — a discriminating branch that requires a
  model the programme has not built is a specification, not a prediction.
- **Falsifiable but not confirmable** — a value at a floor every rival also
  predicts can kill you and cannot vindicate you.
- **Derivation-distinctive only** — real achievement, no discrimination.

### A4. Forward supersession checks, not just dependency tracking

Normal dependency tracking asks *what depends on this claim*. The failure mode
that actually bites asks the opposite: *has this claim been superseded by
something written later?*

This corpus made that mistake twice in one day. In the worse case a luminosity
law had been revised three claims later in the same sector, under a title
announcing the revision in capitals; the resulting number was wrong by **63
orders of magnitude**. Both failures were caught by human reading, not by any
tool. `tools/forward_check.py` now automates it.

### A5. Cross-sector consistency on shared parameters

Sectors that share a parameter must be made to agree on it explicitly. Two
different values had circulated in this corpus under one name for some time
before an adjudication forced the comparison, and the second was never
registered at all.

### A6. Validate in the physical dimension

A mechanism demonstrated in a reduced dimension establishes mathematical
consistency, exact solutions, and useful counterexamples. It does **not**
establish the corresponding physical claim.

Concretely: a soliton stabilisation that worked in 1+1 does not exist in 3+1,
where the scaling exponents differ and every term of dE/dL is positive. A
mechanism shown only in 1+1 is not evidence for a stable 3+1 object until the
appropriate Derrick or virial test is passed.

### A7. Prefer exact identities to truncations, and check exponents anyway

Scaling exponents from exact dimensional identities or dominant-balance
arguments are often more robust than detailed profiles — but they are not
automatically protected, and must still be checked against the untruncated
equations. Exponents can move when anomalous dimensions matter, when
non-analytic terms appear, when the dominant balance changes, or across a
critical point.

The corpus's own example cuts both ways: a sixth-order truncation gave a
qualitatively wrong profile (cusped, where the exact solution is hollow with a
hard core) while its scaling exponents survived exactly. Instructive, not a
theorem.

### A8. Keep failures, and let them count

Twenty-three claims here are registered **Failed and kept**, with their
reasoning. That record is what made honest retirement possible: a sector cannot
be retired credibly if the history has been groomed.

The sharpest instance is worth recording. A theorem about where failures cluster
fell below its own pre-registered bar as the corpus grew, and was reclassified
Failed rather than having the bar relaxed. It then turned out to be classified
in the very category it theorised about — so its own failure counted as evidence
*for* it, a self-reference trap that had to be excluded explicitly.

### A9. Pre-register bars; report the failed ones

Every substantive session here locked its pass criteria before computing, in a
file the computation could not edit. The value shows up precisely when a result
is attractive: a 1+1 stabilisation giving L\* = c/ω was appealing enough that
the pre-locked artifact test is the reason it was caught in one session rather
than carried for months.

### A10. Separate existence, mechanism, and magnitude

**Demonstrating that a mechanism can produce an effect is not the same as
deriving that mechanism from the ontology, and deriving it is not enough unless
the predicted magnitude is nonzero, nontrivial, and observable.**

Three distinct questions, routinely collapsed into one by speculative
programmes:

1. *Can the effect exist?*
2. *Does the proposed ontology generate it?*
3. *Is the generated magnitude physically relevant?*

The gauge branch separates them cleanly and answers them differently.
Aharonov–Bohm holonomy exists (1, yes). The corpus built a solver that
reproduces it to 1e-13 (a demonstration about the *instrument*, not the
ontology). And the framework does not source a nontrivial value (3, no) — the
only phase it derives, 2πN, is exactly what the instrument cannot see.

Five sessions were spent on question 1's machinery before question 2 was asked
and question 3 answered it. This rule is implicit in A1 and is stated separately
because the confusion is common enough to deserve its own name.

---

# Part B — Constraints on finite-scale mechanical substrate theories

These apply to theories in which a substrate with a **finite microscopic scale**
carries disturbances by **mechanical propagation**. They do not apply
automatically to causal sets, disordered or amorphous networks, continua with
internal degrees of freedom, or ontologies where Lorentz symmetry is fundamental
rather than emergent.

### B1. Causal coordination must be demonstrated, and it is quantitative

**Any mechanism requiring collective coordination during an event of duration τ
must identify the causal channel and show the required region fits inside its
causal domain.** Where the operational limiting speed is c, the budget is cτ.

This is the generalised form of a constraint that, in the rope model's specific
case (transverse waves at √(T/μ) = c), closed two escapes outright and
constrained a third: a collective-number rescue needing 1e8 participants where
causality gave ~1, and a bundling escape whose shortfall *grew* as the scale
shrank. The circulation branch was constrained by the same budget but was
ultimately closed by a later source-and-holonomy audit — absence of an undriven
source, available relaxation, and the 2πN null-space obstruction — not by cτ
alone. Compute the budget first regardless: it is the cheapest way to falsify
your own proposal.

### B2. A preferred microscopic scale or frame must satisfy Lorentz bounds

**Any substrate with a preferred scale or frame must show why observable Lorentz
violations remain below experimental limits.** Not every structured medium is a
regular lattice — disordered networks, amorphous substrates, causal sets,
simplicial complexes and topological defects in continuous fields all have
structure without the simple (ka)² dispersion correction — but each still owes
this demonstration in whatever form its own dispersion law takes.

*Rope-specific instance:* for the corpus's specific lattice dispersion relation
and the external Lorentz-violation limit used in FND-REL-003, the inferred upper
bound is a ≲ 1e-16 m — which decouples the substrate from the atomic scale. That
number belongs to that dispersion relation and that limit, not to granularity as
such.

### B3. Establish whether your tension is constitutive or a constraint force

**First determine which it is. If it is a Lagrange multiplier enforcing a rigid
constraint, do not treat it as locally stored material energy or attempt to
derive it from local microstructure alone** — a multiplier is fixed by the state
and boundary conditions, so no local derivation can succeed.

This matters because both cases occur. A medium with constitutive strain energy
E = ∫W(ε)dV has T = ∂W/∂ε derived from local strain, and the no-go does not
apply. A strictly inextensible medium does not.

**Qualification the corpus owes:** a multiplier term vanishing on the constraint
surface does not mean the system stores no energy. A pre-stressed system can
still hold energy in whatever mechanism established the pre-stress, and this
corpus does not explain what established its own.

### B4. If restoring force comes only from maintained pre-tension, that premise is load-bearing

A medium can support waves through elastic compression, bending stiffness, shear
modulus, field-gradient energy, local constitutive restoring forces, or internal
phase stiffness — none of which requires an external reservoir.

**But if transverse restoring energy comes *solely* from externally maintained
pre-tension, then the source and thermodynamic status of that pre-tension are
load-bearing premises and must be stated.**

*Rope-specific instance, and it is severe:* strip the reservoir from this model
and a closed medium absorbs transverse displacement at **exactly zero energy
cost**, by shortening longitudinally wherever it is displaced transversely. Zero
cost means no restoring force and no wave — so the reservoir premise underwrites
the optics sector, the framework's strongest work, and has since the first
transverse wave was written down.

### B5. Reduced-dimension stability does not transfer

Included here as well as in Part A because it bites hardest for substrate
solitons: Derrick's theorem is dimension-dependent, and the scaling exponents in
1+1 and 3+1 differ enough to change which mechanisms stabilise.

---

# Part C — Rope-specific findings

These transfer as **examples and cautions**, not as constraints. A successor
inherits none of them automatically.

### C1. Linking-number charge

Charge as a topological linking number makes integrality transparent and stable
under continuous deformation, because curves cannot pass through one another.
That is a genuinely concrete geometric mechanism.

**It is not unique to object ontologies.** Field theories reach quantisation
through compact gauge groups, representation theory, the Dirac monopole
condition, topological sectors, Chern classes, anomaly cancellation, and
grand-unified embeddings. The fair claim is that linking is a particularly
*transparent* route, not the only one.

### C2. The invariance relation T₀/Σ = a²/3

Holding for any tube radius, this collapsed the framework from several
apparently free scales to one. The transferable advice is the general practice —
**look for ratios invariant under the deformations you are worried about; they
are cheap to find and retire whole disputes** — not this particular ratio.

### C3. Nuclear mass performance, with the right quantity named

**The distinction the headline number hides.** The benchmark predicts *atomic
masses* along two meeting tracks — discrete bond-counting from A=2..16 (one
He-4-calibrated constant) and a derived semi-empirical mass formula from A~8
through U-238 — using **one** calibrated nuclear
constant against roughly five fitted parameters in the standard semi-empirical
formula — and the semi-empirical formula's five terms are now derived from the bond
geometry rather than fitted (heavy-table binding to ~1%). But the benchmark's own docstring states why that figure looks strong:
**binding is only ~1% of mass**, so most of an atomic mass is nucleon rest mass
taken as input. The quantity the model actually predicts is the **binding
energy**, and there the accuracy is ~1.5–2.5% in the original derivation and
**~13% after NUC-018's corrections** — an order of magnitude weaker than the
mass figure suggests.

Quoting the mass accuracy without the binding accuracy overstates the result,
and this document previously did so.

**The honest statement:** a structural bond-counting model reproduces nuclear
binding energies across the table to roughly ten percent with one calibration.
That is still a real result — most binding models carry five or six fitted
parameters — and it is not the 0.5% the mass figure implies.

**Registered boundaries, from the claim itself:** H-1 is inputs only, He-4
**fails at 38% binding error** (the smallest nuclei being quantum-dominated),
the capability is strongest mid-table, the parameter-free surface ratio came out
1.34 against 1.130 empirical, the volume coefficient sits 12.8% high, and the
derived Coulomb term is 9% off.

**Open questions a reviewer is right to press, and which this corpus has not
answered:** whether the constant was fixed before testing the full range;
whether shell, pairing, deformation and magic-number effects are included or
averaged over; whether the quoted error is in-sample or genuinely predictive;
how it performs against a matched baseline of comparable flexibility; and
whether the isotope-by-isotope residuals are structured.

### C4. An Einstein–Hilbert-like tensor pattern in an induced action

The IR-universal part of the medium's induced action reproduced the
parameter-free Einstein–Hilbert tensor pattern in a specified response channel,
with the diagonal and cross channels suppressed.

**This is not emergent gravity and should not be described as one.** A complete
claim would additionally require the correct sign, diffeomorphism or equivalent
gauge structure, universal coupling, nonlinear completion, absence of unwanted
modes, correct Lorentz behaviour, the Newtonian limit, radiative degrees of
freedom, and stability. What is established is narrower and still worth having:
*a mechanical substrate can reproduce an Einstein–Hilbert-like quadratic tensor
pattern in a specified infrared channel.*

### C5. Composite masses reached, fundamental masses not

In **this construction**, a family of composite masses came out with one
calibration while the lepton mass scale did not (registered as an irreducible
input, a kept negative). That is a fact about this corpus. It is **not** a
theorem that object ontologies generally can reach composite masses and cannot
reach fundamental ones.

### C6. The electron/ħ scale incompatibility

Two sectors of the same framework required substrate scales 5.2 decades apart,
with one excluded by the framework's own Lorentz bound unaided. An instructive
example of A2 and A5 in combination.

### C7. The 2πN holonomy obstruction

The only topological circulation the framework derives is spectrally invisible
in a 2π-periodic instrument. The canonical illustration of A1's null-space
clause.

### C8. The reservoir dependence of the optics sector

Recorded here as a rope-specific structural fact, generalised at B4.

---

## What a successor actually inherits

**A successor based on a finite-scale mechanical substrate with tension-supported
propagation** should begin with Parts A and B: a demonstrated causal coordination
budget, a Lorentz-violation account for its own dispersion law, a decision about
whether its tension is constitutive or a constraint force, an honest statement of
what maintains any pre-stress, and full-dimensional validation.

**A generic ontology that merely starts with objects** inherits Part A and these
broader demands only:

- causal coordination must be demonstrated;
- Lorentz symmetry must emerge or be fundamental;
- hidden preferred scales and frames must satisfy bounds;
- quantities require sources and predicted magnitudes;
- sectors must agree on shared parameters;
- claimed predictions must be externally distinctive;
- reduced-dimension results must survive the physical dimension;
- failures must remain part of the evidence.

It does **not** inherit a tension, a reservoir, transverse modes, lattice
dispersion, a constituent spacing, linking-number charge, or mechanical
composite masses.

---

*Every corpus-specific example traces to one or more registered claims and their
associated analyses or benchmarks; see `claims.yaml`. The general methodological
statements in Part A are syntheses across many claims and do not each have a
standalone numerical benchmark.*

*Framework status as of 1 August 2026: one free parameter (the vacuum
stiffness Σ, two candidates 28% apart), one discriminating prediction (the α–G
drift ratio, decision expected 2027–2030), twenty-three kept failures, and an
author who says openly that the world may not be ropes.*

*This edition exists because an external reviewer read the first one and was
right. That is the process working.*
