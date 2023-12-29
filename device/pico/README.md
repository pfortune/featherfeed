# Setting Up Raspberry Pi Pico

## Prerequisites

- Raspberry Pi Pico
- Thonny IDE installed on your computer
- Grove Shield for Raspberry Pi Pico
- Grove Ultrasonic Sensor, Grove DHT11 Sensor, and Grove LED

## Step 1: Setting Up Thonny for MicroPython

1. Open Thonny IDE.
2. Go to `Tools > Options > Interpreter`.
3. Select `MicroPython (Raspberry Pi Pico)` from the dropdown.
4. Connect your Pico to your computer via USB.
5. Click on the `Install or update firmware` button if needed.

## Step 2: Copying Files to the Pico

1. In Thonny, copy the files to your Pico.
2. Save them directly to the Pico by selecting the Pico from the save dialogue's location options.

## Step 3: Installing MQTT Libraries

The `umqtt.simple` and `umqtt.robust` libraries are required for MQTT communication.

1. In Thonny, go to `Tools > Manage packages`.
2. In the search bar, type `micropython-umqtt.simple` and click `Search`.
3. Select the package from the search results and click `Install`.
4. Repeat steps 2 and 3 for `micropython-umqtt.robust`.

## Step 4: Hardware Setup

Before connecting the Pico to power, attach the following components:

1. Attach the Grove Shield to the Raspberry Pi Pico.
2. Connect the Grove Ultrasonic Sensor to port D20 on the Grove Shield.
3. Connect the Grove DHT11 Sensor to port D18.
4. Connect the Grove LED to port D16.

Once all components are securely attached, you can power on the Pico.

## Step 5: Configuring the Pico

Update the `config.txt` file on your Pico with the following details:

```plaintext
SSID=your_wifi_ssid
PASSWORD=your_wifi_password
MQTTSERVER=your_mqtt_server_address
CLIENTID=your_mqtt_client_id
```

Replace your_wifi_ssid, your_wifi_password, your_mqtt_server_address, and your_mqtt_client_id with your actual network and MQTT server details.


