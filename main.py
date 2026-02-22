from fastapi import FastAPI
import pandas as pd
import requests

app = FastAPI()

# Load dataset
try:
    df = pd.read_csv("weather.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["city", "temperature", "humidity"])

@app.get("/")
def home():
    return {"message": "Weather Data API Running"}

@app.get("/live-weather/{city}")
def live_weather(city: str):
    try:
        # First convert city name to latitude & longitude
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_response = requests.get(geo_url, timeout=10).json()

        if "results" not in geo_response:
            return {"error": "City not found"}

        lat = geo_response["results"][0]["latitude"]
        lon = geo_response["results"][0]["longitude"]

        # Fetch weather using coordinates
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&current_weather=true"
        )

        weather_response = requests.get(weather_url, timeout=10).json()
        current = weather_response["current_weather"]

        return {
            "city": city,
            "temperature_C": current["temperature"],
            "windspeed": current["windspeed"],
            "time": current["time"]
        }

    except Exception as e:
        return {"error": str(e)}

# Average temperature by city
@app.get("/avg-temperature")
def avg_temperature():
    result = df.groupby("city")["temperature"].mean()
    return result.to_dict()

# Highest temperature recorded
@app.get("/max-temperature")
def max_temp():
    max_temp = df["temperature"].max()
    return {"highest_temperature": int(max_temp)}
@app.get("/city/{city_name}")
def get_city_data(city_name: str):
    city_data = df[df["city"].str.lower() == city_name.lower()]
    return city_data.to_dict(orient="records")
@app.get("/city-summary")
def city_summary():
    summary = df.groupby("city").max().reset_index()
    return summary.to_dict(orient="records")
@app.get("/generate-report")
def generate_report():
    summary = df.groupby("city").max().reset_index()
    
    # Save report as CSV
    summary.to_csv("report.csv", index=False)
    
    return {"message": "Report Generated Successfully"}


@app.get("/health")
def health_check():
    return {"status": "API is running"}