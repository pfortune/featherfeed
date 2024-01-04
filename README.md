# FeatherFeed

An AI-enhanced bird feeder system using Raspberry Pi 4, Raspberry Pi Zero 2W, Google Coral TPU, and Raspberry Pico W for bird detection and recording.

## Introduction

FeatherFeed is a smart bird feeder monitoring system that merges the beauty of nature with cutting-edge technology. The sytem uses Raspberry Pi 4, Raspberry Pi Zero 2W, Raspberry Pico W, and Google Coral TPU to detect, record, and identify birds that visit the feeder. The system alerts users about bird visitations a user-friendly web application.

## System Architecture

- **Raspberry Pico W**: Equipped with an Ultrasonic Sensor, Temperature/Humidity Sensor, and LED light, it detects bird presence and publishes data on temperature, humidity, and visitor status.
- **Raspberry Pi Zero 2W**: Dedicated to video recording using the Arducam IMX519 16MP camera. It starts recording when a visitor is detected and stops when the visitor leaves.
- **Raspberry Pi 4**: Serves as the main processing unit. It uses the Google Coral TPU and TensorFlow compatibility, runs Mosquitto broker, and processes video files for bird identification and uploading.

## Key Features

- **Real-Time Bird Presence Detection**: Raspberry Pico W detects and publishes bird visitation data.
- **Automated Video Recording**: Raspberry Pi Zero 2W records video upon detecting visitors.
- **AI-Powered Bird Identification**: TensorFlow Lite and Google Coral TPU are used for accurate species identification.
- **Instant Notifications**: Updates users on bird visitations through an interactive web app.

## Technology Stack

- **Raspberry Pi Pico W**: Monitoring bird presence with sensors.
- **Raspberry Pi Zero 2W**: Video recording, running Raspbian 64bit Bullseye Lite.
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

- [Raspberry Pico W Setup](device/pico/README.md): Instructions in `device/pico` directory.
- [Raspberry Pi Zero 2W Setup](device/zero/README.md): Instructions in `device/zero` directory.
- [Raspberry Pi 4 Setup](device/pi/README.md): Instructions in `device/pi` directory.

---

Visit our website: [featherfeed.ie](http://featherfeed.ie)
