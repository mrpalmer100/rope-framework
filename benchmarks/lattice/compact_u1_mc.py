import numpy as np

# 3D compact U(1), Wilson action, single-site Metropolis with the action-change
# computed DIRECTLY from the 4 plaquettes touching the link (no hand staple).
# This removes the sign-convention bug: we literally recompute S before/after.

def plaquette_sum_cos(th, L):
    tot=0.0; n=0
    for mu in range(3):
        for nu in range(mu+1,3):
            ang = (th[mu] + np.roll(th[nu],-1,axis=mu)
                   - np.roll(th[mu],-1,axis=nu) - th[nu])
            tot += np.cos(ang).sum(); n += ang.size
    return tot/n

def link_action_local(th, L, beta, mu, x, y, z):
    # sum of the (up to 4) plaquettes containing link (mu at site x,y,z)
    # returns -beta * sum cos(plaquette)
    s=0.0
    for nu in range(3):
        if nu==mu: continue
        a=[0,0,0]; a[mu]=1
        b=[0,0,0]; b[nu]=1
        # plaquette in +nu: th_mu(x) + th_nu(x+mu) - th_mu(x+nu) - th_nu(x)
        xpmu=((x+a[0])%L,(y+a[1])%L,(z+a[2])%L)
        xpnu=((x+b[0])%L,(y+b[1])%L,(z+b[2])%L)
        ang1 = th[mu][x,y,z] + th[nu][xpmu] - th[mu][xpnu] - th[nu][x,y,z]
        s += np.cos(ang1)
        # plaquette in -nu: th_mu(x) - th_nu(x+mu-nu) - th_mu(x-nu) + th_nu(x-nu)
        xmnu=((x-b[0])%L,(y-b[1])%L,(z-b[2])%L)
        xpmu_mnu=((x+a[0]-b[0])%L,(y+a[1]-b[1])%L,(z+a[2]-b[2])%L)
        ang2 = th[mu][x,y,z] - th[nu][xpmu_mnu] - th[mu][xmnu] + th[nu][xmnu]
        s += np.cos(ang2)
    return -beta*s

def run(L=6, beta=1.0, ntherm=300, nmeas=200, seed=1):
    r=np.random.default_rng(seed)
    th=[r.uniform(-np.pi,np.pi,size=(L,L,L)) for _ in range(3)]
    def sweep():
        for mu in range(3):
          for x in range(L):
            for y in range(L):
              for z in range(L):
                old = th[mu][x,y,z]
                Eold = link_action_local(th,L,beta,mu,x,y,z)
                th[mu][x,y,z] = ((old + r.uniform(-2,2) + np.pi)%(2*np.pi))-np.pi
                Enew = link_action_local(th,L,beta,mu,x,y,z)
                if r.random() >= np.exp(-(Enew-Eold)):
                    th[mu][x,y,z] = old  # reject
    for _ in range(ntherm): sweep()
    P=[]
    for _ in range(nmeas):
        sweep(); P.append(plaquette_sum_cos(th,L))
    return np.mean(P), np.std(P)

print("FIXED MC sanity check: <cos plaq> must rise from ~0 (beta=0) toward ~1 (large beta)")
ok=True; prev=-1
for beta in [0.0,0.5,1.0,1.5,2.0,3.0,5.0]:
    P,dP=run(L=6,beta=beta,ntherm=200,nmeas=100,seed=2)
    print(f"  beta={beta:.1f}   <cos plaq>={P:.3f}")
print("\nExpected: monotone increase, approaching 1 at beta=5. If so, MC is correct.")
