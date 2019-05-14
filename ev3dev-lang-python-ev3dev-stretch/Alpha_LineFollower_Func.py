#!/usr/bin/env python3

from Alpha_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()

ls.mode = 'REFLECT'
cs.mode = 'COL-REFLECT'

while True:
  tank_drive.on(30,30)

  while ls.reflected_light_intensity > 30 and cs.value() > 26:
    print('fahre')

  tank_drive.off()

  if ls.reflected_light_intensity <= 30:
    D.turnRight()
  elif cs.value() <= 26:
    D.turnLeft()

    
  