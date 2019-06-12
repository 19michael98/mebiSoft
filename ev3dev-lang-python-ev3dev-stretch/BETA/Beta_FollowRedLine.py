#!/usr/bin/env python3

from Beta_Library import *

# funkioniert mit den eingestellten Grenzwert nicht siehe Evernote

LA = LiftingArm()
C = Clutch()
D = Drive()

ls.mode = 'REFLECT'
cs.mode = 'COL-COLOR'

print('grad > ')
grad = int(input())

print('gesch > ')
speed = int(input())

while True:

  while cs.value() != 5:
    sp.on_for_rotations(-grad, speed, 0.1,brake=False)

  D.turnLeft()

  sp.on_for_rotations(grad, speed, 0.1,brake=False)

  tank_drive.on(speed,speed)

  # while ls.reflected_light_intensity > 45 and cs.value() != 5:
  #   print('fahre')

  # tank_drive.off()

  # if ls.reflected_light_intensity <= 46:
  #   D.turnRight()
  # elif cs.value() == 5:
  #   D.turnLeft()
