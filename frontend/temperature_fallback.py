"""Run the bundled temperature classifier when the remote API cannot supply it."""
import logging
from pathlib import Path
import sys


def complete_temperature(result, ph, image_bytes=None):
    if result.get('error') or result.get('temperature_tendency', {}).get('status') in ('low', 'high'):
        return result
    try:
        backend = str(Path(__file__).resolve().parents[1] / 'backend')
        if backend not in sys.path:
            sys.path.append(backend)
        from temperature_model import predict_temperature
        if image_bytes is not None:
            from image_processor import preprocess_image
            features = preprocess_image(image_bytes, ph)['features_dict']
        else:
            # Older saved responses contain rounded versions of the same features.
            used = result['features_used']
            features = dict(zip(['R', 'G', 'B'], used['rgb']))
            features.update(zip(['H', 'S', 'V'], used['hsv']))
            features.update(zip(['L', 'a', 'b'], used['lab']))
            features.update(used['ratios'])
        tendency = predict_temperature(features, ph)
        if tendency['status'] in ('low', 'high'):
            result = {**result, 'temperature_tendency': {**tendency, 'source': 'streamlit_bundled_model'}}
    except Exception:
        logging.getLogger(__name__).exception('Bundled temperature inference failed')
    return result
