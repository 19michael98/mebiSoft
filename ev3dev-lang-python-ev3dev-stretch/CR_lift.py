#!/usr/bin/env python3

from CR_library import *
#print('test!')
LA = LiftingArm()
C = Clutch()
D = Drive()

D.drive_until_found()
LA.bring_down()
sleep(2)
C.close()
LA.bring_up()
D.drive_until_found()
LA.bring_to_stage()
sleep(2)
C.open()
sleep(2)
D.back()
D.back()
LA.bring_from_stage_to_up()
sleep(2)
LA.bring_down()
#LA.bring_from_stage_to_up()
#LA.bring_down()

#while True:
#  D.fast()





