import os

import cv2
import pickle

import face_recognition
import numpy as np

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# import cvzone

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://sbhfaceidhospital-default-rtdb.firebaseio.com/"
})

ref = db.reference('Patients')

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

# loading info part of image
folderInfoPart = 'Resources/Info_part'
infoPathList = os.listdir(folderInfoPart)
imgInfoList = []
for path in infoPathList:
    imgInfoList.append(cv2.imread(os.path.join(folderInfoPart, path)))

# load the encoding file
print('Loading Encode file')
file = open('encodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, iDs = encodeListKnownWithIds
# print(iDs)
print('Encode file Loaded')

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurrentFrame = face_recognition.face_locations(imgS)
    encodeCurrentFrame = face_recognition.face_encodings(imgS, faceCurrentFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgInfoList[1]

    for encodeFace, faceLoc in zip(encodeCurrentFrame, faceCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDist = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(matches)
        # print(faceDist)

        matchIndex = np.argmin(faceDist)
        if matches[matchIndex]:
            # print('Known face detected')
            # print(iDs[matchIndex])

            # print(names[int(iDs[matchIndex])-1])
            print(ref.child(f'{int(iDs[matchIndex])}').child('name').get())
            # y1, x2, y2, x1 = faceLoc
            # y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            # bbox = 55+x1, 162+y1, x2-x1, y2-y1
            # imageBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)

    cv2.imshow("Face Recognition", imgBackground)
    cv2.waitKey(1)
