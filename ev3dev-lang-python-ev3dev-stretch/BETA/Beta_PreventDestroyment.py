#!/usr/bin/env python3

from Beta_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()

tank_drive.on(30,30)

ls.mode = 'REFLECT'

while True:
  if ls.reflected_light_intensity <= 22:
    tank_drive.on(-30,-30)
    sleep(0.5)
  else:
    tank_drive.on(30,30)
