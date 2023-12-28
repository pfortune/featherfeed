import wifi
import time
import mqtt
import dht11
import ultrasonic
import json
from machine import Pin

# Initialize LED pin
led = Pin(16, Pin.OUT)

# Load WiFi credentials
ssid, password = wifi.load_config('config.txt')

# Connect to Wi-Fi
wifi.connect(ssid, password)

# MQTT topic
topic = 'featherfeed/sensor/reading'

def main():
    # Connect to MQTT
    mqtt.connect()

    while True:
        # Read sensor data
        distance = ultrasonic.read_distance()
        temp, humidity = dht11.read_temp_humidity()
        visitor = False
        led.value(0)  # Turn off LED initially

        # Check for visitor
        if distance < 10:  # Visitor detected if distance is less than 10 cm
            visitor = True
            led.value(1)  # Turn on LED

        # Prepare sensor data in JSON format
        sensor_data = {
            "temperature": temp,
            "humidity": humidity,
            "distance": distance,
            "visitor": visitor
        }
        message = json.dumps(sensor_data)
        
        # Publish sensor data
        mqtt.publish(topic, message)
        time.sleep(2)  # Adjust sleep time as needed

if __name__ == "__main__":
    main()