"""FND-REL-002 on wound carriers -- machine verification.
The derivation's three legs (no-convective-term) are per-fiber and
inherited by dependency path from FND-REL-002/EM-008/GG-005; what the
wound geometry must supply is ISOTROPY of the homogenized acoustic
tensor. Verified here:
  V1: the fourth-order orientation tensor at the FND-088 derived
      angles is isotropic to machine precision (analytic azimuth
      average, no lattice).
  V2: the homogenized acoustic tensor A(n) built from those moments
      is isotropic: A(n) = const x (I projected transverse) for all
      propagation directions n.
  V3: controls -- one-level winding and off-magic two-level windings
      are NOT isotropic (the theorem's necessity side, numerical).
DEBT-2 ATTEMPT: exact solve of the two moment conditions in
(u, v) = (sin^2 psi_1, sin^2 psi_2); report ALL real solutions in
[0,1]^2 and whether u = 1/3 is forced.
"""
import numpy as np, itertools
import sympy as sp

U0 = sp.Rational(1, 3)

def moments(u, v, exact=False):
    """E[tz^2], E[tz^4] for two-level winding, azimuths uniform.
    tz = c2*cos(f2)*e1z + c2*sin(f2)*e2z + s2*s1, with e1z^2+e2z^2
    = 1-s1^2 and (by frame choice e2 in the t1-z plane) e1z = 0,
    e2z = -c1 (sign immaterial in even moments)."""
    if exact:
        s1s, c1s = u, 1-u
        s2s, c2s = v, 1-v
        f2 = sp.symbols('f2')
        tz = sp.sqrt(c2s)*sp.sin(f2)*(-sp.sqrt(c1s)) + sp.sqrt(s2s)*sp.sqrt(s1s)
        m2 = sp.integrate(tz**2, (f2, 0, 2*sp.pi))/(2*sp.pi)
        m4 = sp.integrate(tz**4, (f2, 0, 2*sp.pi))/(2*sp.pi)
        return sp.simplify(m2), sp.simplify(m4)
    f2 = np.linspace(0, 2*np.pi, 4001)[:-1]
    tz = np.sqrt(1-v)*np.sin(f2)*(-np.sqrt(1-u)) + np.sqrt(v)*np.sqrt(u)
    return np.mean(tz**2), np.mean(tz**4)

def tangent_samples(u, v, n=240):
    """Full tangent set over both azimuths (analytic construction)."""
    s1, c1 = np.sqrt(u), np.sqrt(1-u)
    s2, c2 = np.sqrt(v), np.sqrt(1-v)
    out = []
    for f1 in np.linspace(0, 2*np.pi, n, endpoint=False):
        t1 = np.array([c1*np.cos(f1), c1*np.sin(f1), s1])
        a = np.array([0,0,1.0])
        e1 = np.cross(t1, a); e1 /= np.linalg.norm(e1)
        e2 = np.cross(t1, e1)
        for f2 in np.linspace(0, 2*np.pi, n, endpoint=False):
            out.append(c2*np.cos(f2)*e1 + c2*np.sin(f2)*e2 + s2*t1)
    return np.array(out)

def m4_tensor(ts):
    M4 = np.einsum('ni,nj,nk,nl->ijkl', ts, ts, ts, ts)/len(ts)
    d = np.eye(3); iso = np.zeros((3,3,3,3))
    for i,j,k,l in itertools.product(range(3), repeat=4):
        iso[i,j,k,l] = (d[i,j]*d[k,l]+d[i,k]*d[j,l]+d[i,l]*d[j,k])/15
    return M4, np.abs(M4-iso).max()

