"""QGATE-005 (Modeled): THE WIDTH DETERMINATION RETURNS A TRILEMMA --
AND HANDS THE VERDICT TO AN EXPERIMENT. The vacuum-tension chain,
closed by tension additivity (T_tube = n_t T0, derived from the
registered identity mu = T/c^2: line energy = tension), OVER-determines
the constituent width -- and the four commitments

  {additivity, Sigma_ATLAS ~ 1e25 J/m^3 (EM-RECON-014),
   Lorentz bound a <= 1e-16 m (FND-MATTER-005), n_t = 111 (QGATE-003)}

are mutually inconsistent by a factor 5e10. Any three kill the fourth:

  ARM 1 (keep Sigma + bound + additivity): n_t >= 5.6e12 -- the
        transfer demand dies, and with it the reconnection-hbar
        candidate as constituted.
  ARM 2 (keep n_t + additivity + bound): Sigma >= 5.1e35 -- the
        ATLAS-scale identification dies.
  ARM 3 (keep n_t + Sigma + additivity): a ~ 2.3e-11 m, violating
        the Lorentz bound by 2e5 -- framework-fatal, NOT an option.
  ARM 4: drop additivity -> hierarchical strands (tube constituents
        distinct from ambient strands) -- new structure, conjecture.

THE REGISTRY'S OWN EVIDENCE FINGERS ARM 2: EM-RECON-016 had already
registered the rope vacuum-birefringence discriminator as CONFRONTED
(ratio exactly 3:1, NEGATIVE sign, vs QED's Euler-Heisenberg). The
Sigma identification was the chain's weakest link before tonight.
THE ARBITER IS THEREFORE A PVLAS-CLASS EXPERIMENT: a rope-signature
vacuum birefringence means the Sigma-identification falls and the
reconnection-hbar candidate survives at Sigma >= 5e35; a QED-like
vacuum means Sigma_ATLAS-scale stands and the candidate dies at an
absurd n_t ~ 1e12.

THE KILL-SHAPE PATTERN, now systematic (third occurrence): making
hbar-adjacent structure native at nuclear scales keeps demanding a
coarser mesh than relativity permits (FND-MATTER-033: a ~ 200 fm
forced vs 0.1 fm bound; tonight: a ~ 22500 fm forced). The framework's
resistance to a native quantum is not local to any one construction.
O(1) geometry (g1 = 3 strand families) is dwarfed by the 5e10 factor.
"""
import numpy as np


def test():
    TD, D_fm, g1 = 33.8, 0.8/27.75, 3.0
    T_tube = (TD/D_fm)*1.602e-13/1e-15          # J/m
    Sig_atlas, a_bound, n_demand = 1e25, 1e-16, 111.0
    # additivity from registered identities: mu = T/c^2 -> line energy = tension -> sums
    assert abs(T_tube - 1.878e5)/1.878e5 < 0.01, "T_tube = 1.88e5 J/m from the mass model"
    # ARM 1
    n1 = g1*T_tube/(Sig_atlas*a_bound**2)
    assert n1 > 1e12, "Arm 1: n_t >= ~5.6e12 -- transfer demand dead under Sigma_ATLAS + bound"
    # ARM 2
    Sig2 = g1*(T_tube/n_demand)/a_bound**2
    assert Sig2 > 1e35, "Arm 2: Sigma >= ~5e35 -- ATLAS identification dead under n_t=111 + bound"
    # ARM 3
    a3 = np.sqrt(g1*(T_tube/n_demand)/Sig_atlas)
    assert a3/a_bound > 1e4, "Arm 3: Lorentz bound violated by >1e4 -- framework-fatal arm"
    # the trilemma's single discrepancy factor, appearing identically in arms 1 and 2
    f1, f2 = n1/n_demand, Sig2/Sig_atlas
    assert abs(np.log10(f1) - np.log10(f2)) < 0.1, "one 5e10 inconsistency wearing three costumes"
    print(f"arm 1: n_t >= {n1:.1e} (vs 111); arm 2: Sigma >= {Sig2:.1e} (vs 1e25); "
          f"arm 3: a = {a3:.1e} m (vs 1e-16)")
    print(f"single discrepancy factor: {f1:.1e} -- any three commitments kill the fourth")
    print("PASS: the chain over-closes into a trilemma; the registry's own CONFRONTED")
    print("      discriminator (EM-RECON-016) fingers the Sigma arm; a PVLAS-class")
    print("      measurement now decides whether the reconnection-hbar candidate lives.")


if __name__ == "__main__":
    test()
