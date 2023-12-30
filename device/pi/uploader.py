import os
import json
import mimetypes
import paho.mqtt.client as mqtt
from supabase import create_client, Client
import configparser

# Load configuration
print("Loading configuration...")
config = configparser.ConfigParser()
config.read('config.ini')

# Supabase setup
print("Setting up Supabase client...")
url = config['Supabase']['url']
key = config['Supabase']['key']
supabase: Client = create_client(url, key)

# Function to upload file to Supabase
def upload_file(supabase: Client, file_path: str, bucket: str) -> str:
    print(f"Uploading file: {file_path} to bucket: {bucket}")
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'  # Default MIME type if unknown

    with open(file_path, 'rb') as file:
        file_name = file_path.split('/')[-1]
        stored_path = f"{bucket}/{file_name}"
        response = supabase.storage().from_(bucket).upload(
            path=stored_path,
            file=file,
            file_options={"content-type": mime_type}
        )
        print(f"Upload response: {response}")
        return stored_path

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT with result code "+str(rc))
    client.subscribe("featherfeed/classifier/bird_detected")

def on_message(client, userdata, msg):
    print(f"Received message on topic: {msg.topic}")
    data = json.loads(msg.payload)
    print(f"Message data: {data}")

    # Upload files to Supabase
    try:
        image_path = upload_file(supabase, data['saved_frame'], 'images')
        video_path = upload_file(supabase, data['file_name'], 'videos')
        print(f"Image uploaded to path: {image_path}")
        print(f"Video uploaded to path: {video_path}")

        # Insert data into Supabase database
        insert_data = {
            "temperature": data['temperature'],
            "humidity": data['humidity'],
            "date": data['date'],
            "species": data['bird_species'],
            "videoref": video_path,
            "imageref": image_path
        }
        db_response = supabase.table("detections").insert(insert_data).execute()
        print(f"Database insert response: {db_response}")
    except Exception as e:
        print(f"Error: {e}")

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