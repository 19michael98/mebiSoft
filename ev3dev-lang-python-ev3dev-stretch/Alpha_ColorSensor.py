#!/usr/bin/env python3

from Alpha_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()
R = Roboter()
cs.mode = 'REFLECT'
while True:
  print('cs: ',cs.value())
  sleep(0.5)
  #Roboter.powerNap()




