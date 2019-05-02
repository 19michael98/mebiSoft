#!/usr/bin/env python3

from Alpha_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()
R = Roboter()
ls.mode = 'REFLECT'

while ls.reflected_light_intensity < 50:
  D.fast()
  #print('ls: ',ls.reflected_light_intensity)
  #Roboter.powerNap()
  sleep(0.5)




