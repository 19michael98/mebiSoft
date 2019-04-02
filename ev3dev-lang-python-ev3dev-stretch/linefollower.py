#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering

from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import LightSensor

from time import sleep

tank_drive = MoveTank(OUTPUT_A,OUTPUT_B)
sp = MoveSteering(OUTPUT_A,OUTPUT_B)

while True:
  #print('test')
  #sp.on_for_rotations(-40, 10, 10)

  ls = LightSensor(INPUT_3)
  ls.mode = 'REFLECT'
  print(ls.reflected_light_intensity)
  while ls.reflected_light_intensity < 25:
    tank_drive.on_for_rotations(SpeedPercent(5), SpeedPercent(5), 0.1)
  
 #rotations = 0
  #while (ls.reflected_light_intensity > 20) or (rotations > 2):
  #drehen
  i = 0
  while i < 3 and ls.reflected_light_intensity > 25:
    sp.on_for_rotations(-15, 5, 0.1)
    i = i + 1
    print('rechts drehen')
  while ls.reflected_light_intensity > 25:
    sp.on_for_rotations(30, 5, 0.1)
    print('links drehen!')
    #rotations = rotations + 1
  #if ls.reflected_light_intensity > 20:
    # while ls.reflected_light_intensity > 20:
    #  print('rechts drehen')
      # sp.on_for_rotations(10, -50, 1);
  #sleep(0.5)