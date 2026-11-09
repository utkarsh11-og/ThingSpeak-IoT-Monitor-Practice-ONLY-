# import requests
# import random
# import time
#
# from pathlib import Path
# from dotenv import dotenv_values
#
#
# # ==================================
# # 1. LOAD CONFIGURATION
# # ==================================
#
# ENV_PATH = Path(__file__).resolve().parent / ".env"
# config = dotenv_values(ENV_PATH)
#
# CHANNEL_ID = config.get("THINGSPEAK_CHANNEL_ID")
# WRITE_API_KEY = config.get("THINGSPEAK_WRITE_API_KEY")
#
# if not CHANNEL_ID or not WRITE_API_KEY:
#     raise ValueError("ThingSpeak credentials are missing!")
#
#
# # ==================================
# # 2. THINGSPEAK CONFIGURATION
# # ==================================
#
# URL = "https://api.thingspeak.com/update"
#
#
# # ==================================
# # 3. SENSOR SIMULATION
# # ==================================
#
# def generate_sensor_data():
#
#     temperature = round(random.uniform(20, 35), 2)
#     humidity = round(random.uniform(40, 80), 2)
#
#     return temperature, humidity
#
#
# # ==================================
# # 4. UPLOAD DATA
# # ==================================
#
# def upload_data(temperature, humidity):
#
#     payload = {
#         "api_key": WRITE_API_KEY,
#         "field1": temperature,
#         "field2": humidity
#     }
#
#     try:
#
#         response = requests.post(
#             URL,
#             data=payload,
#             timeout=15
#         )
#
#         if response.status_code == 200:
#
#             entry_id = response.text.strip()
#
#             if entry_id != "0":
#
#                 print("Upload successful!")
#                 print("Entry ID:", entry_id)
#
#             else:
#
#                 print("Upload rejected by ThingSpeak.")
#
#         else:
#
#             print("HTTP Error:", response.status_code)
#
#     except requests.exceptions.RequestException as error:
#
#         print("Connection Error:", error)
#
#
# # ==================================
# # 5. MAIN EXECUTION
# # ==================================
#
# try:
#
#     print("Starting IoT Sensor Simulation...")
#     print("Press CTRL+C to stop.\n")
#
#     while True:
#
#         temperature, humidity = generate_sensor_data()
#
#         print("-----------------------------")
#         print("Temperature:", temperature, "°C")
#         print("Humidity:", humidity, "%")
#
#         upload_data(temperature, humidity)
#
#         print("-----------------------------\n")
#
#         time.sleep(20)
#
#
# except KeyboardInterrupt:

#     print("\nSensor simulation stopped.")









# connecting .env,setting,sensor,thingspeak,analysis all together now

from simulator.sensor import generate_sensor_data
from services.thingspeak import upload_data, get_channel_data
from analytics.analysis import analyze_sensor_data

import time


def main():

    print("=" * 45)
    print("       IoT ENVIRONMENTAL MONITORING")
    print("=" * 45)

    # STEP 1: Generate sensor readings

    print("\n[1] Generating sensor data...")

    sensor_data = generate_sensor_data()

    print("Temperature:", sensor_data["temperature"], "°C")
    print("Humidity:", sensor_data["humidity"], "%")

    # STEP 2: Upload data

    print("\n[2] Uploading data to ThingSpeak...")

    entry_id = upload_data(sensor_data)

    if entry_id is None:
        print("Upload failed. Stopping application.")
        return

    # STEP 3: Retrieve historical data

    print("\n[3] Retrieving historical data...")

    time.sleep(2)

    feeds = get_channel_data(results=100)

    if not feeds:
        print("No sensor data retrieved.")
        return

    print("Retrieved entries:", len(feeds))

    # STEP 4: Analyze sensor data

    print("\n[4] Analyzing sensor data...")

    analysis = analyze_sensor_data(feeds)

    if analysis is None:
        print("Analysis could not be completed.")
        return

    # STEP 5: Display report

    print("\n" + "=" * 45)
    print("             SENSOR ANALYTICS")
    print("=" * 45)

    print("\nTotal Valid Entries:",
          analysis["total_entries"])

    print("\nTEMPERATURE")

    print("Average:",
          analysis["average_temperature"], "°C")

    print("Maximum:",
          analysis["maximum_temperature"], "°C")

    print("Minimum:",
          analysis["minimum_temperature"], "°C")

    print("\nHUMIDITY")

    print("Average:",
          analysis["average_humidity"], "%")

    print("Maximum:",
          analysis["maximum_humidity"], "%")

    print("Minimum:",
          analysis["minimum_humidity"], "%")

    print("\n" + "=" * 45)
    print("         APPLICATION COMPLETED")
    print("=" * 45)


if __name__ == "__main__":
    main()


