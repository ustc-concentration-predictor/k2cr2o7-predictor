"""Deployed chromium(VI) species prediction model.

The route uses pH-specific GradientBoostingRegressor submodels. Each
submodel uses two image features, Lab ``a`` and ``R_over_G``, to predict
three species concentrations directly:

    HCrO4-, Cr2O7^2-, and CrO4^2-

Total Cr(VI), expressed on a chromium-atom basis, is calculated by mass
balance and is not a direct model target:

    Total Cr(VI) = HCrO4- + 2 * Cr2O7^2- + CrO4^2-
"""

from __future__ import annotations

import hashlib
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

import joblib
import numpy as np
import pandas as pd


logger = logging.getLogger(__name__)


# The deployed artifact is the verified Ka2=3e-7, a + R_over_G three-species
# model. Its package omits training-domain metadata, so retain the ranges
# calculated from the exact 114-row training table here.
DEPLOYED_TRAINING_CONCENTRATION_RANGE_MM = [1.0, 10.0]
DEPLOYED_TRAINING_FEATURE_RANGES = {
    "a": {
        "overall": {"min": 120.32704081632652, "max": 141.85545267489712},
        "by_ph": {
            3.0: {"min": 125.83497732426304, "max": 140.72048672343428},
            4.0: {"min": 125.23778344671202, "max": 141.85545267489712},
            5.0: {"min": 125.19733333333332, "max": 140.70950035908484},
            6.0: {"min": 124.43874382857432, "max": 139.0798279689234},
            7.0: {"min": 121.89387654320988, "max": 130.8430410275106},
            8.0: {"min": 120.32704081632652, "max": 122.90827771598072},
        },
    },
    "R_over_G": {
        "overall": {"min": 1.055610967827742, "max": 1.420436104008958},
        "by_ph": {
            3.0: {"min": 1.151548921160088, "max": 1.393979998979049},
            4.0: {"min": 1.1408391983029802, "max": 1.420436104008958},
            5.0: {"min": 1.1355247731604776, "max": 1.3917191708033467},
            6.0: {"min": 1.1259990078379225, "max": 1.3682482627067625},
            7.0: {"min": 1.0820378486184794, "max": 1.233023327980495},
            8.0: {"min": 1.055610967827742, "max": 1.1087590224857222},
        },
    },
}


