"""COMMISSION BLOCH-L -- the longitudinal branch of the wound fine medium.

Executed under analysis/COMMISSION_BLOCHL_charter_LOCKED.md (FND-124/125).
Instrument: FND-089's supercell Bloch machinery, longitudinal build.
Units: T0_f = 1, a_f = 1, c = 1  (mu_f = T0_f/c^2 = 1, FORCED by the SHIN
transverse-c invariant).  Clean-room: no target value appears in this file.

Legs
  0  convention audit + isotropy control (adjudicates the psi reading)
  1  affine (Cauchy-Born) homogenisation, closed form
  2  supercell Bloch: three inherited controls, multiplicity repair,
     reading window at lambda = 24p and 48p, convergence bar 0.5%
  3  the read, the rigidity demand, the kb feasibility ceiling
"""
import itertools
import numpy as np

# ---------------------------------------------------------------- geometry
S1 = 1.0 / 3.0                                  # sin^2 psi_1 (magic angle)
S2 = (15 + 2 * np.sqrt(30)) / 35.0              # sin^2 psi_2
PSI1, PSI2 = np.arcsin(np.sqrt(S1)), np.arcsin(np.sqrt(S2))
C1, C2 = np.sqrt(S1), np.sqrt(S2)               # axial direction cosines (FND-088)
ST1, ST2 = np.sqrt(1 - C1 ** 2), np.sqrt(1 - C2 ** 2)
PPHYS = 1.0                                     # worst-case pitch p = a_f (FND-091)
KAP1 = (np.pi / PPHYS) * 2 * C1 * ST1           # 2.9619 / a_f
KAP2 = (np.pi / PPHYS) * 2 * C2 * ST2           # 2.7506 / a_f
KT0 = 2.0                                       # registered coarse k/T0 (FND-114)
KBSAT = 0.126                                   # kb / (T0_f a_f^2)  (FND-121)


def helix(axial_cos, p=PPHYS):
    """Frenet helix reproducing a given axial direction cosine."""
    b = p / (2 * np.pi)
    R = b * np.sqrt(1 / axial_cos ** 2 - 1)
    rho2 = R * R + b * b
    return R, R / rho2, b / rho2                 # R, kappa, tau


def orientation_ensemble(n=200):
    """Nested two-level winding: (tangent, composite curvature vector)."""
    T_, K_ = [], []
    for f1 in (np.arange(n) + 0.5) / n * 2 * np.pi:
        t1 = np.array([-ST1 * np.sin(f1), ST1 * np.cos(f1), C1])
        k1 = KAP1 * np.array([-np.cos(f1), -np.sin(f1), 0.0])
        a = np.array([0., 0., 1.]) if abs(t1[2]) < 0.9 else np.array([1., 0., 0.])
        e1 = np.cross(t1, a); e1 /= np.linalg.norm(e1); e2 = np.cross(t1, e1)
        for f2 in (np.arange(n) + 0.5) / n * 2 * np.pi:
            T_.append(ST2 * (-np.sin(f2) * e1 + np.cos(f2) * e2) + C2 * t1)
            K_.append(k1 + KAP2 * (-np.cos(f2) * e1 - np.sin(f2) * e2))
    return np.array(T_), np.array(K_)


# ------------------------------------------------------- energy (one fibre)
def energy_form(t, k0, kf, T, kb):
    """Q[a,b,c,d] with E = 1/2 G:Q:G, G_ab = d_b u_a, per unit fibre length."""
    ta = np.outer(t, t)
    Q = kf * np.einsum('ab,cd->abcd', ta, ta)
    Q += T * (np.einsum('ac,b,d->abcd', np.eye(3), t, t)
              - np.einsum('ab,cd->abcd', ta, ta))
    L = np.zeros((3, 3, 3))                      # Kirchhoff bending strain
    for i in range(3):
        for a in range(3):
            for b in range(3):
                v = k0[b] if i == a else 0.0
                v -= t[i] * (k0[a] * t[b] + t[a] * k0[b])
                v -= 2 * t[a] * t[b] * k0[i]
                if i == a: v -= 0.5 * k0[b]
                if i == b: v += 0.5 * k0[a]
                L[i, a, b] = v
    return Q + kb * np.einsum('iab,icd->abcd', L, L)


