# FeatherFeed

An AI-enhanced bird feeder system using Raspberry Pi 4, Raspberry Pi Zero 2W and Google Coral TPU for bird detection and recording.

## Introduction

FeatherFeed is a smart bird feeder monitoring system that merges the beauty of nature with cutting-edge technology. The system uses Raspberry Pi 4, Raspberry Pi Zero 2W, and Google Coral TPU to detect, record, and identify birds that visit the feeder. The system alerts users about bird visitations through a user-friendly web application.

## System Configurations

Throughout the development of Feather Feed, we experimented with two different hardware configurations to optimise bird detection accuracy and system efficiency. Below are the descriptions and images of these configurations:

### Configuration 1: Separate Sensor and Camera Setup

In this setup, the ultrasonic sensor and the camera were placed on either side of the bird feeder box. This configuration allowed for a wide detection range but presented challenges in aligning the sensor's detection with the camera's field of view.

![FeatherFeed Configuration 1](feeder-config1.jpg)

### Configuration 2: Unified Sensor and Camera Setup

After testing and evaluation, we found that placing both the ultrasonic sensor and the camera at the back of the box, pointing outwards, significantly improved the system's performance. This setup ensured that whenever a bird triggered the ultrasonic sensor, it was already in the camera's field of view, making for more efficient and accurate bird detection. This configuration will be the basis for Version 2 of the Feather Feed system.

![FeatherFeed Configuration 2](feeder-config2.jpg)


## Quick Start

To get your FeatherFeed system up and running:

1. **Assemble the Hardware**: Follow the setup instructions for each device.
2. **Install the Software**: Use the provided scripts to install necessary packages and dependencies.
3. **Configure the System**: Set up the Mosquitto broker, Coral TPU, and sensors as per the documentation.
4. **Launch the Web App**: Access the web application to start monitoring bird activity in real-time.

For a detailed guide, refer to the installation instructions for each device below.

## System Architecture

- **Raspberry Pi Zero 2W**: Equipped with an Ultrasonic Sensor, Temperature/Humidity Sensor, and LED light, it detects bird presence and starts video recording using the Raspberry Pi Camera v2.
- **Raspberry Pi 4**: Serves as the main processing unit. It uses the Google Coral TPU and TensorFlow compatibility, runs Mosquitto broker, and processes video files for bird identification and uploading.

## Key Features

- **Real-Time Bird Presence Detection**: Raspberry Pi Zero 2W detects and publishes bird visitation data.
- **Automated Video Recording**: Raspberry Pi Zero 2W records video upon detecting visitors.
- **AI-Powered Bird Identification**: TensorFlow Lite and Google Coral TPU are used for accurate species identification.
- **Instant Notifications**: Updates users on bird visitations through an interactive web app.

## Technology Stack

- **Raspberry Pi Zero 2W**: Monitoring bird presence with sensors. Video recording, running Raspbian 64bit Bullseye Lite.
- **Raspberry Pi 4B 4GB**: AI processing, MQTT broker, and communication hub.
- **Google Coral TPU**: Enhances TensorFlow’s capabilities for species identification.
- **Operating System**: Raspbian.
- **Machine Learning**: TensorFlow Lite.
- **Communication**: MQTT (Mosquitto) broker.
- **Programming Language**: Python, JavaScript.
- **API**: Built with Hapi framework.
- **Data Storage**: PostgreSQL using Supabase.
- **Frontend**: SvelteKit, Tailwind CSS, hosted on Vercel.

## Installation Instructions

- [Raspberry Pi Zero 2W Setup](device/zero/README.md): Instructions in `device/zero` directory.
- [Raspberry Pi 4 Setup](device/pi/README.md): Instructions in `device/pi` directory.

---

Visit our website: [featherfeed.ie](http://featherfeed.ie)
