import requests
from pathlib import Path
from dotenv import dotenv_values

ENV_PATH=Path(__file__).resolve().parent / ".env"
config=dotenv_values(ENV_PATH)

CHANNEL_ID = config.get("THINGSPEAK_CHANNEL_ID")
READ_API_KEY = config.get("THINGSPEAK_READ_API_KEY")


print("Channel ID loaded:", bool(CHANNEL_ID))
print("Read API Key loaded:", bool(READ_API_KEY))

if not CHANNEL_ID or not READ_API_KEY:
    raise ValueError("ThingSpeak Credentials are missing")

url=f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json"

params={
    "api_key":READ_API_KEY,
    "results":100
}

try:
    response=requests.get(
        url,
        params=params,
        timeout=15

    )
    response.raise_for_status()

    data=response.json()

    feeds=data.get("feeds",[])

    if feeds:

        temperatures = []
        humidities = []

        print("\nRetrieved Sensor Data")
        print("=" * 45)

        print("Total Entries:", len(feeds))

        for entry in feeds:

            try:
                temperature = float(entry.get("field1"))
                humidity = float(entry.get("field2"))

                if not (20 <= temperature <= 35):
                    print("Invalid temperature:", temperature)
                    continue

                if not (0 <= humidity <= 100):
                    print("Invalid humidity:", humidity)
                    continue

                temperatures.append(temperature)
                humidities.append(humidity)

            except (TypeError, ValueError):
                print("Invalid sensor data. Skipping entry:", entry.get("entry_id"))
                continue
        if temperatures and humidities:
            print("\n========== SENSOR ANALYTICS ==========")

            print("\nTEMPERATURE ANALYSIS")

            print("Average:", round(sum(temperatures) / len(temperatures), 2), "°C")
            print("Maximum:", max(temperatures), "°C")
            print("Minimum:", min(temperatures), "°C")

            print("\nHUMIDITY ANALYSIS")

            print("Average:", round(sum(humidities) / len(humidities), 2), "%")
            print("Maximum:", max(humidities), "%")
            print("Minimum:", min(humidities), "%")

    else:
        print("No sensor readings found.")


except requests.exceptions.RequestException as error:
    print("API Request Error:", error)

except ValueError as error:
    print("Response Parasing Error:",error)