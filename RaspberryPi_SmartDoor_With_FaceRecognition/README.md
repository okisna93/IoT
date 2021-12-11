# Introduction

In this project, I aim to open the door with a face recognition algorithm. I used a raspberry pi with a camera module. If the algorithm recognizes the face, the system automatically unlocks the door. If it can not recognize the face then the system keeps the door locked.

List of Equipments
-----------------
Raspberry Pi 4
Breadboard and Jumper Wires
T-Shape GPIO Extension Board
40 pin Flat Ribbon Cable
Raspberry Pi Camera Module, 5MP 1080P
DC 12v 1.1A 11.4mm Elctromagnetic Solenoid Lock
5V one Channel Relay Module
DC 12V 2A Power Supply Adapter

Installing Necessary Libraries
---------------------------------
$pip3 install numpy
$pip3 install opencv-python
$pip3 install face-recognition
$pip3 install dlib
$pip3 install os
$sudo apt-get install rpi.gpio
$pip install imutils

First Step
-------------
I started the project by completing the curcuit. After that , I wrote an algorithm which can unlock the door by using GPIO pins.

https://user-images.githubusercontent.com/69834549/144778746-ae8c734f-53ab-4af7-bf3d-64126a80426e.mp4

Second Step
-------------
I wrote a script that can recognize faces that are in the ImageAttandence file. If I add any person's picture on that file, the person will be able to open the door.

![Detection-2](https://user-images.githubusercontent.com/69834549/144782726-c2eff5fc-ec34-47f4-9958-48f8fb08e27b.png)
![Detection-1](https://user-images.githubusercontent.com/69834549/144782730-51d0d9cb-19c7-4e4d-baee-f4c6ac89d520.png)

Third Step
-----------------
I merged the GPIO script and Face_Recognition script. When the system recognizes the face on the attendance file, the system unlocks the door.
