#!/usr/bin/env python3

from Alpha_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()
R = Roboter()
ls.mode = 'REFLECT'
cs.mode = 'COL-REFLECT'
#ins.mode = MODE_IR_PROX
while True:
  #D.fast()
  print('inS: ',ins.proximity)
  #print('inS: ',ins.distance())
  #print('inS: ',ins.heading())
  sleep(1)




