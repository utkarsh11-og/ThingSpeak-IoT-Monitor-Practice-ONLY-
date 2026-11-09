from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path


from analytics.analysis import analyze_sensor_data


from services.thingspeak import get_channel_data

app = FastAPI(title="ThingSpeak IoT Dashboard API")




@app.get("/api/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/sensors")
def get_sensors():
    feeds = get_channel_data(results=20)

    if not feeds:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve ThingSpeak data"
        )

    latest = feeds[-1]

    return {
        "entry_id": latest.get("entry_id"),
        "temperature": latest.get("field1"),
        "humidity": latest.get("field2"),
        "timestamp": latest.get("created_at")
    }




@app.get("/api/history")
def get_sensor_history():

    feeds = get_channel_data(results=20)

    if not feeds:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve historical data"
        )

    history = []

    for feed in feeds:
        history.append({
            "temperature": feed.get("field1"),
            "humidity": feed.get("field2"),
            "timestamp": feed.get("created_at")
        })

    return {"history": history}





@app.get("/api/analytics")
def get_sensor_analytics():

    feeds = get_channel_data(results=100)

    if not feeds:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve sensor data"
        )

    analysis = analyze_sensor_data(feeds)

    if analysis is None:
        raise HTTPException(
            status_code=422,
            detail="No valid sensor readings available"
        )

    return analysis


BASE_DIR = Path(__file__).resolve().parent.parent

FRONTEND_DIR = BASE_DIR / "frontend"

app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static"
)


@app.get("/")
def serve_dashboard():
    return FileResponse(FRONTEND_DIR / "index.html")