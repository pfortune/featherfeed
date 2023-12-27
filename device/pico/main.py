import wifi
import time
import mqtt

# Load SSID and password from config file
ssid, password = wifi.load_config('config.txt')

# Connect to Wi-Fi
wifi.connect(ssid, password)
topic = 'test/topic'

def main():
    client = mqtt.connect()

    if client:
        while True:
            # Replace with your sensor reading logic
            sensor_data = 'Your New sensor data here'
            mqtt.publish(client, topic, sensor_data)
            time.sleep(2)

if __name__ == "__main__":
    main()
