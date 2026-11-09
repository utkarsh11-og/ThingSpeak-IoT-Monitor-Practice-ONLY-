import random


def generate_sensor_data():

    temperature = round(random.uniform(20, 35), 2)
    humidity = round(random.uniform(40, 80), 2)

    return {
        "temperature": temperature,
        "humidity": humidity
    }