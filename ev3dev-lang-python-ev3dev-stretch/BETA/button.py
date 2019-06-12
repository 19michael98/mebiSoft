#!/usr/bin/env python3
from Beta_Library import *
from ev3dev2.button import Button
from ev3dev2.sound import Sound

btn = Button()
sound = Sound()

btn.wait_for_bump('right')
while True:
  sound.beep()