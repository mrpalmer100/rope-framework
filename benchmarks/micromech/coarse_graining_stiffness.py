"""Direct lattice verification that coarse-graining the XY locking gives K=J/a
(scalar), NOT 3J/a. Supports rope_microscopic_mechanics.docx section 4."""
import numpy as np
def lattice_energy(L, qvec, J=1.0, a=1.0):
    xs=np.arange(L)*a; X,Y,Z=np.meshgrid(xs,xs,xs,indexing='ij')
    th=qvec[0]*X+qvec[1]*Y+qvec[2]*Z; E=0.0
    for axis in range(3):
        d=np.roll(th,-1,axis=axis)-th
        sl=[slice(None)]*3; sl[axis]=slice(0,L-1); E+=J*np.sum(1-np.cos(d[tuple(sl)]))
    return E
if __name__=="__main__":
    L=20;a=1.0;J=1.0;q=0.01
    E=lattice_energy(L,(q,0,0),J,a); V=(L-1)*L*L*a**3
    K=2*E/(q**2*V)
    print(f"K_measured = {K:.6f} * J/a  (expected 1.0; NOT 3.0)")
    assert abs(K-1.0)<1e-3, "coarse-graining coefficient is not 1"
    print("PASS: K = J/a confirmed; factor-of-three is not reproduced.")
