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

## Motivation
I built this project in response to a phenomenon I noticed in my university’s dorms. To access one’s room, a student would have to swipe their ID to open the main door, swipe to call the elevator, and swipe to press which floor to go to. However, most are courteous enough to hold open the door or elevator for another person, and it is quite easy to get past all three of these checks without swiping your ID once due to the human element of the process. With a real time facial recognition security logging system, even if someone swipes another person in, all people’s entry and exit timestamps are recorded well, and in the event of an incident, being able to identify the cause and time of suspicious activity becomes a lot easier. The functionality of this program is applicable to lots of settings outside of college dorms, virtually in any setting that involves restricted physical access to an area. Whether it’s a corporate office, government facility, or residential building, FaceLogger can offer a solution for tracking access and ensuring the safety of restricted areas.

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
