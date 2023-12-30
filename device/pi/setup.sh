
#!/bin/bash

# Exit if any command fails
set -e

# Welcome message
echo "Starting full setup for the Raspberry Pi project..."

# Update and upgrade system packages
echo "Updating and upgrading system packages..."
sudo apt-get update
sudo apt-get dist-upgrade -y

# Install MQTT Broker
echo "Installing MQTT Broker..."
sudo apt-get install -y mosquitto mosquitto-clients

# Enable Mosquitto Broker to start on boot
echo "Enabling Mosquitto Broker..."
sudo systemctl enable mosquitto.service

# Automatically determine the project directory
project_directory=$(pwd)

# Install Python packages
echo "Installing Python packages..."
pip3 install supabase configparser

# Copy service files to the systemd directory
echo "Setting up services..."
sudo cp "$project_directory/bird_classifier.service" /etc/systemd/system/
sudo cp "$project_directory/uploader.service" /etc/systemd/system/

# Enable and start services
echo "Enabling and starting services..."
sudo systemctl enable bird_classifier.service
sudo systemctl start bird_classifier.service
sudo systemctl enable uploader.service
sudo systemctl start uploader.service

# Rename the config file
echo "Renaming config file..."
mv "$project_directory/config.sample.ini" "$project_directory/config.ini"

echo "Full setup completed successfully. Please edit the config.ini file with your specific configurations."
