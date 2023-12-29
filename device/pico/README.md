# Setting Up Raspberry Pi Pico

## Prerequisites

- Raspberry Pi Pico
- Thonny IDE installed on your computer

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