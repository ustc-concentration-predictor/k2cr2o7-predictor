"""Image preprocessing and color feature extraction.

The frontend is expected to upload a cropped solution-region image. The backend
then applies a consistent lighting normalization step before extracting RGB,
HSV, Lab, and ratio features. The deployed final model uses only Lab ``a``, but
the full feature vector is kept for compatibility and frontend display.
"""

from __future__ import annotations

import io
import logging
from typing import Dict

import cv2
import numpy as np


logger = logging.getLogger(__name__)


class ImagePreprocessor:
    """Preprocess cropped colorimetric images and extract color features."""

    FEATURE_ORDER = [
        "pH",
        "R",
        "G",
        "B",
        "H",
        "S",
        "V",
        "L",
        "a",
        "b",
        "R_over_G",
        "R_over_B",
        "G_over_B",
        "R_ratio",
        "G_ratio",
        "B_ratio",
    ]

    def preprocess(self, image: np.ndarray) -> Dict:
        if image is None or image.size == 0:
            raise ValueError("Input image is empty.")

        normalized = self._normalize_lighting(image)
        features = self._extract_color_features(normalized)
        return {
            "roi": normalized,
            "features": features,
            "metadata": {
                "original_shape": image.shape,
                "roi_shape": normalized.shape,
                "extraction_method": "frontend_roi_lighting_normalized",
            },
        }

    def _normalize_lighting(self, image: np.ndarray) -> np.ndarray:
        """Normalize illumination using CLAHE on the Lab L channel."""
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l_channel, a_channel, b_channel = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        l_normalized = clahe.apply(l_channel)
        normalized_lab = cv2.merge([l_normalized, a_channel, b_channel])
        return cv2.cvtColor(normalized_lab, cv2.COLOR_LAB2BGR)

    def _extract_color_features(self, image: np.ndarray) -> Dict[str, float]:
        features: Dict[str, float] = {}

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        r_mean = float(np.mean(rgb[:, :, 0]))
        g_mean = float(np.mean(rgb[:, :, 1]))
        b_mean = float(np.mean(rgb[:, :, 2]))
        features["R"] = r_mean
        features["G"] = g_mean
        features["B"] = b_mean

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features["H"] = float(np.mean(hsv[:, :, 0]))
        features["S"] = float(np.mean(hsv[:, :, 1]))
        features["V"] = float(np.mean(hsv[:, :, 2]))

        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        features["L"] = float(np.mean(lab[:, :, 0]))
        features["a"] = float(np.mean(lab[:, :, 1]))
        features["b"] = float(np.mean(lab[:, :, 2]))

        eps = 1e-6
        features["R_over_G"] = r_mean / (g_mean + eps)
        features["R_over_B"] = r_mean / (b_mean + eps)
        features["G_over_B"] = g_mean / (b_mean + eps)

        rgb_sum = r_mean + g_mean + b_mean + eps
        features["R_ratio"] = r_mean / rgb_sum
        features["G_ratio"] = g_mean / rgb_sum
        features["B_ratio"] = b_mean / rgb_sum
        return features

    def get_feature_vector(self, features: Dict[str, float], ph: float) -> np.ndarray:
        features_with_ph = features.copy()
        features_with_ph["pH"] = float(ph)
        vector = np.array([features_with_ph[key] for key in self.FEATURE_ORDER], dtype=float)
        logger.info("Extracted Lab a=%.4f for pH=%.2f", features_with_ph["a"], ph)
        return vector.reshape(1, -1)


def _decode_image(image_bytes: bytes) -> np.ndarray:
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if image is not None:
        return image

    try:
        from PIL import Image

        pil_image = Image.open(io.BytesIO(image_bytes))
        if pil_image.mode != "RGB":
            pil_image = pil_image.convert("RGB")
        return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    except Exception as exc:
        raise ValueError(f"Unable to decode image. Please upload a valid image file. Details: {exc}") from exc


def preprocess_image(image_bytes: bytes, ph: float) -> Dict:
    image = _decode_image(image_bytes)
    preprocessor = ImagePreprocessor()
    result = preprocessor.preprocess(image)
    feature_vector = preprocessor.get_feature_vector(result["features"], ph)
    return {
        "feature_vector": feature_vector,
        "features_dict": result["features"],
        "roi_image": result["roi"],
        "metadata": result["metadata"],
    }
