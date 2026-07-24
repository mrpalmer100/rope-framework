"""GRV-047 (Modeled): THE f-EFFICIENCY RESOLVED BY CHANNEL SATURATION --
and the luminosity law honestly REVISED: a switch, not a slope.

THE TWO-SIDED BUDGET, bars locked first:
(SUPPLY) accretion sweeps the marginal band: as the horizon grows by
dr_s = 2G dM/c^2, every Planck cell (GRV-007's identification) in the
swept shell hosts a punch-through whose quantum arrives at infinity at
hbar x 0.23 kappa (GRV-040's cancellation). At Eddington-class feeding
this supplies 10^72-10^90 W-equivalents -- oversupplying the channel by
10^105 to 10^141. The naive supply-side f would exceed unity by ~70
orders; the energetics bar caught it, and the diagnosis is the claim.
(CHANNEL) the horizon at omega = 0.23 kappa is a DEEP-SUB-WAVELENGTH
emitter (lambda ~ 55 r_s): mode count (r_s/lambda)^2 ~ 3e-4, per-mode
one-way 1D Stefan-Boltzmann at the measured T = 0.21 kappa, times the
measured greybody. The ceiling: L_ch = 5.8e-4 x P_Hawking -- and this
ratio is MASS-INDEPENDENT (both sides scale as hbar kappa^2; the ratio
is the pure coefficient), verified identical across 10 Msun, Sgr A*,
and M87*.

THE REVISION, registered loudly: GRV-040's 'L proportional to Mdot'
holds only below Mdot_crit ~ 1e-113 Msun/yr -- no astrophysical
meaning. At any physical feeding the whisper SATURATES: the true law is
    L = L_ceiling(M) x Theta(feeding),   L_ceiling = 5.8e-4 P_Hawking.
A SWITCH: fed holes hum at a universal mass-set faintness; unfed holes
are silent. The feeding discriminator survives as on/off.

OBSERVABILITY, quantified away with INSTRUMENTS-grade honesty: 5e-34 W
for a stellar hole -- 1700x fainter than Hawking's own unobservable
glow. The four-discriminator suite (silence, the switch, the running
tail, the temperature coefficient) stands as in-principle physics; no
detection claim survives, and none was ever made.

f ITSELF, the last bounded-not-derived in Prediction 17, now computed:
f(Mdot) = L_ceiling/(Mdot c^2) -- a ratio, not a constant; ~4e-67 at
stellar Eddington.
"""
import numpy as np

G = 6.674e-11; c = 2.998e8; hbar = 1.055e-34; Msun = 1.989e30
lP = np.sqrt(hbar*G/c**3)
c1 = 0.23; Tg = 0.05; p_intact = 0.5


def budget(M):
    rs = 2*G*M/c**2
    kappa = c**3/(4*G*M)
    omega = c1*kappa
    Mdot = 1.26e31*(M/Msun)/(0.1*c**2)
    supply = 4*np.pi*rs**2*(2*G*Mdot/c**2)/lP**3*p_intact*hbar*omega
    lam = 2*np.pi*c/omega
    L_ch = np.pi*(0.21*kappa)**2*hbar/12*Tg*(rs/lam)**2
    P_H = hbar*c**6/(15360*np.pi*G**2*M**2)
    return supply, L_ch, P_H, Mdot


def test():
    ratios = []
    for M in (10*Msun, 4e6*Msun, 6.5e9*Msun):
        supply, L_ch, P_H, Mdot = budget(M)
        assert supply/L_ch > 1e50, "saturation: supply oversupplies the channel astronomically"
        ratios.append(L_ch/P_H)
        assert 1e-5 < L_ch/P_H < 1e-2, "the ceiling is Hawking-order (sub)"
    assert max(ratios)/min(ratios) < 1.01, "channel/Hawking ratio is MASS-INDEPENDENT (pure coefficient)"
    supply, L_ch, P_H, Mdot = budget(10*Msun)
    f = L_ch/(Mdot*c**2)
    assert f < 1e-50, "f is microscopic at Eddington -- a ratio, not a constant"
    Mdot_crit = Mdot*L_ch/supply
    assert Mdot_crit < 1e-50, "the proportional regime is unphysical: the law is a SWITCH"
    print(f"channel/Hawking = {ratios[0]:.2e} (mass-independent to {max(ratios)/min(ratios)-1:.1e})")
    print(f"10 Msun: L_ceiling = {L_ch:.2e} W; f(Eddington) = {f:.1e}; Mdot_crit = {Mdot_crit:.1e} kg/s")
    print("PASS: the whisper saturates -- a universal, mass-set, Hawking-faint ceiling, gated by")
    print("      feeding. L ~ Mdot is revised to a switch; f is computed and dissolved.")


if __name__ == "__main__":
    test()
