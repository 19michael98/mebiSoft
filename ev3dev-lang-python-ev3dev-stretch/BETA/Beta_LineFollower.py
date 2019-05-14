#!/usr/bin/env python3

from Beta_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()

ls.mode = 'REFLECT'
cs.mode = 'COL-REFLECT'

print('Geschwindigkeit > ')
speed = int(input())

while True:
  tank_drive.on(speed,speed)

  while ls.reflected_light_intensity > 30 and cs.value() > 26:
    print('fahre')

  tank_drive.off()
  #tank_drive.on(speed/2,speed/2) --> hat eigentlich überhaupt keinen Einfluss
  if ls.reflected_light_intensity <= 30:
    D.turnRight()
  elif cs.value() <= 26:
    D.turnLeft()

