#!/usr/bin/env python3

from Alpha_Library import *

print('Alpha_Push_Func')

LA = LiftingArm();
C = Clutch();
D = Drive();

#D.drive_until_found()
LA.bring_down()
C.close()
D.drive_until_color()
C.open()
D.back()
#Roboter.powerNap()
