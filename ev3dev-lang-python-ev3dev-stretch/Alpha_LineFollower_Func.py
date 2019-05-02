#!/usr/bin/env python3

from Alpha_Library import *

LA = LiftingArm()
C = Clutch()
D = Drive()

ls.mode = 'REFLECT'
cs.mode = 'COL-REFLECT'

tank_drive.on(30,30)

while ls.reflected_light_intensity > 30 and cs.value() > 26:
  print('fahre')

tank_drive.off()

#while True:
  #print('light sensor: ',ls.reflected_light_intensity)
  #print('color sensor: ',cs.value())
  #while ls.reflected_light_intensity > 30 and cs.value() > 26:
    #tank_drive.on_for_rotations(SpeedPercent(15), SpeedPercent(15), 0.1,False) #hier noch das Haltemoment des motors mit break=False deaktivieren
    #D.fast()
  #if ls.reflected_light_intensity <= 35:
  #  print('rechts drehen')
  #  print(ls.reflected_light_intensity)
  #  D.turnRight()
  #  #sp.on_for_rotations(30, 10, 0.1,False) #Haltemoment deaktivieren 
  #elif cs.value() <= 9:
  #  print('links drehen')
  #  print(cs.value())
  #  D.turnLeft()
  #  #sp.on_for_rotations(-15, 10, 0.1,False) #Haltemoment deaktivieren
    
  