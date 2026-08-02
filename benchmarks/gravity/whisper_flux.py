"""GRV-049 -- COMMITTING THE WHISPER'S FLUX: the frequency, the luminosity, and
the fork that decides whether anything can see it.

Bars locked in analysis/GRV049_whisper_flux_bars_LOCKED.md BEFORE computing.
"""
import numpy as np

G = 6.674e-11
C = 2.99792458e8
MSUN = 1.989e30
T_GREY = (0.04, 0.11)      # GRV-040 S2, transfer-matrix transmission
OMEGA_COEF = 0.23          # GRV-040 S1, strand scale cancels
ETA = 0.1                  # standard radiative efficiency
L_EDD_PER_MSUN = 1.26e31   # W


def kappa(M_msun):
    return C ** 3 / (4 * G * M_msun * MSUN)


def main():
    print("B1 THE FREQUENCY (omega_inf = 0.23 kappa, kappa = c^3/4GM):")
    srcs = [("stellar-mass BH", 10), ("GW150914-scale remnant", 60),
            ("Sgr A*", 4.3e6), ("M87*", 6.5e9)]
    for lab, M in srcs:
        nu = OMEGA_COEF * kappa(M) / (2 * np.pi)
        print(f"   {lab:24s} M = {M:8.1e} Msun -> nu = {nu:10.3e} Hz")
    print("   BAND ASSIGNMENT: the stellar and remnant cases (31-186 Hz) fall in")
    print("   the LIGO/Virgo acoustic band; the supermassive cases (4e-4, 3e-7 Hz)")
    print("   fall below LISA and into the pulsar-timing regime. AS ELECTROMAGNETIC")
    print("   radiation these frequencies are unusable -- 186 Hz is a 1600 km")
    print("   wavelength, far below any plasma or ionospheric cutoff.\n")

    print("B2 THE LUMINOSITY (L = f Mdot c^2 T_grey, Eddington accretion, eta = 0.1):")
    M = 10
    L_edd = L_EDD_PER_MSUN * M
    mdot_c2 = L_edd / ETA
    for tg in T_GREY:
        L = mdot_c2 * tg
        print(f"   T_grey = {tg:.2f}:  L_whisper = f x {L:.2e} W, against "
              f"L_Edd = {L_edd:.2e} W  -> f x {L/L_edd:.2f}")
    print("   THE WHISPER IS NOT A WHISPER. At f ~ 1 it carries 40-110 percent of")
    print("   the entire accretion budget, in a channel nobody has ever seen.\n")

    print("B3 THE CONFRONTATION -- observation already bounds f:")
    budget = 0.01   # a conservative allowance for an unaccounted channel
    for tg in T_GREY:
        print(f"   allowing {budget:.0%} of the budget, T_grey = {tg:.2f}: "
              f"f <= {budget * ETA / tg:.4f}")
    print("   So accreting black holes ALREADY constrain the ratchet efficiency to")
    print("   f <~ 1e-2, three orders below the energetic ceiling f <= 1 that")
    print("   GRV-040 quotes. THE PREDICTION HAS BEEN CONVERTED FROM A SIGNAL INTO")
    print("   A BOUND by data that already exists -- which is a real result, and")
    print("   not the one the corpus was hoping for.\n")

    print("B4 THE CHANNEL FORK, priced both ways:")
    print("   (A) THE WHISPER COUPLES ELECTROMAGNETICALLY. Then B3's bound applies")
    print("       and is severe (f <~ 1e-2), AND the frequencies are electro-")
    print("       magnetically unusable, so the energy would have to emerge")
    print("       reprocessed rather than at 0.23 kappa -- destroying the frequency")
    print("       signature that made the prediction distinctive in the first place.")
    print("   (B) THE WHISPER IS A MEDIUM EXCITATION NOT COUPLED TO EM. Then it")
    print("       evades the bound entirely -- and is undetectable by any existing")
    print("       instrument, since no detector for strand-medium excitations")
    print("       exists or is proposed. Unless it couples as a metric perturbation")
    print("       (which the corpus has NOT shown), the LIGO-band coincidence is")
    print("       numerology rather than a detection channel.")
    print("   NEITHER BRANCH LEAVES A CHECKABLE SIGNAL. Under (A) the signature is")
    print("   destroyed and f is bounded; under (B) there is nothing to look with.\n")

    print("B5 THE VERDICT: GRV-040 LOSES T1.")
    print("   It fails ELEC-062's checkability criterion on both branches of a fork")
    print("   the corpus cannot currently resolve. It is DEMOTED TO T2 -- distinctive")
    print("   and live, but not checkable until the coupling channel is derived.")
    print("   THE CORPUS IS LEFT WITH ONE T1 PREDICTION: PRED-003.")
    print("   WHAT WAS GAINED: a real, data-backed bound f <~ 1e-2 on the ratchet")
    print("   efficiency, and a sharply named next question -- DOES THE WHISPER")
    print("   COUPLE AS A METRIC PERTURBATION? If it does, the LIGO-band numbers")
    print("   above stop being a coincidence and become a search specification.")


if __name__ == "__main__":
    main()
