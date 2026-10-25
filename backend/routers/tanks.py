"""
Tanks API Router Wireframe
Endpoints for fetching monitored Gram Panchayat tanks, GeoJSON geometries, and telemetry time-series.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import json
import os

router = APIRouter(prefix="/api/v1/tanks", tags=["Tanks"])

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "samples")

@router.get("/")
def list_monitored_tanks(district: Optional[str] = None, risk_level: Optional[str] = None):
    """
    Returns list of all monitored tanks with optional filtering by Karnataka district or risk stage.
    """
    geojson_file = os.path.join(DATA_PATH, "karnataka_pilot_tanks.geojson")
    with open(geojson_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = []
    for f in data["features"]:
        props = f["properties"]
        if district and props["district"].lower() != district.lower():
            continue
        if risk_level and props["current_risk_level"].lower() != risk_level.lower():
            continue
        results.append(props)

    return {"count": len(results), "tanks": results}

@router.get("/{tank_id}/telemetry")
def get_tank_bloom_history(tank_id: str):
    """
    Returns the 14-day bloom progression curve (NDCI, Chlorophyll, Dissolved Oxygen) for a tank.
    """
    hist_file = os.path.join(DATA_PATH, "simulated_14day_telemetry.json")
    with open(hist_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if data.get("tank_id") != tank_id and tank_id != "KA-MND-0412":
        raise HTTPException(status_code=404, detail="Tank telemetry record not found")

    return data
