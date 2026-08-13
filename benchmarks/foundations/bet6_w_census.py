"""
COMMISSION BET6 -- the w census. Audit the NAME before the NUMBER.
Bars: analysis/BET6_w_census_bars_LOCKED.md (locked first).
B1 definitions, B2 the a dependency, B3 proximity refused, B4 no census run.
"""
import math
fm = 1e-15
f_c = 0.309                                  # FND-MATTER-038
w_over_a = math.sqrt(4*f_c/(3*math.pi))      # EM-RECON-018 coverage counting

print("B1  DEFINITIONS (from each claim, before any value)")
print(" W1 EM-RECON-018 : VACUUM-MESH strand width, 3 pi w^2/(4 a^2) = f_c")
print(" W2 QGATE-004    : FLUX-TUBE CONSTITUENT width, n_t = f_c (D/w)^2")
print(" W3 ELEC-050     : tube constituent from the LATTICE radius band")
print(" => W2, W3 share a ROLE (tube constituent), differ in provenance.")
print("    W1 is a different object (ambient weave strand). Identity with")
print("    W2/W3 is the ONE-MEDIUM question: arguable, NOT automatic.")

print("\nB2  THE a DEPENDENCY (W1 is a RATIO; every w carries its a)")
print("   w/a = %.4f" % w_over_a)
for a, lab in [(1e-16, "Lorentz bound (NUCQ-003/ELEC-050)"),
               (1.63e-17, "FND-040 re-solve reading 1"),
               (9.53e-18, "FND-040 re-solve reading 2")]:
    print("   a = %-9.3g m -> W1 = %.4f fm   [%s]" % (a, w_over_a*a/fm, lab))
print("   W3 registered : 0.0395 - 0.0565 fm")
print("   W2 demanded   : ~1.5e-3 fm")

print("\nB3  PROXIMITY -- REPORTED AND REFUSED")
w1 = w_over_a*1e-16/fm
print("   W1(Lorentz) = %.4f fm vs W3 low edge 0.0395 fm : ratio %.2f" % (w1, w1/0.0395))
print("   REFUSED as identity evidence. CONFOUND NAMED: both use a at the")
print("   Lorentz bound and both route through a packing count (f_c, 3pi),")
print("   so the agreement is partly STRUCTURAL, not independent.")
print("   W2 gap swings %.1fx to %.0fx across the registered a values --" %
      ((w_over_a*9.53e-18/fm)/1.5e-3, w1/1.5e-3))
print("   no identification is possible while a is unsettled.")

print("\nVERDICT: V-COLLISION. B4 HELD -- no census executed.")
