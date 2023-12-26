import network
import time

wlan = network.WLAN(network.STA_IF)

def load_config(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    config = {}
    for line in lines:
        key, value = line.strip().split('=')
        config[key] = value
    return config['SSID'], config['PASSWORD']

def connect(ssid, password):
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # wait for connect or fail
    max_attempts = 10
    attempts = 0
    while attempts < max_attempts and not wlan.isconnected():
        attempts += 1
        print(f"Attempt {attempts}")
        time.sleep(1)
        
    if wlan.isconnected():
        print(f"Connected to {ssid}!")
        print("Network config:", wlan.ifconfig())
    else:
        print(f"Failed to connect to {ssid}. Check your details and try again.")

def disconnect():
    if wlan.isconnected():
        wlan.disconnect()
        wlan.active(False)
        print("Disconnected from Wi-Fi")
    else:
        print("Wi-Fi was not connected")

def is_connected(wlan):
    wlan = network.WLAN(network.STA_IF)
    return wlan.isconnected()