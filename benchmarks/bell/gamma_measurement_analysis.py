"""Analysis of whether the config-entropy measurement model (S=k ln|C|) delivers
the Born rule / gamma=1. Supports rope_measurement_born_problem.docx.
RESULT (negative): a linear configuration COUNT gives hemisphere-overlap
(pi-theta)/pi = the TRIANGLE wave (classical), NOT Born cos^2(theta/2). Reproducing
Born requires amplitude interference, which a ln|C| count does not supply."""
import numpy as np

def hemisphere_overlap_fraction(theta, N=2_000_000):
    """Fraction of state-hemisphere also in axis-hemisphere; poles differ by theta."""
    v=np.random.randn(N,3); v/=np.linalg.norm(v,axis=1,keepdims=True)
    a=np.array([0,0,1.0]); n=np.array([np.sin(theta),0,np.cos(theta)])
    return np.mean((v@a>0)[v@n>0])

def config_count_E(theta):
    """Correlation from a linear config-area count = triangle wave."""
    return 2*(theta/np.pi) - 1

def born_E(theta):
    return -np.cos(theta)  # singlet; here compare magnitudes of the conditional

if __name__=="__main__":
    # 1. hemisphere overlap is LINEAR (pi-theta)/pi, not (1+cos)/2
    for deg in [0,60,90,120,180]:
        th=np.radians(deg)
        mc=hemisphere_overlap_fraction(th, 500_000)
        lin=(np.pi-th)/np.pi; cos2=(1+np.cos(th))/2
        assert abs(mc-lin)<0.01, f"overlap should be linear (pi-th)/pi, got {mc}"
        print(f"theta={deg:>3}: MC overlap={mc:.3f}  (pi-th)/pi={lin:.3f}  cos^2(th/2)={cos2:.3f}")
    # 2. confirm config-count gives triangle, diverging from -cos
    maxdev=max(abs(config_count_E(np.radians(d))-(-np.cos(np.radians(d)))) for d in range(0,181,5))
    print(f"max |config-count E - (-cos)| = {maxdev:.3f}  (triangle != cosine)")
    assert maxdev>0.2, "config count should diverge from cosine"
    print("PASS: config-entropy COUNT gives the triangle wave, NOT Born. "
          "gamma=1 is NOT delivered by a linear ln|C| count; Born needs amplitude interference.")
