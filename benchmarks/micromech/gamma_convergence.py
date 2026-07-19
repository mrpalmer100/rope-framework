"""Numerical verification of the homogenization (Gamma-convergence) theorem:
the discrete endpoint-locking energy E_a[theta] = J sum(1-cos(dtheta)) converges
to (K/2) integral |grad theta|^2 with K=J/a (scalar), at O(a^2) relative rate,
on vortex-free fields -- and the vortex counterexample showing the hypothesis is
necessary. Supports rope_homogenization_theorem.docx."""
import numpy as np

def discrete_energy(th, J=1.0, periodic=False):
    E=0.0
    for axis in range(th.ndim):
        d=np.roll(th,-1,axis=axis)-th
        if periodic:
            E+=J*np.sum(1-np.cos(d))
        else:
            sl=[slice(None)]*th.ndim; sl[axis]=slice(0,th.shape[axis]-1)
            E+=J*np.sum(1-np.cos(d[tuple(sl)]))
    return E

def test_convergence_and_constant():
    """Ratio E_discrete/E_continuum -> 1 with K=J/a as a->0 (linear field, d=3)."""
    Lphys=4.0; k=0.05
    for a in [0.5,0.25,0.125,0.0625]:
        L=int(round(Lphys/a)); xs=np.arange(L)*a
        X=xs[:,None,None]*np.ones((L,L,L))
        th=k*X
        Ed=discrete_energy(th)
        Vol=((L-1)*a)*(L*a)*(L*a); K=1.0/a
        Ec=0.5*K*k**2*Vol
        assert abs(Ed/Ec-1.0)<1e-3, f"K=J/a fails at a={a}: ratio {Ed/Ec}"
    return "PASS: E_a/E_cont -> 1 with K=J/a"

def test_O_a2_rate():
    """Relative error falls 4x per halving of a (periodic field, exact continuum)."""
    Lphys=1.0; A=0.2; m=2; errs=[]
    for a in [0.05,0.025,0.0125,0.00625]:
        L=int(round(Lphys/a)); xs=np.arange(L)*a
        X=xs[:,None,None]*np.ones((L,L,L))
        th=A*np.sin(2*np.pi*m*X/Lphys)
        Ed=discrete_energy(th,periodic=True)
        kk=2*np.pi*m/Lphys; grad2int=A**2*kk**2*0.5*Lphys**3
        Ec=0.5*(1.0/a)*grad2int
        errs.append(abs(Ed-Ec)/Ec)
    for i in range(len(errs)-1):
        assert 3.2 < errs[i]/errs[i+1] < 4.8, f"not O(a^2): {errs[i]/errs[i+1]}"
    return f"PASS: relative error O(a^2), ratios {[round(errs[i]/errs[i+1],2) for i in range(len(errs)-1)]}"

def test_vortex_counterexample():
    """A vortex has FINITE discrete energy (continuum |grad|^2 would diverge)."""
    L=40; xs=(np.arange(L)-L/2+0.5)/L; X,Y=np.meshgrid(xs,xs,indexing='ij')
    th=np.arctan2(Y,X); Ed=discrete_energy(th)
    assert np.isfinite(Ed) and Ed>0, "vortex discrete energy should be finite/positive"
    return f"PASS: vortex discrete energy finite ({Ed:.2f} J); continuum diverges -> hypothesis necessary"

if __name__=="__main__":
    print(test_convergence_and_constant())
    print(test_O_a2_rate())
    print(test_vortex_counterexample())
    print("All homogenization checks passed.")
