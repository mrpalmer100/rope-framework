# Instruments the Framework Points At

*Status note, read first: this document registers **no claims**. It is a map
from the corpus's differentiating commitments to the physical instruments that
could test them. Everything here is an observational program, not a derivation;
the claim anchors cited carry their own statuses (mostly Modeled), and nothing
below upgrades them. Where the corpus and standard physics agree — which is
almost everywhere — the machines are the same machines, and this document has
nothing to add. Only where the framework diverges from the textbook can a
genuinely new instrument live; the corpus has exactly a handful of such
handles (seven instruments and two impossibilities), listed here with their honest prerequisites.*

*A framing worth savoring before the list: **MRI is already a rope machine.**
It tips spin-1/2 nuclei — framed-strand holonomies, per FND-STRAND-005 — with
RF rotations and reads the precession. Every MRI image is the belt trick,
performed by the hydrogen in a human body. The model reinterprets; the
hardware does not care. That is what "re-derivation of known physics" means in
practice, and it is why the instruments below are few.*

---

## 1. The mesh anemometer (Lorentz-violation interferometry)

**What it is.** An ultra-long-baseline optical interferometer, or a network of
comparative optical clocks, hunting for direction-dependent phase velocity
correlated with motion through the CMB-adjacent preferred frame.

**Why the framework points at it.** The corpus commits to a preferred frame
(QB-008: independently motivated, CMB-adjacent, with the quantified mechanical
demand K_L/K_T >= 1.9e8) and to a lattice dispersion correction of order
(ka)^2 — the term that literally **measures** the mesh spacing *a*.
FND-MATTER-003 registers *a* as the corpus's one irreducible network constant,
fixable by no amount of reasoning: only a measured Lorentz-violation signal
(or a deeper theory) can supply it. Today's Lorentz-violation experiments
(modern Michelson–Morley cavities, clock-comparison networks) are this
machine's prototypes; the framework gives them a specific target structure and
a specific meaning for a detection — the first measurement of the grain of
space.

**Consequence of a result.** A measured *a* converts several Modeled scale
statements into numbers (the FND-MATTER-002/003/004 chain: N ~ 3e11 becomes a
sharp count; the FND-KIN-002 residual-drag form acquires a magnitude). A null
result at improving precision pushes the mesh scale down and is registrable as
a bound. Both outcomes are corpus-relevant; neither is predicted with a
number, because *a* is exactly what is missing.

**Sharpening from the relativity sector.** FND-REL-002 proves the lattice
frame is *inaccessible to every sub-lattice probe* through two suppression
channels — dispersion ~ (ka)^2 and defect-odometer coupling ~ exp(-pi^2 w/a)
— and names the (ka)^2 dispersion as **the one falsifiable signature**. So
this instrument is not merely suggested by the framework; it is the unique
channel the framework's own no-go analysis leaves open. FND-REL-003 requires
a <~ 1e-16 m for survivability, which sets the (brutal) sensitivity target.

**Anchors:** FND-MATTER-003, FND-REL-002, FND-REL-003, QB-008.

## 2. The birefringence telescope (LiteBIRD)

**What it is.** A CMB polarization observatory measuring EB cross-correlation.
Being built now; launch era 2030s.

**Why the framework points at it.** The one forward prediction in the corpus
with a date attached: the Chern–Simons cosmic birefringence chain (photon
sector, v1.3.0) reproduces the Eskilt–Komatsu beta = 0.342 deg constraint via
sin(2 theta_W) n_rope r_H^2 = 9.18e-29/m and predicts **EB/EE = sin(4 beta)/2
= 0.0119**. LiteBIRD tests this. The corpus has skin in an instrument someone
else is already building — the cheapest kind of falsifiability there is.

**Consequence of a result.** Confirmation strengthens the photon-sector chain;
a clean null at sufficient precision falsifies the birefringence limb and gets
recorded per the programme's negative-results discipline.

**Anchors:** the photon submodule (`rope_solver.electromagnetism.photon`),
CHANGELOG v1.3.0.

## 3. The residual-drag decelerometer (conditional design)

**What it is.** A heroically isolated torsion balance or matter-wave
interferometer searching for **size-dependent** anomalous deceleration of
freely drifting masses.

**Why the framework points at it.** The transport series (FND-KIN-002/003/004,
strand fidelity FND-STRAND-002) establishes that mesh-scale transport
dissipation is exponentially suppressed in structure-size/mesh-spacing:
deceleration ~ exp(-c * size / a). The corpus deliberately registers this as a
**structural observation, not a prediction** — with no value of *a*, no
magnitude exists (FND-MATTER-003). But the *design* is nameable now: the
signature is a drag that depends on the size of the coasting structure, not
its mass or composition — unlike every conventional systematic.

**Prerequisite, stated loudly.** This instrument has a target only if
Instrument 1 (or a deeper theory) fixes *a* first. Until then it is a design
note, kept here so the dependency is visible.

