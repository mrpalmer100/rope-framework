"""GRV-092: the quantum of the ring -- THE FOURTH CANCELLATION. The snap action
A* = e_bit/omega_loc is independent of depth AND of the black hole's mass: the
horizon mechanism secretes a universal action constant of the medium. Evaluated
against hbar: each snap is a sub-quantum coherent pulse (n_q ~ 1e-4 on F-Lor),
so the whisper is CLASSICAL radiation at leading order -- waves, not gravitons
-- and the fork gains its third internal discriminator.
Bars locked in analysis/GRV092_ring_quantum_bars_LOCKED.md.
"""
import numpy as np
import sympy as sp

HBAR = 1.0546e-34
H_CORE = 1.87e-19
BETA = 35.4
RING = 0.23
FORKS = {"F-Lor": (1.0e-16, 3.6e35, 5.1e35),
         "F-Sak": (1.26e-34, 2.3e71, 3.2e71)}


def b1_fourth_cancellation():
    sig, kap, c, Sg, a, chi, h, beta, w0 = sp.symbols(
        'sigma kappa c Sigma a chi h beta omega_0', positive=True)
    e_bit = beta * Sg * a**3 * h / (chi * sig)          # the snap energy
    alpha = kap * sig / c                                # Tolman lapse
    w_loc = (w0 * kap) / alpha                           # blueshifted ring
    A = sp.simplify(e_bit / w_loc)
    assert sp.diff(A, sig) == 0
    assert sp.diff(A, kap) == 0
    assert sp.simplify(A - beta * Sg * a**3 * h / (chi * c * w0)) == 0
    print("B1 PASS  THE FOURTH CANCELLATION, by machine: sigma cancels between")
    print("         the snap energy (~1/sigma, the pressing) and the local ring")
    print("         frequency (~1/sigma, the blueshift), and kappa cancels with")
    print("         it -- the snap ACTION")
    print("           A* = e_bit/omega_loc = (beta/0.23) Sigma a^3 h/(chi c)")
    print("         is independent of DEPTH and of the BLACK HOLE'S MASS: a")
    print("         universal action constant of the medium, secreted by the")
    print("         horizon chain without being asked for one.")


def main():
    b1_fourth_cancellation()
    print("B2       evaluation against hbar (chi = 1-3 bracket):")
    nq = {}
    for fork, (a, Slo, Shi) in FORKS.items():
        vals = []
        for S in (Slo, Shi):
            for chi in (1.0, 3.0):
                A = (BETA / RING) * S * a**3 * H_CORE / (chi * 2.998e8)
                vals.append(A / HBAR)
        nq[fork] = (min(vals), max(vals))
        print(f"           {fork}: n_q = A*/hbar = {min(vals):.1e} .. "
              f"{max(vals):.1e}")
    lo, hi = nq["F-Lor"]
    assert hi < 0.1
    print("B3       INTERPRETATION per the locked grammar (n_q << 1 branch):")
    print("         each snap is a SUB-QUANTUM coherent pulse -- on the")
    print(f"         favourable fork, one graviton's worth of action per")
    print(f"         {1/hi:.0f}..{1/lo:.0f} snaps. THE WHISPER IS CLASSICAL")
    print("         GRAVITATIONAL RADIATION at leading order: many overlapping")
    print("         sub-quantum snaps building a wave, with hbar-quantized")
    print("         emission occurring only at the thinned rate (snap rate x")
    print("         n_q). This is a sharp structural DIVERGENCE from Hawking,")
    print("         whose emission is quantized at hbar omega by construction:")
    print("         the corpus's horizon radiates WAVES, NOT GRAVITONS, and a")
    print("         quantization-sensitive measurement of the whisper would")
    print("         find no shot structure at hbar omega_ring.")
    ratio = nq["F-Lor"][0] / nq["F-Sak"][1]
    print(f"B4       THE FORK'S THIRD DISCRIMINATOR: n_q differs between forks")
    print(f"         by {np.log10(ratio):.0f} orders (a^3-driven) -- joining")
    print("         the Hawking coefficient (18 orders) and the PVLAS-class")
    print("         nonlinearity as internal fork levers. THE RESIDUE, stated")
    print("         honestly: A* != hbar convicts nothing -- the corpus has")
    print("         never derived that gravitational emission is hbar-")
    print("         quantized, and tonight's product is the RATIO, its")
    print("         universality, and the sharpened question the L1 frontier")
    print("         now owns: the medium carries its OWN action constant,")
    print("         (beta/0.23) Sigma a^3 h/(chi c), depth- and mass-blind;")
    print("         WHY it sits 3-4 orders under hbar (F-Lor) is the hbar")
    print("         question wearing measurable clothes. Named next: whether")
    print("         the SAME combination Sigma a^3 h/c appears in the corpus's")
    print("         registered hbar relations (GRV-075's G formula; HBAR-005;")
    print("         PRED-003's alpha) -- a cross-registry action audit, one")
    print("         session, purely internal.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