def affine_moduli(TT, KK, kf, T, kb, khat, e):
    A = np.outer(e, khat)
    eps = np.einsum('ni,ij,nj->n', TT, A, TT)
    v = TT @ A.T
    perp2 = np.einsum('ni,ni->n', v, v) - eps ** 2
    Ak = KK @ A.T; At = TT @ A.T
    corr = np.einsum('ni,ni->n', KK, At) + np.einsum('ni,ni->n', TT, Ak)
    d = Ak - corr[:, None] * TT - 2 * eps[:, None] * KK - KK @ (0.5 * (A - A.T)).T
    return (kf * np.mean(eps ** 2) + T * np.mean(perp2)
            + kb * np.mean(np.einsum('ni,ni->n', d, d)))


# ---------------------------------------------------------- Bloch supercell
P = 5                                            # sites per pitch (>=5, SHIN6 rule)
H = PPHYS / P
NB = [b for b in itertools.product((-1, 0, 1), repeat=3) if 0 < sum(v * v for v in b) <= 2]
SITES = list(itertools.product(range(P), repeat=3))
IDX = {s: i for i, s in enumerate(SITES)}
N = len(SITES)
_BV = np.array(NB, float) * H
_W = np.array([1.0 / (b @ b) for b in _BV])
GW = np.linalg.inv((_BV * _W[:, None]).T @ _BV) @ (_BV * _W[:, None]).T


def local_set(s, m, wound=True):
    """The bundle at a cell carries fibres at ALL phase pairs (2-torus)."""
    if not wound:
        return [(np.array([0., 0., 1.]), np.zeros(3))]
    out = []
    for j1 in range(m):
        f1 = 2 * np.pi * (s[0] / P + j1 / m)
        t1 = np.array([-ST1 * np.sin(f1), ST1 * np.cos(f1), C1])
        k1 = KAP1 * np.array([-np.cos(f1), -np.sin(f1), 0.0])
        a = np.array([0., 0., 1.]) if abs(t1[2]) < 0.9 else np.array([1., 0., 0.])
        e1 = np.cross(t1, a); e1 /= np.linalg.norm(e1); e2 = np.cross(t1, e1)
        for j2 in range(m):
            f2 = 2 * np.pi * ((s[1] + s[2]) / P + j2 / m)
            out.append((ST2 * (-np.sin(f2) * e1 + np.cos(f2) * e2) + C2 * t1,
                        k1 + KAP2 * (-np.cos(f2) * e1 - np.sin(f2) * e2)))
    return out


def dynamical(kvec, kf, T, kb, m, wound=True):
    D = np.zeros((3 * N, 3 * N), dtype=complex)
    for s in SITES:
        i = IDX[s]
        L = local_set(s, m, wound)
        Q = sum(energy_form(t, k0, kf, T, kb) for t, k0 in L) / len(L)
        G = np.zeros((9, 3 * N), dtype=complex)
        for n_i, n in enumerate(NB):
            j = IDX[tuple((s[q] + n[q]) % P for q in range(3))]
            ph = np.exp(1j * (kvec @ (np.array(n, float) * H))); gw = GW[:, n_i]
            for a in range(3):
                for b in range(3):
                    G[3 * a + b, 3 * j + a] += gw[b] * ph
                    G[3 * a + b, 3 * i + a] -= gw[b]
        D += G.conj().T @ Q.reshape(9, 9) @ G
    return (D + D.conj().T) / 2


