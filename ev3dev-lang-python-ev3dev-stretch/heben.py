#!/usr/bin/env python3

from ev3dev2.motor import MediumMotor, OUTPUT_C, OUTPUT_D, SpeedPercent
from time import sleep
m1 = MediumMotor(OUTPUT_C)
m2 = MediumMotor(OUTPUT_D)


#m2.on_for_rotations(SpeedPercent(-10),2)
m2.on_for_rotations(SpeedPercent(-10),5)
m1.on_for_rotations(SpeedPercent(30),5)
sleep(3)
m1.on_for_rotations(SpeedPercent(-30),5)
m2.on_for_rotations(SpeedPercent(10),5)





