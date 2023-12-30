
# Setting up Raspberry Pi 4 and Coral TPU

## Initial Setup with AI Maker Image
- Follow the steps from the AIY Projects website to set up Raspberry Pi with Coral TPU ([AIY Projects Setup Guide](https://aiyprojects.withgoogle.com/)).

## Updating Package Manager
- Retrieve the signing key for the Google Coral repository using the command:
  ```
  curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add –
  ```

# Automated Setup

Run `bash ./setup.sh` to execute all the steps. Make sure to update the config.ini with your details. See below.

# Manual Setup Instructions (Optional)

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

# SSH Key-Based Authentication
This step is significant as it allows the Raspberry Pi to transfer files from the Raspberry Pi Zero 2W without the need for entering passwords.

- **Generate an SSH Key Pair**: 
  Run the following command to create a new SSH key pair. I chose not to set a passphrase for this key pair to facilitate smoother access.

  ```
  ssh-keygen -t rsa -b 4096 -C "pfortune@gmail.com"
  ```

- **Transferring the Key to Raspberry Pi Zero**: 
  Deploy the generated key to the Raspberry Pi Zero using this command. This step is crucial to establish a secure and password-less connection between the Raspberry Pi 4 and the Pi Zero 2W.

  ```
  ssh-copy-id pfortune@192.168.178.37
  ```
  
# Creating and Managing Services

To enable the bird classification and upload functionalities to run as services, follow these steps:

1. **Creating Service Files**:
   - Create two service files: `bird_classifier.service` and `uploader.service`.
   - Use the provided configurations for each service file.

2. **Placing Service Files**:
   - Place the service files in the `/etc/systemd/system/` directory.

3. **Starting and Enabling Services**:
   - To start the services, use the command:
     ```
     sudo systemctl start bird_classifier.service
     sudo systemctl start uploader.service
     ```
   - To enable the services to start on boot, use:
     ```
     sudo systemctl enable bird_classifier.service
     sudo systemctl enable uploader.service
     ```

## Installing Additional Python Packages

You need to install `supabase` and `configparser` for the project to function properly. Use the following commands to install them:

```
pip3 install supabase
pip3 install configparser
```

## Updating Configuration File

The `config.sample.ini` file contains placeholders for various configurations. Update this file with your specific details:

- **Supabase Configuration**: Add your Supabase project URL and API key.
- **MQTT Configuration**: Set the MQTT broker address and port.
- **SCP Configuration**: Provide the username and IP address for SCP file transfers.

After updating, rename the file to `config.ini`:

```
mv config.sample.ini config.ini
```
