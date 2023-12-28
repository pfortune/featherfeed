import paho.mqtt.client as mqtt
import os
import json
import datetime
import subprocess

# MQTT configurations
broker_address = "192.168.178.29"  # Change to your broker's IP
sensor_topic = "featherfeed/sensor/reading"
file_topic = "featherfeed/files/copied"
recording_topic = "featherfeed/camera/recording_done"

# Global variable to track recording status
is_recording = False
filename_video = ""
current_recording_process = None
meta_data = {}

# Function to start recording
def start_recording(filename):
    global current_recording_process
    current_recording_process = subprocess.Popen(["libcamera-vid", "-o", filen>
    print(f"Started recording: {filename}")

# Function to stop recording
def stop_recording():
    global current_recording_process
    if current_recording_process:
        current_recording_process.terminate()
        current_recording_process.wait()
        print("Stopped recording")

# Callback function when connected to MQTT Broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(sensor_topic)
    client.subscribe(file_topic)

# Callback function when a message is received
def on_message(client, userdata, msg):

    if msg.topic == sensor_topic:
        global is_recording, filename_video
        payload = json.loads(msg.payload)
        visitor = payload.get("visitor", False)

        if visitor and not is_recording:
            is_recording = True
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename_video = f"/home/pfortune/video/video_{timestamp}.h264"
            start_recording(filename_video)
        elif not visitor and is_recording:
            is_recording = False
            stop_recording()
            
            # Publishing the recording completion message
            completion_message = json.dumps({
                    "recorded_file": filename_video,
                    "temperature": payload.get("temperature"),
                    "humidity": payload.get("humidity")
            })
            client.publish(recording_topic, completion_message)

    if msg.topic == file_topic:
        filepath = msg.payload.decode()
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"Deleted file: {filepath}")
            client.publish("featherfeed/files/deleted", filepath)
        else:
            print(f"File not found: {filepath}")

# Setup MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, 1883, 60)

# Run the MQTT client
client.loop_forever()