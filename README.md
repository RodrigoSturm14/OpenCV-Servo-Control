# Servo Control with OpenCV

![banner_servo_control](https://github.com/RodrigoSturm14/OpenCV-Servo-Control/assets/105557226/f62486fe-020a-428e-a8f9-9e4de00b499e)

## Index

* [Description](#description)
* [Demo and overview](#demo-and-overview)
* [Improvement areas](#improvement-areas)
  * [To-Do list](#to-do-list)
* [Notes](#notes)
  

# Description
Object detection system capable of controlling the position of a servo motor by image procesing, using `OpenCV`, `Python` and an `ESP32` micro-controller. The goal is to develop a system capable of moving a servo motor depending of the object's position being tracked.

# Demo and overview

First the program gets the center of the object being tracked (see the 🟦 dot), in order to trigger an action whether the center point is in the left, center or right division.

Therefore, if the object is on center section, the servo motor moves 90°, if it is on the left section it will move 180° and 0° on the right one:

| Screen divisions | Output servo control |
|         :---:            |          :---:         |
| ![OpenCV-Servo-Control-gif-2](https://github.com/RodrigoSturm14/OpenCV-Servo-Control/assets/105557226/3e4fdc53-e15a-4dc7-a14f-8782b5f251d0) | ![OpenCV-Servo-Control-gif-3](https://github.com/RodrigoSturm14/OpenCV-Servo-Control/assets/105557226/6aea2f0b-82d0-4a21-b5ea-f60aa27ef148) |

> [!NOTE]
> 
> _Currently, the Python program is just capable of detecting and tracking things with certain colours, for example green objects._

# Improvement areas
### To-Do list
- [ ] Use a cellphone for object detection. Currently the Python program uses the laptop camara; using a cellphone camara will improve the frames's quality and the scability of the application.
- [ ] Add other ways of object recognition. At the moment the application just uses a basic mask color detection to track the objects; the next goal is to detect specific objects, like books, persons, or a football ball.

# Notes
This repo is being develop, it will be updated with the latest upgrades.

Drop a ⭐ if you are interested!
