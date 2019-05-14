#!/usr/bin/env python3

from Alpha_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()

ls.mode = 'REFLECT'
while True:
  print('ls: ',ls.reflected_light_intensity)
  sleep(0.5)




