def analyze_sensor_data(feeds):

    temperatures = []
    humidities = []

    # Process each sensor entry
    for entry in feeds:

        try:
            temperature = float(entry.get("field1"))
            humidity = float(entry.get("field2"))

            # Validate temperature
            if not (20 <= temperature <= 35):
                continue

            # Validate humidity
            if not (0 <= humidity <= 100):
                continue

            temperatures.append(temperature)
            humidities.append(humidity)

        except (TypeError, ValueError):
            print("Skipping invalid entry:", entry.get("entry_id"))
            continue

    # Check whether valid data exists
    if not temperatures or not humidities:
        print("No valid sensor data available.")
        return None

    # Calculate statistics
    analysis = {

        "total_entries": len(temperatures),

        "average_temperature": round(
            sum(temperatures) / len(temperatures), 2
        ),

        "maximum_temperature": max(temperatures),

        "minimum_temperature": min(temperatures),

        "average_humidity": round(
            sum(humidities) / len(humidities), 2
        ),

        "maximum_humidity": max(humidities),

        "minimum_humidity": min(humidities)
    }

    return analysis

