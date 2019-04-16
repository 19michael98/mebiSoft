#!/usr/bin/env python3

from CR_library import *

LA = LiftingArm();
C = Clutch();
D = Drive();

LA.bring_down();
C.close();
LA.bring_up();
LA.bring_to_stage();
C.open();
LA.bring_from_stage_to_up();
LA.bring_down();

while True:
  D.fast();





