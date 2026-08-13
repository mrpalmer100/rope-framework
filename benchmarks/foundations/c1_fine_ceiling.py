"""COMMISSION C1 -- the fine-ceiling exhibition on the SHIN engine.

Executed under analysis/C1_fine_ceiling_bars_LOCKED.md. Instrument
inherited verbatim from shin6_3d_bloch.py (18-neighbour stencil,
g = 2 shell weighting, derived angles, straight-medium acoustic
normalization). Certificate: S = omega_max/(c_eff/a_f) >= pi/2.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
import itertools
from shin6_3d_bloch import build_cell, dyn_matrix, norm_scale

PI = np.pi

def omega_max(P, sites, T, PR, ngrid):
    ks = np.linspace(-PI, PI, ngrid, endpoint=False)
    om = 0.0
    for kx in ks:
        for ky in ks:
            for kz in ks:
                D = dyn_matrix(np.array([kx, ky, kz]), P, sites, T, PR)
                w2 = np.linalg.eigvalsh(D)
                om = max(om, np.sqrt(max(w2.max(), 0.0)))
    return om

def run(f, wound, label):
    P, sites, T, PR = build_cell(f, wound)
    Ps, ss, Ts, PRs = build_cell(f, False)
    c_eff = norm_scale(Ps, ss, Ts, PRs)   # acoustic slope, straight medium
    o9 = omega_max(P, sites, T, PR, 9)
    o13 = omega_max(P, sites, T, PR, 13)
    S9, S13 = o9/c_eff, o13/c_eff
    stable = abs(S13 - S9)/S9 <= 0.02
    S = S13
    print(f"  {label}: P={P} c_eff={c_eff:.4f} "
          f"S(9^3)={S9:.4f} S(13^3)={S13:.4f} stable={stable} "
          f"-> S = {S:.4f} {'>=' if S >= PI/2 else '<'} pi/2={PI/2:.4f}")
    return S, stable

def main():
    print("C1 -- fine-ceiling exhibition (locked bars; certificate S >= pi/2)")
    print("\nStraight control:")
    Sc, stc = run(1/5, False, "straight")
    print("\nWound members:")
    S3, st3 = run(1/3, True, "f=1/3 (context)")
    S4, st4 = run(1/4, True, "f=1/4 (context)")
    S5, st5 = run(1/5, True, "f=1/5 (ADJUDICATING)")
    ok = (S5 >= PI/2) and (Sc >= PI/2) and st5 and stc
    print(f"\nVERDICT: {'C1-CERTIFIED' if ok else 'C1-FAILED or UNSTABLE (kept)'}")
    print(f"  adjudicating S = {S5:.4f}; certificate needs >= {PI/2:.4f}")
    print(f"  label gap at window edge: E_gap = S x (4/2pi) x 1.4 PeV = "
          f"{S5*(4/(2*PI))*1.4:.3f} PeV (m = 1)")

if __name__ == "__main__":
    main()
