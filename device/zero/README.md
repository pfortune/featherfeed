# Raspberry Pi Zero 2W Setup Guide

## Introduction
Provide a brief introduction that outlines the purpose of the setup and the role of the Arducam IMX519 camera within the project.

## Preparation and Initial Configuration
1. Using the Raspberry Pi Imager:
   - Choose the Pi Zero 2 W device
   - For the OS, go to Raspberry Pi OS (other) and select Raspberry Pi OS (Legacy, 64-bit) lite with no desktop environment
   - Choose the microSD card for storage
   - Configure with your chosen username and password, and wifi
   - Enable SSH

## Enabling Graphics Acceleration
- Access the 'raspi-config' tool:
  - Open a terminal window
  - Execute `sudo raspi-config`
  - Navigate to 'Advanced Options'
  - Select and enable 'Glamor graphic acceleration'
  - Reboot the Raspberry Pi to apply changes


## Camera Software Installation
- Update the system packages:
  - Open a terminal window
  - Execute 
    ```
    sudo apt update
    sudo apt upgrade
    ```
- Enable the camera via `sudo raspi-config`
- Install Picamera
  - Execute `sudo apt install python3-picamera`
- Install ffmpeg
  - Execute `sudo apt-get update` and `sudo apt-get install ffmpeg`

## Testing and Verification
- Test the camera functionality:
  - Execute `raspistill -o test.jpg`

## Transferring the Test Image
- Transfer the image file to a personal computer:
  - Execute `scp <user>@192.168.178.37:/home/<user>/test.jpg /Users/<user>/`
- Or review the image using VSCode and Remote SSH

**Note:** The setup of the Raspberry Pi Zero 2W was successful, with functional network connectivity and camera operations. The device is now ready for the next stages of the project.

## Setup MQTT & LibCamera

### Install Pip
- Execute:
    ```
    sudo apt update
    sudo apt install python3-pip
    pip3 install paho-mqtt
    ```

### Setup the MQTT camera service
- Create a new service file:
  - Execute `sudo nano /etc/systemd/system/mqtt_camera.service`
  - Enter the following content:
    ```
    [Unit]
    Description=MQTT Camera Service
    After=network-online.target

    [Service]
    ExecStartPre=/bin/sleep 10
    ExecStart=/usr/bin/python3 /home/pfortune/main.py
    WorkingDirectory=/home/pfortune
    StandardOutput=inherit
    StandardError=inherit
    Restart=always
    User=pfortune

    [Install]
    WantedBy=multi-user.target
    ```
- Then execute:
    ```
    sudo systemctl daemon-reload
    sudo systemctl enable mqtt_camera.service
    sudo systemctl start mqtt_camera.service
    ```
- To check if it's running:
  - Execute `sudo systemctl status mqtt_camera.service`
