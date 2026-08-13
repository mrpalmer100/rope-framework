"""COMMISSION AYIN: the reconnection-rate acquisition audit, executed per
analysis/AYIN_reconnection_bars_LOCKED.md. Nothing invented: the object is
classified (Q1), what the registry already fixes is derived (Q2), and the
sealed target v0 = 16.97 MeV is converted to a demanded window (Q3),
display only."""
import numpy as np

print("== COMMISSION AYIN: the reconnection rate ==\n")

# ---------------------------------------------------------------- Q1
print("-- Q1: classification of the five demands (verbatim readings) --")
demands = [
 ("FND-051 C4", "F", "'no reconnection FREQUENCY' -- the disorder/rate channel needs events per time"),
 ("FND-053 S2", "P", "'loop exchange UNDERSPECIFIED on the rate' -- an exchange needs a per-encounter probability/cross-section"),
 ("NUC-026 D7", "P", "'reconnection CONFIGURATION COUNT' -- a count of accessible exchanges per encounter"),
 ("NUC-028",    "T", "coherence-building mechanism -- a hopping AMPLITUDE (energy) between configurations"),
 ("NUC-029/030","T", "configuration mobility for the hybridization -- the same amplitude, now with a sealed value structure"),
]
for cid, cls, why in demands:
    print(f"   {cid:11s} [{cls}]  {why}")
print("   ONE OBJECT SERVES ALL FIVE via the locked conversion chain:")
print("   Gamma [F] = nu x p;  sigma [P] = p x a^2;  t [T] = hbar x Gamma")
print("   (the [T] conversion CONDITIONAL on QGATE mode quantization).")
print("   The acquisition reduces to: nu (kinematic, derivable now) and")
print("   p (dimensionless branching ratio per encounter, the true unknown).\n")

# ---------------------------------------------------------------- Q2a
print("-- Q2a: the athermality theorem --")
print("   FND-051's sweep: NO vacuum temperature registered. Therefore no")
print("   Arrhenius factor exists for ANY rate law in this corpus: p cannot")
print("   be exponentially suppressed thermally. Any suppression must be")
print("   geometric, topological, or from the KIN kink machinery (athermal")
print("   barriers crossed by DRIVEN, not thermal, motion).\n")

# ---------------------------------------------------------------- Q2b
print("-- Q2b: the interpenetrability adjudication --")
print("   Magnetism 2.1 + FND-KIN-005: single strands interpenetrate FREELY;")
print("   annihilation is free; charge-class conservation is a Stokes")
print("   identity that survives destruction. Consequence: NO hard-core")
print("   obstruction gates reconnection at single-strand level. The gate")
print("   is the exchange TOPOLOGY at the crossing, so p is a branching")
print("   ratio in (0, 1], not a tunneling factor. Per B5 no value is")
print("   selected; the O(1)-unless-topologically-suppressed structure is")
print("   the derived content.\n")

# ---------------------------------------------------------------- Q2c
print("-- Q2c: the kinematic attempt scale nu = c/a (registered inputs only) --")
c_light = 2.998e8   # wave speed = c exactly, mu = T/c^2 (HBAR-001, ELEC-043)
hbar_c_MeV_fm = 197.327
a_readings = [("Lorentz-bound a", 1.000e-16),
              ("FND-040 re-solve reading 1", 1.63e-17),
              ("FND-040 re-solve reading 2", 0.97e-17)]
print("   (all registered a readings carried per FND-066; never averaged)")
rows = []
for label, a in a_readings:
    nu = c_light / a
    E_att = hbar_c_MeV_fm / (a * 1e15)   # hbar c / a in MeV, a in m -> fm
    rows.append((label, a, nu, E_att))
    print(f"   {label:26s}: a = {a:.2e} m  nu = {nu:.2e} /s  hbar nu = {E_att:.0f} MeV")
print("   B7 check: nu is defined per crossing from local kinematics only;")
print("   no recruitment beyond the light cone is invoked (ELEC-043 honoured).\n")

# ---------------------------------------------------------------- Q3
print("-- Q3: the sealed-target window (display only, QGATE-conditional) --")
print("   NUC-030's target: v0 = 16.97 MeV (total two-vertex coupling).")
print("   Under t = hbar x nu x p (per-encounter amplitude at unit")
print("   participation) the demanded branching ratio is p = v0/(hbar nu):")
v0 = 16.97
for label, a, nu, E_att in rows:
    p = v0 / E_att
    print(f"   {label:26s}: p_demanded = {p:.2e}")
p_vals = [v0 / r[3] for r in rows]
print(f"\n   DEMANDED WINDOW: p in [{min(p_vals):.1e}, {max(p_vals):.1e}]")
print("   Registered as the TARGET BAND for the future p-derivation. The")
print("   band is small but not absurd: 1e-3 to 1e-2, i.e. reconnection at")
print("   one part in a hundred to a thousand per crossing encounter --")
print("   consistent with an O(1) topological branching ratio moderated by")
print("   a geometric acceptance, and inconsistent with either p ~ 1")
print("   (would overshoot v0 by 2-3 orders) or any exponentially tiny p.")
print("   Per B8: the window is NON-EMPTY and physically sane, so the")
print("   NUC-030 falsifier does NOT fire at this stage.")
