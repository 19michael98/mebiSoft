#!/usr/bin/env python3

from Alpha_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()

D.drive_until_found()
LA.bring_down()
D.fast()
sleep(2)
C.close()
LA.bring_up()
D.drive_until_found()
#D.back()
LA.bring_to_stage()
sleep(2)
C.open()
sleep(2)
D.back()
D.back()
LA.bring_from_stage_to_up()
sleep(2)
LA.bring_down()
print('Error kann nur zwei stapeln')
#LA.bring_from_stage_to_up()
#LA.bring_down()

#while True:
#  D.fast()