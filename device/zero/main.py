import paho.mqtt.client as mqtt
import json
import datetime
import subprocess
import threading
import os

# MQTT configurations
broker_address = "192.168.178.29"  # Change to your broker's IP
topic = "test/topic"
recording_topic = "test/recording_done"

# Global variable to track recording status
is_recording = False
current_recording_process = None
recorded_files = []

# Function to start recording
def start_recording(filename):
    global current_recording_process
    current_recording_process = subprocess.Popen(["libcamera-vid", "-o", filename])
    recorded_files.append(filename)
    print(f"Started recording: {filename}")

# Function to stop recording
def stop_recording():
    global current_recording_process
    if current_recording_process:
        current_recording_process.terminate()
        print("Stopped recording")

# Callback function when connected to MQTT Broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

# Callback function when a message is received
def on_message(client, userdata, msg):
    global is_recording
    payload = json.loads(msg.payload)
    visitor = payload.get("visitor", False)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename_video = f"/path/to/save/video_{timestamp}.h264"

    if visitor and not is_recording:
        is_recording = True
        start_recording(filename_video)
    elif not visitor and is_recording:
        is_recording = False
        stop_recording()
        # Publishing the recording completion message
        completion_message = json.dumps({"recorded_files": recorded_files})
        client.publish(recording_topic, completion_message)

# Setup MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, 1883, 60)

# Run the MQTT client
client.loop_forever()