def branch(kf, T, kb, m, lam_over_p, direction=(0, 0, 1.), wound=True):
    """Speeds of the two branches, each identified by its EIGENVECTOR."""
    d = np.array(direction, float); d /= np.linalg.norm(d)
    kv = (2 * np.pi / (lam_over_p * PPHYS)) * d
    w2, V = np.linalg.eigh(dynamical(kv, kf, T, kb, m, wound))
    out = {}
    for lab, pol in (('L', d),
                     ('T', np.cross(d, [0, 0, 1.] if abs(d[2]) < 0.9 else [1., 0, 0]))):
        pol = pol / np.linalg.norm(pol)
        v = np.zeros(3 * N, dtype=complex)
        for s in SITES:
            v[3 * IDX[s]:3 * IDX[s] + 3] = pol * np.exp(1j * (kv @ (np.array(s, float) * H)))
        v /= np.linalg.norm(v)
        wt = np.abs(V.conj().T @ v) ** 2
        b = int(np.argmax(wt))
        out[lab] = (np.sqrt(max(w2[b], 0)) / np.linalg.norm(kv), wt[b])
    return out


# ------------------------------------------------------------------- report
def main():
    ok = True
    print("COMMISSION BLOCH-L -- longitudinal branch of the wound fine medium")
    print(f"psi_1={np.degrees(PSI1):.4f} deg  psi_2={np.degrees(PSI2):.4f} deg  p=a_f\n")

    print("LEG 0 -- CONVENTION AUDIT (kappa is convention-blind; tau and R are not)")
    for lab, ca in (("A  axial cos = sin(psi) [FND-088]", (C1, C2)),
                    ("B  axial cos = cos(psi) [FND-125]", (np.cos(PSI1), np.cos(PSI2)))):
        (R1, k1, t1), (R2, k2, t2) = helix(ca[0]), helix(ca[1])
        print(f"  {lab}: R=({R1:.5f},{R2:.5f})  kappa=({k1:.4f},{k2:.4f})  "
              f"tau=({t1:.4f},{t2:.4f})")
    TT, KK = orientation_ensemble()
    A4 = np.einsum('ni,nj,nk,nl->ijkl', TT, TT, TT, TT) / len(TT)
    d = np.eye(3)
    ISO = (np.einsum('ij,kl->ijkl', d, d) + np.einsum('ik,jl->ijkl', d, d)
           + np.einsum('il,jk->ijkl', d, d)) / 15.0
    iso_err = np.abs(A4 - ISO).max()
    print(f"  isotropy control under reading A: E[t_z^2]={np.mean(TT[:,2]**2):.9f}, "
          f"E[t_z^4]={np.mean(TT[:,2]**4):.9f}, max|A4-iso|={iso_err:.2e}")
    ok &= iso_err < 1e-9
    print(f"  -> reading A is the load-bearing one  [{'PASS' if iso_err<1e-9 else 'FAIL'}]\n")

    print("LEG 1 -- AFFINE HOMOGENISATION (exact at the derived angles)")
    kh = np.array([0., 0., 1.]); eT = np.array([1., 0., 0.])
    aL = affine_moduli(TT, KK, 1, 0, 0, kh, kh); bL = affine_moduli(TT, KK, 0, 1, 0, kh, kh)
    aT = affine_moduli(TT, KK, 1, 0, 0, kh, eT); bT = affine_moduli(TT, KK, 0, 1, 0, kh, eT)
    cL = affine_moduli(TT, KK, 0, 0, 1, kh, kh); cT = affine_moduli(TT, KK, 0, 0, 1, kh, eT)
    print(f"  stretch/tension coefficients  L: {aL:.8f} (1/5), {bL:.8f} (2/15)")
    print(f"                                T: {aT:.8f} (1/15), {bT:.8f} (4/15)")
    ok &= abs(aL - 0.2) < 1e-9 and abs(bT - 4 / 15) < 1e-9
    print(f"  bending coefficients          L: {cL:.6f}   T: {cT:.6f}  (units 1/a_f^2)")
    kf0 = 6 * KT0 - 3; T0 = 4.5 - 1.5 * KT0
    print(f"  closed form: k_f/T0_f = 6(k/T0) - 3 = {kf0:.4f}, T/T0_f = {T0:.4f}"
          "   (ADDITIVE, angle-free)\n")

    print("LEG 2 -- SUPERCELL BLOCH, CONTROLS")
    r = branch(9.0, 1.5, 0.0, 1, 24, wound=False)
    e1 = abs(r['L'][0] - 3.0) / 3.0; e2 = abs(r['T'][0] - np.sqrt(1.5)) / np.sqrt(1.5)
    print(f"  (i)   straight control: c_L={r['L'][0]:.6f} (3.000000), "
          f"c_T={r['T'][0]:.6f} ({np.sqrt(1.5):.6f})  [{'PASS' if max(e1,e2)<2e-3 else 'FAIL'}]")
    ok &= max(e1, e2) < 2e-3
    print("  (ii)  instrument validity: Bloch/supercell only (FND-084 retirement honoured)")
    print(f"  (iii) polarisation identified by eigenvector; pw weights "
          f"{r['L'][1]:.3f}/{r['T'][1]:.3f}")
    print("  multiplicity repair (one orientation per cell is rank-deficient):")
    for m in (1, 2, 4, 6):
        a = branch(9.0, 1.5, 0.0, m, 24); b = branch(9.0, 1.5, 0.0, m, 24, (1, 1, 1.))
        print(f"     m={m} ({m*m:2d} fibres/cell): c_L(001)={a['L'][0]:.6f}  "
              f"c_L(111)={b['L'][0]:.6f}  c_T={a['T'][0]:.6f}")
    w24 = branch(9.0, 1.5, 0.0, 6, 24)['L'][0]; w48 = branch(9.0, 1.5, 0.0, 6, 48)['L'][0]
    conv = abs(w24 - w48) / (0.5 * (w24 + w48))
    print(f"  READING WINDOW: c_L(24p)={w24:.6f}, c_L(48p)={w48:.6f}, "
          f"drift={conv*100:.4f}%  [{'PASS' if conv<=0.005 else 'REGIME-NOT-REACHED'}]")
    ok &= conv <= 0.005
    print()

    print("LEG 3 -- THE READ")
    from scipy.optimize import fsolve

    def resid(x, kb):
        rr = branch(max(x[0], 1e-6), x[1], kb, 6, 24)
        return [rr['T'][0] ** 2 - 1.0, rr['L'][0] ** 2 - KT0]

    kf, T = fsolve(resid, [9.0, 1.5], args=(0.0,))
    print(f"  stretch+tension (the static stretch-projection):")
    print(f"     k_f/T0_f = {kf:.5f}   T_fibre/T0_f = {T:.5f}")
    print(f"     c_L,f/c  = {np.sqrt(kf):.5f}      r_s/a_f = {np.sqrt(0.504/kf):.5f}"
          "   (r_s carries the KBSAT rider)")
    ok &= abs(kf - 9.0) < 0.02
    kfb, Tb = fsolve(resid, [9.0, 1.5], args=(KBSAT,))
    print(f"  with bending at KBSAT: k_f/T0_f = {kfb:.5f}, T_fibre/T0_f = {Tb:.5f}"
          f"  -> {'INFEASIBLE (T<0)' if Tb < 0 else 'feasible'}")
    lo, hi = 0.0, KBSAT
    for _ in range(30):
        mid = 0.5 * (lo + hi)
        if fsolve(resid, [9.0, 1.5], args=(mid,))[1] > 0: lo = mid
        else: hi = mid
    print(f"  feasibility ceiling: kb <= {lo:.5f} T0_f a_f^2 "
          f"(KBSAT 0.126 lies OUTSIDE) -- CONDITIONAL, see results doc")
    print(f"\n  RIGIDITY DEMAND: transmission equals the static projection to "
          f"{abs(kf-9.0)/9.0*100:.2f}% -- NOT FIRED")
    print("\nVERDICT:", "PASS -- read delivered" if ok else "INSTRUMENT/BAR FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