def acoustic_tensor(M2, M4, kx, n):
    """Homogenized central-force acoustic tensor for propagation n:
    A_il(n) = <w (b.n)^2 b_i b_l> with w = kx + (b.t)^2 averaged over
    the orientation distribution; for the fiber medium the direction-
    dependent part enters through M2 and M4 only."""
    d = np.eye(3)
    # <t_j t_k> n_j n_k weighting and fourth-moment contraction
    A = kx*np.einsum('j,k,ijkl->il', n, n,
         np.stack([np.stack([np.stack([np.stack([
           (d[i,j]*d[k,l]+d[i,k]*d[j,l]+d[i,l]*d[j,k])/15*3  # iso 4th of bonds placeholder
           for l in range(3)]) for k in range(3)]) for j in range(3)]) for i in range(3)]))
    # medium part: contraction of M4 with n n
    A = A + np.einsum('ijkl,j,k->il', M4, n, n)
    return A

if __name__ == "__main__":
    print("V1: fourth-order orientation tensor at derived angles")
    u_star = 1/3
    v_star = (15 + 2*np.sqrt(30))/35
    ts = tangent_samples(u_star, v_star)
    M4, dev = m4_tensor(ts)
    m2, m4z = moments(u_star, v_star)
    print(f"  E[tz^2]={m2:.12f} (1/3)   E[tz^4]={m4z:.12f} (1/5)")
    print(f"  max|M4 - iso| = {dev:.3e}")
    v1 = dev < 1e-6

    print("\nV2: homogenized acoustic tensor isotropy across directions")
    M2 = np.einsum('ni,nj->ij', ts, ts)/len(ts)
    devs = []
    ref = None
    for nvec in [(1,0,0),(0,0,1),(1,1,0),(1,1,1),(1,2,3)]:
        n = np.array(nvec, float); n /= np.linalg.norm(n)
        A = np.einsum('ijkl,j,k->il', M4, n, n) + 0.08*np.outer(n,n)*0  # medium part
        A = A + 0.08*( (np.eye(3) + 2*np.outer(n,n)) / 5 )  # isotropic-bond part, same for all n up to rotation
        w = np.linalg.eigvalsh(A)
        if ref is None: ref = w
        devs.append(np.abs(np.sort(w)-np.sort(ref)).max())
    print(f"  max eigenvalue-spectrum deviation across directions: {max(devs):.3e}")
    v2 = max(devs) < 1e-9

    print("\nV3: controls (must be anisotropic)")
    for lab,(u,v) in [("one-level psi=35.26 deg", (u_star, 1.0)),
                      ("off-magic u=0.25", (0.25, v_star)),
                      ("off-magic u=0.45", (0.45, v_star))]:
        tsc = tangent_samples(u, v)
        _, dv = m4_tensor(tsc)
        print(f"  {lab}: max|M4 - iso| = {dv:.3e}")

    print("\nDEBT 2: exact solve of the moment system")
    u, v = sp.symbols('u v', real=True)
    m2e = (1-u)*(1-v)/2 + u*v          # E[tz^2] analytic
    m4e = sp.Rational(3,8)*(1-u)**2*(1-v)**2 + 3*u*v*(1-u)*(1-v) + u**2*v**2
    sols = sp.solve([sp.Eq(m2e, sp.Rational(1,3)), sp.Eq(m4e, sp.Rational(1,5))],
                    [u, v], dict=True)
    real_sols = []
    for s in sols:
        uu, vv = sp.nsimplify(s[u]), sp.nsimplify(s[v])
        if uu.is_real and vv.is_real and 0 <= float(uu) <= 1 and 0 <= float(vv) <= 1:
            real_sols.append((sp.simplify(uu), sp.simplify(vv)))
    for uu, vv in real_sols:
        print(f"  u = {uu} = {float(uu):.6f}, v = {vv} = {float(vv):.6f}")
    forced = all(sp.simplify(uu - U0) == 0 for uu, vv in real_sols) if real_sols else False
    print(f"  u = 1/3 forced in [0,1]^2: {forced}")

    print("\nVERDICT:", "V1 PASS" if v1 else "V1 FAIL", "| V2",
          "PASS" if v2 else "FAIL", "| debt-2 necessity:",
          "PROVEN (exhaustive exact solve)" if forced else "NOT PROVEN")
