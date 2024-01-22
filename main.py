import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import keyboard


path = input("Enter the path of the folder which contains your known faces: ")
unknownsPath = input("Enter the path of the folder which you want to store unknown faces in: ")
logfile = input("Enter the full name of the file that you want to write logs to (must be a .txt file): ")
images = []
names = []
known_encountered = set()
unknown_encountered = set()
unknown_images = []
unknown_encodings = []
unknown_counter = 0

myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    names.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

def findUnknownEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(img)
        
        if face_encodings:
            encodeList.append(face_encodings[0])

    return encodeList

encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

entered_people = set()

print('Press q to quit')

while True:
    success, img = cap.read()
    
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    facesCurrFrame = face_recognition.face_locations(imgS)
    encodesCurrFrame = face_recognition.face_encodings(imgS, facesCurrFrame)

    current_frame_people = set()

    for encodeFace, faceLoc in zip(encodesCurrFrame, facesCurrFrame):
        matches_known = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDist_known = face_recognition.face_distance(encodeListKnown, encodeFace)

        matches_unknown = face_recognition.compare_faces(list(unknown_encodings), encodeFace)
        faceDist_unknown = face_recognition.face_distance(list(unknown_encodings), encodeFace)

        match_known_found = False
        match_unknown_found = False

        for i, (match_known, dist_known) in enumerate(zip(matches_known, faceDist_known)):
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            
            if match_known and dist_known < 0.6:
                matchIndex_known = np.argmin(faceDist_known)
                name_known = names[matchIndex_known].upper()
                current_frame_people.add(name_known)

                if name_known not in entered_people:
                    entered_people.add(name_known)
                    with open(logfile, 'a') as file:
                        file.write(f"{name_known} entered at {datetime.now()}\n")

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name_known, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                match_known_found = True

        for i, (match_unknown, dist_unknown) in enumerate(zip(matches_unknown, faceDist_unknown)):
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

            if match_unknown and dist_unknown < 0.6:
                matchIndex_unknown = np.argmin(faceDist_unknown)
                name_unknown = f"Unknown_{matchIndex_unknown}"
                current_frame_people.add(name_unknown)

                if name_unknown not in entered_people:
                    entered_people.add(name_unknown)
                    with open(logfile, 'a') as file:
                        file.write(f"{name_unknown} entered at {datetime.now()}\n")

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name_unknown, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                match_unknown_found = True

        if not match_known_found and not match_unknown_found:
            name_unknown = f"Unknown_{unknown_counter}"
            unknown_counter += 1
            current_frame_people.add(name_unknown)

            if name_unknown not in entered_people:
                entered_people.add(name_unknown)
                with open(logfile, 'a') as file:
                    file.write(f"{name_unknown} entered at {datetime.now()}\n")

                cv2.imwrite(f"{unknownsPath}/{name_unknown}.jpg", img[y1:y2, x1:x2])
                unknown_images.append(img[y1:y2, x1:x2])
                unknown_encodings = findUnknownEncodings(unknown_images)

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name_unknown, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    for exited_person in entered_people - current_frame_people:
        with open(logfile, 'a') as file:
            file.write(f"{exited_person} exited at {datetime.now()}\n")
        entered_people.remove(exited_person)

    cv2.imshow('Camera', img)
    cv2.waitKey(1)

    if keyboard.is_pressed('q'):
        break

cap.release()
cv2.destroyAllWindows()
