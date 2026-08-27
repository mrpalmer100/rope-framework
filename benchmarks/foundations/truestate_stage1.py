"""COMMISSION TRUE-STATE, STAGE 1 (FND-140, 2026-08-18) -- the true
composite relative equilibrium and the Sigma_wave re-pricing.

Executed under analysis/TRUESTATE_stage1_bars_LOCKED.md.
Co-rotating equations (adjudicated force law, kb = 0, mu = 1):
    (T w')' + Omega^2 w = 0,   T = F/z',   z' = sqrt(1 - |w'|^2).
Units: T0_f = a_f = c = 1.
"""
import numpy as np
from scipy.optimize import fsolve

S1 = 1 / 3
S2 = (15 + 2 * np.sqrt(30)) / 35
C1, C2 = np.sqrt(S1), np.sqrt(S2)
B = 1 / (2 * np.pi)
R1 = B * np.sqrt(1 / C1 ** 2 - 1)
R2 = B * np.sqrt(1 / C2 ** 2 - 1)
TBAR = 1.5
K1 = 2 * np.pi / np.sqrt(3)          # level-1 arc wavenumber (arc/axial = sqrt 3)

ok = True
print("COMMISSION TRUE-STATE, STAGE 1 -- the rigidly rotating composite\n")

# ------------------------------------------------------------- CONTROL 0
print("CONTROL 0 -- the level-1 member (single mode, closed form)")
om_l1 = K1 * np.sqrt(TBAR)
print(f"  Omega = k1 sqrt(T) = {om_l1:.4f} c/a_f vs registered 4.4429  "
      f"[{'PASS' if abs(om_l1-4.4429) < 1e-3 else 'HALT'}]")
print(f"  |w'| = R1 k1 = {R1*K1:.6f} = sin(psi_1) = {np.sqrt(1-S1):.6f}, "
      f"z' = {np.sqrt(1-(R1*K1)**2):.6f} = cos-axial {C1:.6f}")
ok &= abs(om_l1 - 4.4429) < 1e-3
if not ok:
    raise SystemExit(1)

# ------------------------------------------------------------- OBSTRUCTION
print("\nOBSTRUCTION LEG -- no pure two-mode member")
print("  |w'|^2 for w = A1 e^{i k1 s} + A2 e^{i k2 s} contains a term")
print("  2 k1 k2 A1 A2 cos((k1 - k2) s): z' and T oscillate at the")
print("  difference wavenumber, and (T w')' then carries harmonics")
print("  k1 -+ (k1 - k2), ... outside the two modes. A two-mode w cannot")
print("  close the equation: the true state carries a harmonic TAIL.")
print("  (This is the structural reason FND-139 measured the superposed")
print("  ansatz order-one off-shell, pre-registered in the bars.)")

# ------------------------------------------------------------- THE SOLVE
# clean formulation: hard pins, least-squares, continuation in R2 pin.
from scipy.optimize import least_squares

Lcell = 2 * np.sqrt(3)
NH = 24
NG = 160
sgrid = np.arange(NG) / NG * Lcell
kn = 2 * np.pi / Lcell * np.arange(-NH, NH + 1)
NM = 2 * NH + 1
E = np.exp(1j * np.outer(sgrid, kn))
n1 = 2

def residual_vec(x, A2pin, sgn):
    n2i = 3 * sgn + NH
    n1i = n1 + NH
    # unpack: coefficients except c_{n1} (fixed real A1=R1); c_{n2} free
    c = np.zeros(NM, dtype=complex)
    idx = [i for i in range(NM) if i != n1i]
    c[idx] = x[:NM - 1] + 1j * x[NM - 1:2 * (NM - 1)]
    c[n1i] = R1
    Om, F = x[-2], x[-1]
    wp = E @ (1j * kn * c)
    zp2 = 1 - np.abs(wp) ** 2
    if zp2.min() <= 1e-9:
        return np.full(2 * NM + 2, 1e2)
    zp = np.sqrt(zp2)
    T = F / zp
    Twp_c = np.conj(E).T @ (T * wp) / NG
    res = E @ (1j * kn * Twp_c) + Om ** 2 * (E @ c)
    rc = np.conj(E).T @ res / NG
    return np.concatenate([rc.real, rc.imag,
                           [np.mean(T) - TBAR,
                            np.abs(c[n2i]) - A2pin]])

print("\nTHE SOLVE -- continuation from the exact level-1 member")
print(f"  cell q = 3/2, harmonics -{NH}..{NH}, grid {NG}; pins hard;")
print("  least-squares (a true solution must reach cost ~ 0)\n")
results = {}
for sgn in (+1, -1):
    n2i = 3 * sgn + NH
    x = np.zeros(2 * (NM - 1) + 2)
    x[-2], x[-1] = om_l1, TBAR * C1        # exact level-1 member
    tag = "sign=+1 (co-handed)" if sgn > 0 else "sign=-1 (counter-handed)"
    print(f"  {tag}:")
    converged_full = None
    for A2pin in (1e-3, 3e-3, 1e-2, 0.03, R2):
        # seed the n2 mode at the pin
        cseed = x[:NM - 1] + 1j * x[NM - 1:2 * (NM - 1)]
        j = n2i if n2i < n1 + NH else n2i - 1
        if abs(cseed[j]) < A2pin / 2:
            x[j] = A2pin
        sol = least_squares(residual_vec, x, args=(A2pin, sgn),
                            xtol=3e-16, ftol=3e-16, gtol=3e-16,
                            max_nfev=4000)
        rn = np.linalg.norm(sol.fun)
        print(f"    R2 pin = {A2pin:.4f}:  |residual| = {rn:.3e}   "
              f"Omega = {sol.x[-2]:.4f}  F = {sol.x[-1]:.4f}")
        if rn < 1e-9:
            x = sol.x
            if abs(A2pin - R2) < 1e-12:
                converged_full = sol
        else:
            print("      -> branch does not close at this pin; stopping"
                  " continuation for this sign")
            break
    results[sgn] = converged_full

print("\nFINAL LEG -- comparison (registered numbers appear here only)")
print("  registered box (kb=0 edges): 3.222 (anti-aligned) / 3.826 (aligned)")
print("  FND-139 refit display:       3.089 (anti, railed) / 3.335 (aligned)")
priced = False
for sgn in (+1, -1):
    sol = results.get(sgn)
    if sol is None:
        print(f"  sign={sgn:+d}: NO rigidly-rotating state at the registered"
              " pins (see continuation)")
        continue
    priced = True
    n1i = n1 + NH
    c = np.zeros(NM, dtype=complex)
    idx = [i for i in range(NM) if i != n1i]
    c[idx] = sol.x[:NM - 1] + 1j * sol.x[NM - 1:2 * (NM - 1)]
    c[n1i] = R1
    Om, F = sol.x[-2], sol.x[-1]
    wp = E @ (1j * kn * c); zp = np.sqrt(1 - np.abs(wp) ** 2)
    ke = 0.5 * Om ** 2 * np.mean(np.abs(E @ c) ** 2)
    Sig = (1 / np.mean(zp)) * (1 + ke)
    print(f"  TRUE-STATE sign={sgn:+d}: Sigma_wave(kb=0) = {Sig:.4f} T0")

print("\nVERDICT: written after the run -- see results doc.")
raise SystemExit(0)
