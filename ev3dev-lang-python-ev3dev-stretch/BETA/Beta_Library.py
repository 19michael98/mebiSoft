#!/usr/bin/env python3

from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MoveSteering

from ev3dev2.sensor import INPUT_2, INPUT_3, INPUT_4

from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor, InfraredSensor, LightSensor

from time import sleep

#driving motors declaration
tank_drive = MoveTank(OUTPUT_A,OUTPUT_B)

#lift arm declaration
m1 = MediumMotor(OUTPUT_C) #lift
m2 = MediumMotor(OUTPUT_D) #grab 

#steering
sp = MoveSteering(OUTPUT_A,OUTPUT_B)

#distance measure sensor declaration
#us = UltrasonicSensor(INPUT_3)
ins = InfraredSensor(INPUT_3)

#color detection
cs = ColorSensor(INPUT_4)

#light detection
ls = LightSensor(INPUT_2)

class LiftingArm:
  def __init__(self):
    print('Init LiftingArm')
    self.speed = 30
    #if us.distance_centimeters_ping < 9.5:
    m1.on_for_rotations(SpeedPercent(self.speed),5)

  def bring_down(self):
    m1.on_for_rotations(SpeedPercent(-self.speed),6) #one more down than up....

  def bring_up(self):
    m1.on_for_rotations(SpeedPercent(self.speed),5)

  def bring_to_stage(self):
    m1.on_for_rotations(SpeedPercent(-self.speed),2.5)

  def bring_from_stage_to_up(self):
    m1.on_for_rotations(SpeedPercent(self.speed),2.5)


class Clutch:
  def __init__(self):
    print('Init clutch')
    self.speed = 10

  def open(self):
    m2.on_for_rotations(SpeedPercent(self.speed),5)

  def close(self):
    m2.on_for_rotations(SpeedPercent(-self.speed),5)

class Drive:
  def __init__(self):
    print('Init drive')
    self.step_size = 0.1
    self.speed_fast = 30
    self.speed_slow = 5

  def fast(self):
    tank_drive.on_for_rotations(SpeedPercent(self.speed_fast), 
                                SpeedPercent(self.speed_fast), 
                                self.step_size,brake=False,block=False)

  def slow(self):
    tank_drive.on_for_rotations(SpeedPercent(self.speed_slow), 
                                SpeedPercent(self.speed_slow), 
                                self.step_size,brake=False,block=False)

  def back(self):
    tank_drive.on_for_rotations(SpeedPercent(-self.speed_slow), 
                                SpeedPercent(-self.speed_slow), 
                                self.step_size)

  def turnLeft(self):
    print('turn left')
    sp.on_for_rotations(30, 10, 0.1,brake=False)

  def turnRight(self):
    print('turn right')
    sp.on_for_rotations(-30, 10, 0.1,brake=False)

 #################

  def driveOnLineUntilRedStation(self):
    ls.mode = 'REFLECT'
    cs.mode = 'COL-REFLECT'
    station = False
    while not station:
      tank_drive.on(10,10)

      while ls.reflected_light_intensity > 30 and cs.value() > 26:
        print('fahre')
        cs.mode = 'COL-COLOR'
        if cs.value() == 5:
          print('station erkannt')
          station = True
          tank_drive.off()
          break
        cs.mode = 'COL-REFLECT'

      tank_drive.off()
      if not station:
        if ls.reflected_light_intensity <= 30:
          self.turnRight()
        elif cs.value() <= 26:
          self.turnLeft()

 #################

  def driveOnLineUntilGreenStation(self):
    ls.mode = 'REFLECT'
    cs.mode = 'COL-REFLECT'
    station = False
    while not station:
      tank_drive.on(30,30)

      while ls.reflected_light_intensity > 30 and cs.value() > 26:
        print('fahre')
        cs.mode = 'COL-COLOR'
        print('cs:', cs.value())
        sleep(0.01);
        if cs.value() == 3:
          print('station erkannt')
          station = True
          tank_drive.off()
          break
        cs.mode = 'COL-REFLECT'

      tank_drive.off()
      if not station:
        if ls.reflected_light_intensity <= 30:
          self.turnRight()
        elif cs.value() <= 26:
          self.turnLeft()

  #################

  def drive_until_found(self):
    while ins.proximity >= 6:
      #self.fast()
      tank_drive.on(15,15)
      print(ins.proximity)
    tank_drive.off()

  #################

  def drive_until_color(self):
    cs.mode = 'COL-COLOR'
    while cs.value() != 2:
      self.slow()

  #################

  def turn90degleft(self):
    tank_drive.on_for_degrees(10,-10,110)

  def turn90degright(self):
    tank_drive.on_for_degrees(-10,10,110)

  #################

  def findObject(self,distance):
    while ins.proximity >= distance:
      tank_drive.on(15,15)
      print('Distance: ',ins.proximity)
    tank_drive.off()

  #################

  def findSurfaceColor(self,colorNr):
    cs.mode = 'COL-COLOR'
    while cs.value() != colorNr:
      tank_drive.on(15,15)
      print('SurfaceColor: ',cs.value())
    tank_drive.off()

  #################

  def driveBackSec(self,seconds):
    tank_drive.on(-10,-10)
    sleep(seconds)
    tank_drive.off()

  #################
  
