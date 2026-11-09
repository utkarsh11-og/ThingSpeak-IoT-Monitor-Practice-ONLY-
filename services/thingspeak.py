import requests

from config.settings import (
    CHANNEL_ID,
    WRITE_API_KEY,
    READ_API_KEY,
    BASE_URL
)


def upload_data(sensor_data):

    url = f"{BASE_URL}/update"

    payload = {
        "api_key": WRITE_API_KEY,
        "field1": sensor_data["temperature"],
        "field2": sensor_data["humidity"]
    }

    try:

        response = requests.post(
            url,
            data=payload,
            timeout=15
        )

        response.raise_for_status()

        entry_id = response.text.strip()

        if entry_id == "0":
            print("ThingSpeak rejected the update.")
            return None

        print("Data uploaded successfully!")
        print("Entry ID:", entry_id)

        return entry_id

    except requests.exceptions.RequestException as error:

        print("Upload error:", error)
        return None



def get_channel_data(results=100):

    url = f"{BASE_URL}/channels/{CHANNEL_ID}/feeds.json"

    params = {
        "api_key": READ_API_KEY,
        "results": results
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        feeds = data.get("feeds", [])

        return feeds

    except requests.exceptions.RequestException as error:

        print("Data retrieval error:", error)
        return []