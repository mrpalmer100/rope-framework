"""ELEC-001 (Failed): STABLE LOCALISED CHARGED EXCITATION, FIRST GATE.

Pre-data locked bars:
 B1 charge/topology: perturbed Hopf links retain |Lk| within 0.15 of unity.
 B2 dissipation: total energy falls by at least 5% in every trial.
 B3 localisation: final rms radius stays finite in 0.4 < R_rms < 2.0.
 B4 attractor: coefficient of variation of final R_rms across seeds < 15%.
 B5 control: an unlinked pair remains |Lk| < 0.15.

Outcome: B1, B2, B4, B5 pass. B3 fails reproducibly: the curve dynamics
relaxes to an expanded R_rms ~2.58 rather than the published sourced-field
Hopf scale ~0.84. The benchmark passes only by asserting that this locked-bar
failure remains visible. No electron candidate is claimed.
"""
import numpy as np
from rope_solver.topology.linking import hopf_curves, linking_number
from rope_solver.relaxation.relax import relax_link
from rope_solver.geometry.curve import tension_energy, curve_field_energy


def total_energy(c1, c2, T0=1.0, q2=0.04, a=0.14):
    return tension_energy(c1, T0) + tension_energy(c2, T0) + curve_field_energy([c1, c2], q2, a)


def rms_radius(c1, c2):
    x = np.vstack([c1, c2]); x = x - x.mean(axis=0)
    return float(np.sqrt(np.mean(np.sum(x*x, axis=1))))


def perturb(c1, c2, seed, amp=0.16):
    rng = np.random.default_rng(seed); n = len(c1)
    t = np.linspace(0, 2*np.pi, n, endpoint=False)
    def one(c):
        d = np.zeros_like(c)
        for k in (1, 2, 3):
            for axis in range(3):
                d[:, axis] += rng.normal()*np.sin(k*t + rng.uniform(0, 2*np.pi))/k
        d *= amp/(np.sqrt(np.mean(np.sum(d*d, axis=1))) + 1e-12)
        return c + d
    return one(c1), one(c2)


def unlinked_pair(M=40, R=0.85):
    t = np.linspace(0, 2*np.pi, M, endpoint=False)
    a = np.stack([R*np.cos(t)-1.8, R*np.sin(t), np.zeros(M)], axis=1)
    b = np.stack([R*np.cos(t)+1.8, R*np.sin(t), np.zeros(M)], axis=1)
    return a, b


def test():
    radii, drops, links = [], [], []
    for seed in range(5):
        c1, c2 = hopf_curves(40, R=0.85)
        c1, c2 = perturb(c1, c2, seed)
        e0 = total_energy(c1, c2)
        f1, f2, info = relax_link(c1, c2, steps=2500, dt=0.0025,
                                  core=0.16, record_every=500)
        drop = (e0-info['energy'])/e0
        lk = abs(info['Lk1']); rr = rms_radius(f1, f2)
        assert abs(lk-1.0) < 0.15, f'B1 failed seed {seed}: {lk}'
        assert drop > 0.05, f'B2 failed seed {seed}: {drop}'
        radii.append(rr); drops.append(drop); links.append(lk)

    cv = float(np.std(radii, ddof=1)/np.mean(radii))
    assert cv < 0.15, f'B4 failed: CV={cv}'

    # Locked B3 is expected to fail and must remain encoded as the kept loss.
    b3_pass = all(0.4 < r < 2.0 for r in radii)
    assert not b3_pass, 'B3 unexpectedly passed: update the claim and analysis before changing this assertion'
    assert min(radii) > 2.3, 'registered expansion signature moved; investigate before accepting drift'

    u1, u2 = unlinked_pair()
    ulk0 = abs(linking_number(u1, u2))
    _, _, uinfo = relax_link(u1, u2, steps=1500, dt=0.002,
                             core=0.16, record_every=500)
    ulk1 = abs(uinfo['Lk1'])
    assert ulk0 < 0.15 and ulk1 < 0.15, f'B5 created topology: {ulk0}->{ulk1}'

    print('ELEC-001 locked-bar results')
    print(f'B1 PASS |Lk|={min(links):.3f}..{max(links):.3f}')
    print(f'B2 PASS energy reduction={100*min(drops):.1f}%..{100*max(drops):.1f}%')
    print(f'B3 FAIL final rms radius={min(radii):.3f}..{max(radii):.3f} (locked window 0.4..2.0)')
    print(f'B4 PASS attractor CV={100*cv:.2f}%')
    print(f'B5 PASS unlink |Lk|={ulk0:.4f}->{ulk1:.4f}')
    print('KEPT LOSS: topology survives and a common attractor exists, but the current')
    print('curve dynamics does not reproduce the sourced-field localized Hopf scale.')


if __name__ == '__main__':
    test()
