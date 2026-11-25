
from fastapi import FastAPI

app = FastAPI(
    title="Power Bill Estimator API",
    description="Backend API for automatic electricity bill fetching and estimation",
    version="2.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Power Bill Estimator API",
        "version": "2.0.0",
        "status": "Running"
    }


@app.get("/calculate-units")
def calculate_units(opening_reading: float, current_reading: float):

    if current_reading < opening_reading:
        return {
            "error": "Current reading cannot be less than opening reading"
        }

    units_consumed = current_reading - opening_reading

    return {
        "opening_reading": opening_reading,
        "current_reading": current_reading,
        "units_consumed": units_consumed
    }

