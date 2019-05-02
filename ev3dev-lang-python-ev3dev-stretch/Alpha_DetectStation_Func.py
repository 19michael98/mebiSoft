#!/usr/bin/env python3

from Alpha_Library import *

ls.mode = 'REFLECT'
cs.mode = 'COL-REFLECT'

while True:
  print('light sensor: ',ls.reflected_light_intensity)
  print('color sensor: ',cs.value())
  while ls.reflected_light_intensity > 30 and cs.value() > 3:
    tank_drive.on_for_rotations(SpeedPercent(15), SpeedPercent(15), 0.1,False) #hier noch das Haltemoment des motors mit break=False deaktivieren
    #detect station
    cs.mode = 'COL-COLOR'
    if cs.value() == 5: # 3 color code red
      print('Stationsfarbe erkannt!')
      print('folge Stationslinie')
      sp.on_for_rotations(30, 10, 0.5,False) # eigenlich notwenidig am Stand drehen
    cs.mode = 'COL-REFLECT'
  if ls.reflected_light_intensity <= 30:
    print('links drehen')
    sp.on_for_rotations(30, 10, 0.1,False) #Haltemoment deaktivieren
  elif cs.value() <= 3:
    print('rechts drehen')
    sp.on_for_rotations(-15, 10, 0.1,False) #Haltemoment deaktivieren