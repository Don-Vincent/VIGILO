# VIGILO
# 🔊 Gunshot Detection System and Alert System using ML(CNN)– CSE Mini Project

A real-time, AI-powered gunshot detection and alert system built with **Flutter** for the frontend and **Python (TensorFlow + Flask)** for the backend. Designed to assist law enforcement or emergency responders by analyzing audio files and detecting potential gunshot events with high accuracy.

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Setup Instructions](#setup-instructions)
  - [Backend (Python + Flask)](#backend-python--flask)
  - [Frontend (Flutter Web)](#frontend-flutter-web)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Credits](#credits)

---

## 🧠 Project Overview

This project was developed as part of the **B.Tech CSE Mini Project**. The system uses deep learning to detect gunshot audio events from environmental recordings. It includes:

- A browser-based interface for uploading `.wav` files
- A Python backend using Flask and TensorFlow to process and classify sounds
- Real-time prediction results displayed via a web interface
- Trained on a real-world dataset: UrbanSound8K

The original plan included integrating a hardware-based microphone input, but due to time and resource constraints, this component was not implemented in the current version.

---

## 🚀 Features

- 🔍 Detects gunshot vs. non-gunshot audio
- 🎯 ~85% test accuracy using 1D CNN
- 🌐 Flutter web interface
- 📁 Upload `.wav` files and receive predictions instantly
- 🧭 Alert History and Map interface for future expansion

---

## 🛠 Tech Stack

| Layer       | Technology             |
|-------------|------------------------|
| Frontend    | Flutter Web (Dart)     |
| Backend     | Python 3.10, Flask     |
| ML Model    | TensorFlow (1D CNN)    |
| Audio Tools | Librosa, NumPy         |
| Dataset     | [UrbanSound8K](https://urbansounddataset.weebly.com/urbansound8k.html) |

---

## 🧩 System Architecture

The system follows a modular client-server architecture:

1. **Frontend (Flutter Web):**
   - Allows the user to upload audio files (.wav)
   - Sends audio to the backend server via HTTP POST
   - Displays prediction results (e.g., gunshot detected or not)

2. **Backend (Python Flask API):**
   - Receives the audio file from the frontend
   - Extracts features from the audio using Librosa
   - Passes features to a trained 1D CNN model (TensorFlow)
   - Returns prediction to the frontend as JSON

3. **Machine Learning Model:**
   - Trained on UrbanSound8K dataset
   - Uses MFCCs, Mel spectrograms, chroma, contrast features
   - Outputs class index (e.g., gunshot = 6)

4. **Dataset (UrbanSound8K):**
   - Used for training and testing
   - Audio samples labeled by class

The system is designed to be lightweight, responsive, and expandable for real-time or mobile deployment in the future.

---

## 🛠️ Setup Instructions

### 🔹 Backend (Python + Flask)

1. **Install Python 3.10+**
2. **Create virtual environment:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4.**Run API:**
  ```bash
  python app.py
```
The backend will start at: http://127.0.0.1:5000

### 🔹 Frontend (Flutter Web)
1.**Install Flutter SDK: https://flutter.dev/docs/get-started/install**
2.**Open frontend/ folder in VS Code**
3.**Install packages:**
```bash
   flutter pub get
```
4.**Run app in browser:**
 ```bash
 flutter run -d chrome
```
## 🔍 How It Works

The system follows a step-by-step workflow:

1. **User uploads a `.wav` audio file** using the Flutter web interface.
2. The **Flutter app sends the file to the backend** (Flask API) using an HTTP POST request.
3. The **Flask server receives the file** and processes it:
   - Uses **Librosa** to extract audio features (MFCC, Chroma, Mel, etc.)
4. The extracted features are fed into a **trained 1D Convolutional Neural Network (CNN)**.
5. The **model classifies the audio** and determines whether it contains a gunshot.
6. The backend returns a **JSON response** (e.g., `{ "prediction": 6 }`).
7. The frontend displays the **prediction result** to the user in a readable format (e.g., "Gunshot Detected").

This workflow ensures fast, accurate, and user-friendly prediction of gunshot sounds in audio files.

---

### 🙌 Credits
- 📚 Dataset: UrbanSound8K
- 🛠 Frameworks: Flutter, TensorFlow, Flask
- 👨‍💻 Developer: Don Vincent
- 🎓 Project Type: Mini Project – B.Tech Computer Science & Engineering

### 📜 License
This project is created for academic purposes. You may use and adapt the code with proper attribution.
