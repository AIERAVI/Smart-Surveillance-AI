# Smart-Surveillance-AI
Turns any smartphone into an IP camera with real-time YOLOv8 object detection and WhatsApp motion alerts.


# Smart IP Surveillance System with YOLOv8 & Real-Time Alerts

An advanced, AI-powered smart surveillance system that transforms a standard smartphone into an IP camera. It implements deep learning for real-time object detection and computer vision for motion analysis. Upon detecting suspicious activities, the system automatically captures an image and sends a WhatsApp alert to the user's provided phone number.

## Table of Contents
- [Features](#features)
- [System Architecture](#system-architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Step-by-Step Usage Guide](#step-by-step-usage-guide)
- [Directory Structure](#directory-structure)
- [Technologies Used](#technologies-used)

## Features
* **IP Camera Integration:** Utilizes your mobile phone camera over the local network via IP streaming, eliminating the need for expensive CCTV hardware.
* **YOLOv8 Object Detection:** Identifies people and objects in real-time with high accuracy.
* **Motion & Misbehavior Detection:** Uses background subtraction and thresholding to detect sudden, suspicious movements.
* **Automated WhatsApp Alerts:** Captures a frame upon detecting motion and sends it directly to a user-defined WhatsApp number using a background thread (zero camera lag).
* **Dynamic User Input:** Prompts the user to enter their target WhatsApp number securely at runtime via a Tkinter GUI.
* **Smart Cooldown System:** Prevents spamming by implementing a 60-second cooldown timer between consecutive alerts.

## System Architecture
1. **Video Capture:** IP Webcam application streams video from the phone to the local network.
2. **Processing:** OpenCV reads the stream and YOLOv8 processes each frame for object classification.
3. **Motion Analysis:** OpenCV calculates the absolute difference between frames to trigger the motion threshold.
4. **Alert Mechanism:** If the threshold is breached, the frame is saved locally, and a background Python thread triggers PyWhatKit to send the evidence via WhatsApp Web.

## Prerequisites
Before running the project, ensure you have the following ready:
* Python 3.8 or higher installed on your system.
* A default web browser logged into **WhatsApp Web**.
* A smartphone with the **IP Webcam** app (available on Android/iOS) installed.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/AIERAVI/Smart-Surveillance-AI.git](https://github.com/yourusername/Smart-Surveillance-AI.git)
   cd Smart-Surveillance-AI



   ## 📱 IP Webcam App Setup & Settings

To ensure smooth video streaming and prevent your laptop from lagging while running the YOLOv8 model, please configure the IP Webcam app with these optimal settings:

**1. Download the App:** * Install the **IP Webcam** app from the Google Play Store (Android) or App Store (iOS).

**2. Video Preferences (Crucial for Speed):**
* Open the app and go to **Video Preferences**.
* Tap on **Video Resolution** and set it to a medium resolution like `640x480` or `1280x720`. (Do not use 4K or 1080p, as it slows down the AI model).
* Set **Video Quality** to `50%` to reduce network latency.

**3. Power Management (For long-term use):**
* Go to **Power Management** in the app.
* Enable **Keep screen active** if you are testing, or select **Run in background** if you want the camera to monitor silently while the phone screen is off.

**4. Start the Surveillance:**
* Go back to the main menu, scroll down to the very bottom, and tap **Start server**.
* Grant the necessary camera and network permissions.
* The screen will display an IP address at the bottom (e.g., `http://192.168.1.100:8080`). Use this exact URL in your Python script.
