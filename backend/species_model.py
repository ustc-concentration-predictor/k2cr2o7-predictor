"""Deployed chromium(VI) species prediction model.

The final deployed route uses pH-specific GradientBoostingRegressor
submodels. Each submodel uses a single image feature, Lab ``a``, to predict
three quantities directly:

    Total Cr(VI), HCrO4-, and Cr2O7^2-

CrO4^2- is not predicted as a separate target. It is calculated by mass
balance:

    CrO4^2- = Total Cr(VI) - HCrO4- - 2 * Cr2O7^2-
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

import joblib
import numpy as np
import pandas as pd


logger = logging.getLogger(__name__)


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
        self.feature_cols: List[str] = ["a"]
        self.target_cols: List[str] = ["total_cr_mM", "HCrO4_mM", "Cr2O7_mM"]
        self.valid_ph_range = (3.0, 8.0)
        self.ka1 = 2.94e-2
        self.ka2 = 1.26e-6
        self.model_name = "pH-submodel GradientBoostingRegressor, single a"
        self.route_strategy = "nearest_available_pH_submodel"
        self.metrics: List[Dict[str, Any]] = []
        self.mass_balance_formula = "CrO4_mM = total_cr_mM - HCrO4_mM - 2 * Cr2O7_mM"
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

        total_cr_mM = float(values["total_cr_mM"])
        hcro4_mM = float(values["HCrO4_mM"])
        cr2o7_mM = float(values["Cr2O7_mM"])
        cro4_raw_mM = total_cr_mM - hcro4_mM - 2.0 * cr2o7_mM
        cro4_mM = max(cro4_raw_mM, 0.0)
        mass_balance_residual_mM = total_cr_mM - hcro4_mM - 2.0 * cr2o7_mM - cro4_raw_mM

        warnings = self._generate_warnings(ph, values["route_pH_model"], cro4_raw_mM)
        confidence = self._calculate_confidence(ph)

        species = {
            "HCrO4_mM": hcro4_mM,
            "Cr2O7_mM": cr2o7_mM,
            "CrO4_mM": cro4_mM,
            "CrO4_raw_mM": cro4_raw_mM,
            "estimated_total_cr_mM": total_cr_mM,
            "mass_balance_residual_mM": mass_balance_residual_mM,
        }

        return {
            "species_concentrations": species,
            "confidence": confidence,
            "warnings": warnings,
            "model_info": {
                "model_name": self.model_name,
                "feature_cols": self.feature_cols,
                "target_cols": self.target_cols,
                "computed_species": ["CrO4_mM"],
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

    def _generate_warnings(self, ph: float, routed_ph: float, cro4_raw_mM: float) -> List[str]:
        warnings: List[str] = []
        ph_min, ph_max = self.valid_ph_range
        if ph < ph_min or ph > ph_max:
            warnings.append(
                f"pH={ph:.1f} is outside the training range ({ph_min:g}-{ph_max:g}); "
                "the prediction may be unreliable."
            )
        if abs(ph - routed_ph) > 1e-9:
            warnings.append(f"pH={ph:.1f} was routed to the nearest trained pH submodel: pH {routed_ph:g}.")
        if cro4_raw_mM < 0:
            warnings.append(
                "The mass-balance CrO4^2- estimate was negative and was clipped to zero for display. "
                "This usually indicates amplified prediction error in the derived CrO4^2- term."
            )
        if ph >= 7.0:
            warnings.append(
                "At higher pH values, CrO4^2- is derived by subtraction and can be more sensitive "
                "to small errors in the directly predicted species."
            )
        return warnings

    def get_model_info(self) -> Dict[str, Any]:
        return {
            "model_type": self.model_name,
            "feature_count": len(self.feature_cols),
            "features": self.feature_cols,
            "target_cols": self.target_cols,
            "computed_species": ["CrO4_mM"],
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
