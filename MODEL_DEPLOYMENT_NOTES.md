# Model Deployment Notes

Current deployed model:

- Model: pH-submodel GradientBoostingRegressor
- Feature set: single Lab `a`
- Training pH range: pH 3-8
- Direct targets: Total Cr(VI), HCrO4-, Cr2O7^2-
- Derived target: CrO4^2- by mass balance

Mass-balance formula:

`CrO4_mM = Total Cr(VI)_mM - HCrO4_mM - 2 * Cr2O7_mM`

The deployed model file is:

`backend/models/species_model.joblib`

The backend prediction logic is implemented in:

`backend/species_model.py`

The image-processing route is:

1. Frontend uploads cropped ROI image and pH.
2. Backend standardizes illumination with CLAHE on the Lab L channel.
3. Backend extracts the full 16-feature vector for compatibility/display.
4. Final deployed model uses only Lab `a` plus pH-based routing.

Private training data, final training outputs, figure data, and manuscript
analysis scripts are intentionally stored outside this deployable project:

`J:\codex_workplace\重铬酸钾\final_gbr_single_a_model_package_20260722`

Do not move private source data into this deployable project unless you intend
to publish it.
