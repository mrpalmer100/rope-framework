"""Analytic (calibrated-adjoint) gradient for the ELEC Poisson curve-field energy.
Tension part exact; field part via the self-energy pairing with ONE globally
calibrated constant (solver-convention scale), validated on held-out coordinates."""
import sys, importlib.util
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location("al", ROOT/"benchmarks"/"foundations"/"electron_augmented_lagrangian.py")
al = importlib.util.module_from_spec(spec); spec.loader.exec_module(al)
from rope_solver.psi.solver import solve_psi, field_energy
from rope_solver.geometry.curve import tension_energy
from rope_solver.topology.linking import hopf_curves

M = al.M_ENERGY; K = al.K


class Grad:
    def __init__(self):
        self.m = al.Model()
        self.basis = self.m.basis[M]          # (2K, M)
        self.gp = self.m.gp                    # (Ng,3)
        self.s_cal = None

    def _points(self, z):
        R = float(np.exp(z[0])); c1, c2 = hopf_curves(M, R=R)
        co = z[1:].reshape(2, 3, 2*K)
        p1 = c1 + np.einsum('ak,kn->na', co[0], self.basis)
        p2 = c2 + np.einsum('ak,kn->na', co[1], self.basis)
        cen = np.vstack([p1, p2]).mean(0)
        return p1 - cen, p2 - cen, c1, c2

    def _jacobian(self, z):
        """d(point coords)/dz for the 2M curve points (3 comps each), 97 params.
        Points are affine in z[1:]; base curves scale linearly with R = e^{z0}."""
        R = float(np.exp(z[0])); c1, c2 = hopf_curves(M, R=R)
        n = 2*M
        J = np.zeros((n, 3, len(z)))
        # z0: d(base)/dz0 = base (linear in R, dR/dz0 = R)
        J[:M, :, 0] = c1; J[M:, :, 0] = c2
        # coeffs: point a-component of curve j gets basis[k, :]
        for j in range(2):
            for a in range(3):
                for k in range(2*K):
                    idx = 1 + j*3*2*K + a*2*K + k
                    J[j*M:(j+1)*M, a, idx] = self.basis[k]
        # centering: subtract the mean over all 2M points
        J -= J.mean(axis=0, keepdims=True)
        return J

    def energy(self, z, rtol=1e-6):
        cs = self.m.curves(z, M)
        ET = float(sum(tension_energy(c, al.T0) for c in cs))
        psi = solve_psi(self.m.src(cs), self.m.H, L3=self.m.L3, rtol=rtol, maxiter=3000)
        return ET + float(al.KAPPA*field_energy(psi, self.m.H)), psi, cs

    def gradient(self, z, psi=None, cs=None):
        if psi is None:
            _, psi, cs = self.energy(z)
        p1, p2 = cs
        pts = np.vstack([p1, p2])                       # 2M curve points
        # sample set exactly as src(): points + midpoints, per curve
        def samps(c): return np.vstack([c, .5*(c + np.roll(c, -1, axis=0))])
        S1, S2 = samps(p1), samps(p2)
        SP = np.vstack([S1, S2])                        # (4M, 3)
        # nearest-sample assignment and s-values (mirror src())
        d2 = np.full(len(self.gp), np.inf); arg = np.zeros(len(self.gp), int)
        for j, p in enumerate(SP):
            dd = np.sum((self.gp - p)**2, axis=1)
            upd = dd < d2; d2[upd] = dd[upd]; arg[upd] = j
        a2 = al.A_THICK**2
        s = np.exp(-d2/(2*a2)); S = s.sum()
        # TRUE DISCRETE ADJOINT: lambda = -4 pi kappa L3^{-1} (dFE/dpsi)
        Nn = psi.shape[0]; h = self.m.H
        def DT_axis(gv, axis):
            gv = np.moveaxis(gv, axis, 0); out = np.zeros_like(gv)
            out[2:] += gv[1:-1]/(2*h); out[:-2] -= gv[1:-1]/(2*h)
            out[1] += gv[0]/h; out[0] -= gv[0]/h
            out[-1] += gv[-1]/h; out[-2] -= gv[-1]/h
            return np.moveaxis(out, 0, axis)
        gx, gy, gz = np.gradient(psi, h)
        dFE = (h**3)*(DT_axis(gx, 0) + DT_axis(gy, 1) + DT_axis(gz, 2))
        from scipy.sparse.linalg import cg as _cg
        lam_pert, _ = _cg(self.m.L3, dFE.ravel(), rtol=1e-8, maxiter=4000)
        lam = -4.0*np.pi*al.KAPPA*lam_pert
        # dE_F/d rho_x weights through rho = s/(S H^3)
        w = (lam - (lam@s)/S)/(S*h**3)
        # dE_F/d(sample p_j) = sum_x w_x * s_x * (x - p_j)/a2   [only x assigned to j]
        Gs = np.zeros_like(SP)
        coef = w*s/a2
        np.add.at(Gs, arg, coef[:, None]*(self.gp - SP[arg]))
        # samples -> curve points: sample j<M is point j; sample M+j is midpoint (j, j+1)
        def fold(Gs_c, Mn):
            Gp = Gs_c[:Mn].copy()
            mid = Gs_c[Mn:]
            Gp += .5*mid
            Gp += .5*np.roll(mid, 1, axis=0)
            return Gp
        Gp = np.vstack([fold(Gs[:2*M], M), fold(Gs[2*M:], M)])   # (2M,3)
        # tension gradient on points (exact): dL/dp_i = u(i-1->i) - u(i->i+1)
        def tgrad(c):
            e = np.roll(c, -1, axis=0) - c
            u = e/np.linalg.norm(e, axis=1, keepdims=True)
            return al.T0*(np.roll(u, 1, axis=0) - u)
        Gp += np.vstack([tgrad(p1), tgrad(p2)])
        J = self._jacobian(z)                            # (2M,3,97)
        return np.einsum('na,nap->p', Gp, J)

    def calibrate(self, z, idx_cal, idx_val, fd=2e-4):
        _, psi, cs = self.energy(z)
        self.s_cal = 1.0
        g_raw = self.gradient(z, psi, cs)
        # analytic tension part alone (for subtraction): recompute with field weight zero
        # (cheap trick: s_cal huge/small separation) -- instead compute FD of full E and of ET
        def E(zz):
            e, _, _ = self.energy(zz); return e
        def ET_only(zz):
            csz = self.m.curves(zz, M)
            return float(sum(tension_energy(c, al.T0) for c in csz))
        fd_full = {}; fd_t = {}
        for i in idx_cal + idx_val:
            d = np.zeros_like(z); d[i] = fd
            fd_full[i] = (E(z + d) - E(z - d))/(2*fd)
            fd_t[i] = (ET_only(z + d) - ET_only(z - d))/(2*fd)
        # analytic tension component via jacobian on tension-only point grads
        p1, p2 = cs
        def tgrad(c):
            e = np.roll(c, -1, axis=0) - c
            u = e/np.linalg.norm(e, axis=1, keepdims=True)
            return al.T0*(np.roll(u, 1, axis=0) - u)
        J = self._jacobian(z)
        gT = np.einsum('na,nap->p', np.vstack([tgrad(p1), tgrad(p2)]), J)
        gF_raw = g_raw - gT
        num = sum((fd_full[i] - fd_t[i])*gF_raw[i] for i in idx_cal)
        den = sum(gF_raw[i]**2 for i in idx_cal)
        self.s_cal = float(num/den)
        # validation on held-out
        gA = gT + self.s_cal*gF_raw
        errs = {}
        for i in idx_val:
            ref = fd_full[i]
            errs[i] = abs(gA[i] - ref)/max(abs(ref), 1e-8)
        # also check tension part alone against FD
        terr = max(abs(gT[i] - fd_t[i])/max(abs(fd_t[i]), 1e-8) for i in idx_cal + idx_val)
        return self.s_cal, errs, terr
