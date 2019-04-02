#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_A, OUTPUT_B, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4, INPUT_3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import LightSensor

from time import sleep
#from ev3dev2.sensor.lego import InfraredSensor
#from ev3dev2.led import Leds
#from ev3dev2.sound import Sound
#from ev3dev2.display import Display
#import os

# color sensor
#from ev3dev2.sensor.lego import ColorSensor
#from ev3dev2.sensor import INPUT_1

#from ev3dev2.sensor.lego import *
#from ev3dev2.sensor import INPUT_1

# TODO: Add code here

#cS = ColorSensor(INPUT_1)
#while true:
 # while cS.color() == 5:

#Fahren - mit verwendung von Sensoren
#ts = TouchSensor(INPUT_1)
#while ts.is_pressed:
 # tank_drive = MoveTank(OUTPUT_A,OUTPUT_B);
 # tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 10)

#us = UltrasonicSensor(INPUT_4)
#print(us.distance_centimeters_ping)
#while us.distance_centimeters_ping > 20:
 # tank_drive = MoveTank(OUTPUT_A,OUTPUT_B);
 # tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 10)

#ausgaben der reflexionswerte
#cs = ColorSensor(INPUT_2)
#while True:
 # cs.mode = 'COL-REFLECT'
 # print(cs.value())
 # sleep(0.5)

#ausgaben der color werte 1-7
#cs = ColorSensor(INPUT_2)
#while True:
 # cs.mode = 'COL-COLOR'
 # print(cs.value())
 # sleep(0.5)

#reflektiertes licht bei schwarz unter 20 und alles andere über 30 ca.
#ls = LightSensor(INPUT_3)
#while True:
 # ls.mode = 'REFLECT'
 # print(ls.reflected_light_intensity)
 # sleep(0.5)

#Fährt nur wenn der lichtsensor auf schwarzen untergrund zeigt
#while True:
 # ls = LightSensor(INPUT_3)
 # ls.mode = 'REFLECT'
 # print(ls.reflected_light_intensity)
 # while ls.reflected_light_intensity < 20:
 #   tank_drive = MoveTank(OUTPUT_A,OUTPUT_B);
 #   tank_drive.on_for_rotations(SpeedPercent(5), SpeedPercent(5), 0.5)
 # sleep(0.5)

cs = ColorSensor(INPUT_1)
while True:
  cs.mode = 'COL-REFLECT'
  print(cs.value())
  sleep(0.5)

#Greifer aufmachen
#m2 = MediumMotor(OUTPUT_D)
#m2.on_for_rotations(SpeedPercent(10),1)

#Greifer zumachen
#m2 = MediumMotor(OUTPUT_D)
#m2.on_for_rotations(SpeedPercent(-10),1)

#Greifer Heben
#m1 = LargeMotor(OUTPUT_C)
#m1.on_for_rotations(SpeedPercent(20), 0.5, hold=true)
#m1.on_for_degrees(SpeedPercent(10),90)
#m1.stop()
#m1.STATE_HOLDING()
#m1.is_holding()
#m1.STOP_ACTION_HOLD()

#Greifer aufmachen
#m2 = MediumMotor(OUTPUT_D)
#m2.on_for_rotations(SpeedPercent(10),1)

#Drehen rechts/links
#m1 = LargeMotor(OUTPUT_A)
#m1.on_for_rotations(SpeedPercent(75), 20)

#m2 = LargeMotor(OUTPUT_B)
#m2.on_for_rotations(SpeedPercent(75), 20)

print ('test')








