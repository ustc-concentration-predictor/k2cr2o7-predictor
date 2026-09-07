"""Optional experimental temperature tendency, independent of concentration inference."""
from functools import lru_cache
from pathlib import Path
import logging
import joblib
import numpy as np
import pandas as pd

MODEL_PATH = Path(__file__).resolve().parent / 'models/temperature_classifier.joblib'

@lru_cache(maxsize=1)
def load_model():
    return joblib.load(MODEL_PATH)

def predict_temperature(features, ph):
    result = {'status': 'unavailable', 'reason': 'unavailable', 'experimental': True,
              'reference_temperatures_C': [25, 45]}
    try:
        bundle = load_model()
        values = {**features, 'pH': ph}
        row = np.array([values[k] for k in bundle['features']], dtype=float)
        if not np.isfinite(row).all():
            return {**result, 'reason': 'invalid_features'}
        score = float(bundle['model'].predict_proba(pd.DataFrame([row], columns=bundle['features']))[0, 1])
        result.update(status='high' if score >= 0.5 else 'low', reason='reference_similarity')
        return result
    except Exception:
        logging.getLogger(__name__).exception('Temperature inference unavailable')
        return {**result, 'reason': 'unavailable'}
