# Release v2.5.2 — The decider executed (2026-07-31)

One claim, ELEC-052, closing the question v2.5.1 left open. The public
ancillary data of Baker-Cea-Chelnokov-Cosmai-Papa (EPJ C 85, 29 (2025);
arXiv 2409.20168v1) was uploaded by hand after automated access proved
blocked, and the E^2-weighted mass-density radius was computed on the
paper's actual lattice points under bars locked before parsing.

- VERDICT: R_eq = 0.407(14) fm. The v2.5.1 reconstruction (0.404 fm)
  confirmed to 0.8%. The framework's prediction (0.342 fm) in +19% tension,
  one-signed at every source distance; the propagated scale chain
  (n = 156, T0 = 1201 J/m, Sigma_eq = 3.60e35 J/m^3) sits ~28% below the
  Sigma-route registrations, now on measurement.
- METHOD: the locked validation bar rejected d = 0.9 and 1.0 fm twice (full
  range, then an answer-blind SNR cut) because the paper's own integral is
  tail-dominated there; a third rule was refused by name. The verdict rests
  on d = 0.7 fm, where the instrument reproduces the paper's integral under
  both rules (-0.7%, -0.3%) and the target is stable to 0.001 fm.
- REGISTERED OPEN, the scale-chain fork: absorb the 28% into Sigma
  (inflating HBAR lengths ~13-18%, re-confronting NUCQ-001) or defend the
  strand-count-follows-energy-density identification -- choice to be made
  before its consequences are computed. VMB@CERN polarimetry (QGATE-007)
  remains the external arbiter for Sigma.
- The ancillary data ships in anc_data/ (CC BY 4.0): the benchmark now
  reproduces from the repository alone.

Corpus at cut: 344 registered claims, 330 code-backed, 3/3 tests green.
