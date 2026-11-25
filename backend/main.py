
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

app = FastAPI(
    title="Power Bill Estimator API",
    description="Backend API for automatic electricity bill fetching and estimation",
    version="2.0.0"
)

class MeterReading(BaseModel):
    opening_reading: float
    current_reading: float

@app.get("/")
def home():
    return {
        "message": "Welcome to Power Bill Estimator API",
        "version": "2.0.0",
        "status": "Running"
    }


@app.get("/calculate-units")
@app.post("/calculate-units")
def calculate_units_post(readings: MeterReading):

    opening_reading = readings.opening_reading
    current_reading = readings.current_reading

    if opening_reading < 0 or current_reading < 0:
        raise HTTPException(
            status_code=400,
            detail="Meter readings cannot be negative"
        )

    if current_reading < opening_reading:
        raise HTTPException(
            status_code=400,
            detail="Current reading cannot be less than opening reading"
        )

    units_consumed = current_reading - opening_reading

    return {
        "opening_reading": opening_reading,
        "current_reading": current_reading,
        "units_consumed": units_consumed
    }