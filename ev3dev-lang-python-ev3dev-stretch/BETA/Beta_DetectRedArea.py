#!/usr/bin/env python3

from Beta_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()

#Linie folgen und im Anschluss die 1. Station finden
D.driveOnLineUntilRedStation()