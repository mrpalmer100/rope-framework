"""GRV-113 -- COMMISSION NUN-GRV9: THE chi BOUND FROM REGISTERED POLARIMETRY.

Bars locked in analysis/NUNGRV9_chi_bound_bars_LOCKED.md BEFORE this
script was written. The named next-order on GRV-112's face, and the
check PRED-002-FREQ's standing constraint demands of any proposal that
lets the strand scale into an optical observable. Clean-room held.
NO NEW OPTICS: every physical number below is taken verbatim from the
registered PRED-002-FREQ benchmark; the only new operation is the
locked linear-in-chi reading and the locked inversion.
"""
import numpy as np

# ---- REGISTERED INPUTS, verbatim from pred002_frequency_scaling.py ----
C = 2.99792458e8
NU0 = 150e9                    # the registered evaluation frequency
W_STRUCT = 5.774e-17           # l_struct = w = a/sqrt(3), ELEC-053
L_HUBBLE = 1.3e26              # the registered path
# ---- REGISTERED OBSERVATION (PRED-002 / Eskilt-Komatsu 2022) ----
BETA, SIG = 0.342, 0.094       # deg
# ---- LOCKED INVERSION CONVENTION (bars B2) ----
CEILING = np.radians(BETA + 2 * SIG)   # 0.530 deg, conservative ceiling
# ---- GRV-112 registered per-strand writhe magnitudes (check values) ----
TAU1, TAU2 = 4.1888, 1.6239    # in 1/a_f, FND-091 geometry


def main():
    om = 2 * np.pi * NU0
    psi_full = 0.5 * om ** 2 * W_STRUCT / C ** 2   # registered R2 rate
    total_full = psi_full * L_HUBBLE
    print("STEP 1 -- THE REGISTERED INSTRUMENT, reproduced exactly:")
    print(f"   R2 rate at full coherent handedness: {psi_full:.3e} rad/m")
    print(f"   at 150 GHz on l_struct = {W_STRUCT:.3e} m;")
    print(f"   accumulated over the registered path: {total_full:.3e} rad.")
    assert abs(psi_full - 2.85e-10) / 2.85e-10 < 0.02
    assert abs(total_full - 3.7e16) / 3.7e16 < 0.02
    print("   Matches PRED-002-FREQ's registered 2.85e-10 rad/m and")
    print("   3.7e16 rad. The instrument is the registered one.\n")

    print("STEP 2 -- THE LOCKED LINEAR-IN-chi READING (bars B1):")
    print("   The R2 rotation is odd under mirror (it IS the medium's")
    print("   optical activity), so a weave whose strands carry handedness")
    print("   +1 with weight (1+chi)/2 and -1 with weight (1-chi)/2 rotates")
    print("   at the NET rate chi x psi_full. Equivalently the bounded")
    print("   object is the effective chirality length l_chi = chi x")
    print("   l_struct, since the registered rate is linear in the")
    print("   structural chirality length. No new optics is derived.\n")

    print("STEP 3 -- THE LOCKED INVERSION (bars B2):")
    print(f"   ceiling: |psi_total| <= ({BETA} + 2 x {SIG}) deg"
          f" = {np.degrees(CEILING):.3f} deg = {CEILING:.3e} rad")
    chi_max = CEILING / total_full
    l_chi_max = chi_max * W_STRUCT
    print(f"   chi <= {CEILING:.3e} / {total_full:.3e}")
    print(f"   CHI BOUND (at l_struct = w):  chi <= {chi_max:.2e}")
    print(f"   SCALE-HONEST FORM:  l_chi = chi l_struct <= {l_chi_max:.2e} m\n")

    print("STEP 4 -- WHAT THE BOUND DOES TO THE GRANTED SECTOR:")
    print("   GRV-111/GRV-112: the microscopically supported coupling is")
    print("   lambda = chi (G I_p) |tau|, |tau| registered "
          f"({TAU1}/a_f, {TAU2}/a_f).")
    print(f"   The polarimetric cap therefore reads")
    print(f"     lambda / ((G I_p) |tau|) = chi <= {chi_max:.2e},")
    print("   i.e. the mesh-chirality channel of lambda is capped NINETEEN")
    print("   ORDERS below its natural (fully chiral) scale. No absolute")
    print("   lambda in joules is quoted: (G I_p) at the fine scale is")
    print("   unregistered (the FND-091 kb precedent), and bars B4 refuse")
    print("   the assembly.\n")

    print("STEP 5 -- CONSISTENCY AND FLAGS:")
    print("   (i) Frequency shape: the chi-suppressed channel is still")
    print("   n = +2; at the capped magnitude it is invisible in Eskilt's")
    print("   beta(nu) fit, so no registered exclusion is disturbed.")
    print("   (ii) GRV-109 untouched: that null was the DYNAMICAL phi")
    print("   exchange at O(lambda^2); this session bounds the STRUCTURAL")
    print("   chirality directly. Different operators, no overlap.")
    print("   (iii) The bound inherits PRED-002-FREQ's nineteen-order")
    print("   suppression finding and gives it a NAME in the gravity")
    print("   sector: the suppression IS a chirality bound.")
    print(f"   (iv) Resemblance flag, REFUSED per the standing rule:")
    print(f"   l_chi <= {l_chi_max:.2e} m lands numerically near 1.6e-35 m;")
    print("   the corpus has a registered history of refusing exactly this")
    print("   identification (the mesh-spacing discussion), and this")
    print("   session quotes the number and identifies it with NOTHING.\n")

    print("VERDICT (per bars B3): BOUNDED.")
    print(f"   chi <= {chi_max:.2e} at the registered structural length;")
    print(f"   l_chi <= {l_chi_max:.2e} m scale-free.")
    print("   CONSEQUENCES: (1) GRV-110 condition 4's 'independently")
    print("   bounded' leg is PARTIALLY DISCHARGED -- the microscopically")
    print("   supported channel (GRV-111's vertex) is now capped nineteen")
    print("   orders under its natural scale; a lambda large enough to")
    print("   matter at any conceivable confrontation cannot come from")
    print("   mesh chirality without violating registered polarimetry.")
    print("   (2) The exposure clause does NOT arm: a bound is not a pin")
    print("   (failure mode 1, refused by name). (3) The grant's standing")
    print("   is the author's call with this cap on the desk: L_C3 is now")
    print("   a granted term whose only located microscopic source is")
    print("   polarimetrically strangled. The honest options are to keep")
    print("   the grant as an effective-coupling placeholder at measurement")
    print("   framing, or to register it structurally disfavored.")


if __name__ == "__main__":
    main()
