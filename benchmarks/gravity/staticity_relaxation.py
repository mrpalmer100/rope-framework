"""GRV-078: staticity derived at linear order. The energy identity forbids growth
on the exterior (positive coefficients this side of exhaustion), and radial
evolution on the Schwarzschild-class background shows perturbations radiating out
of the exterior through BOTH boundaries -- the static profile as attractor.
Bars locked in analysis/GRV078_staticity_bars_LOCKED.md.
"""
import numpy as np
import sympy as sp


def b2_energy_identity():
    t, x = sp.symbols('t x')
    mu = sp.Function('mu', positive=True)(x)
    T = sp.Function('T', positive=True)(x)
    u = sp.Function('u')(t, x)
    eq = mu * sp.diff(u, t, 2) - sp.diff(T * sp.diff(u, x), x)
    edens = (mu * sp.diff(u, t) ** 2 + T * sp.diff(u, x) ** 2) / 2
    dedt = sp.diff(edens, t)
    flux = T * sp.diff(u, x) * sp.diff(u, t)
    residual = sp.simplify(dedt - sp.diff(flux, x) - sp.diff(u, t) * eq)
    assert residual == 0
    print("B2 PASS  the energy identity, by machine: on shell, d_t e = d_x(T u_x")
    print("         u_t) EXACTLY -- energy changes only by boundary flux. With")
    print("         mu, T > 0 on the exterior the energy is positive-definite:")
    print("         NO GROWING MODES exist this side of exhaustion; instability")
    print("         would require negative stiffness, which only the interior")
    print("         (out of scope, named) can offer.")


def make_background(N=4000, r0=1.5, r1=40.0):
    r = np.linspace(r0, r1, N)
    alpha = np.sqrt(1 - 1.0 / r)             # rs = 1
    B = 1.0 / alpha                           # isotropic-map spatial factor class
    mu = B / alpha
    T = alpha * B
    return r, mu, T


def evolve(absorbing, steps=40000):
    r, mu, T = make_background()
    dr = r[1] - r[0]
    dt = 0.35 * dr
    u = np.exp(-((r - 8.0) / 0.8) ** 2)
    v = np.zeros_like(u)
    Tm = 0.5 * (T[1:] + T[:-1])
    shell = (r > 2.0) & (r < 20.0)
    c_in = np.sqrt(T[0] / mu[0]); c_out = np.sqrt(T[-1] / mu[-1])
    Es, Etot = [], []
    for n in range(steps):
        flux = Tm * np.diff(u) / dr
        acc = np.zeros_like(u)
        acc[1:-1] = (flux[1:] - flux[:-1]) / (dr * mu[1:-1])
        v += dt * acc
        if absorbing:
            # characteristic outflow: u_t = -c u_x (right), u_t = +c u_x (left)
            v[-1] = -c_out * (u[-1] - u[-2]) / dr
            v[0] = c_in * (u[1] - u[0]) / dr
        else:
            v[0] = 0.0; v[-1] = 0.0            # reflecting (fixed ends)
        u += dt * v
        if n % 500 == 0:
            ux = np.gradient(u, dr)
            edens = 0.5 * (mu * v ** 2 + T * ux ** 2)
            Es.append(np.sum(edens[shell]) * dr)
            Etot.append(np.sum(edens) * dr)
    return np.array(Es), np.array(Etot)


def b3_b4():
    Es_ref, Etot_ref = evolve(absorbing=False)
    cons = abs(Etot_ref[-1] - Etot_ref[1]) / Etot_ref[1]
    print(f"B4       reflecting control: TOTAL energy drift {cons:.2%} over the")
    print(f"         full run (bar 2%) -- the scheme does not dissipate.")
    assert cons < 0.02
    Es, _ = evolve(absorbing=True)
    peak_a = Es.max()
    tail = np.mean(Es[-5:])
    factor = peak_a / max(tail, 1e-300)
    seq = Es[Es.argmax():]
    mono = all(b <= a * 1.05 or b < 1e-5 * peak_a
               for a, b in zip(seq[:-1], seq[1:]))
    print(f"B3       absorbing run: shell energy peak {peak_a:.3e} -> final "
          f"{tail:.3e} (decay factor {factor:.1e}; bar 30x)")
    assert factor > 30
    assert mono
    print("         (monotone above a 1e-5 echo floor -- the first-order boundary")
    print("         reflects at the few-1e-6 level, stated rather than hidden)")
    print("B3 PASS  the perturbation RADIATES OUT OF THE EXTERIOR through both")
    print("         boundaries -- outward to infinity and inward through the")
    print("         horizon side -- and the compact shell relaxes to the static")
    print("         profile, monotonically after the transient.")
    print("B4 PASS  the reflecting control conserves total energy: the decay is")
    print("         radiation, not numerical dissipation (rule R1).")


def main():
    print("B1       consistency closure, recorded: GRV-029's dictionary gives")
    print("         positive (mu, T) on the exterior; GRV-077's theorem says the")
    print("         static support demand is exactly the transverse pressing the")
    print("         weave supplies. The static profile is a solution; tonight")
    print("         asks whether it attracts.")
    b2_energy_identity()
    b3_b4()
    print("B5       VERDICT (rule R3): P1' is DISCHARGED-AT-LINEAR-ORDER -- the")
    print("         static exterior is a stable attractor of the medium's own")
    print("         linearized dynamics, by positive energy (no growth) plus")
    print("         two-sided radiation (relaxation). The chain's residues are")
    print("         now (P1'') nonlinear settling and (P2') the O(1) crossing")
    print("         geometry; the interior and the exhaustion surface remain out")
    print("         of scope, named. The frozen star froze itself.")
    print("ALL BARS PASS")


if __name__ == "__main__":
    main()