**Anchors:** FND-KIN-002 (the exponential hierarchy), FND-KIN-001 (the
dissipationless-drift demand), FND-MATTER-003 (the missing scale).

## 5. The decoherence spectrometer (the gapped-floor hunt)

**What it is.** Precision noise spectroscopy on maximally isolated quantum
systems — trapped ions, superconducting qubits, levitated nanoparticles —
characterizing the *irreducible* environmental noise spectrum after every
ordinary-matter channel is subtracted.

**Why the framework points at it.** FND-STRAND-008 (Prediction 10 of the
predictions paper) commits to a structural shape: the weave reservoir is
GAPPED at the strand mass scale, band width sqrt(1 + 4 kt) times the gap, no
soft modes. Ordinary environments are gapless; the framework says the
*fundamental* one is not. The instrument is any platform sensitive enough
that residual, subtraction-resistant decoherence could be attributed to the
medium itself — at which point the spectrum's shape decides.

**Prerequisite, stated loudly.** The gap's *location* is scale-open (the same
missing *a* as Instrument 1), so this shares Instrument 3's honest status:
the shape is committed now; the frequency is not. A gapless irreducible
spectrum at every accessible scale is the standing falsifier.

**Anchors:** FND-STRAND-007, FND-STRAND-008; Prediction 10.

## 6. The click statistician (nucleation kinetics in detectors)

**What it is.** Not a new detector — a new *measurement campaign on existing
ones*: high-statistics waiting-time distributions, dark-count-vs-temperature
curves, and latency-vs-drive calibrations on threshold single-photon
detectors (SNSPDs, avalanche photodiodes).

**Why the framework points at it.** FND-STRAND-006/007 (Prediction 11) commit
to the full first-passage package: near-exponential waiting times at fixed
drive, Arrhenius dark counts, latency decreasing with channel energy, and the
Born square arriving as channel *energy*. Parts overlap known avalanche
phenomenology — the overlap is declared in the predictions paper — but the
commitment is to the whole package, and much of it is testable with hardware
that already sits on optics benches. This is the cheapest instrument on this
list: the machines exist; the framework asks only for their statistics.

**Anchors:** FND-STRAND-006, FND-STRAND-007; Prediction 11.

## 7. The analog bench (universality made tabletop)

**What it is.** Deliberately built implementations of the twist-chain and
coverage physics: coupled pendulum arrays, magnetic domain-wall lattices,
cold-atom sine-Gordon simulators, engineered filament brushes.

**Why the framework points at it.** Prediction 15: the friction cliff (slope
~ -8.5 per width unit, seven orders, arrest/coast) and the transparent-to-
solid coverage crossover (gap ~ contact size, inverse-fourth-power approach)
must appear in *any* faithful implementation, with only prefactors carrying
the engineering — the law transfers, per the STRAND-002 lesson (0.16 percent
slope agreement across implementations). Uniquely on this list, the no-scale
caveat does not apply: the experimenter builds the system, so the scale is
theirs. Josephson-junction arrays deserve special mention — the governing
equation is the twist chain symbol for symbol, so superconducting labs have
been running this bench, unlabeled, for decades.

**Anchors:** FND-KIN-002, FND-STRAND-002, FND-STRAND-004; Prediction 15.

## 8. Impossibility results as engineering knowledge

Two machines the framework says **cannot** be built, which is also
information:

- **The phase telegraph.** FND-STRAND-005's fibre-blindness is mechanical: a
  full 2pi twist flips the strand holonomy's sign and changes any energy
  detector's response by nothing. No instrument reading energy can read the
  global phase; a device signaling through it has no channel to couple to.
- **The PR-box communicator.** QB-022's SOVO clause is structural on strands:
  the measurement setting enters the model through exactly one degree-1
  channel, and supra-Tsirelson statistics would require a setting-dependence
  of polynomial degree > 24 that the physics does not contain. Correlation
  devices cap at 2 sqrt 2 — which is, not incidentally, the ceiling on
  quantum-computing correlations too.

A well-characterized impossibility tells engineers where not to spend money;
QB-012's four-clause wall specification is the corpus's most developed example.

## What is deliberately NOT here

The tempting sci-fi tier. The coverage threshold is real in the model
(FND-STRAND-004: solid is a height, not a rule; single strands interpenetrate
freely), but the barrier heights for bulk matter are astronomical and the
corpus offers **no knob** — no derived mechanism for tuning a bundle below
threshold. "Phase through walls" remains a beautiful way to understand why
touching works, not a device. If a future claim ever changes that, it will
arrive through the registry with a benchmark, not through this document.

---

*Doc-only; registers no claims; corpus counts unaffected. Anchored claims
carry their statuses unchanged.*

*Companion document: papers/falsifiable_predictions — the fifteen-prediction
inventory; this map supplies the hardware side of Predictions 3, 10, 11, and 15.*
