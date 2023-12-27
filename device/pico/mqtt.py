from umqtt.robust import MQTTClient

# MQTT Configurations
mqtt_server = '192.168.178.29'
client_id = 'HDipRPi'

# Function to connect to MQTT
def connect():
    try:
        client = MQTTClient(client_id, mqtt_server)
        client.connect()
        print("Connected to MQTT")
        return client
    except Exception as e:
        print("Error connecting to MQTT:", e)
        return None

# Function to publish a message
def publish(client, topic, message):
    try:
        if client:
            client.publish(topic, message)
            print("Message published")
    except Exception as e:
        print("Error publishing message:", e)
