# ROPE-MODE-013 — Matched topology-preserving sham test

ROPE-MODE-013 matched topology-preserving sham test  
families=5 boxes=(4.0, 5.0) h=0.25  
median/max sham-unlink field mismatch=0.0114191/0.0348953  
median geometry RMS=0.00385196  
max outer probability=7.98662e-07  
max domain contrast drift=2.29445e-08  
median |unlink-sham spectral residual|=0.000217366  
median topology/sham effect ratio=0.0760479  
consistent modes=[np.True_, np.True_, np.True_]  
B1_reference_and_triplets_certified: PASS  
B2_sham_unlink_field_matched: FAIL  
B3_boundary_leakage: PASS  
B4_domain_stable_contrasts: PASS  
B5_topology_residual_significant: PASS  
B6_topology_residual_consistent: PASS  
B7_topology_exceeds_sham_disturbance: FAIL  
FINDING: MATCHED_SHAM_DOES_NOT_ISOLATE_TOPOLOGY

Controls were frozen using geometry and full-field information only. Spectra were computed afterward; no classifier was trained.
