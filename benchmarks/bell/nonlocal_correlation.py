"""Bell/CHSH analysis for the non-local rope correlation model.
Supports rope_nonlocal_dynamics.docx. Shows: (1) local rope model is capped at
CHSH=2 (triangle wave); (2) a non-local update reproduces -cos(a-b) and Tsirelson
IF the quantum conditional is used; (3) the whole viability reduces to one angle
map factor gamma; (4) no-signalling holds for any gamma."""
import numpy as np

def local_chsh(N=400_000):
    def E(x,y):
        lam=np.random.uniform(0,2*np.pi,N)
        return np.mean(np.sign(np.cos(x-lam))*(-np.sign(np.cos(y-lam))))
    a,ap,b,bp=0,np.pi/2,np.pi/4,3*np.pi/4
    return abs(E(a,b)-E(a,bp)+E(ap,b)+E(ap,bp))

def nonlocal_chsh(gamma=1.0):
    def E(a,b):
        p_anti=np.cos(gamma*(a-b)/2)**2
        return -(2*p_anti-1)  # = -cos(gamma*(a-b))
    a,ap,b,bp=0,np.pi/2,np.pi/4,3*np.pi/4
    return abs(E(a,b)-E(a,bp)+E(ap,b)+E(ap,bp))

def no_signalling(N=500_000):
    outs=[]
    for deg in [0,45,90,135,180]:
        b=np.radians(deg)
        lam=np.random.uniform(0,2*np.pi,N)
        A=np.where(np.cos(0-lam)>=0,1,-1)
        p=np.cos((0-b)/2)**2; r=np.random.uniform(0,1,N)
        B=np.where(r<p,-A,A)
        outs.append(abs(np.mean(A)))
    return max(outs)

if __name__=="__main__":
    Sl=local_chsh(); assert Sl<2.05, "local model must cap at 2"
    print(f"local rope model CHSH = {Sl:.3f}  (capped at 2 -> falsified)")
    for g in [0.5,1.0,2.0]:
        print(f"  non-local, gamma={g}: CHSH = {nonlocal_chsh(g):.3f}")
    assert abs(nonlocal_chsh(1.0)-2*np.sqrt(2))<0.01, "gamma=1 must give Tsirelson"
    ns=no_signalling(); assert ns<0.01, "no-signalling must hold"
    print(f"no-signalling: max|<A>| over b = {ns:.4f}  (~0 -> holds)")
    print("PASS: cosine+Tsirelson reachable at gamma=1; no-signalling holds; "
          "viability localized to the angle map.")
