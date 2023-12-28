import paho.mqtt.client as mqtt
import json
import time
import subprocess

# MQTT configurations
broker_address = "localhost"  
recording_topic = "featherfeed/camera/recording_done"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(recording_topic)

def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}")

    if msg.topic == recording_topic:
        # Parse message
        data = json.loads(msg.payload.decode("utf-8"))
        video_file_remote = data['recorded_file']  # Path on Pi Zero
        video_file_local = f"/home/pfortune/Code/video/{video_file_remote.split('/')[-1]}"

        # SCP command to transfer file from Zero to Pi4
        scp_command = f"scp pfortune@192.168.178.37:{video_file_remote} {video_file_local}"
        scp_result = subprocess.run(scp_command, shell=True)

        if scp_result.returncode == 0:
            # Publish a message indicating successful file transfer
            client.publish("featherfeed/files/copied", video_file_remote)
            time.sleep(1)
        else:
            print("Error in file transfer")


# Setup MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, 1883, 60)

# Run the MQTT client
client.loop_forever()