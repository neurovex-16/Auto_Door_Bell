# 🔔 Smart Doorbell using Face Detection ( A Fun Project)

A Python-based Smart Doorbell system that uses real-time face detection with OpenCV and the `face_recognition` library.  
Whenever a person appears in front of the camera, the system automatically rings a virtual doorbell sound.

This project demonstrates the practical implementation of:
- Computer Vision
- Real-Time Face Detection
- Multithreading
- Audio Playback Automation

# 📌 Features

✅ Real-time webcam monitoring  
✅ Automatic face detection  
✅ Doorbell sound alert when a face is detected  
✅ Prevents continuous repeated ringing  
✅ Multi-threaded sound playback for smoother performance  
✅ Lightweight and beginner-friendly project  
✅ Works completely offline  

# 🛠 Technologies Used

- Python
- OpenCV
- face_recognition
- pygame
- threading

# Installing `face_recognition` on Windows

The `face_recognition` package depends on native C++ libraries such as `dlib`, so a few development tools must be installed before setting it up successfully on Windows.

# 1️⃣ Install Python

Download Python from the official website.
Recommended versions:
- Python 3.7 – Python 3.13

During installation:
✅ Enable the option:

Add Python to PATH
This allows Python commands to work directly from the terminal.

# 2️⃣ Install CMake

dlib requires CMake to compile its source files
Download Cmake from:https://cmake.org/download/

During installation:Add CMake to the system PATH

# 3️⃣ Install Microsoft C++ Build Tools

Since dlib contains C++ code, Windows needs the Visual C++ compiler tools.
Download from:https://visualstudio.microsoft.com/visual-cpp-build-tools/

While installing, make sure these components are selected:
Desktop development with C++,
Windows SDK

# 4️⃣ Create a Virtual Environment (Recommended)
Using a virtual environment keeps project dependencies isolated.

# 5️⃣ Update pip and Build Packages

Before installation, upgrade package management tools:pip install --upgrade pip setuptools wheel

# 6️⃣ Install face_recognition

Now install the library: pip install face_recognition
If the installation stops during dlib compilation, install dependencies manually:pip install cmake
pip install dlib
pip install face_recognition

# 7️⃣ Verify Installation

Run the following command to confirm everything works correctly:python -c "import face_recognition; print('Installation successful')"
If no errors appear, the library has been installed successfully.

## To Check if Cmake is in your laptop or not 
Cmake --version

# ❗ Common Issues

| Problem | Solution |
|---|---|
| `CMake not found` | Verify that CMake is properly added to the system PATH |
| `Build tools not detected` | Install Visual C++ Build Tools and Windows SDK |
| `dlib installation fails` | Install `dlib` separately before installing `face_recognition` |
| `wheel build failed` | Upgrade `pip`, `setuptools`, and `wheel` packages |

## Recommended Fix Commands

pip install --upgrade pip setuptools wheel,
pip install cmake,
pip install dlib,
pip install face_recognition

# 📁 Project Structure

```bash
Smart_Doorbell/
│
├── main.py
├── requirements.txt
├── README.md
│
└── Audio/
    └── doorbell.wav
```