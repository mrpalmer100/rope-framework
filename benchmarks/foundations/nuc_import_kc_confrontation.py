"""NUC-IMPORT: the nuclear contact scale vs the core survival threshold.
Bars locked first (analysis/NUCIMPORT_bars_LOCKED.md): identification
chain committed from registrations; L1 = O(1) band (factor 3, direction-
neutral); L2 = bounds only (m_b in [1, 500]); numerology guard on
displayed estimates."""
import numpy as np

EB = 4.716            # MeV, NUC-007 registered bond energy (He-4 calibrated)
T0A = 0.16268         # MeV, M-point T0*a (FND-MATTER-044)
THRESH = (0.40, 3.00) # EM-RECON-017 survival band (sealed)
L1 = (1/3.0, 3.0)     # bond->barrier O(1) conversion band
MB = (1.0, 500.0)     # bundle multiplicity bounds

print("== NUC-IMPORT: the confrontation ==\n")
print(f"   registered inputs: e_b = {EB} MeV, T0*a = {T0A:.5f} MeV")
print(f"   raw bundle-level ratio e_b/(T0 a) = {EB/T0A:.1f}\n")

lo = EB * L1[0] / (MB[1] * T0A)
hi = EB * L1[1] / (MB[0] * T0A)
print(f"   E_x/(T0 a) bound: [{lo:.4f}, {hi:.1f}]")
print(f"   survival band:    [{THRESH[0]}, {THRESH[1]}]")
straddle = lo < THRESH[0] and hi > THRESH[1]
print(f"   VERDICT: {'BOUNDED REDUCTION -- the bound STRADDLES the threshold' if straddle else 'decided'}\n")

print("-- displayed estimates (assumptions visible; NOT adopted; bar 3) --")
for name, mb in [("m_b = 1 (single-pair contact)", 1.0),
                 ("m_b = sqrt(n_t) ~ 22 (line of surface strands)", 22.0),
                 ("m_b = n_t^(2/3) ~ 63 (contact patch)", 63.0),
                 ("m_b = n_t = 498 (full cross-section)", 498.0)]:
    r = EB / (mb * T0A)   # L1 = 1 shown; band applies around each
    inside = THRESH[0] <= r <= THRESH[1]
    print(f"   {name:48s}: ratio {r:8.3f}  "
          f"{'INSIDE the survival band' if inside else ('above' if r > THRESH[1] else 'below')}")
print("   OBSERVATION (numerology guard applied): the geometric estimates")
print("   (line/patch multiplicities) place the ratio near or inside the")
print("   band -- reported as an observation only; the guard notes that a")
print("   4-order m_b range crossing a 1-order band makes proximity weak")
print("   evidence by itself.\n")

print("-- the block, located exactly --")
print("   The confrontation is blocked at ONE quantity: the bundle contact")
print("   multiplicity m_b, a function of the constituent width w -- the")
print("   SAME unregistered width on which QGATE-005's tube census (and")
print("   with it the corpus's entire hbar scale branch) already waits.")
print("   ONE NUMBER now carries BOTH: whether the framework owns its own")
print("   quantum of action, AND whether its contact physics stabilizes")
print("   its own matter. The standing tripwire extends: any future claim")
print("   fixing w feeds through BOTH censuses immediately.")
