#!/usr/bin/env python3

from Alpha_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()
R = Roboter()
ls.mode = 'REFLECT'
cs.mode = 'COL-REFLECT'
while True:
  #D.fast()
  print('ls: ',ls.reflected_light_intensity) #unter 30
  print('cs: ',cs.value())  #unter 26
  sleep(1)




