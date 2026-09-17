import unittest
from unittest.mock import patch
import numpy as np
from temperature_model import predict_temperature

class FakeClassifier:
    def __init__(self, score):
        self.score = score
    def predict_proba(self, x):
        return np.array([[1-self.score, self.score]])

class TemperatureTests(unittest.TestCase):
    def bundle(self, score):
        return {'model': FakeClassifier(score), 'features': ['pH', 'a'], 'threshold': .8,
                'minimum': {'pH': 4, 'a': 100}, 'maximum': {'pH': 7, 'a': 150}}
    def test_decisions(self):
        for score, expected in [(.1, 'low'), (.5, 'uncertain'), (.9, 'high')]:
            with self.subTest(score=score), patch('temperature_model.load_model', return_value=self.bundle(score)):
                self.assertEqual(predict_temperature({'a': 125}, 5)['status'], expected)
    def test_domain_and_invalid(self):
        with patch('temperature_model.load_model', return_value=self.bundle(.9)):
            self.assertEqual(predict_temperature({'a': 125}, 8)['reason'], 'out_of_range')
            self.assertEqual(predict_temperature({'a': float('nan')}, 5)['reason'], 'invalid_features')
    def test_optional_model_failure(self):
        with patch('temperature_model.load_model', side_effect=FileNotFoundError), self.assertLogs('temperature_model', level='ERROR'):
            self.assertEqual(predict_temperature({'a': 125}, 5)['reason'], 'unavailable')

if __name__ == '__main__':
    unittest.main()
