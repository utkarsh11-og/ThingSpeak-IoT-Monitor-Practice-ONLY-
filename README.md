# 🌡️ ThingSpeak IoT Environmental Monitoring System

A Python-based IoT environmental monitoring application that integrates **ThingSpeak Cloud, FastAPI, and a custom web dashboard** to collect, store, analyse, and visualize environmental sensor data.

This project uses simulated sensor readings to demonstrate an end-to-end IoT monitoring workflow without requiring physical hardware.

## 📌 Project Overview

The application simulates environmental sensors that generate temperature and humidity readings. The readings are uploaded to ThingSpeak Cloud using its Write API.

A FastAPI backend retrieves the stored readings through the ThingSpeak Read API, processes the data, and exposes REST endpoints to a custom web dashboard.

The dashboard displays current sensor readings, historical charts, and statistical analytics.

## ✨ Features

- **Sensor Simulation:** Generates random temperature and humidity readings using Python.
- **Cloud Integration:** Uploads sensor data to ThingSpeak using REST APIs.
- **Data Retrieval:** Retrieves historical sensor readings in JSON format.
- **Data Validation:** Checks sensor readings and skips invalid entries.
- **Statistical Analytics:** Calculates average, maximum, and minimum values.
- **REST API:** Provides endpoints through FastAPI.
- **Live Dashboard:** Displays current temperature and humidity.
- **Historical Visualization:** Interactive temperature and humidity charts using Chart.js.
- **Automatic Refresh:** Updates dashboard data periodically.
- **Manual Refresh:** Allows users to refresh dashboard data on demand.
- **Connection Monitoring:** Displays backend connection status.
- **Responsive Interface:** Dark-themed dashboard with responsive layouts.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Sensor simulation and data processing |
| ThingSpeak | IoT cloud platform and data storage |
| FastAPI | Backend REST API |
| HTML5 | Dashboard structure |
| CSS3 | Dashboard styling |
| JavaScript | Frontend functionality |
| Chart.js | Historical data visualization |
| Requests | HTTP communication |
| python-dotenv | Environment configuration |
| Uvicorn | ASGI application server |

## 🏗️ System Architecture

```text
        Python Sensor Simulator
                  |
                  |
                  v
          ThingSpeak Write API
                  |
                  v
           ThingSpeak Cloud
             Data Storage
                  |
                  |
             Read API
                  |
                  v
           FastAPI Backend
                  |
          +-------+-------+
          |       |       |
          v       v       v
        Latest  History Analytics
          |       |       |
          +-------+-------+
                  |
                  v
          JavaScript Frontend
                  |
          +-------+-------+
          |       |       |
          v       v       v
        Sensor  Historical Statistics
        Cards    Charts    Cards
```

## 📂 Project Structure

```text
ThingSpeak-IoT-Monitor/
│
├── analytics/
│   ├── __init__.py
│   └── analysis.py
│
├── backend/
│   ├── __init__.py
│   └── app.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── services/
│   ├── __init__.py
│   └── thingspeak.py
│
├── simulator/
│   ├── __init__.py
│   └── sensor.py
│
├── .env.example
├── .gitignore
├── main.py
├── read_data.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/utkarsh11-og/ThingSpeak-IoT-Monitor-Practice-ONLY-.git
```

```bash
cd ThingSpeak-IoT-Monitor-Practice-ONLY-
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure ThingSpeak

Create a ThingSpeak account and a channel with these fields:

| Field | Description |
|---|---|
| Field 1 | Temperature (°C) |
| Field 2 | Humidity (%) |

Copy the `.env.example` file and rename the copy to `.env`.

Add your own ThingSpeak credentials:

```env
THINGSPEAK_CHANNEL_ID=your_channel_id
THINGSPEAK_WRITE_API_KEY=your_write_api_key
THINGSPEAK_READ_API_KEY=your_read_api_key
```

**Never upload your actual `.env` file or API credentials to GitHub.**

## 🚀 Running the Application

The application has two independent processes.

### 1. Start the sensor simulator

Open a terminal in the project directory:

```bash
python main.py
```

The simulator generates environmental readings and uploads them to ThingSpeak.

### 2. Start the FastAPI backend

Open another terminal:

```bash
python -m uvicorn backend.app:app --reload
```

### 3. Open the dashboard

Visit:

```text
http://127.0.0.1:8000
```

The dashboard will retrieve sensor readings and display the available analytics and visualizations.

## 🔌 API Endpoints

The FastAPI backend exposes the following endpoints:

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Serves the dashboard |
| `/api/health` | GET | Checks backend health |
| `/api/sensors` | GET | Retrieves the latest sensor reading |
| `/api/history` | GET | Retrieves historical sensor readings |
| `/api/analytics` | GET | Returns statistical sensor analytics |
| `/docs` | GET | Opens interactive API documentation |

## 📊 Dashboard Preview

The dashboard includes:

- Current temperature and humidity cards.
- Temperature history line chart.
- Humidity history line chart.
- Average temperature and humidity.
- Maximum and minimum temperature.
- Maximum and minimum humidity.
- Connection status indicator.
- Last sensor reading timestamp.
- Automatic and manual data refresh.

*Add your dashboard screenshots here when documenting the final interface.*

## 📈 Data Analytics

The analytics module processes retrieved sensor readings and calculates:

- Total valid entries.
- Average temperature.
- Maximum temperature.
- Minimum temperature.
- Average humidity.
- Maximum humidity.
- Minimum humidity.

Invalid or out-of-range sensor readings are skipped during processing.

## 🔐 Security

- API credentials are stored in a local `.env` file.
- `.env` is excluded through `.gitignore`.
- `.env.example` provides a configuration template.
- API keys are handled by the backend rather than exposed in frontend JavaScript.

## ⚠️ Project Limitations

- Sensor readings are simulated using Python; no physical Arduino or ESP32 hardware is currently connected.
- Internet connectivity is required for ThingSpeak communication.
- ThingSpeak free-tier update restrictions apply.
- Analytics are calculated from the latest retrieved records rather than the entire lifetime of the channel.

## 🎯 Learning Objectives

This project was developed as a hands-on learning exercise to understand:

- IoT architecture and cloud integration.
- ThingSpeak channels, fields, and API communication.
- HTTP GET and POST requests.
- Python modular programming.
- Data validation and statistical analysis.
- REST API development using FastAPI.
- Frontend and backend communication.
- Interactive data visualization.

## 📜 License

No license has currently been assigned to this practice repository.

---

**Built as a hands-on IoT learning project using Python, ThingSpeak, FastAPI, and JavaScript.**