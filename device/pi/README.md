
# Setting up Raspberry Pi 4 and Coral TPU

## Initial Setup with AI Maker Image
- Follow the steps from the AIY Projects website to set up Raspberry Pi with Coral TPU ([AIY Projects Setup Guide](https://aiyprojects.withgoogle.com/)).

## Updating Package Manager
- Retrieve the signing key for the Google Coral repository using the command:
  ```
  curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add –
  ```

## Upgrading System Packages
- Update and upgrade all packages (over 300) using:
  ```
  sudo apt-get update
  ```
- Encountered an issue with VLC packages during the upgrade. Resolved by using a more aggressive and intelligent command:
  ```
  sudo apt-get dist-upgrade
  ```

With the Raspberry Pi 4 successfully set up with the Coral TPU using Google's AI Maker image, previous software conflicts are resolved, and the system is prepared for reinstalling and configuring the software used later in the project.

# Setting up MQTT Broker

## Step 1: Install MQTT Broker on Pi4
- Update your Pi4: Run `sudo apt-get update` and then `sudo apt-get upgrade` to make sure everything’s up to date.
- Install Mosquitto: Type `sudo apt-get install -y mosquitto mosquitto-clients` and hit enter.
- Enable Mosquitto Broker: After installation, enable Mosquitto to start on boot by typing `sudo systemctl enable mosquitto.service`.

## Step 2: Verify MQTT Broker Status
- Check Mosquitto Status: In the terminal, type `sudo systemctl status mosquitto` and press Enter. You should see an output indicating that Mosquitto is active and running.
