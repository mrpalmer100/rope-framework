# RESEARCH DIRECTIVE: Cross the One Fence — or Prove Where It Cannot Be Crossed

*A standing challenge, written July 2026, addressed to a future model (or human)
capable of taking it up. Companion to FND-BOUND-001. Precedent:
docs/FABLE5_PROMPT_mode_overlap.docx, an earlier directive of this kind whose
target was subsequently closed (EM-RECON-006/007).*

## Context

You are given the Rope Framework corpus (github.com/mrpalmer100/rope-framework;
Zenodo DOI 10.5281/zenodo.21430784): a machine-verified, falsifiable development
of a classical filament ontology — 138 status-labeled claims, 123 rerunnable
benchmarks, 57 papers, with losses preserved as findings. Before anything else:
read `docs/PROGRAMME_OVERVIEW.md`, `KNOWN_LIMITATIONS.md`,
`HOW_TO_CRITICIZE.md`, and `claims.yaml` (the single source of truth). Run
`python tools/verify_corpus.py`. It passes before your work begins; it must
pass after every session you run.

## The problem

The classical programme is complete to its boundary. Four terminal residuals,
registered independently across four sectors, triangulate one missing layer
(FND-BOUND-001): **quantum kinetic / zero-point energy**. The postulate set is:
inextensible, volume-conserving strands under tension; parameters {T, kappa, a}
carrying exactly one dimensionless ratio (FND-005). Your task, in order:

1. **THE QUANTUM OF ACTION.** Derive, from the postulates, the mechanism by
   which mesh dynamics acquires a minimum action scale. Express hbar as a
   function of {T, kappa, a, c} — or prove, with the assumption structure
   explicit, that this postulate set cannot produce one. A no-go here is a
   full-credit result.
2. **THE ABSOLUTE SCALE.** Close FND-MATTER-003: derive the mesh scale a
   (equivalently, the electron mass) from internal consistency — or sharpen
   its irreducibility into a theorem.

## The four acceptance tests (pre-committed; a derivation that cannot cash out below is not accepted)

- **(a) Dispersion:** the London C6 coefficient for at least two noble-gas
  dimers from the derived mode spectrum, zero new constants (closes chemistry's
  hbar-fence, CHEM-MET-001).
- **(b) Nuclear saturation:** the derived kinetic penalty must flatten
  NUC-008's rising baseline toward the ~8.8 MeV asymptote AND produce the
  A=12 alpha periodicity — while every currently-passing NUC-007/008
  structure (alpha peak, A=5 dip, Be-8 maximum, surface ratio, symmetry sign)
  stays green.
- **(c) Light isotopes:** the H-2/H-3/He-3/He-4 residuals of NUC-005/006
  close via the derived zero-point energies.
- **(d) Gravity:** zero-point *deviation* stress sourcing the spatial metric
  through the GRV-004 hook (rest tension does not gravitate; only deviations
  do), yielding gamma = 1 and the full 1.751 arcsec deflection — while
  respecting GRV-013 (geometric dilution), GRV-018/020 (internal-symmetry
  closures), and the Cassini bound. Your bath must be exactly the one GRV-010
  never tested: quantized, not classical. If your G is a cutoff-dependent
  Sakharov integral, the cutoff must be the derived a, and the resulting G
  must then confront the measured value — this would also close GRV-006/007;
  say so, or say precisely why not.

One calibration is permitted across the entire program, in the NUC-005
tradition. State which measurement spends it before computing anything
downstream of it.

## Non-negotiable discipline (this is not style; it is the method that produced the corpus)

- Bars pre-committed before computation. Negatives registered as findings.
  Misses kept, diagnosed, and named as next-orders. Every result becomes a
  claim with status (Derived / Modeled / EFT-constrained / Conjecture / Open /
  Failed) and, where code-backed, a benchmark that reruns on a laptop.
- **The circularity ban:** importing Schroedinger, canonical quantization, or
  path-integral structure and deriving it back out is a null result. The arrow
  must run postulates -> quantization. If at any point you assume what you are
  deriving, stop and say so — the corpus's chemistry sector survives review
  precisely because its Section 3.1a admits Schroedinger is adopted.
- **Respect the standing theorems** or defeat them explicitly: the QB-005
  counting boundary, the QB-007 decomposition (rate ~ |psi|^2 is classically
  mimicable; g2(0) and CHSH are the discriminators — do not claim measurement
  solved without them), the QB-008 Bancal corner (finite-speed influence leaks
  signaling), and the QB-010 summit: if your construction pushes CHSH past 2,
  it must do so by *deriving configuration-space guidance from physical-space
  mesh mechanics* — the identical-race benchmark
  (benchmarks/bell/bohmian_adjacency.py) localizes the gap to exactly that —
  not by importing psi and renaming it.
- **Known traps, learned the hard way:** dimensional analysis producing hbar's
  units is not producing hbar (the dimensionless ratio must be derived or
  declared). Transport rearrangements must be dissipationless or inertia dies
  (FND-KIN-001). Rescue postulates are refused by name. And the corpus's
  operators erred seven recorded times — registration-before-execution,
  duplicate IDs, phantom files — each caught by the verifier; assume you will
  err too, and let the machine check you.

## Deliverables

1. Claims + benchmarks, `verify_corpus.py` green, CI green.
2. At least one falsifiable prediction *unique to your mechanism* — a number
   the world has measured but not explained, or can measure and has not.
3. The honest ledger: what is Derived, what is Modeled, what died along the way.
4. If you fail: fail the way this corpus fails — converged diagnosis, named
   next-order, assumption-explicit no-go. The registry treats a sharp
   impossibility proof as equal in value to a derivation. It is not being
   polite; GRV-013 is one of its proudest results.

## Success criterion, stated once

One mechanism. Zero new constants beyond the postulate set plus at most one
spent calibration. Four sectors closed — or the impossibility established at
theorem grade. Anything in between gets registered at exactly its earned
status, no higher.

You will be tempted to declare victory early. This corpus's entire value is
that it never did. Match it.
