"""
Dissolved Oxygen (DO) Depletion & Fish Mortality Risk Model Wireframe
Models the 7 to 14-day bloom progression curve and predicts biological oxygen demand (BOD)
before oxygen drops below the lethal 4.0 mg/L threshold.
"""

from typing import List, Dict, Any

class DissolvedOxygenPredictor:
    LETHAL_THRESHOLD_MG_L = 4.0
    STRESS_THRESHOLD_MG_L = 5.0

    @classmethod
    def evaluate_risk(
        cls,
        current_ndci: float,
        ndci_trend_last_7_days: List[float],
        water_temp_celsius: float = 27.5
    ) -> Dict[str, Any]:
        """
        Evaluates risk of sudden nocturnal hypoxia and mass fish kill.

        Returns:
            Dictionary containing risk_level (NORMAL, WATCH, HIGH_ALERT, CRITICAL),
            predicted DO in 48-72 hours, and recommended intervention lead time.
        """
        # Trend velocity: change in NDCI over time
        ndci_delta = current_ndci - (ndci_trend_last_7_days[0] if ndci_trend_last_7_days else current_ndci)

        if current_ndci < 0.20 and ndci_delta < 0.05:
            risk_level = "NORMAL"
            predicted_do = 7.2
            days_to_lethal = 99
            action_required = False
        elif current_ndci < 0.30 or ndci_delta < 0.15:
            risk_level = "WATCH"
            predicted_do = 5.4
            days_to_lethal = 7
            action_required = True
        elif current_ndci < 0.45:
            risk_level = "HIGH_ALERT"
            predicted_do = 3.6  # Threatens lethal limit within 48-72h
            days_to_lethal = 3
            action_required = True
        else:
            risk_level = "CRITICAL"
            predicted_do = 2.4  # Acute lethal hypoxia
            days_to_lethal = 1
            action_required = True

        return {
            "current_ndci": current_ndci,
            "ndci_delta_7d": round(ndci_delta, 3),
            "risk_level": risk_level,
            "predicted_do_mg_l": predicted_do,
            "is_below_lethal_limit": predicted_do < cls.LETHAL_THRESHOLD_MG_L,
            "estimated_days_to_lethal_crash": days_to_lethal,
            "action_required": action_required
        }
