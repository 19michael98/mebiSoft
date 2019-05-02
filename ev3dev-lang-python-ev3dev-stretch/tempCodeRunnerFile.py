#!/usr/bin/env python3

from CR_library import *

LA = LiftingArm();
C = Clutch();
D = Drive();

#D.drive_until_found()
LA.bring_down()
C.close()
D.drive_until_color()
C.open()
D.back()
Roboter.powerNap()







