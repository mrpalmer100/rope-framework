"""GRV-052 -- THE STRAIN AT A DETECTOR: the number that decides the sector.

Bars locked in analysis/GRV052_strain_bars_LOCKED.md BEFORE computing.
"""
import numpy as np

G = 6.674e-11
C = 2.99792458e8
MSUN = 1.989e30
KPC = 3.086e19

F_BOUND = 1e-2          # GRV-049, data-backed
T_GREY = 0.07           # GRV-040 S2 midpoint
ETA = 0.925             # GRV-051 overlap with the EH channel
EFF_ACC = 0.1           # standard radiative efficiency
LIGO_ASD = 4e-24        # design, per root Hz near 100-200 Hz
YEAR = 3.156e7


def kappa(M_msun):
    return C ** 3 / (4 * G * M_msun * MSUN)


def main():
    M, D = 10, 10 * KPC
    nu = 0.23 * kappa(M) / (2 * np.pi)
    L_edd = 1.26e31 * M
    mdot_c2 = L_edd / EFF_ACC

    print(f"B1 THE SOURCE: {M} Msun at Eddington, {D/KPC:.0f} kpc, nu = {nu:.1f} Hz")
    for f in (F_BOUND, 1.0):
        L = f * mdot_c2 * T_GREY * ETA
        F = L / (4 * np.pi * D ** 2)
        h = (1 / (2 * np.pi * nu * D)) * np.sqrt(4 * G * L / C ** 3)
        print(f"   f = {f:.0e}: L = {L:.2e} W, flux = {F:.2e} W/m^2, "
              f"h_amplitude = {h:.2e}")

    L = F_BOUND * mdot_c2 * T_GREY * ETA
    F = L / (4 * np.pi * D ** 2)
    # B2: broadband ASD, bandwidth ~ nu (quasi-thermal, GRV-041..044)
    F_f = F / nu
    S_h = 4 * G * F_f / (np.pi * C ** 3 * nu ** 2)
    asd = np.sqrt(S_h)
    print(f"\nB2 THE SPECTRAL DENSITY (bandwidth ~ nu, since GRV-041..044 establish a")
    print(f"   QUASI-THERMAL broadband spectrum, not a line):")
    print(f"   signal ASD = {asd:.2e} /rtHz  vs  LIGO design {LIGO_ASD:.1e} /rtHz")
    print(f"   the signal sits {LIGO_ASD/asd:.2e}x BELOW the noise floor.")

    print("\nB3 THE SNR, both ways:")
    h_coh = (1 / (2 * np.pi * nu * D)) * np.sqrt(4 * G * L / C ** 3)
    snr_coh = h_coh / (LIGO_ASD / np.sqrt(YEAR))
    print(f"   (a) COHERENT MONOCHROMATIC, one year: SNR = {snr_coh:.1f}")
    print(f"       THIS IS FORBIDDEN by the corpus's own spectral claims -- GRV-041")
    print(f"       through GRV-044 establish a broadband quasi-thermal spectrum with")
    print(f"       a running temperature. Reported only as a ceiling.")
    snr_bb = (asd / LIGO_ASD) ** 2 * np.sqrt(YEAR * nu)
    print(f"   (b) BROADBAND CROSS-CORRELATION, one year (the honest reading):")
    print(f"       SNR = (S_sig/S_noise) x sqrt(T x delta_nu) = {snr_bb:.2e}")
    assert snr_bb < 1

    print("\nB4 THE VERDICT: THE WHISPER IS NOT DETECTABLE.")
    print(f"   At the data-backed efficiency bound the honest SNR is {snr_bb:.1e},")
    print(f"   short of unity by {1/snr_bb:.0e}. Even at the energetic ceiling f = 1")
    print(f"   -- which GRV-049 excluded from accretion budgets -- the SNR rises only")
    print(f"   to {snr_bb*1e4:.2e}, still short by {1/(snr_bb*1e4):.0e}.")
    print("   GRV-040 IS T1 ON STRUCTURE AND UNOBSERVABLE IN PRACTICE. The corpus")
    print("   should say so rather than describing the LIGO-band frequency as a")
    print("   detection prospect.")

    print("\nB5 REAL SOURCES, since the required factor is small enough to check:")
    print("   SNR scales as f and as 1/D^2. At the bound f = 1e-2:")
    for name, d_kpc, note in (("Cygnus X-1", 2.2, "persistent, sub-Eddington"),
                              ("V404 Cygni", 2.4, "transient, Eddington in outburst"),
                              ("GRS 1915+105", 8.6, "persistent, near-Eddington"),
                              ("Gaia BH1", 0.48, "quiescent -- Mdot ~ 0, L ~ 0")):
        snr = snr_bb * (10 / d_kpc) ** 2
        print(f"   {name:14s} {d_kpc:5.2f} kpc: SNR = {snr:.2e}  ({note})")
    d_need = 10 * np.sqrt(snr_bb)
    print(f"   Unity at the bound requires D = {d_need:.2f} kpc for an EDDINGTON")
    print(f"   accretor. That is not an absurd distance -- it is inside the known")
    print(f"   black-hole census -- but the nearby holes are quiescent (Mdot ~ 0,")
    print(f"   hence L ~ 0 by GRV-040's own law) and the Eddington-rate accretors")
    print(f"   are further out. THE SHORTFALL FOR THE BEST REAL CANDIDATE,")
    print(f"   V404 Cygni in outburst, is {1/(snr_bb*(10/2.4)**2):.0f}x in SNR.")
    print("   CORRECTED FROM AN EARLIER DRAFT OF THIS BENCHMARK, which asserted no")
    print("   such source could exist; the distance factor is modest and the real")
    print("   obstruction is the ACCRETION STATE of the nearby holes, not distance.")
    print("   The only other lever is the spectrum: a NARROWBAND whisper would permit")
    print("   coherent integration and reading (a), where the SNR is 11. GRV-041 to")
    print("   GRV-044 measured it broadband, so the corpus's own work closes that")
    print("   door -- and that measurement is now load-bearing for a negative.")


if __name__ == "__main__":
    main()
