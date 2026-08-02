# ROPE-MODE-008 locked bars

1. Certified linked samples and numerically unlinked controls: PASS only if every control has |Lk| < 0.02.
2. Geometry matching: PASS only if median pair-match score < 0.20 and every ensemble descriptor standardized mean difference < 0.50.
3. Reduced spectral solver: PASS only if maximum validated excitation-gap error < 0.01.
4. Blind classification: PASS only if leave-family-out balanced accuracy >= 0.70.
5. Statistical significance: PASS only if paired-label permutation p < 0.05.
6. Family robustness: PASS only if every held-out surgery family has balanced accuracy >= 0.625.

The topology-signal claim requires all six bars to pass.
