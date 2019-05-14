#!/usr/bin/env python3

from Beta_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()

print('Distanz > ')
distance = int(input())

D.findObject(distance)
LA.bring_down()
tank_drive.on_for_rotations(10, 10, 0.1)
C.close()
LA.bring_up()
D.findObject(distance)
LA.bring_to_stage()
C.open()
sleep(0.5)
D.driveBackSec(1)
LA.bring_from_stage_to_up()
LA.bring_down()
