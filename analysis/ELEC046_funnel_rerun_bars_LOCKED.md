# ELEC-046 — QGATE-008's funnel re-run at the derived action: locked bars (before computation)

## Commission
ELEC-045 derived the elementary reconnection action W1 = (pi/(4 sqrt3)) T_s w^2/c
in closed form and killed the n_t = 111 cell. QGATE-006/008's cross-sector funnel
was built on the OLD normalization (kappa = 1.80, tube-level T*D). This re-run
replaces the elementary action with the derived one and asks whether the chain
heals (all sectors and the electron demand ONE n_t) or breaks (the demands stay
scattered between 111 and ~500).

## Structural honesty, declared up front
The matter leg's residue S = hbar BY CONSTRUCTION (the Bohr chain demanded hbar),
and chemistry inherits it. Therefore "the funnel demands hbar/W1" is near-circular
for those legs. The funnel's ONLY independent content is:
  (a) the nuclear Fermi inversion S3, computed with no reference to W, landing
      near hbar on its own (0.955 in the old run), and
  (b) whether ONE elementary action now serves the electron sector AND the funnel,
      where the old chain carried two inconsistent normalizations
      (electron: n_t = 2.95e8 at D = d_c; funnel: n_t = 111 at tube D).
Any PASS below must be read through that lens, stated in the output.

## Inputs (all previously registered; nothing tuned)
kappa_3D = pi/(4 sqrt3) = 0.45345 (ELEC-045, closed form)
T_s = 1.70e3 J/m (ELEC-040), w = 2.87e-16 m (ELEC-040, nuclear-density spacing)
Old funnel constants verbatim from benchmarks/qgate/transfer_test.py.

## Locked bars
B1 (regression). The old funnel reproduces: demands {112.4, 112.4, 107.4},
    common factor ~111, spread < 10%. FAIL voids the comparison.

B2 (the new universal demand). n_t_new = hbar / W1 computed in SI. Reported.
    Sector demands recomputed as S_sector/W1 with S unchanged (matter hbar,
    nuclear S3). PASS if the spread across sectors stays < 10% (uniformity
    survives the change of elementary action).

B3 (THE DECIDER). Does the funnel's independent leg (nuclear) and the electron
    sector's closure demand (hbar/W1, ELEC-045) now agree on one n_t within a
    factor of 2? PASS = the chain HEALS: one elementary action, one collective
    number, replacing the old 111-vs-2.95e8 inconsistency. FAIL = the chain is
    broken and the claim registers that verdict.

B4 (what dissolves, what replaces). The old structural prediction D/w = 19 was
    derived FROM n_t = 111 and dissolves with it; the replacement observable is
    the coherence radius R_c = sqrt(n_t_new) * w and event duration R_c/c, and
    the ELEC-043 causality bill at the new n_t must be stated (spacings of
    pre-correlation required).

B5 (falsifiability guard). The output must name what would make n_t_new more
    than arithmetic: an independent registered mechanism producing ~n_t_new
    (the weave-reservoir / bundle census). Until then the healed chain is a
    CONSISTENCY, not a derivation, and the claim stays Modeled with that
    sentence in it.

## Kill condition
B1 fail => Failed-and-kept, no downstream numbers.
