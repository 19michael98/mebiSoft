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

class Roboter:
  def __init__(self):
    print('init roboter')
  
  def powerNap(self):
    sleep(1.5)

class LiftingArm:
  def __init__(self):
    print('Init LiftingArm')
    self.speed = 30
    #if us.distance_centimeters_ping < 9.5:
    m1.on_for_rotations(SpeedPercent(self.speed),5)

  def bring_down(self):
    m1.on_for_rotations(SpeedPercent(-self.speed),5)

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
    self.speed_fast = 15
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
                                
  #def drive_until_found(self):
  #  while us.distance_centimeters > 10:
  #    self.fast()
  #    print(us.distance_centimeters)

  def drive_until_found(self):
    while ins.proximity > 12:
      self.fast()
      print(ins.proximity)

  def drive_until_color(self):
    cs.mode = 'COL-COLOR'
    while cs.value() != 2:
      self.slow()