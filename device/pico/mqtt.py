from umqtt.robust import MQTTClient
import machine
import time

#MQTT Server details
mqtt_server = '192.168.178.29'
client_id = 'HDipRPi'

client = MQTTClient(client_id, mqtt_server)
client.connect()

while True:
    client.publish('test/topic', 'Your sensor data here')
    time.sleep(2)