import wifi
import mqtt
import network
import time

# Load SSID and password from config file
ssid, password = wifi.load_config('config.txt')

# Connect to Wi-Fi
wifi.connect(ssid, password)

while True:
    wlan = network.WLAN(network.STA_IF)
    if wifi.is_connected(wlan):
        print("Still connected!")
    else:
        print("Lost connection, attempting to reconnect...")
        wifi.connect_to_wifi(ssid, password)
    
    time.sleep(60)