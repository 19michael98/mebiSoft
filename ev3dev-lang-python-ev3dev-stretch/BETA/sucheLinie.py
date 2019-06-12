#!/usr/bin/env python3

from Beta_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()

D.turn180degright()
sleep(0.5)
D.findSurfaceColor(1)
sleep(0.5)
D.turn45degleft()
sleep(0.5)

ls.mode = 'REFLECT'
cs.mode = 'COL-REFLECT'

#print('Geschwindigkeit > ')
#speed = int(input())

speed = 20

while True:
  tank_drive.on(speed,speed)

  while ls.reflected_light_intensity > 30 and cs.value() > 26:
    print('fahre')

  tank_drive.off()
  if ls.reflected_light_intensity <= 30:
    D.turnRight()
  elif cs.value() <= 26:
    D.turnLeft()
