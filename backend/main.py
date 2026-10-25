"""
FastAPI Server Entrypoint
Matsya-Watch: Satellite-powered Algal Bloom & Fish Mortality Early Warning Service.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import tanks, alerts

app = FastAPI(
    title="Matsya-Watch API",
    description="Early warning system predicting algal bloom fish-kill events in Karnataka village tanks using Sentinel-2 imagery.",
    version="1.0.0-wireframe"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tanks.router)
app.include_router(alerts.router)

@app.get("/")
def health_check():
    return {
        "status": "ONLINE",
        "service": "Matsya-Watch Backend Wireframe",
        "state": "Karnataka",
        "monitored_panchayat_tanks": 3407,
        "docs_url": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
