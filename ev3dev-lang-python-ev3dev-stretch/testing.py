#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_A, OUTPUT_B, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.display import Display
import os

# color sensor
#from ev3dev2.sensor.lego import ColorSensor
#from ev3dev2.sensor import INPUT_1

#from ev3dev2.sensor.lego import *
#from ev3dev2.sensor import INPUT_1

# TODO: Add code here

#cS = ColorSensor(INPUT_1)
#while true:
 # while cS.color() == 5:

#Fahren
tank_drive = MoveTank(OUTPUT_A,OUTPUT_B);
tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 10)

#Greifer aufmachen
m2 = MediumMotor(OUTPUT_D)
m2.on_for_rotations(SpeedPercent(10),1)
#Greifer zumachen
m2 = MediumMotor(OUTPUT_D)
m2.on_for_rotations(SpeedPercent(-10),1)

#Greifer Heben
m1 = LargeMotor(OUTPUT_C)
m1.on_for_rotations(SpeedPercent(20), 1)

#Greifer aufmachen
m2 = MediumMotor(OUTPUT_D)
m2.on_for_rotations(SpeedPercent(10),1)

#Drehen rechts/links
#m1 = LargeMotor(OUTPUT_A)
#m1.on_for_rotations(SpeedPercent(75), 20)

#m2 = LargeMotor(OUTPUT_B)
#m2.on_for_rotations(SpeedPercent(75), 20)








