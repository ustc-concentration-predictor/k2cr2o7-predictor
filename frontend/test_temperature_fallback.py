import sys
from pathlib import Path
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'backend'))
from image_processor import preprocess_image
from temperature_fallback import complete_temperature


class TemperatureFallbackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from PIL import Image
        from io import BytesIO
        output = BytesIO()
        Image.new('RGB', (80, 80), (175, 150, 60)).save(output, format='PNG')
        cls.image = output.getvalue()
        features = preprocess_image(cls.image, 5)['features_dict']
        cls.features = {'rgb': [features[k] for k in ['R','G','B']],
                        'hsv': [features[k] for k in ['H','S','V']],
                        'lab': [features[k] for k in ['L','a','b']],
                        'ratios': {k:v for k,v in features.items() if '_' in k}}

    def test_missing_and_legacy_status_get_real_model_prediction(self):
        for status in [None, 'uncertain', 'unavailable']:
            result = {'features_used': self.features}
            if status:
                result['temperature_tendency'] = {'status': status}
            for image in [None, self.image]:
                with self.subTest(status=status, image=image is not None):
                    updated = complete_temperature(result, 5, image)
                    self.assertIn(updated['temperature_tendency']['status'], ['low', 'high'])
                    self.assertEqual(updated['temperature_tendency']['source'], 'streamlit_bundled_model')

    def test_existing_result_is_preserved(self):
        result = {'temperature_tendency': {'status': 'low'}}
        self.assertIs(complete_temperature(result, 5), result)

    def test_failure_does_not_fabricate_temperature(self):
        with patch('temperature_model.predict_temperature', return_value={'status': 'unavailable'}):
            result = {'features_used': self.features}
            self.assertNotIn('temperature_tendency', complete_temperature(result, 5))

if __name__ == '__main__':
    unittest.main()
