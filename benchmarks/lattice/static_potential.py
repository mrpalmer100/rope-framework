import numpy as np
exec(open('/tmp/mc_fixed.py').read().split('print("FIXED')[0])  # reuse run/plaquette/action fns

def wilson_RT(th, L, R, T):
    # planar RxT Wilson loop in the (0,1) plane, averaged over all positions & z
    tot=0.0; cnt=0
    for z in range(L):
      for x0 in range(L):
        for y0 in range(L):
          ph=0.0
          for i in range(R): ph+=th[0][(x0+i)%L,y0,z]
          for j in range(T): ph+=th[1][(x0+R)%L,(y0+j)%L,z]
          for i in range(R): ph-=th[0][(x0+i)%L,(y0+T)%L,z]
          for j in range(T): ph-=th[1][x0,(y0+j)%L,z]
          tot+=np.cos(ph); cnt+=1
    return tot/cnt

def measure_potential(L=8, beta=1.0, ntherm=300, nmeas=250, seed=3, Rmax=4, T=2):
    r=np.random.default_rng(seed)
    th=[r.uniform(-np.pi,np.pi,size=(L,L,L)) for _ in range(3)]
    def sweep():
        for mu in range(3):
          for x in range(L):
            for y in range(L):
              for z in range(L):
                old=th[mu][x,y,z]; Eo=link_action_local(th,L,beta,mu,x,y,z)
                th[mu][x,y,z]=((old+r.uniform(-2,2)+np.pi)%(2*np.pi))-np.pi
                En=link_action_local(th,L,beta,mu,x,y,z)
                if r.random()>=np.exp(-(En-Eo)): th[mu][x,y,z]=old
    for _ in range(ntherm): sweep()
    W={R:[] for R in range(1,Rmax+1)}
    for _ in range(nmeas):
        sweep()
        for R in range(1,Rmax+1): W[R].append(wilson_RT(th,L,R,T))
    Wm={R:np.mean(v) for R,v in W.items()}
    # potential V(R) = -(1/T) ln W(R,T)
    V={R:-np.log(abs(Wm[R])+1e-12)/T for R in Wm}
    return V

print("Static potential V(R) across the transition (beta_c ~ 1.0 for 3+1D; here 3D spatial")
print("slice diagnostic). Confined: V rises ~linearly. Coulomb: V flattens.\n")
for beta,tag in [(0.7,"below (expect confined/rising)"),
                 (1.1,"near"),
                 (1.8,"above (expect Coulomb/flattening)"),
                 (3.0,"deep Coulomb")]:
    V=measure_potential(L=8,beta=beta,ntherm=250,nmeas=200,seed=4,Rmax=4,T=2)
    Rs=sorted(V); 
    dV=[V[Rs[i+1]]-V[Rs[i]] for i in range(len(Rs)-1)]
    # confinement = dV stays roughly constant/positive (linear); Coulomb = dV shrinks toward 0
    flattening = dV[-1] < 0.5*dV[0]
    print(f"beta={beta:.1f} [{tag}]")
    print("   V(R): "+"  ".join(f"{V[R]:.3f}" for R in Rs))
    print("   dV/dR:"+"  ".join(f"{d:+.3f}" for d in dV)+
          f"   => {'COULOMB (flattening)' if flattening else 'CONFINED (linear rise)'}\n")
