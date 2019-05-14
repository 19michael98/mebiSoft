#!/usr/bin/env python3

from Alpha_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()

cs.mode = 'COL-COLOR'
while True:
  print('cs: ',cs.value())
  sleep(0.5)




