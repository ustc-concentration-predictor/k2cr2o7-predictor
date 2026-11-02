# Model Deployment Notes

Current deployed model:

- Model: pH-submodel GradientBoostingRegressor
- Feature set: Lab `a` + `R_over_G`
- Training pH range: pH 3-8
- Equilibrium constant: Ka2 = 3.0e-7
- Direct targets: HCrO4-, Cr2O7^2-, CrO4^2-
- Computed output: Total Cr(VI) by chromium mass balance

Mass-balance formula:

`Total Cr(VI)_mM = HCrO4_mM + 2 * Cr2O7_mM + CrO4_mM`

The deployed model file is:

`backend/models/species_model.joblib`

The backend prediction logic is implemented in:

`backend/species_model.py`

The image-processing route is:

1. Frontend uploads cropped ROI image and pH.
2. Backend standardizes illumination with CLAHE on the Lab L channel.
3. Backend extracts the full 16-feature vector for compatibility/display.
4. Final deployed model uses Lab `a` and `R_over_G` plus pH-based routing.

Private training data, final training outputs, figure data, and manuscript
analysis scripts are intentionally stored outside this deployable project:

`final_gbr_single_a_model_package_20261017`

Do not move private source data into this deployable project unless you intend
to publish it.
