"""FND-MATTER-061: the compliance correction adjudicated -- regulator
stability, exact mode sums, and the fork the mechanism actually faces.
Bars locked BEFORE computing (analysis/MATTER061_compliance_results.md):
(1) THE ADVERSE OUTCOME IS PERMITTED AND PRE-NAMED: if the computation shows
the dilute-exclusion microphysics is unsupported by the registered strand
model, that is registered as a fork/adverse finding against FND-MATTER-056/
059/060, whose grades become CONDITIONAL. The 1.44x landing does not buy the
mechanism protection; a landing without a foundation is coincidence-class.
(2) METHOD IS EXACT, NOT SCHEMATIC: finite-string Dirichlet mode sums,
computed numerically with BOTH a sharp and a smooth (exponential) cutoff.
A contribution is PHYSICAL only if regulator-stable; a contribution that
changes class between regulators is an artifact and may not carry weight.
(3) REGISTERED INPUTS ONLY: strands are inextensible continuous curves with
finite smooth contact energetics and no crossing axiom (FND-STRAND-001;
FND-MATTER-004 as corrected). No hard-wall exclusion may be assumed -- the
corpus already retracted that reading once.
(4) 060's PRE-INSTALLED FALSIFIER BINDS: any correction must move all knots
DOWN together; a correction landing all three at 1.0x is over-fitted on its
face. A parametric collapse (moving all knots far below target) is a
permitted outcome and means the mechanism is wrong in detail.
(5) NOTHING RE-FITTED; spend stays at ONE; targets enter only in the final
confrontation section, clearly marked.
"""
import numpy as np

HBAR, C = 1.0, 1.0     # natural units; only ratios and scalings matter
A = 1.0                # mesh cutoff scale: Lambda = pi/a
LAM = np.pi / A

def E_sharp(L):
    """ZP energy of Dirichlet string length L, sharp cutoff k < Lambda."""
    N = int(np.floor(LAM * L / np.pi))
    n = np.arange(1, N + 1)
    return float(np.sum(0.5 * HBAR * C * np.pi * n / L))

def E_smooth(L):
    """ZP energy, smooth regulator exp(-k/Lambda)."""
    # sum to convergence
    N = int(20 * LAM * L / np.pi) + 200
    n = np.arange(1, N + 1)
    k = np.pi * n / L
    return float(np.sum(0.5 * HBAR * C * k * np.exp(-k / LAM)))

print("== FND-MATTER-061: compliance adjudication (registered inputs only) ==\n")

print("-- (1) the point-constraint (pin) contribution: regulator stability --")
print("   Pinning an interior point of a string = splitting L into two L/2")
print("   (Dirichlet). Physical iff Delta E_pin converges, same class, both")
print("   regulators as L grows:")
for L in [50, 100, 200, 400, 800]:
    dp_sharp = 2 * E_sharp(L / 2) - E_sharp(L)
    dp_smooth = 2 * E_smooth(L / 2) - E_smooth(L)
    print(f"   L={L:>4}: sharp {dp_sharp:+.4f}   smooth {dp_smooth:+.6f}")
print("   ADJUDICATION: the smooth-regulator pin cost -> 0 as L grows (the")
print("   -pi/8L Casimir tail); the sharp-regulator value is an O(hbar c")
print("   Lambda) oscillating boundary artifact that does not converge.")
print("   THE POINT-CONSTRAINT CONTRIBUTION IS REGULATOR-UNSTABLE AND")
print("   CARRIES NO WEIGHT (bar 2). Constraining a continuous strand at a")
print("   point removes NO regulator-stable zero-point content.\n")

print("-- (2) the extensive (length-removal) contribution --")
print("   Delta E_del(l) = 2 E((L-l)/2) - E(L); extensive part per length:")
for L in [200, 400]:
    for l in [1.0, 2.0, 4.0]:
        ds = (2 * E_smooth((L - l) / 2) - E_smooth(L)) / l
        print(f"   L={L:>4} l={l}: smooth dE/dl = {ds:+.4f}  "
              f"(theory -Lambda^2/(2 pi) = {-LAM**2/(2*np.pi):+.4f})")
print("   ADJUDICATION: the extensive term is regulator-stable in CLASS")
print("   (proportional to removed length, coefficient = the scheme's own")
print("   ZP density, cancelling in the ratio lambda = displaced/total).")
print("   REMOVING mode-carrying length removes ZP content; only actual")
print("   length removal does.\n")

print("-- (3) does the registered strand model remove any length? --")
print("   Registered facts (FND-STRAND-001; FND-MATTER-004 corrected):")
print("   strands are inextensible CONTINUOUS curves; contact is FINITE and")
print("   SMOOTH (no hard wall, no crossing axiom, no termination).")
print("   An ambient strand meeting a thin inclusion (r << a) REROUTES.")
print("   Exact detour length for a straight strand, impact parameter b,")
print("   anchors at distance X, deviating to graze radius r:")
r = 1.0
for X in [10, 100, 1000, 10000]:
    b = 0.0
    extra = 2 * (np.sqrt(X**2 + (r - b)**2) - X)
    print(f"   X={X:>6}: extra length = {extra:.3e}  (-> (r-b)^2/X -> 0)")
print("   ADJUDICATION: rerouting removes NO length in the far-anchored")
print("   limit. Under the REGISTERED strand physics, a thin inclusion")
print("   deletes no mode-carrying length and pins no regulator-stable")
print("   point cost: the corpus's own strand model supplies NO mechanism")
print("   for the dilute-exclusion count.\n")

print("== THE FORK (registered as the outcome; targets marked below) ==")
print(" (A) If a registered occupation/routing fact exists or is later")
print("     registered (ambient strands genuinely ABSENT from the knot's")
print("     volume -- fixed routing, not dynamic exclusion), the 056/059")
print("     count stands on that fact and lambda = 6 pi (r/a)^2 survives.")
print("     The corpus currently registers NO such fact.")
print(" (B) If routing is dynamic (the natural reading of FND-STRAND-001's")
print("     relaxational dynamics), the exclusion count has no foundation:")
print("     the correction is not a modest factor but a parametric")
print("     collapse, lambda -> ~0, and the 1.44x landing is")
print("     coincidence-class. The mechanism dies in detail.")
print("     [Consistency with 060's falsifier: a collapse moves all three")
print("      knots down TOGETHER -- permitted outcome, pre-named.]")
print("\n-- confrontation (marked; inherited numbers only) --")
print("   Under fork B nothing lands: no comparison is licensed.")
print("   Under fork A the 059/060 numbers stand unchanged: no new")
print("   comparison exists. EITHER WAY this session adds no fit and")
print("   spends nothing. The adjudicating question is now a ROUTING fact")
print("   about the weave, decidable by the strand engine (FND-STRAND")
print("   relaxation of an ambient weave around a fixed knot: measure the")
print("   steady-state strand length density inside the knot volume).")
print("   That computation is named as the settler; it is NOT run here.")