class SpeciesPredictor:
    """Predict chromium(VI) species from backend image features and pH."""

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

    def __init__(self, model_path: Optional[str] = None):
        if model_path is None:
            model_path = Path(__file__).parent / "models" / "species_model.joblib"
        self.model_path = Path(model_path)
        self.models_by_ph: Dict[float, Any] = {}
        self.feature_cols: List[str] = ["a", "R_over_G"]
        self.target_cols: List[str] = ["HCrO4_mM", "Cr2O7_mM", "CrO4_mM"]
        self.valid_ph_range = (3.0, 8.0)
        self.ka1 = 2.94e-2
        self.ka2 = 3.0e-7
        self.model_name = "pH-submodel GradientBoostingRegressor, a + R_over_G"
        self.route_strategy = "nearest_available_pH_submodel"
        self.metrics: List[Dict[str, Any]] = []
        self.computed_species: List[str] = ["total_cr_mM"]
        self.prediction_strategy = "three_species_direct_total_cr_by_mass_balance"
        self.mass_balance_formula = "total_cr_mM = HCrO4_mM + 2*Cr2O7_mM + CrO4_mM"
        self._load_model()

    def _load_model(self) -> None:
        if not self.model_path.exists():
            raise FileNotFoundError(f"Species model file does not exist: {self.model_path}")

        package = joblib.load(self.model_path)
        if not isinstance(package, dict):
            raise ValueError("Species model package must be a dictionary.")

        if "models_by_ph" not in package:
            raise ValueError("Species model package is missing 'models_by_ph'.")

        self.models_by_ph = {float(k): v for k, v in package["models_by_ph"].items()}
        self.feature_cols = list(package.get("feature_cols", self.feature_cols))
        self.target_cols = list(package.get("target_cols", self.target_cols))
        self.valid_ph_range = tuple(package.get("valid_ph_range", self.valid_ph_range))
        self.ka1 = float(package.get("ka1", self.ka1))
        self.ka2 = float(package.get("ka2", self.ka2))
        self.model_name = package.get("model_name", self.model_name)
        self.route_strategy = package.get("route_strategy", self.route_strategy)
        self.metrics = package.get("external_test_metrics", [])
        self.computed_species = list(package.get("computed_species", self.computed_species))
        self.prediction_strategy = package.get("prediction_strategy", self.prediction_strategy)
        self.model_version = hashlib.sha256(self.model_path.read_bytes()).hexdigest()[:12]
        self.training_feature_ranges = (
            package.get("training_feature_ranges") or DEPLOYED_TRAINING_FEATURE_RANGES
        )
        self.training_concentration_range_mM = (
            package.get("training_concentration_range_mM")
            or DEPLOYED_TRAINING_CONCENTRATION_RANGE_MM
        )
        self.mass_balance_formula = package.get("mass_balance_formula", self.mass_balance_formula)
        logger.info("Species model loaded: %s", self.model_name)

    def _route_ph(self, ph: float) -> float:
        available = np.array(sorted(self.models_by_ph), dtype=float)
        if available.size == 0:
            raise RuntimeError("No pH submodels are available.")
        return float(available[np.argmin(np.abs(available - ph))])

    def _predict_direct_targets(self, feature_dict: Dict[str, float], ph: float) -> Dict[str, float]:
        routed_ph = self._route_ph(ph)
        model = self.models_by_ph[routed_ph]
        x = pd.DataFrame(
            [[float(feature_dict[col]) for col in self.feature_cols]],
            columns=self.feature_cols,
            dtype=float,
        )
        pred = np.asarray(model.predict(x)[0], dtype=float)
        pred = np.clip(pred, 0.0, None)
        values = dict(zip(self.target_cols, pred))
        values["route_pH_model"] = routed_ph
        return values

    def predict(self, feature_vector: np.ndarray) -> Dict[str, Any]:
        if feature_vector.shape[1] != len(self.FEATURE_ORDER):
            raise ValueError(
                f"Feature dimension mismatch: input {feature_vector.shape[1]}, "
                f"expected {len(self.FEATURE_ORDER)}"
            )

        feature_dict = dict(zip(self.FEATURE_ORDER, feature_vector[0]))
        ph = float(feature_dict["pH"])
        values = self._predict_direct_targets(feature_dict, ph)

        hcro4_mM = float(values["HCrO4_mM"])
        cr2o7_mM = float(values["Cr2O7_mM"])
        cro4_mM = float(values["CrO4_mM"])
        total_cr_mM = hcro4_mM + 2.0 * cr2o7_mM + cro4_mM
        mass_balance_residual_mM = total_cr_mM - hcro4_mM - 2.0 * cr2o7_mM - cro4_mM

        warnings = self._generate_warnings(ph, values["route_pH_model"], feature_dict)
        confidence = self._calculate_confidence(ph)

        species = {
            "HCrO4_mM": hcro4_mM,
            "Cr2O7_mM": cr2o7_mM,
            "CrO4_mM": cro4_mM,
            "estimated_total_cr_mM": total_cr_mM,
            "mass_balance_residual_mM": mass_balance_residual_mM,
        }

        return {
            "species_concentrations": species,
            "confidence": confidence,
            "warnings": warnings,
            "model_info": {
                **self.get_model_info(),
                "model_name": self.model_name,
                "feature_cols": self.feature_cols,
                "target_cols": self.target_cols,
                "computed_species": self.computed_species,
                "prediction_strategy": self.prediction_strategy,
                "valid_ph_range": self.valid_ph_range,
                "route_strategy": self.route_strategy,
                "route_pH_model": values["route_pH_model"],
                "ka1": self.ka1,
                "ka2": self.ka2,
                "mass_balance_formula": self.mass_balance_formula,
            },
        }

    def _calculate_confidence(self, ph: float) -> float:
        ph_min, ph_max = self.valid_ph_range
        if ph < ph_min or ph > ph_max:
            return 0.35
        if ph >= 7.0:
            return 0.75
        return 0.9

    def _generate_warnings(
        self, ph: float, routed_ph: float, feature_dict: Dict[str, float]
    ) -> List[str]:
        warnings: List[str] = []
        if not self.training_feature_ranges:
            warnings.append("Training color-feature ranges are unavailable; image domain validity cannot be assessed. Consult your teacher.")
        else:
            feature_labels = {"a": "Lab a*", "R_over_G": "R_over_G"}
            for feature_name in self.feature_cols:
                metadata = self.training_feature_ranges.get(feature_name, {})
                by_ph = metadata.get("by_ph", {}) if isinstance(metadata, dict) else {}
                bounds = by_ph.get(routed_ph) or by_ph.get(str(routed_ph))
                if not bounds or feature_name not in feature_dict:
                    continue
                value = float(feature_dict[feature_name])
                lower = float(bounds["min"])
                upper = float(bounds["max"])
                tolerance = 1e-9 * max(1.0, abs(lower), abs(upper))
                if value < lower - tolerance or value > upper + tolerance:
                    label = feature_labels.get(feature_name, feature_name)
                    warnings.append(
                        f"{label}={value:.4f} is outside the training color-feature range "
                        f"for routed pH {routed_ph:g} ({lower:.4f}–{upper:.4f}); image domain "
                        "validity is uncertain. Consult your teacher."
                    )
        ph_min, ph_max = self.valid_ph_range
        if ph < ph_min or ph > ph_max:
            warnings.append(
                f"pH={ph:.1f} is outside the training range ({ph_min:g}-{ph_max:g}); "
                "the prediction may be unreliable."
            )
        if abs(ph - routed_ph) > 1e-9:
            warnings.append(f"pH={ph:.1f} was routed to the nearest trained pH submodel: pH {routed_ph:g}.")
        if ph >= 7.0:
            warnings.append(
                "At higher pH values, predictions remain within the trained range but receive a lower "
                "heuristic confidence score; verify image conditions and interpret the result cautiously."
            )
        return warnings

    def get_model_info(self) -> Dict[str, Any]:
        return {
            "model_version": self.model_version,
            "training_feature_ranges": self.training_feature_ranges,
            "training_concentration_range_mM": self.training_concentration_range_mM,
            "confidence_method": "pH heuristic only; not a calibrated probability",
            "model_type": self.model_name,
            "feature_count": len(self.feature_cols),
            "features": self.feature_cols,
            "target_cols": self.target_cols,
            "computed_species": self.computed_species,
            "prediction_strategy": self.prediction_strategy,
            "available_pH_submodels": sorted(self.models_by_ph),
            "valid_ph_range": self.valid_ph_range,
            "route_strategy": self.route_strategy,
            "constants": {
                "Ka1": self.ka1,
                "Ka2": self.ka2,
            },
            "mass_balance_formula": self.mass_balance_formula,
            "external_test_metrics": self.metrics,
        }


_species_predictor_instance = None


def get_species_predictor() -> SpeciesPredictor:
    global _species_predictor_instance
    if _species_predictor_instance is None:
        _species_predictor_instance = SpeciesPredictor()
    return _species_predictor_instance
