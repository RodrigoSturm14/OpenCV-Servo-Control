# Servo Control with OpenCV

![banner_servo_control](https://github.com/RodrigoSturm14/OpenCV-Servo-Control/assets/105557226/f62486fe-020a-428e-a8f9-9e4de00b499e)

## Index

* [Description](#description)
* [Demo and overview](#demo-and-overview)
* [Notes](#notes)

# Description
Object detection system capable of controlling the position of a servo motor by image procesing, using `OpenCV`, `Python` and a `ESP32` micro-controller. The goal is to develop a system that follows the position of an object being tracked with a servo motor.

# Demo and overview

First the program gets the center of the object being tracked (see the 🟦 dot), in order to trigger an action whether the center point is in the left, center or right division.

Therefore, if the object is on center section, the servo motor moves 90°, if it is on the left section it will move 180° and 0° on the right one:

| Screen divisions | Output servo control |
|         :---:            |          :---:         |
| ![OpenCV-Servo-Control-gif-2](https://github.com/RodrigoSturm14/OpenCV-Servo-Control/assets/105557226/3e4fdc53-e15a-4dc7-a14f-8782b5f251d0) | ![OpenCV-Servo-Control-gif-3](https://github.com/RodrigoSturm14/OpenCV-Servo-Control/assets/105557226/6aea2f0b-82d0-4a21-b5ea-f60aa27ef148) |

# Notes
This repo is being develop, it will be updated with the latest upgrades.

Drop a ⭐ if you are interested!
