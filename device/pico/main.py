import wifi
import time
import mqtt
import dht11
import ultrasonic
import json

# Load SSID and password from config file
ssid, password = wifi.load_config('config.txt')

# Connect to Wi-Fi
wifi.connect(ssid, password)

# MQTT topic
topic = 'test/topic'

def main():
    mqtt.connect()

    while True:
        # Get sensor data
        temp, humidity = dht11.read_temp_humidity()
        distance = ultrasonic.read_distance()
        
        sensor_data = {
            "temperature": temp,
            "humidity": humidity,
            "distance": distance
        }
        
        message = json.dumps(sensor_data)
        
        mqtt.publish(topic, message)
        time.sleep(2)

if __name__ == "__main__":
    main()

