"""
Intervention Advisory & Mitigation Engine
Calculates precise treatment dosage based on tank surface area, depth, and predicted DO.
"""

from typing import Dict, Any

class AdvisoryEngine:
    @staticmethod
    def generate_intervention_plan(surface_area_ha: float, current_do: float, risk_level: str) -> Dict[str, Any]:
        """
        Generates standard operating procedure (SOP) mitigation steps:
        - Aeration run hours
        - Agricultural limestone (CaCO3) or quicklime (CaO) application
        - Nutrient inflow diversion
        """
        # Aeration requirement rule: 1.5 HP paddle-wheel aerator or diesel pump per hectare
        if risk_level in ["HIGH_ALERT", "CRITICAL"]:
            aeration_hours = 8 if risk_level == "HIGH_ALERT" else 14
            lime_kg_per_ha = 150.0  # Precipitates excess phosphates and stabilizes pH
        elif risk_level == "WATCH":
            aeration_hours = 4
            lime_kg_per_ha = 75.0
        else:
            aeration_hours = 0
            lime_kg_per_ha = 0.0

        total_lime_kg = round(lime_kg_per_ha * surface_area_ha, 1)

        emergency_harvest = "NOT_REQUIRED"
        if risk_level == "CRITICAL" and current_do < 3.0:
            emergency_harvest = "RECOMMENDED: Initiate partial emergency netting to minimize total capital loss."

        return {
            "surface_area_hectares": surface_area_ha,
            "risk_level": risk_level,
            "aeration_hours_per_day": aeration_hours,
            "recommended_quicklime_kg": total_lime_kg,
            "inflow_diversion_required": risk_level in ["WATCH", "HIGH_ALERT", "CRITICAL"],
            "emergency_harvest_status": emergency_harvest,
            "best_practice_steps": [
                "1. Run aeration strictly between 02:00 AM and 07:00 AM when photosynthesis stops and oxygen is lowest.",
                "2. Dilute quicklime in water drums before uniform broadcast across the tank surface.",
                "3. Stop feeding artificial pelleted feed immediately to avoid increasing organic load."
            ]
        }
