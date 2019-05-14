#!/usr/bin/env python3

from Beta_Library import *

# funkioniert mit den eingestellten Grenzwert nicht siehe Evernote

LA = LiftingArm()
C = Clutch()
D = Drive()

ls.mode = 'REFLECT'
cs.mode = 'COL-COLOR'

while True:
  tank_drive.on(30,30)

  while ls.reflected_light_intensity > 45 and cs.value() != 5:
    print('fahre')

  tank_drive.off()

  if ls.reflected_light_intensity <= 46:
    D.turnRight()
  elif cs.value() == 5:
    D.turnLeft()
