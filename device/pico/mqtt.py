from umqtt.robust import MQTTClient

# MQTT Configurations
mqtt_server = '192.168.178.29'
client_id = 'HDipRPi'
client = None

# Function to connect to MQTT
def connect():
    global client
    try:
        client = MQTTClient(client_id, mqtt_server)
        client.connect()
        print("Connected to MQTT")
    except Exception as e:
        print("Error connecting to MQTT:", e)

# Function to publish a message
def publish(topic, message):
    global client
    try:
        if client:
            client.publish(topic, message)
            print("Message published")
        else:
            print("MQTT client not connected.")
    except Exception as e:
        print("Error publishing message:", e)
