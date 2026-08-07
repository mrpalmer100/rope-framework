# Release v3.0.0 — The audit release (1 August 2026)

**381 registered claims (104 Derived, 242 Modeled, 4 EFT-constrained, 3
Conjecture, 5 Open, 23 Failed-and-kept); 366 code-backed, all passing.**

A major version rather than a minor one, because what the corpus *claims* changed
— not merely what it contains. One sector retired, the distinctive-prediction
list cut from eight to one, a canonical-set fork resolved, two registry
corruptions repaired, and the front-door document rewritten. A reader who knew
this project at v2.5.2 would be misled by that knowledge today.

---

## The headline: the mesoscopic-ħ sector is retired

The framework's one claim modified gravity could not make — that ħ's action
length is a mesoscopic patch of the medium, implying Born statistics should fail
near the nuclear scale — is withdrawn after **six independent closures**:

1. **Nuclear data** (NUCQ-001). The whole nuclear chart sits inside one
   sub-quantum grain, where standard QM works to percent accuracy.
2. **The Lorentz bound, unaided** (ELEC-057). Fitting even one patch in He-4
   needs a strand scale 6.75× *larger* than the bound permits — two of the
   framework's own constraints contradicting each other, with no experiment
   consulted.
3. **Every strand scale** (ELEC-057). The one free length swept over its entire
   allowed range: the electron and ħ requirements pass **5.2 decades** apart.
4. **Bundling** (ELEC-058). The causal recruitment budget is scale-invariant
   while the required coherence radius is fixed by measurement, so the shortfall
   grows as 1/a — worst exactly where the electron needs it.
5. **Coherent-unit width** (ELEC-059). The diameter cancels *exactly*: widening
   lengthens the causal reach and enlarges the required radius in the same
   proportion. Only constituent count matters, and closing needs 12 strands per
   unit against the electron's two.
6. **The two-medium option** (ELEC-060). Splitting vacuum from matter rescues the
   electron only; the ħ failure is against the Lorentz bound, which constrains
   the vacuum whatever else it shares its world with.

Five of the six required no new experiment. **The standing-wave form
S = πTA²/2c survives untouched** — the length cancels identically — and what
selects its amplitude remains open (ELEC-054).

Retirement was not demolition: a classification rule locked before any status
was inspected returned **2 CLOSED, 10 SURVIVES**, preserving six kept negatives
whose lessons never depended on the scale being viable. Record:
`docs/HBAR_SECTOR_CLOSURE.md`.

## The prediction accounting: eight to one

A census against four locked criteria (quantitative; distinctive in *observable
outcome*; checkable; live), then a full audit of every survivor against what the
standard alternatives actually predict:

- **PRED-003** (α–G drift ratio) — **the sole survivor.** Confronted against
  published optical-clock and lunar-laser-ranging data across four independent
  α determinations and three independent G determinations: holds at **1.74σ**.
  Named weak point: PSR J1713+0747, already 2.06σ on its own. A 3σ confirmation
  of its 2025 central value refutes the claim and needs only a factor 1.45 in σ
  — reachable **2027–2030**.
- **PRED-002** (cosmic birefringence) — **CONFIRMED and demoted.** The flatness
  test already existed; Planck legacy data favours the constant model by
  Bayesian evidence. But the standard axion predicts a constant angle too, and
  the frequency scaling that *would* discriminate was derived and closes the
  door: material optical activity gives ν², excluded at 4.9σ and overshooting
  the observed angle by 7e18 at the framework's own strand scale.
- **GRV-040** (the black-hole whisper) — fully characterised and unobservable.
  Genuinely sourced in the gravitational channel (a reconnection is purely
  deviatoric, trace zero to machine precision, 93% of excited power in the
  Einstein–Hilbert channel), but the strain is 7.9e−27 at 10 kpc and the best
  real candidate falls **36× short**. The corpus's *own* spectral work closes
  it: read as a line it would be detectable at SNR 11.
- **GRV-039**, **QGATE-007/010**, **PRED-001**, **HBAR-010** — demoted on
  conditional-population, unbuilt-model, weak-confirmation and dependency
  grounds respectively.

## What did not change

The reconstruction, which is the programme's substance and is untouched: 10/10
optical phenomena derived; charge as topological linking; magnetism with no free
parameters (current–current force at correct magnitude, 1/d and signs; Lorentz
force from gauge-forced coupling); Maxwell from Bianchi + Chern–Weil; the four
classical weak-field gravity tests at GR values; and the nuclear mass table from
C-12 to U-238 at 0.00–0.51% on **one** calibrated constant.

## Repairs

- **Registry corruption.** Six claims (ROPE-MODE-006/012, ROPE-VALIDATION-001–004)
  were written into the `sectors:` block rather than `claims:`. They parsed as
  valid YAML and were invisible to every tool: the corpus reported 348 claims
  while holding 360. The entire AB validation campaign had never been counted.
- **A verifier passing vacuously.** `verify_corpus.py` was parsing **zero**
  claims and still printing ALL CHECKS PASS, after a re-serialisation changed the
  sequence indentation. Now carries four guards, each tested to fire: sectors
  misfiling, empty parse, parser disagreement, dangling dependencies.
- **`add_claim.py` rewritten structurally** — v1 matched a regex against one
  exact serialisation and failed silently when the format changed.
- **Two dangling dependencies** (ELEC-032, ROPE-MODE-011) found by a crashing
  build. Recorded, not invented.
- **Paper/registry divergence closed both ways.** Three headline predictions in
  `falsifiable_predictions` had no registry claim while the paper asserted full
  traceability; they are now PRED-001/002/003 with benchmarks. The paper gains
  Part VI and the scale-chain note.
- **Stale renders quarantined.** `STATE_OF_THE_PROGRAMME.docx/.pdf` were the
  17 July edition; a reader opening the PDF would have got 122 claims and the
  pre-audit prediction list. Moved to `_superseded/`; `docs/PROVENANCE.md` now
  records which documents decay.

## Also

- **THM-006 falsified by the corpus's own growth** — the layer-separation
  enrichment fell from ~4× to 1.85×, below its locked 2.0 bar. The bar was not
  relaxed. A self-reference trap was caught and excluded: marking THM-006 Failed
  made it evidence *for itself*, since it is classified Layer III.
- **New standing rule**: `docs/STANDING_RULE_SOURCE_BEFORE_INSTRUMENT.md` — ask
  what sources a quantity before building the apparatus to measure it. Two
  branches were retired on that pattern at a cost of roughly eight sessions.
- **New front door**: `docs/STATE_OF_THE_PROGRAMME.md`, current and written for
  an outside reader.

---

*The failures are the point. A framework that recorded only its successes would
have a longer list of predictions and no way to tell which of them meant
anything.*
