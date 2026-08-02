# ROPE-MODE-008 results — matched ensembles do not yield a blind topology classifier

ROPE-MODE-008 implemented the next-order named by ROPE-MODE-007: paired linked and locally unlinked geometry ensembles, nuisance-geometry matching, a reduced bound-state spectral solver validated against exact sparse eigensolves, and blinded leave-one-surgery-family-out classification.

## Design

Fifteen paired geometries were generated across five held-out surgery-location families. Each linked member was a small smooth topology-preserving perturbation of the certified reference. Each unlinked member was selected from multiple local surgery candidates to minimize differences in total length, radial second moment, quadrupole tensor, radial-density histogram, and curvature histogram. The scalar-field Hamiltonian was unchanged from the preceding branch (`alpha=12`, `beta=0.5`, `epsilon=0.30`, `sigma=0.16`).

The low spectrum was computed in a 12-state central-field reduced basis on a `31^3` grid at `h=0.25`. Two held-out geometries were also solved with the full sparse Hamiltonian. The maximum reduced-versus-exact excitation-gap error was `3.92e-4`, so the reduced solver was adequate for this classification screen.

## Blinded classification

Spectral features were residualized against the geometry descriptors using training folds only. A regularized logistic classifier was then evaluated by leaving out one entire surgery-location family at a time.

- balanced accuracy: **0.5000**;
- ROC AUC: **0.6267**;
- leave-family-out balanced accuracies: `0.333, 0.333, 0.667, 0.667, 0.500`;
- paired-label permutation p-value: **0.5695**.

The classifier therefore did not predict linking status above chance in a statistically significant or family-robust way.

## Matching limitation

The median within-pair matching score was `0.0717`, but the largest ensemble-level standardized mean difference among the descriptor components was `1.65`. Thus the candidate search improved pairwise matching but did not fully balance all nuisance features across the complete linked and unlinked ensembles. This causes the strict geometry-matching bar to fail.

Importantly, that imbalance did not create a positive classifier result: after training-fold nuisance residualization, accuracy remained at chance. The experiment therefore supplies no evidence that the present spectral features carry a robust topology label. It also does not prove that no such signal exists, because the ensemble is small and the full nuisance-balance gate was not met.

## Locked bars

- topology controls: **PASS**
- geometric ensemble matching: **FAIL**
- reduced solver validation: **PASS**
- blinded balanced accuracy >= 0.70: **FAIL**
- paired permutation significance: **FAIL**
- held-out surgery-family robustness: **FAIL**

## Finding

**`NO_BLIND_TOPOLOGY_SIGNAL`**

Within this 15-pair, five-family matched-ensemble screen, the low bound-state spectrum did not support out-of-sample classification of linked versus unlinked status after nuisance residualization. The earlier single-control and repeated-surgery spectral shifts remain geometry-sensitive candidate effects, not an isolated signature of the Gauss linking number.

The next scientifically useful move is not a more elaborate classifier. It is to improve the generative control problem first: construct larger linked and unlinked ensembles with explicit optimization of the *full sampled tubular potential* or its high-dimensional distance, verify descriptor balance before examining spectra, and only then preregister a held-out classification test.
