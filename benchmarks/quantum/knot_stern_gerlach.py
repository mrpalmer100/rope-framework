"""QB-018 (Modeled): THE KNOT-PROXY STERN-GERLACH -- the massive-particle
analyzer realized: a gapped (massive) spin-carrying wavepacket in a 2D
lattice is SPLIT INTO TWO RESOLVED BEAMS by a gyroscopic-gradient
strip, deflection sign tracking handedness, with the beam weights
obeying cos^2(theta_P/2) : sin^2(theta_P/2) -- position-resolved
measurement statistics for massive particles, completing the analyzer
family (QB-016 derived the law; QB-017 built it for polarization; here
it is built for the massive, moving, spin-carrying excitation that is
the corpus's registered effective description of a knot).

THE DEVICE: 2D lattice, two-component displacement (the spin), on-site
pinning m^2 (the mass gap -- group velocity measured at 0.82 against
the gapped band's sin(k)/omega = 0.825: the packet is genuinely
massive), and an analyzer strip with gyroscopic coupling
gamma(y) = gamma_0 (y - y_mid)/W: the chiral term shifts R and L
oppositely, so the GRADIENT exerts opposite transverse forces --
Stern-Gerlach from springs, a Coriolis term, and a slope.

MEASURED: pure R and L land 44 lattice units either side of center
(fully resolved); the gamma-off control lands dead center (|dy| < 1);
superposition inputs split into two spots whose energy weights match
the half-angle law within 3 percent (the residual is finite-gradient
diffraction leakage, stated).

(Sixteenth instrument catch: the first harness assumed up = cos^2 --
but which handedness deflects which way is the DEVICE'S choice, set by
the gradient sign; the weights were exact under the measured mapping.
The benchmark now self-calibrates its channels from the pure-state
centroids, as any real Stern-Gerlach analysis must.)

HONEST SCOPE: the knot is represented by its registered effective
description -- a massive gapped mode carrying circulation -- not a
literal 3D topological knot (the literal-knot construction on the
weave solver is the named next-order that would promote this);
2D scalar-pair lattice; Modeled.
"""
import numpy as np

Nx, Ny = 320, 140; k0 = 0.8; m2 = 0.15
om0 = np.sqrt(m2 + 4*np.sin(k0/2)**2)
X, Y = np.meshgrid(np.arange(Nx), np.arange(Ny), indexing='ij')
g2d = np.zeros((Nx, Ny))
strip = (X >= 130) & (X < 205)
g2d[strip] = 0.35*((Y[strip] - 70)/70.0)


def lap(z):
    out = -4*z.copy()
    out[1:, :] += z[:-1, :]; out[:-1, :] += z[1:, :]
    out[:, 1:] += z[:, :-1]; out[:, :-1] += z[:, 1:]
    return out


def run(theta=None, pol='R', gamma_on=True, T=390.0, dt=0.05):
    env = np.exp(-((X - 65)/22.0)**2 - ((Y - 70)/16.0)**2)
    u = env*np.exp(1j*k0*X)
    if theta is None:
        zx = u; zy = (-1j if pol == 'R' else 1j)*u
    else:
        a_, b_ = np.cos(theta/2), np.sin(theta/2)
        zx = (a_ + b_)*u; zy = (-1j*a_ + 1j*b_)*u
    vx = -1j*om0*zx; vy = -1j*om0*zy
    g = g2d if gamma_on else 0*g2d
    for s in range(int(T/dt)):
        ax = lap(zx) - m2*zx; ay = lap(zy) - m2*zy
        vx = vx + dt*(ax + g*vy); vy = vy + dt*(ay - g*vx)
        zx = zx + dt*vx; zy = zy + dt*vy
        for z in (zx, zy, vx, vy):
            z[0, :] = z[-1, :] = 0; z[:, 0] = z[:, -1] = 0
    E = np.abs(vx)**2 + np.abs(vy)**2 + m2*(np.abs(zx)**2 + np.abs(zy)**2)
    return E


def screen_centroid(E):
    scr = E[225:, :]
    return np.sum(scr*np.arange(Ny)[None, :])/np.sum(scr)


def test():
    # massive dispersion
    E = run(pol='R', gamma_on=False, T=180.0)
    vg = (np.sum(E*X)/np.sum(E) - 65)/180.0
    assert abs(vg - np.sin(k0)/om0) < 0.03, "massive dispersion: gapped band group velocity"
    # splitting + control; SELF-CALIBRATE channel mapping from pure states
    ycR = screen_centroid(run(pol='R'))
    ycL = screen_centroid(run(pol='L'))
    yc0 = screen_centroid(run(pol='R', gamma_on=False))
    assert abs(yc0 - 70) < 2.0, "control: no gradient, no deflection"
    assert abs(ycR - ycL) > 40 and (ycR - 70)*(ycL - 70) < 0, "resolved opposite-side beams"
    R_side_up = ycR > 70
    errs = []
    for th in np.deg2rad([60, 90, 120]):
        E = run(theta=th)
        scr = E[225:, :]
        Wu = np.sum(scr[:, 71:]); Wd = np.sum(scr[:, :70]); tot = Wu + Wd
        W_R = (Wu if R_side_up else Wd)/tot
        errs.append(abs(W_R - np.cos(th/2)**2))
    assert max(errs) < 0.04, "Stern-Gerlach weights: the half-angle law, channel-calibrated"
    print(f"v_g = {vg:.3f} (band {np.sin(k0)/om0:.3f}); beams at y = {ycR:.1f}/{ycL:.1f} (control {yc0:.1f})")
    print(f"weights: max |W_R - cos^2(theta/2)| = {max(errs):.4f}")
    print("PASS: Stern-Gerlach from springs, a Coriolis term, and a slope -- the massive")
    print("      spin-carrying excitation splits by handedness with half-angle statistics.")


if __name__ == "__main__":
    test()
