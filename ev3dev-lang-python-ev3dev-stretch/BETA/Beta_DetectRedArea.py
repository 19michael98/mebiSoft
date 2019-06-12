#!/usr/bin/env python3

from Beta_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()

#Linie folgen und im Anschluss die 1. Station finden
D.driveOnLineUntilRedStation()
tank_drive.on_for_rotations(30,30,0.2)
D.turn90degleft()
tank_drive.on_for_rotations(30,30,0.5)
LA.bring_down()