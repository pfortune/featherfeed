import wifi
import time

# Load SSID and password from config file
ssid, password = wifi.load_config('config.txt')

# Connect to Wi-Fi
wifi.connect(ssid, password)

while True:
    if wifi.is_connected(wifi.wlan):
        print("Still connected!")
    else:
        print("Lost connection, attempting to reconnect...")
        wifi.connect_to_wifi(ssid, password)
    
    time.sleep(60)
