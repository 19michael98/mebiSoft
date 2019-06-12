#!/usr/bin/env python3

from Beta_Library import *
from ev3dev2.button import Button

def LineFollower:
  ls.mode = 'REFLECT'
  cs.mode = 'COL-REFLECT'
  station = False
  tank_drive.on(20,20)

  while ls.reflected_light_intensity > 30 and cs.value() > 26:
    cs.mode = 'COL-COLOR'
    if cs.value() == 5:
      print('station erkannt')
      station = True
      tank_drive.off()
      break
    cs.mode = 'COL-REFLECT'

  tank_drive.off()
  if not station:
    if ls.reflected_light_intensity <= 30:
      self.turnRight()
    elif cs.value() <= 26:
      self.turnLeft()
  else
    return == cs.value()

while True:
  col = LineFollower
  if col = 5:
    print('station A detected')