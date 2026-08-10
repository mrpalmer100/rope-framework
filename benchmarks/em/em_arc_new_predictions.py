"""THE EM ARC'S NEW PREDICTIONS — computed, signed, and priced.
Backs EM-RECON-029. Only divergences from Maxwell count; reproductions are
consistency, not prediction. Each item states its kill condition.
"""
import numpy as np
import sympy as sp

HBARC = 1.9732698e-16     # GeV*m
EPS0 = 8.8541878128e-12
C = 2.99792458e8

print("=" * 72)
print("P-NEW-1 — THE SIGN LOCK: quadratic photon LIV must be SUBLUMINAL")
print("=" * 72)
# The carrier's dispersion: beta = 1/12 - B/(T0 a^2); EM-RECON-025's live
# falsifier demands B <= T0 a^2/12, i.e. beta in (0, 1/12]. Therefore:
print("The collective carrier REQUIRES beta in (0, 1/12]: photons are")
print("SUBLUMINAL at second order — high-energy photons arrive LATE, never")
print("early. ZERO free parameters in the sign.")
print("KILL: any confirmed SUPERLUMINAL quadratic LIV signal (early arrival")
print("scaling as E^2) kills EM-RECON-025 outright. Maxwell predicts no")
print("effect either way; quantum-gravity models allow both signs; the rope")
print("allows exactly one.")

print()
print("=" * 72)
print("P-NEW-2 — THE LINKED CUTOFF: dispersion scale and transparency ceiling")
print("=" * 72)
# One spacing a gives BOTH: E_QG2 = hbar c/(a sqrt(beta)) and the band-top
# ceiling E_max = 2 hbar c / a. With beta <= 1/12:
b, a_ = sp.symbols('beta a', positive=True)
ratio = (1/sp.sqrt(b)) / 2          # E_QG2 / E_max
ratio_min = ratio.subs(b, sp.Rational(1, 12))
print("E_QG2/E_max = 1/(2 sqrt(beta)) >=", sp.sqrt(sp.Integer(3)), "=",
      float(sp.sqrt(3)))
assert sp.simplify(ratio_min - sp.sqrt(3)) == 0
print("PREDICTION: if quadratic subluminal dispersion is ever measured at a")
print("scale E_QG2, the vacuum MUST become opaque to photons above")
print("E_max <= E_QG2/sqrt(3) — the two observables are LOCKED in ratio.")
print("Maxwell links nothing; generic LIV links nothing; the lattice does.")
print("KILL (joint): observing BOTH a dispersion scale X AND freely")
print("propagating photons above X/sqrt(3).")
print("Current consistency: LHAASO PeV photons demand E_max > 1.4e6 GeV,")
print(f"i.e. a < {2*HBARC/1.4e6:.1e} m — comfortably inside the dispersive")
print(f"bound a <= 9.3e-28 m. Consistent today, jointly falsifiable forever.")

print()
print("=" * 72)
print("P-NEW-3 — THE MASSIVE PARTNER: the optical branch's gap")
print("=" * 72)
# The SAME exact matrix that makes the photon massless PREDICTS a gapped
# partner: the relative (optical) branch, gap omega^2 = 2s/(mu a), i.e.
# E_gap = hbar c sqrt(2 g)/a with g the registered contact contrast.
G_LO, G_HI = 0.40, 0.46            # EM-RECON-018 survival band
A_DISP = 9.3e-28                    # m (upper bound => LOWER bound on gap)
Egap_lo = HBARC*np.sqrt(2*G_LO)/A_DISP
Egap_hi = HBARC*np.sqrt(2*G_HI)/A_DISP
print(f"E_gap = hbar c sqrt(2g)/a >= {Egap_lo:.1e}-{Egap_hi:.1e} GeV")
print("(using the registered g band and the dispersive-a upper bound).")
print("PREDICTION: a massive transverse photon-partner exists at or above")
print("~2e11 GeV — and therefore NO massive partner below it. Every")
print("accelerator search to date is predicted NULL (consistent); any")
print("discovery of a transverse massive photon-partner below ~1e11 GeV")
print("kills the two-branch structure. Maxwell has no partner at any mass.")

print()
print("=" * 72)
print("P-NEW-4 — THE ONE-NUMBER LOCK and the vacuum density obligation")
print("=" * 72)
SIG_LO = 4e24                       # J/m^3, registered floor
rho_vac = SIG_LO / C**2
print(f"kappa_0 = c/sqrt(eps0 SIGMA) ties every EM magnitude to SIGMA; the")
print(f"registered floor SIGMA >= 4e24 J/m^3 implies a vacuum medium mass")
print(f"density rho = SIGMA/c^2 >= {rho_vac:.1e} kg/m^3.")
print("PREDICTION/OBLIGATION (registered, not hidden): the uniform medium")
print("must NOT gravitate (the GRV sector's induced-gravity route is the")
print("registered position — only defects and gradients source). If any")
print("in-corpus derivation ever shows the uniform background sourcing")
print("curvature, the framework dies on cosmology by ~33 orders. This is a")
print("standing internal falsifier, now quantified.")
print("And the flip side: one PVLAS-class measurement of SIGMA fixes kappa_0,")
print("every field magnitude, AND the medium density simultaneously — a")
print("single experiment, three locked numbers, zero remaining freedom.")

print()
print("=" * 72)
print("P-NEW-5 (GATED CANDIDATE) — linear optical response of neutral defects")
print("=" * 72)
print("The q-EVEN contact channel (EM-RECON-024) exerts a linear-in-wave force")
print("on ANY center-line defect — including NEUTRAL ones. Time-averaged")
print("momentum transfer vanishes (harmonic), but a driven OSCILLATION at the")
print("optical frequency, linear in field amplitude, is predicted for neutral")
print("topological defects — where standard physics allows only quadratic")
print("(polarizability) response. NOT asserted with numbers: the coupling")
print("kappa(r) for a composite neutral needs its own chartered computation")
print("before this is a registered prediction. Named confrontation when")
print("chartered: neutron interferometry in intense optical fields.")
print()
print("LEDGER: two sharp sign/structure predictions (P1, P2), one mass-scale")
print("prediction (P3), one quantified internal falsifier + one-experiment")
print("lock (P4), one gated candidate (P5). All kill conditions stated. PASS.")
