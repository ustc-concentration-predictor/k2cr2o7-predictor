# Current display policy (updated)

Temperature inference now selects high when the classifier score is >= 0.5, otherwise low. Abstention and min/max range rejection are disabled at the user’s request. Invalid inputs or missing models return an unavailable service status, not a fabricated class. The earlier 89.7% accuracy applies only to the former selective policy; the current binary policy has grouped validation accuracy 46/56 (82.1%). No retraining was required.

The results UI uses responsive concentration cards with four decimal places and units in the label. It omits the former temperature explanatory captions, heuristic score, residual/pH metrics, pipeline caption, and model metadata/evaluation section. Missing training color-range warnings remain available and are localized in Chinese.

## Historical training and validation record

# Experimental temperature tendency

Both prediction endpoints return `temperature_tendency`: status `low`, `high`, or `uncertain`, plus a machine-readable reason. Streamlit displays a bilingual qualitative result without a probability or measured temperature. Missing models do not interrupt concentration prediction. Restart the backend after replacing the cached model.

Training source: `../temperature_model_project_20260706/scripts/train_temperature_classifier.py`. Model: `backend/models/temperature_classifier.joblib`, scikit-learn 1.8.0. Historical T50 labels remain 45°C; their physical correctness has not been independently confirmed.

Matched pH/concentration conditions only: 28 samples per temperature, 56 total. Features: pH plus 15 backend color features. ExtraTreesClassifier: 500 trees, min_samples_leaf=1, random_state=42, balanced class weights. Grouped outer five-fold validation keeps each pH/concentration condition together. Inner four-fold validation selects the lowest score threshold from 0.70–0.95 giving at least three accepted predictions and 80% precision in each class; if none qualifies, all predictions abstain. Deployment threshold: 0.70. Scores are not calibrated probabilities.

Outer validation, before deployment feature-range rejection:
- Confusion matrix (true/predicted low, high): [[24, 4], [6, 22]].
- Low recall: 85.7%; high recall: 78.6%; balanced accuracy: 82.1%.
- With abstention: 39/56 accepted, 35/39 correct (89.7%); 17 inconclusive.

At inference, any non-finite feature or feature outside the matched training min/max range also causes abstention. Consequently deployment coverage may be lower than the validation coverage above. Cropping and illumination changes can affect this gate and predictions. No independent acquisition-batch validation exists, so these results do not establish a causal temperature effect or support intermediate-temperature measurement. The temperature output does not adjust concentration predictions.

Deploy the changed frontend, backend, and model artifact together. An older backend yields an unavailable temperature message in the updated frontend. Local verification covered low/high/uncertain decisions, invalid/out-of-range inputs, optional model failure, and both multipart and base64 prediction endpoints using a real T50 image.
