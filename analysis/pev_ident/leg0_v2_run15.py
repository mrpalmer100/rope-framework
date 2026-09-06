import sys, time; sys.path.insert(0,'.'); sys.path.insert(0,'benchmarks/foundations')
import c1_fine_ceiling as c1
t=time.time(); S, st = c1.run(1/5, True, "f=1/5 (ADJUDICATING)"); print("S =", S, "secs", round(time.time()-t))
