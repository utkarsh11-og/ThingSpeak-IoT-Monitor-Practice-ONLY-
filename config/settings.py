from pathlib import Path
from dotenv import dotenv_values

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
ENV_PATH = BASE_DIR / ".env"
config = dotenv_values(ENV_PATH)

if not ENV_PATH.exists():
    raise FileNotFoundError(
        f".env file not found at: {ENV_PATH}"
    )



# ThingSpeak credentials
CHANNEL_ID = config.get("THINGSPEAK_CHANNEL_ID")
WRITE_API_KEY = config.get("THINGSPEAK_WRITE_API_KEY")
READ_API_KEY = config.get("THINGSPEAK_READ_API_KEY")

# ThingSpeak API endpoint
BASE_URL = "https://api.thingspeak.com"

# Validate configuration
if not CHANNEL_ID:
    raise ValueError("Channel ID missing!")

if not WRITE_API_KEY:
    raise ValueError("Write API Key missing!")

if not READ_API_KEY:
    raise ValueError("Read API Key missing!")

