import dht
import machine

def read_temp_humidity():
    sensor_type = dht.DHT11
    pin_number = 18
    sensor = sensor_type(machine.Pin(pin_number))

    sensor.measure()
    temp = sensor.temperature()
    humidity = sensor.humidity()
    return temp, humidity

