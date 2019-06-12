#!/usr/bin/env python3

from Beta_Library import *
from ev3dev2.button import Button

LA = LiftingArm()
C = Clutch()
D = Drive()
btn = Button()

state = 'start' # start
finished = False

#distance = int(input())
distance = 4

countA = 0

def findback():
  D.turn180degright()
  sleep(0.5)
  D.findSurfaceColor(1)
  sleep(0.5)
  D.turn45degleft()
  sleep(0.5)


while not finished:

  # ---------------------------------------------------
    # INIT
  # ---------------------------------------------------

  if state == 'start':
    # waiting for button press
    print('STATE: start')
    print('please press right button...')
    btn.wait_for_bump('right')
    state = 'find-A'

  # ---------------------------------------------------
    # find station Lift 
  # ---------------------------------------------------

  elif state == 'find-A':
    # fahre auf der schwarzen Linie bis rote Abzweigung gefunden wurde
    # Drehung um 90 nach links
    print('STATE: find-A')
    ######################
    D.driveOnLineUntilRedStation()
    tank_drive.on_for_degrees(10,-10,30) # --> um 30 grad drehen
    ######################
    sleep(1)
    state = 'station-A'

  # ---------------------------------------------------
    # station lift
  # ---------------------------------------------------

  elif state == 'station-A':
    countA = countA + 1
    # suche ersten Stein und hebe ihn auf den zweiten gefundenen
    print('STATE: station-A')
    #####################
    ls.mode = 'REFLECT'
    cs.mode = 'COL-COLOR'
    found = False
    while not found:
      while cs.value() != 5:
        sleep(0.5)
        if ins.proximity <= distance:
          found = True
          break
        sp.on_for_rotations(-10, 10, 0.1,brake=False)
      if ins.proximity <= distance:
        found = True
      else:
        D.turnLeft()
      sp.on_for_rotations(10, 10, 0.1,brake=False)
      #tank_drive.on(10,10)
    print('object found... distanc: ', ins.proximity)
    sp.on_for_rotations(-10, -10, 0.2,brake=False)
    LA.bring_down()
    C.close()
    LA.bring_up()
    D.findObject(distance)
    sleep(0.5)
    LA.bring_to_stage()
    sleep(0.5)
    C.open()
    sleep(0.5)
    D.driveBackSec(1)
    sleep(0.5)
    LA.bring_from_stage_to_up()
    
    ######################
    sleep(1)
    #finished = True
    state = 'find_main_line_from_A'

  # ---------------------------------------------------
    # find station push
  # ---------------------------------------------------

  elif state == 'find-B':
    # fahre auf der schwarzen Linie bis gruene Flaeche gefunden wurde
    # Drehung um 90 nach links
    print('STATE: station-B')
    ######################
    D.driveOnLineUntilGreenStation()
    tank_drive.on_for_rotations(20,20,0.2)
    D.turn90degleft()
    #tank_drive.on_for_rotations(20,20,0.5)
    ######################
    sleep(1)
    state = 'station-B'

  # ---------------------------------------------------
    # station push
  # ---------------------------------------------------

  elif state == 'station-B':
    # suche Steine und schiebe sie in den zielbereich
    print('STATE: station-B')
    ######################
    LA.bring_down()
    tank_drive.on_for_rotations(15,15,0.4)
    D.turn90degright()
    tank_drive.on_for_rotations(15,15,1)
    D.turn90degleft()
    D.findSurfaceColor(4)
    sleep(0.5)
    tank_drive.on_for_rotations(-15,-15,0.4)
    ######################
    sleep(1)
    state = 'find_main_line_from_B'

  # ---------------------------------------------------
    # find main line after station A
  # ---------------------------------------------------

  elif state == 'find_main_line_from_A':
    # suche schwarze linie von station A kommend
    print('STATE: find_main_line')
    ######################
    findback()
    ######################
    sleep(1)
    if countA == 2:
      state = 'find-B'
    else:
      state = 'find-A'

  # ---------------------------------------------------
    # find main line after station B
  # ---------------------------------------------------

  elif state == 'find_main_line_from_B':
    # suche schwarze linie von station B kommend
    print('STATE: find_main_line')
    ######################
    findback()
    ######################
    sleep(1)
    state = 'follow_line'

  # ---------------------------------------------------
    # last state follow line --> finish
  # ---------------------------------------------------

  elif state == 'follow_line':
    print('STATE: follow_line')
    ###################### --> Line Follower
    ls.mode = 'REFLECT'
    cs.mode = 'COL-REFLECT'
    run = True
    while run:
      tank_drive.on(20,20)

      while ls.reflected_light_intensity > 30 and cs.value() > 26:
        if btn.any():
          run = False
          break

      tank_drive.off()
      if ls.reflected_light_intensity <= 30:
        D.turnRight()
      elif cs.value() <= 26:
        D.turnLeft()
    
    finished = True
    ######################   

LA.bring_down()
print('--------')
print('finished')