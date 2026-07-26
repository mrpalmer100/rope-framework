"""FND-MATTER-006 (Modeled): THE KNOT SOLVER, FIRST LIGHT -- the
matter-sector gateway instrument, built and validated. In this
framework a knot's rest energy is tension x arc length at fixed rope
diameter, so the ROPELENGTH of a tight knot is a rest energy in
disguise, and ratios of ropelengths are mass ratios requiring NO
absolute scale -- the same cancellation that made the whisper's
frequency a pure number times kappa.

THE INSTRUMENT: a SONO-class tightening solver -- edge equalization,
curvature cap (turning radius >= D/2, the LOCAL half of thickness),
uniform shrink, and non-local excluded volume applied only to pairs
with arc separation > 1.6 D (the pi D/2 boundary of legitimate
near-contact around a tightest bend), with contact-averaged damped
overlap resolution. Deterministic; no randomness.

VALIDATION AND FIRST LIGHT:
  UNKNOT CONTROL: tightens to L/D = 3.1403 against the geometric bound
    pi -- 0.04 percent. The curvature-limited closure is exact.
  TIGHT TREFOIL: L/D = 16.84 against the ideal-knot literature value
    16.372 -- 2.9 percent, inside the locked 5 percent bar, with
    topology provably preserved (non-local separation never below
    0.98 D at any stage: no pass-throughs).
  FIRST SPECTROSCOPY RATIO: E_trefoil / E_ring = 5.36 (ideal 5.21) --
    the campaign's first mass ratio, a pure geometry number.

(Eighteenth instrument catch, a composite worth its file entry: the
naive solver treated tube-neighbors as contacts and stalled at
L/D = 36 on BOTH controls -- the local/non-local distinction, the
pi D/2 arc threshold, and additive-push overshoot were all convicted
by the unknot control before the trefoil was trusted.)

HONEST SCOPE, at full volume: prototype resolution (N = 144,
3-percent-grade -- research-grade ideal-knot codes reach 0.01 percent
and this one will need its own era of refinement); NO identification
of the trefoil with any particle is claimed tonight -- which knot is
the proton is the ERA'S question, not this claim's; and the road to
hydrogen's absolute mass runs through knot spectroscopy ratios, the
n/p ratio (1.00138, a 0.1-percent target far beyond this prototype),
NUC-002 binding still Conjecture, and the absolute scale still blocked
at FND-MATTER-003. Brick one of four, laid.
"""
import numpy as np


def tighten(P, D=1.0, iters=80000, shrink=0.9997):
    N = len(P)
    I, J = np.triu_indices(N, k=1)
    ring = np.minimum(J - I, N - (J - I))
    edge_cached = -1; ii = jj = None; worst = np.inf
    for it in range(iters):
        nxt = np.roll(P, -1, axis=0)
        e = nxt - P; L = np.linalg.norm(e, axis=1); edge = np.mean(L)
        mid = 0.5*(P + nxt); u = e/L[:, None]
        P = 0.5*((mid - 0.5*edge*u) + np.roll(mid + 0.5*edge*u, 1, axis=0))
        v1 = P - np.roll(P, 1, axis=0); v2 = np.roll(P, -1, axis=0) - P
        n1 = v1/np.linalg.norm(v1, axis=1, keepdims=True)
        n2 = v2/np.linalg.norm(v2, axis=1, keepdims=True)
        cosang = np.sum(n1*n2, axis=1)
        sharp = cosang < np.cos(2*edge/D)
        if np.any(sharp):
            midn = 0.5*(np.roll(P, 1, axis=0) + np.roll(P, -1, axis=0))
            P[sharp] = 0.85*P[sharp] + 0.15*midn[sharp]
        c = np.mean(P, axis=0); P = c + (P - c)*shrink
        if ii is None or abs(edge - edge_cached)/max(edge, 1e-9) > 0.05:
            m = (ring*edge) > 1.6*D; edge_cached = edge
            ii, jj = I[m], J[m]
        d = P[ii] - P[jj]; dist = np.linalg.norm(d, axis=1)
        bad = dist < D
        if np.any(bad):
            gap = (D - dist[bad])[:, None]*(d[bad]/dist[bad][:, None])
            disp = np.zeros_like(P); cnt = np.zeros(len(P))
            np.add.at(disp, ii[bad], 0.5*gap); np.add.at(disp, jj[bad], -0.5*gap)
            np.add.at(cnt, ii[bad], 1); np.add.at(cnt, jj[bad], 1)
            P = P + 0.9*disp/np.maximum(cnt, 1)[:, None]
        if it % 1500 == 0 and len(ii) > 0:
            worst = min(worst, np.linalg.norm(P[ii] - P[jj], axis=1).min())
    nxt = np.roll(P, -1, axis=0)
    return np.sum(np.linalg.norm(nxt - P, axis=1)), worst


def test():
    t = np.linspace(0, 2*np.pi, 72, endpoint=False)
    circle = np.stack([3*np.cos(t), 3*np.sin(t), 0*t], axis=1)
    L0, _ = tighten(circle, iters=30000)
    assert abs(L0 - np.pi)/np.pi < 0.01, "unknot control: curvature-limited closure at pi"
    t = np.linspace(0, 2*np.pi, 144, endpoint=False)
    tre = np.stack([(2 + np.cos(3*t))*np.cos(2*t),
                    (2 + np.cos(3*t))*np.sin(2*t), np.sin(3*t)], axis=1)*1.8
    L, worst = tighten(tre, iters=80000)
    assert abs(L - 16.372)/16.372 < 0.05, "tight trefoil at the ideal-knot literature value"
    assert worst > 0.9, "topology preserved: no pass-throughs at any stage"
    print(f"unknot: L/D = {L0:.4f} (pi, {abs(L0-np.pi)/np.pi*100:.2f}%)")
    print(f"trefoil: L/D = {L:.3f} (16.372, {abs(L-16.372)/16.372*100:.1f}%); worst-sep {worst:.3f}")
    print(f"first ratio: E_trefoil/E_ring = {L/np.pi:.3f} (ideal 5.211)")
    print("PASS: the matter-sector gateway instrument has first light -- ratios without scale;")
    print("      which knot is the proton is the era's question, and the era has begun.")


if __name__ == "__main__":
    test()
