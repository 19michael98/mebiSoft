#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering

from ev3dev2.sensor import INPUT_3, INPUT_1
from ev3dev2.sensor.lego import LightSensor, ColorSensor

from time import sleep

tank_drive = MoveTank(OUTPUT_A,OUTPUT_B)
sp = MoveSteering(OUTPUT_A,OUTPUT_B)
ls = LightSensor(INPUT_3)
cs = ColorSensor(INPUT_1)
ls.mode = 'REFLECT'
cs.mode = 'COL-REFLECT'

while True:
  print('light sensor: ',ls.reflected_light_intensity)
  print('color sensor: ',cs.value())
  while ls.reflected_light_intensity > 30 and cs.value() > 3:
    tank_drive.on_for_rotations(SpeedPercent(15), SpeedPercent(15), 0.1)
  if ls.reflected_light_intensity <= 30:
    print('links drehen')
    sp.on_for_rotations(30, 10, 0.1)
  elif cs.value() <= 3:
    print('rechts drehen')
    sp.on_for_rotations(-15, 10, 0.1)