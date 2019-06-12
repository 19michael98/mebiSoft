#!/usr/bin/env python3

from Beta_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()

D.driveOnLineUntilGreenStation()
tank_drive.on_for_rotations(30,30,0.2)
D.turn90degleft()
tank_drive.on_for_rotations(30,30,0.5)

# #Linie folgen und im Anschluss die 2. Station finden
# #D.driveOnLineUntilGreenStation()

# print('Distanz:')
# distance = int(input())
# print('Farbe')
# colorNr = int(input())

# #D.turn90degleft()
# D.findObject(distance)
# LA.bring_down()
# C.close()
# D.findSurfaceColor(colorNr)  #param --> colorNr (0-7)
# C.open()
# sleep(2)
# #D.turn90degright()

