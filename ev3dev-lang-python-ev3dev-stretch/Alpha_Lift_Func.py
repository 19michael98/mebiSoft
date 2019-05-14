#!/usr/bin/env python3

from Alpha_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()

D.drive_until_found()
LA.bring_down()
tank_drive.on_for_rotations(10, 10, 0.1)
#D.fast()
#sleep(2)
C.close()
LA.bring_up()
D.drive_until_found()
#D.back()
LA.bring_to_stage()
#sleep(2)
C.open()
#sleep(2)
tank_drive.on(-10,-10)
sleep(2)
tank_drive.off()
LA.bring_from_stage_to_up()
#sleep(2)
LA.bring_down()
