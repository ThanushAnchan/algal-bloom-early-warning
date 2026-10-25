"""
Pydantic Data Schemas for Matsya-Watch API
Defines input/output models for Tanks, Telemetry, Alerts, and Advisory Actions.
"""

from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field

class RiskLevel(str, Enum):
    NORMAL = "NORMAL"
    WATCH = "WATCH"
    HIGH_ALERT = "HIGH_ALERT"
    CRITICAL = "CRITICAL"

class ContactPerson(BaseModel):
    name: str
    role: str
    phone_number: str
    preferred_language: str = "kn"

class TankSummary(BaseModel):
    tank_id: str
    name_english: str
    name_kannada: str
    district: str
    taluk: str
    panchayat_name: str
    surface_area_hectares: float
    current_risk_level: RiskLevel
    latest_ndci: float
    predicted_do_48h: float
    contact: ContactPerson

class TelemetryPoint(BaseModel):
    day: int
    date: str
    ndci: float
    chlorophyll_ug_l: float
    dissolved_oxygen_mg_l: float
    water_temp_c: float
    status: RiskLevel
    note: str

class AlertDispatchPayload(BaseModel):
    tank_id: str
    risk_level: RiskLevel
    channel: str = Field(default="WHATSAPP_AND_SMS", description="SMS, WHATSAPP, or IVR")
    custom_note: Optional[str] = None

class AdvisoryIntervention(BaseModel):
    tank_id: str
    risk_level: RiskLevel
    aeration_hours_required: int
    recommended_lime_kg: float
    stop_inflow_runoff: bool
    harvest_recommendation: str
