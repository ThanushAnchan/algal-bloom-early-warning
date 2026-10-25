"""
Alerts API Router Wireframe
Endpoints for viewing active warnings and triggering multi-channel Kannada/English SMS broadcasts.
"""

from fastapi import APIRouter
from backend.services.alert_dispatcher import AlertDispatcher
from backend.services.advisory_engine import AdvisoryEngine
from backend.models.schemas import AlertDispatchPayload

router = APIRouter(prefix="/api/v1/alerts", tags=["Alerts & Advisories"])

@router.get("/active")
def get_active_warnings():
    """
    Returns tanks in WATCH, HIGH_ALERT, or CRITICAL status needing intervention.
    """
    return {
        "active_alerts_count": 2,
        "high_priority": [
            {
                "tank_id": "KA-MND-0412",
                "tank_name": "Hosahalli Gram Panchayat Kere",
                "district": "Mandya",
                "risk_level": "HIGH_ALERT",
                "predicted_do_in_48h": 3.2,
                "days_into_bloom": 7,
                "advisory": AdvisoryEngine.generate_intervention_plan(12.0, 3.2, "HIGH_ALERT")
            }
        ]
    }

@router.post("/dispatch")
def dispatch_manual_alert(payload: AlertDispatchPayload):
    """
    Triggers immediate SMS/WhatsApp alert in Kannada and English to the cooperative heads.
    """
    tank_mock = {
        "name_english": "Hosahalli GP Tank",
        "name_kannada": "ಹೊಸಹಳ್ಳಿ ಗ್ರಾಮ ಪಂಚಾಯತಿ ಕೆರೆ",
        "panchayat": "Hosahalli",
        "phone": "+919845012345",
        "predicted_do_48h": 3.2
    }
    result = AlertDispatcher.dispatch_alert(tank_mock, payload.risk_level)
    return {"message": "Alert dispatched successfully", "details": result}
