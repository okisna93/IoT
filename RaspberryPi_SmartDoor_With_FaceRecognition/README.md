# Introduction

In this project, I aim to open the door with a face recognition algorithm. I used a raspberry pi with a camera module. If the algorithm recognizes the face, the system automatically unlocks the door. If it can not recognize the face then the system keeps the door locked.

## List of Equipments
* Raspberry Pi 4
* Breadboard and Jumper Wires
* T-Shape GPIO Extension Board
* 40 pin Flat Ribbon Cable
* Raspberry Pi Camera Module, 5MP 1080P
* DC 12v 1.1A 11.4mm Elctromagnetic Solenoid Lock
* 5V one Channel Relay Module
* DC 12V 2A Power Supply Adapter

## Installing Necessary Libraries
```
$pip3 install numpy
$pip3 install opencv-python
$pip3 install dlib
$pip3 install cmake
$pip3 install face-recognition
$pip3 install os
$sudo apt-get install rpi.gpio
$pip install imutils
```
### Clone the IoT Repository on a Raspberry Pi
```
pi@raspberrypi:~ $ git clone https://github.com/okisna93/IoT.git
```
## First Step
Build a circuit similar to the example picture.
https://github.com/okisna93/IoT/blob/main/RaspberryPi_SmartDoor_With_FaceRecognition/BreadBoard_Lock_System1.png
```
$ # Copy the GPIO.py to another location and add the codes below to the end of the script to test your circuit
$GPIO_Unlock(18)   # I used GPIO18, you need to update the number if you use a different GPIO pin than GPIO18
$GPIO_Lock(18)
```
https://user-images.githubusercontent.com/69834549/144778746-ae8c734f-53ab-4af7-bf3d-64126a80426e.mp4

## Second Step
Add the JPEG format picture of the person inside the ImageAttandence file.

![Detection-2](https://user-images.githubusercontent.com/69834549/144782726-c2eff5fc-ec34-47f4-9958-48f8fb08e27b.png)
![Detection-1](https://user-images.githubusercontent.com/69834549/144782730-51d0d9cb-19c7-4e4d-baee-f4c6ac89d520.png)

## Third Step
Run the FaceRecognition.py.
The system will automatically unlock the door if it recognizes the person's picture which is in the ImageAttandence file. 
Also, the script adds the person's name and the time inside the Attandance.csv when it unlocks the door.
I highly suggest you consider adding a fan on the raspberry pi.


https://user-images.githubusercontent.com/69834549/145863410-dbfd78c4-fecb-4b48-bc10-cbf8f51e93e4.mp4


