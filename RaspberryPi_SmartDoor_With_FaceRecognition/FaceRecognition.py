import numpy as np
import cv2
import face_recognition
import os
from datetime import datetime
from picamera import PiCamera
import time
from time import sleep
import GPIO as GP
import imutils
from imutils.video import VideoStream


path='ImageAttandence'
images=[]
classNames=[]
myList=os.listdir(path)
print(myList)

for cl in myList:
    curImg=cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])  #This will extract the only the image name not the extract .jpg
print(classNames)

def findEncodings(images):
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def Attandance(name):
    with open('Attandance.csv','r+') as f:
        myDataList=f.readlines()
        nameList=[]
        for line in myDataList:
            entry=line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now=datetime.now()
            dtString=now.strftime('%H:%M:%S') #Format -->> Hour ,Minute , Second
            f.writelines(f'\n{name},{dtString}')

encodeListKnown=findEncodings(images)
print('Encoding Complete')


# cap=cv2.VideoCapture(0)
camera=VideoStream(src=0).start()
time.sleep(1)

while True:
    img=camera.read()
    imgS=imutils.resize(img,width=500)
    # imgS=cv2.resize(img,(0,0),width=500)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    facesCurFrame=face_recognition.face_locations(imgS)
    encodeCurFrame=face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLoc in zip(encodeCurFrame,facesCurFrame):
        matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDis)
        matchIndex=np.argmin(faceDis)

        if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            print(name)
            y1,x2,y2,x1=faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4

            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),-1)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            Attandance(name)

            #Unlock the Door
            GP.GPIO_Unlock(18)

        else:
            name='NOT DETECTED'
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), -1)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            #Lock the Door
            GP.GPIO_Lock(18)


    cv2.imshow('Webcam',img)
    cv2.waitKey(1)
