"""EFT / RG support calculations for rope_renormalization_eft.docx.
(1) operator scaling in d=3 spatial; (2) one-loop stiffness renormalization
showing K is perturbatively stable in the stiff/Coulomb regime."""
import numpy as np
from numpy import pi

def operator_classes(d=3):
    dim_theta=(d-2)/2
    ops={"(grad theta)^2":(2,2),"(grad theta)^4":(4,4),"(grad^2 theta)^2":(2,4)}
    out={}
    for name,(nt,ng) in ops.items():
        O=nt*dim_theta+ng; g=d-O
        out[name]=("RELEVANT" if g>1e-9 else "MARGINAL" if abs(g)<1e-9 else "irrelevant", g)
    return out

def stiffness_oneloop(Theta_over_K, a=1.0):
    Lambda=pi/a; I=Lambda/(2*pi**2)
    return -Theta_over_K*I   # dK/K

if __name__=="__main__":
    oc=operator_classes(3)
    assert oc["(grad theta)^2"][0]=="MARGINAL"
    assert oc["(grad theta)^4"][0]=="irrelevant"
    assert oc["(grad^2 theta)^2"][0]=="irrelevant"
    print("operator scaling d=3:", {k:v[0] for k,v in oc.items()})
    for r in [0.05,0.1,0.2,0.5]:
        dK=stiffness_oneloop(r)
        assert dK<0 and abs(dK)<1.0
        print(f"  Theta/K={r}: dK/K={dK:+.4f}, K_R/K={1+dK:.4f}")
    # stiff regime correction must be small (<5% for Theta/K<=0.2)
    assert abs(stiffness_oneloop(0.2))<0.05
    print("PASS: stiffness perturbatively stable in stiff/Coulomb regime; leading operators justified.")
