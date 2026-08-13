"""
COMMISSION BET5 -- does FND-064's sign identity compose with
FND-MATTER-063's three-census exclusivity into a dilemma?

Bars: analysis/BET5_dilemma_bars_LOCKED.md (locked first).
B1 units FIRST, then B2 gap robustness, then B3 branch pricing.
"""

# ---- registered inputs (values quoted from claims, not invented)
w_over_a      = 0.362          # EM-RECON-018, from f_c = 0.309 coverage counting
sigma0_over_a = w_over_a       # EM-RECON-018: sigma0 = w by the interpenetration id
band_surv     = (0.40, 0.46)   # EM-RECON-018, in Ac/(T0 a)
band_eta      = (1e-6, 3.5e-6) # FND-MATTER-063, in Ac*sigma0/(T0 a)
straddle_029  = (0.019, 87.0)  # FND-029 nuclear import, in Ac/(T0 a)

print("="*72); print("B1  UNITS -- the two censuses are NOT the same quantity as written")
print("="*72)
print("EM-RECON-017/018 census :  R1 = Ac/(T0 a)          [dimensionless]")
print("FND-MATTER-063 census   :  R2 = Ac*sigma0/(T0 a)   [length, unless sigma0 in units of a]")
print("Registered bridge (EM-RECON-018): sigma0 = w, w/a = %.3f" % w_over_a)
print("   => R2 = R1 * (sigma0/a) = %.3f * R1   (reading sigma0 in units of a)" % sigma0_over_a)

# convert the survival band into FND-MATTER-063's units
band_surv_in_R2 = tuple(x*sigma0_over_a for x in band_surv)
print()
print("survival band in R1 : [%.2f, %.2f]" % band_surv)
print("survival band in R2 : [%.4f, %.4f]" % band_surv_in_R2)
print("eta demand   in R2 : [%.1e, %.1e]" % band_eta)

print()
print("="*72); print("B2  GAP ROBUSTNESS -- with the conversion APPLIED")
print("="*72)
gap_lo = band_surv_in_R2[0]/band_eta[1]
gap_hi = band_surv_in_R2[1]/band_eta[0]
import math
print("gap (survival / eta-demand) : %.3e to %.3e" % (gap_lo, gap_hi))
print("orders of magnitude          : %.2f to %.2f" % (math.log10(gap_lo), math.log10(gap_hi)))
print("FND-MATTER-063 quoted 'five orders' comparing 1e-6 to 0.40 directly,")
print("i.e. WITHOUT the sigma0/a factor. Corrected gap:")
print("   %.2f to %.2f orders -- the conversion is O(1) (%.3f) and does NOT" %
      (math.log10(gap_lo), math.log10(gap_hi), sigma0_over_a))
print("   close the gap. FND-MATTER-063's headline SURVIVES, slightly reduced.")
print("VERDICT B1/B2: the censuses DO compose; not a units artefact.")

print()
print("="*72); print("B3  BRANCH PRICING -- both tines, registered terms only")
print("="*72)
print("FND-064: c4_loc > 0  <=>  k_eff > T0  <=>  R1 above the survival band.")
print()
print("TINE A -- R1 >= 0.40 (core survives):")
print("   c4 > 0, FND-040's negative sign EXCLUDED, matter stable.")
print("   COST: R1 exceeds the eta demand by ~%.0f-%.0f orders, so FND-MATTER-063's"
      % (math.log10(gap_lo), math.log10(gap_hi)))
print("   contact dispersion overshoots -> zero-point content ~1e4 x tension mass.")
print("   That is FND-MATTER-063's registered consistency problem, INHERITED.")
print()
print("TINE B -- R1 <= 3.5e-6/%.3f = %.1e (eta demand met):" % (sigma0_over_a, band_eta[1]/sigma0_over_a))
print("   c4 < 0, FND-040's sign correct, BUT k_eff < T0 -> NO repulsive core.")
print("   COST: no stable matter (EM-RECON-009's founding stability argument).")
print()
print("NEITHER TINE IS FREE. The sign cannot be chosen without paying.")

print()
print("="*72); print("B4  WHERE THE NUCLEAR IMPORT ACTUALLY LANDS -- three regions, not two")
print("="*72)
eta_R1 = band_eta[1]/sigma0_over_a          # upper edge of the eta-satisfying region, in R1
print("region I   R1 < %.1e            : eta satisfied, NO core   (c4 < 0)" % eta_R1)
print("region II  %.1e < R1 < %.2f  : no core AND eta overshot" % (eta_R1, band_surv[0]))
print("region III R1 > %.2f            : core survives, eta overshot" % band_surv[0])
print()
print("FND-029 nuclear import straddle : R1 in [%.3f, %.1f]" % straddle_029)
print("   lower edge %.3f vs region-I ceiling %.1e  ->  ratio %.0f" %
      (straddle_029[0], eta_R1, straddle_029[0]/eta_R1))
print("   REGION I IS EXCLUDED: even the import's most pessimistic end sits")
print("   %.1f orders ABOVE the eta-satisfying region." % math.log10(straddle_029[0]/eta_R1))
print()
print("CONSEQUENCE, and it is the commission's product:")
print("  * TINE B (FND-040's sign correct, eta consistent) is EXCLUDED by the")
print("    nuclear import -- the escape from FND-MATTER-063's consistency")
print("    problem does not exist on the registered import.")
print("  * The straddle still spans regions II and III, so THE SIGN REMAINS OPEN.")
print("  * eta is overshot in BOTH surviving regions: the zero-point")
print("    consistency problem is UNCONDITIONAL given the import, not")
print("    contingent on core survival as FND-MATTER-063 framed it.")
print()
print("NO BRANCH PICKED on the sign. w remains the decider (FND-029), and")
print("EM-RECON-018's narrowing does not resolve it: the straddle is wider")
print("than both bands.")
