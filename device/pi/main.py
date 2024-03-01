import paho.mqtt.client as mqtt
from bird_classifier import run_bird_detection
import os
import json
import time
import datetime
import subprocess
import configparser

#TODO: Refactor to use classes
#TODO: Add error handling
#TODO: Add type hints
#TODO: Add logging
#TODO: More direct handling of events

# Load configuration
print("Loading configuration...")
config = configparser.ConfigParser()
config.read('config.ini')

# File Transfer credentials
scp_user = config['SCP']['scp_user']
scp_host = config['SCP']['scp_host']

# MQTT configurations
recording_topic = "featherfeed/camera/recording_done"

# Function to transfer video file from Pi Zero to Pi4
def transfer_file(remote_path, local_path):
    # SCP command for file transfer
    scp_command = f"scp {scp_user}@{scp_host}:{remote_path} {local_path}"
    # Execute SCP command and return the result status
    return subprocess.run(scp_command, shell=True).returncode == 0

# Function to delete a local file, typically after processing
def delete_local_file(file_path):
    # Check if file exists before attempting to delete
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted file: {file_path}")

# Function to handle the video file processing and subsequent actions
def analyse_video_file(client, video_file_local, temperature, humidity):
    # Run bird detection on the video file
    detections, saved_frame_path = run_bird_detection(video_file_local)
    
    # If detections are found, publish the detection data
    if detections:
        # Determine the most likely bird species from detections
        bird_species = max(detections, key=lambda x: x[1])[0]
        # Prepare data for publishing
        detection_data = {
            "temperature": temperature,
            "humidity": humidity,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "bird_species": bird_species,
            "file_name": video_file_local,
            "saved_frame": saved_frame_path
        }
        client.publish("featherfeed/classifier/bird_detected", json.dumps(detection_data))
    else:
        # If no birds are detected, publish a no-detection message and delete the video file
        client.publish("featherfeed/classifier/no_bird_detected", "No bird detected")
        delete_local_file(video_file_local)

# Callback function for MQTT when connected
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to the recording topic on successful connect
    client.subscribe(recording_topic)

# Callback function for handling MQTT messages
def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}")
    
    # Process messages from the recording topic
    if msg.topic == recording_topic:
        data = json.loads(msg.payload.decode("utf-8"))
        # Extract file paths and sensor data from message
        video_file_remote = data['recorded_file']
        video_file_local = f"/home/pfortune/Code/video/{video_file_remote.split('/')[-1]}"
        temperature = data.get("temperature")
        humidity = data.get("humidity")

        # Transfer file and process if successful
        if transfer_file(video_file_remote, video_file_local):
            client.publish("featherfeed/video/copied", video_file_remote)
            time.sleep(1)
            analyse_video_file(client, video_file_local, temperature, humidity)

# MQTT setup
print("Setting up MQTT client...")
client = mqtt.Client()
mqtt_server = config['MQTT']['server']
mqtt_port = int(config['MQTT']['port'])
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_server, mqtt_port, 60)

# Start the loop
print("Starting MQTT loop...")
client.loop_forever()