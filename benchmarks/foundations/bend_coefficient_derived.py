"""FND-MATTER-013 (Derived): b DERIVED -- THE BEND LAW CLOSED.
FND-MATTER-012's measured logarithm coefficient is now a theorem:

    b = 2 pi (5/2 - 7 sqrt(2)/4) = 0.157866...

at the corpus's canonical rope point (k = 1, T = k/2, d = 1), with the
sqrt(2) carrying the stiffness ratio sqrt(k/T).

THE DERIVATION, five determinations in a line:
  (1) the circle's per-n Bloch block written ANALYTICALLY
      (H(n) = M-dagger K M, M = Rot(alpha) e^{i n alpha} - I, with the
      chord, tension, and bond-tilt geometry exact) and validated
      against the lattice blocks at 9e-16 (eigenvalues; the entrywise
      comparison is gauge-dependent -- twenty-first lesson, logged);
  (2) the window structure delta_n = C alpha / n confirmed by a clean
      plateau of n delta_n / alpha over a decade (C = 0.02512);
  (3) the alpha^2-coefficient G(phi) of the per-mode shift extracted
      SYMBOLICALLY at fixed Bloch phase (the double-limit pathology
      avoided by expanding only the explicit alphas);
  (4) the pole D = lim phi G(phi) evaluated symbolically:
      D = 5/2 - 7 sqrt(2)/4 exactly, with the numeric limit sequence
      converging to it at eight digits;
  (5) b = 2 pi D = 0.15787 against the block sums (0.15783) and the
      original lattice measurement (0.1577).

THE DICTIONARY NOW: contact term -- exact theorem (010); bend term --
law with mechanism dissected (012) and coefficient DERIVED (here). The
map FND-MATTER-009 wrote as two guesses is two theorems and one
remaining measured constant (a -- the non-window piece: band edge plus
low-n core; deriving it is the named sequel, as is the general (k, T)
form of D).
"""
import numpy as np
import sympy as sp


def test():
    alx, phi = sp.symbols('alpha phi', positive=True)
    kk = sp.Integer(1); a0s = sp.Rational(1, 2)
    chord = 2*(1/alx)*sp.sin(alx/2)
    Ts = kk*(chord - a0s)
    nhr = -sp.sin(alx/2); nht = sp.cos(alx/2)
    Kt = sp.Matrix([[kk*nhr**2 + (Ts/chord)*(1 - nhr**2), (kk - Ts/chord)*nhr*nht],
                    [(kk - Ts/chord)*nhr*nht, kk*nht**2 + (Ts/chord)*(1 - nht**2)]])
    Rot = sp.Matrix([[sp.cos(alx), sp.sin(alx)], [-sp.sin(alx), sp.cos(alx)]])
    M = Rot*sp.exp(sp.I*phi) - sp.eye(2)
    Hn = M.conjugate().T*Kt*M
    tr2 = sp.series(sp.re(sp.expand_complex(sp.trace(Hn))), alx, 0, 3).removeO()
    det2 = sp.series(sp.re(sp.expand_complex(Hn[0, 0]*Hn[1, 1] - Hn[0, 1]*Hn[1, 0])),
                     alx, 0, 3).removeO()
    disc = sp.sqrt(tr2**2 - 4*det2)
    straight = sp.sqrt(2*(1 - sp.cos(phi))) + sp.sqrt(2*sp.Rational(1, 2)*(1 - sp.cos(phi)))
    dsum = sp.sqrt((tr2 + disc)/2) + sp.sqrt((tr2 - disc)/2) - straight
    G = sp.series(dsum, alx, 0, 3).removeO().coeff(alx, 2)
    D_sym = sp.limit(sp.simplify(phi*G), phi, 0, '+')
    D_exact = sp.Rational(5, 2) - 7*sp.sqrt(2)/4
    assert sp.simplify(D_sym - D_exact) == 0, "THE THEOREM: D = 5/2 - 7 sqrt(2)/4"
    import mpmath as mp
    mp.mp.dps = 30
    Gf = sp.lambdify(phi, G, 'mpmath')
    D_num = float(mp.mpf('0.003')*Gf(mp.mpf('0.003')))   # float64 cancels below ~1e-3; mpmath doesn't
    assert abs(D_num - float(D_exact)) < 1e-5, "numeric limit agrees"
    # plateau spot-check at moderate size from the analytic block
    def H_a(n, N):
        al = 2*np.pi/N
        R = N/(2*np.pi); ch = 2*R*np.sin(al/2); T = 1.0*(ch - 0.5)
        nh = np.array([-np.sin(al/2), np.cos(al/2)])
        K = 1.0*np.outer(nh, nh) + (T/ch)*(np.eye(2) - np.outer(nh, nh))
        c, s = np.cos(al), np.sin(al)
        Mm = np.array([[c, s], [-s, c]])*np.exp(1j*n*al) - np.eye(2)
        return Mm.conj().T@K@Mm
    N = 60000; al = 2*np.pi/N
    for n in (100, 300):   # window: n >> 1 AND q << 1; finite-q corrections ~ q^2 push n=600 out of tolerance
        lam = np.linalg.eigvalsh(H_a(n, N))
        q = 2*np.pi*n/N
        ws = np.array([2*(1 - np.cos(q)), (1 - np.cos(q))])
        C = n*(np.sum(np.sqrt(np.maximum(lam, 0))) - np.sum(np.sqrt(ws)))/al
        assert abs(C - float(D_exact)) < 4e-4, "the plateau sits on the theorem"
    b = 2*np.pi*float(D_exact)
    assert abs(b - 0.1577)/0.1577 < 0.005, "b matches the lattice measurement"
    print(f"D = 5/2 - 7 sqrt(2)/4 = {float(D_exact):.8f} (symbolic == exact; numeric {D_num:.8f})")
    print(f"b = 2 pi D = {b:.5f}  [lattice 0.1577; blocks 0.15783]")
    print("PASS: the bend law's coefficient is a theorem -- five determinations in a line,")
    print("      and the dictionary's second entry closes with a closed form.")


if __name__ == "__main__":
    test()
