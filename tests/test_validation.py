"""
tests/test_validation.py  --  Pin each module to analytic ground truth.

Run:  python3 tests/test_validation.py

Catches the class of errors this programme has repeatedly surfaced
(spring-vs-tension force, soft-potential unlinking, placeholder potentials).

BOUNDARY NOTE (documented limitation, not a bug): the psi solver uses
Dirichlet (psi->0) boundaries. A finite grid cannot represent the slow 1/r
falloff of a point source at the grid EDGE, so the discrete Laplacian of an
analytic 1/r profile shows spurious residuals within a few nodes of the
boundary. Physics calculations use smooth localised sources and measure
energy in the interior, where this is negligible. Tests exclude a boundary
layer and use a resolved (smoothed) source.
"""
import numpy as np
import sys
from rope_solver.psi.solver import grid, solve_psi, laplacian_3d
from rope_solver.topology.linking import linking_number, torus_link, hopf_curves
from rope_solver.geometry.curve import tension_force, tension_energy

results = []
def check(name, cond, detail=""):
    results.append((name, cond))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}  {detail}")

print("="*64); print("VALIDATION SUITE"); print("="*64)

print("\n1. Laplacian operator: exact on a plane wave")
N, L = 40, 6.0
coords, X, Y, Z, h = grid(N, L)
L3 = laplacian_3d(N, h)
k = 2*np.pi/L*2
f = np.sin(k*X)
lap_f = (L3 @ f.flatten()).reshape(N,N,N)
ana = -k**2*f
s = slice(5, N-5)
ratio = np.median(lap_f[s,s,s]/(ana[s,s,s]+1e-12))
check("nabla^2 sin(kx) = -k^2 sin(kx)", abs(ratio-1)<0.03, f"ratio={ratio:.4f}")

print("\n2. psi solver: smoothed point source ~ 1/r in the interior")
N, L = 56, 10.0
coords, X, Y, Z, h = grid(N, L)
Rg = np.sqrt(X**2+Y**2+Z**2)
src = np.exp(-(Rg/0.4)**2/2); src = src/(src.sum()*h**3)
psi = solve_psi(src, h)
bl = 6
interior = np.zeros((N,N,N), bool)
interior[bl:N-bl, bl:N-bl, bl:N-bl] = True
shell = (Rg>1.5)&(Rg<3.0)&interior
# Dirichlet finite-box solution is Q/r - Q/(L/2): boundary forces psi->0
# at the edge, a constant offset that the test must include. Verified by
# box-size scaling (ratio -> 1 as L -> inf).
pert = (psi-1.0)[shell]
ana_inf = 1.0/Rg[shell]                      # infinite-space Q/r (Q=1)
ana_box = 1.0/Rg[shell] - 1.0/(L/2)          # Dirichlet box correction
corr = np.corrcoef(pert, ana_inf)[0,1]       # shape unaffected by offset
ratio = np.median(pert/ana_box)
check("psi ~ 1/r shape (interior, corr>0.999)", corr>0.999, f"corr={corr:.5f}")
check("psi normalisation, box-corrected (ratio~1)", abs(ratio-1)<0.25,
      f"ratio={ratio:.3f}")

print("\n3. Brill-Lindquist psi=1+rs/4r harmonic (interior, away from source)")
psi_bl = 1.0 + 0.25/np.maximum(Rg, h)
lap = (L3b := laplacian_3d(N, h)) @ (psi_bl-1.0).flatten()
lap = lap.reshape(N,N,N)
far = (Rg>1.5)&interior
mx = np.abs(lap[far]).max()
check("nabla^2(1+rs/4r) ~ 0 (interior)", mx<0.01, f"max={mx:.4f}")

print("\n4. linking number: known links give known integers")
C1, C2 = hopf_curves(60, R=1.0)
lkh = linking_number(C1, C2)
check("Hopf link Lk=1", abs(abs(lkh)-1.0)<0.1, f"Lk={lkh:.3f}")
for n in [1,2,3]:
    A, B = torus_link(80, n); lk = linking_number(A, B)
    check(f"(2,{2*n}) torus link Lk={n}", abs(abs(lk)-n)<0.15, f"Lk={lk:.3f}")
t = np.linspace(0, 2*np.pi, 60, endpoint=False)
U1 = np.stack([np.cos(t), np.sin(t), np.zeros(60)], 1)
U2 = np.stack([np.cos(t)+5, np.sin(t), np.zeros(60)], 1)
lku = linking_number(U1, U2)
check("Unlinked circles Lk=0", abs(lku)<0.1, f"Lk={lku:.3f}")

print("\n5. tension force = -gradient of length energy (NOT spring)")
t = np.linspace(0, 2*np.pi, 30, endpoint=False)
C = np.stack([np.cos(t), np.sin(t), 0.2*np.sin(3*t)], 1)
F = tension_force(C, T0=1.0)
eps = 1e-6; i_t = 7; g = np.zeros(3)
for kk in range(3):
    Cp = C.copy(); Cp[i_t,kk] += eps
    Cm = C.copy(); Cm[i_t,kk] -= eps
    g[kk] = (tension_energy(Cp)-tension_energy(Cm))/(2*eps)
err = np.linalg.norm(F[i_t]-(-g))
check("tension force matches finite-diff gradient", err<1e-3, f"err={err:.2e}")

print("\n"+"="*64)
npass = sum(1 for _, ok in results if ok)
print(f"RESULT: {npass}/{len(results)} validation tests passed")
print("="*64)
sys.exit(0 if npass==len(results) else 1)
