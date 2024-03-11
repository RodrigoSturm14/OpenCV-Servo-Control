# Servo Control with OpenCV

![banner_servo_control](https://github.com/RodrigoSturm14/OpenCV-Servo-Control/assets/105557226/f62486fe-020a-428e-a8f9-9e4de00b499e)

## Index

* [Description](#description)
* [Demo and overview](#demo-and-overview)
* [Notes](#notes)

# Description
Object detection system capable of controlling the position of a servo motor by image procesing, using `OpenCV`, `Python` and a `ESP32` micro-controller. The goal is to develop a system that follows the position of an object being tracked with a servo motor.

# Demo and overview

First the program gets the center of the object being tracked (see the 🟦 dot) in order to trigger an action whether the centroid is in the left, center or right division:

<p align="center">
  <img src="https://github.com/RodrigoSturm14/OpenCV-Servo-Control/assets/105557226/95701882-da75-4f49-a1c8-e50af8db7d49" alt="animated" />
</p>

Therefore, if the object is on center section, an LED turn on, and if it is on the left or right section, the LED will turn off:

<p align="center">
  <img src="https://github.com/RodrigoSturm14/OpenCV-Servo-Control/assets/105557226/21e43c64-d8b9-4ac4-a002-a0d1db4102cb" alt="animated" />
</p>



# Notes
This repo is being develop, it will be updated with the latest upgrades.

Drop a ⭐ if you are interested!
