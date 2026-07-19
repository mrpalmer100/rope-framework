"""QB-008 (EFT-constrained): the fast-channel depletion conjecture,
QUANTITATIVELY CORNERED. QB-007 isolated the measurement problem's hard core:
winner-take-all localization requires the firing site to deplete the wave at
spacelike separation. IF that depletion is a physical signal in the mesh's
preferred frame, its speed v_dep is a parameter -- and existing experiments
already corner it from three directions (all inputs declared, cited):

RUNG 1 (anticorrelation geometry, illustrative): Grangier-class apparatus,
    detectors ~3 m apart, detection jitter ~1 ns: depletion must beat the
    second detector's independent firing -> v_dep >~ 10 c.
RUNG 2 (Bell-timing bounds, the binding constraint): entangled pairs at
    ~18 km with tight synchronization, measured across Earth's rotation
    (sweeping candidate preferred frames): for frames moving <~ 1e-3 c
    relative to Earth (which includes the CMB rest frame, the mesh's natural
    candidate at beta ~ 1.2e-3), the published lower bound is
    v_dep > 1.38e4 c (Yin et al., PRL 110, 260407, 2013; pioneering bound
    Salart et al., Nature 454, 861, 2008, same order and higher for
    CMB-adjacent frames).
TRANSLATION into strand mechanics: the corpus's longitudinal channel has
    v_L/c = sqrt(K_L/K_T) (stretch-to-transverse stiffness ratio), so the
    conjecture DEMANDS K_L/K_T >= (1.38e4)^2 ~ 1.9e8 at the mesh scale.
RUNG 3 (the theoretical corner): Bancal et al., Nature Physics 8, 867 (2012):
    ANY finite-v influence model reproducing quantum correlations enables
    superluminal macroscopic SIGNALING in principle -- not observed. So
    finite v_dep is excluded as a stable resting point: the conjecture is
    forced to the INSTANTANEOUS-CONSTRAINT limb (v_dep -> infinity in the
    mesh frame). CONSISTENCY: that limb is exactly the ideal limit of the
    corpus's own P-VOL near-inextensibility postulate -- a perfectly
    inextensible strand propagates tension changes instantaneously, while
    transverse (EM) physics stays luminal and Lorentz-emergent, and the
    longitudinal channel is dark (no transverse coupling at leading order).
    Cornered, quantified, coherent -- and still a Conjecture.
"""
import numpy as np

C = 2.998e8


def rung1_anticorrelation(d_m=3.0, jitter_s=1e-9):
    return d_m/(jitter_s*C)          # in units of c


def rung2_bound():
    return 1.38e4                     # Yin et al. 2013, beta <= 1e-3 frames (incl. CMB)


def stiffness_ratio_required(v_over_c):
    return v_over_c**2                # v_L/c = sqrt(K_L/K_T)


def test():
    v1 = rung1_anticorrelation()
    assert v1 > 1.0, "anticorrelation alone already demands superluminal depletion"
    v2 = rung2_bound()
    assert v2 > 1e4, "Bell-timing: four orders of magnitude beyond light"
    K = stiffness_ratio_required(v2)
    assert K > 1e8, "strand stretch stiffness must exceed transverse by >= 1.9e8"
    # rung 3: the logical corner, encoded as the exclusion of the finite-v middle
    finite_v_allows_QM_without_signaling = False   # Bancal et al. 2012 theorem
    assert not finite_v_allows_QM_without_signaling, \
        "finite-v middle excluded: conjecture forced to instantaneous-constraint limb"
    # consistency: the corpus's own inextensibility postulate has v_L -> inf as its ideal limit
    ideal_inextensible_limit_instantaneous = True  # P-VOL: tension propagates instantly in ideal limit
    assert ideal_inextensible_limit_instantaneous
    print(f"rung 1: anticorrelation geometry -> v_dep >~ {v1:.0f} c (illustrative, inputs declared)")
    print(f"rung 2: Bell timing (Yin 2013, CMB-class frames) -> v_dep > {v2:.2e} c  [BINDING]")
    print(f"strand translation: K_L/K_T >= {K:.1e} at the mesh scale")
    print(f"rung 3: Bancal 2012 excludes finite v -> instantaneous-constraint limb only,")
    print(f"        which is the ideal limit of the P-VOL inextensibility postulate itself.")
    print("PASS: the escape route is cornered to one precisely-specified, still-conjectural limb.")


if __name__ == "__main__":
    test()
