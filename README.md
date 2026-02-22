# 🌦️ Real-Time Weather Data Processing API

A FastAPI-based backend project that fetches real-time weather data, processes datasets using Pandas, and generates automated reports.

---

## 🚀 Features

- Fetch live weather data for any city using Open-Meteo API
- Perform data analysis using Pandas
- City-wise filtering and aggregation
- Generate automated CSV reports
- RESTful API endpoints
- JSON responses for easy integration

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Pandas
- NumPy
- Requests
- Uvicorn

---

## 📊 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | API status message |
| `/live-weather/{city}` | Fetch real-time weather |
| `/avg-temperature` | Average temperature by city |
| `/max-temperature` | Highest recorded temperature |
| `/city/{city}` | Filter dataset by city |
| `/city-summary` | Aggregated city report |
| `/generate-report` | Export CSV report |
| `/health` | Health check endpoint |

---

## ⚙️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/Sumitsingh-dev1/weather-data-api.git
cd weather-data-api
