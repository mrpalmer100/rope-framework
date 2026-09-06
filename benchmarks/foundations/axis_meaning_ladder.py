"""AXIS-MEANING (ITEM 6b) Q3 -- the s-ladder on ELEC-099's engine (pe2_pbc_prefactor.py
functions reused byte-identically), one (s, axis) relaxation per invocation, checkpointed.
Box L = 16 s/3 (integer-rounded), npts = 3L. Floor at each s from three seeds of axis [100]."""
import numpy as np, pickle, pathlib, sys, time
ROOT = pathlib.Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT/'benchmarks'/'foundations'))
src = (ROOT/'benchmarks'/'foundations'/'pe2_pbc_prefactor.py').read_text()
exec(src.split("NPTS, STEPS = 24, 250")[0])       # definitions only (K, wrap, build_pbc, inclusion, inter_energy, relax, amplitude)
CK = ROOT/'analysis'/'axis_ladder_ckpt.pkl'
LADDER = {1.5: 8, 2.0: 11, 3.0: 16, 4.0: 21}
DIRS6 = [(1,0,0),(1,1,0),(1,1,1),(2,1,0),(2,1,1),(3,2,1)]
STEPS = 250
st = pickle.loads(CK.read_bytes()) if CK.exists() else {}
for s, L in LADDER.items():
    npts = 3*L
    for d in DIRS6:
        key = (s, d, 0)
        if key in st: continue
        t0 = time.time(); Xs = relax(inclusion(d, s, L), L, npts, STEPS, seed=0)
        st[key] = inter_energy(Xs, inclusion(d, s, L), L); CK.write_bytes(pickle.dumps(st))
        print(f"s={s} L={L} axis {d}: E = {st[key]:.4f}  ({time.time()-t0:.0f}s)", flush=True); sys.exit(0)
    for seed in (1, 2):                                   # floor: axis [100], seeds 1,2 (seed 0 above)
        key = (s, DIRS6[0], seed)
        if key in st: continue
        t0 = time.time(); Xs = relax(inclusion(DIRS6[0], s, L), L, npts, STEPS, seed=seed)
        st[key] = inter_energy(Xs, inclusion(DIRS6[0], s, L), L); CK.write_bytes(pickle.dumps(st))
        print(f"s={s} L={L} floor seed {seed}: E = {st[key]:.4f}  ({time.time()-t0:.0f}s)", flush=True); sys.exit(0)
print("LADDER COMPLETE")
