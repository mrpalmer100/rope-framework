# ELEC-009 locked bars — variational remeshing and quadrature consistency

The physical functional, hard separation floor, and Gauss-linking certificate are unchanged from ELEC-008. Only the spline remeshing and numerical consistency machinery are changed.

1. Final topology certificate passes at 128/256/512 polygonal samples.
2. Final physical energy is below the campaign start.
3. Every accepted optimization state remains inside the certified linked sector.
4. The 16→20-control remesh is certified, changes physical energy by less than 0.1%, has RMS geometric error below 0.004, and Hausdorff error below 0.012.
5. Identical-geometry source-quadrature energies at 48 and 64 samples agree within 0.2%.
6. At least five topology-certified descent steps are accepted.
7. Final projected physical-gradient norm divided by physical energy is below 0.05.

No bar may be weakened after execution.
