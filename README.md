# FaceLogger

A simple yet powerful and efficient face detection and logging security system built with the face_detection and opencv python libraries. The program takes in a video stream, comparing the faces in frame to the user's known faces which are stored in a folder. If an unknown face is detected, a picture of it is taken and stored in a folder containing all unknown faces detected. The program outputs logs to a text file proving entry and exit timestamps for all individuals.

## Demo

<img src="https://github.com/TN0123/FaceLogger/blob/main/Demos/FaceLoggerDemo.gif" alt="Camera"/>
<img src="https://github.com/TN0123/FaceLogger/blob/main/Demos/Logs.png" alt="Logs"/>

## Current Features

- Real time machine learning based facial recognition
- Dynamic logging of entry and exit timestamps for both recognized and unknown individuals
- Capture and storage of facial images for detected unknown faces

## Technologies

- Python
- OpenCV
- face-detection

## Installation and Usage
1. Clone the Repository
   ```sh
   https://github.com/TN0123/FaceLogger.git
   ```
2. Run the application
   ```
   python main.py
   ```
3. Specify the path to your folder of known persons, folder to store unknowns in, and text file to write logs to
