#!/usr/bin/env python3

from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import LightSensor
from time import sleep

ls = LightSensor(INPUT_3)
ls.mode = 'REFLECT'

while True:
  print(ls.reflected_light_intensity)
  sleep(0.5)