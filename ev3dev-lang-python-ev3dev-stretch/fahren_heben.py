#!/usr/bin/env python3

from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MoveSteering

from ev3dev2.sensor import INPUT_3

from ev3dev2.sensor.lego import UltrasonicSensor

from time import sleep

tank_drive = MoveTank(OUTPUT_A,OUTPUT_B)
us = UltrasonicSensor(INPUT_3)
m1 = MediumMotor(OUTPUT_C)
m2 = MediumMotor(OUTPUT_D)

#while True:
m1.on_for_rotations(SpeedPercent(30),5)
while us.distance_centimeters_ping > 9.5:
  tank_drive.on_for_rotations(SpeedPercent(15), SpeedPercent(15), 0.1)
m1.on_for_rotations(SpeedPercent(-30),5)
m2.on_for_rotations(SpeedPercent(-10),5)
m1.on_for_rotations(SpeedPercent(30),5)
sleep(3)
while us.distance_centimeters_ping > 9.5:
  tank_drive.on_for_rotations(SpeedPercent(15), SpeedPercent(15), 0.1)
m1.on_for_rotations(SpeedPercent(-30),3.5)
m2.on_for_rotations(SpeedPercent(10),5)
