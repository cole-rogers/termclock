# -*- coding: utf-8 -*-
from random import randint
from asciimatics.screen import Screen
import math
from time import sleep
from datetime import datetime as dt

def drawCircle(screen, max_circle, x_cen, y_cen):
#    font_ratio = 2;
    for i in range(0,60):
        y =math.sin(i*math.pi/180*6)*max_circle+y_cen
        x =math.cos(i*math.pi/180*6)*2*max_circle+x_cen
        screen.print_at(u'◉',round(x),round(y))
 #       ev = screen.get_key()
  #      if ev in (ord('Q'), ord('q')):
          #  return

def drawHand(screen, length, unit):
    hype = 0
    if(unit == "second"):
        hype = dt.now().second
    screen.print_at(u'☎', 0)
def defineParams(screen):
   dimTup = screen.dimensions
   y_cen = round(dimTup[0]/2)
   x_cen = round(dimTup[1]/2)
   if(x_cen/2 > y_cen):
       max_radius = round(y_cen*.75)
   else:
       max_radius = round (x_cen*.75/2)
   dimData = (dimTup[0],dimTup[1],x_cen, y_cen, max_radius)
   return dimData
def analogScreen(screen):
    while (screen.has_resized() == False):
        dimData = defineParams(screen)
        drawCircle(screen,dimData[4], dimData[2], dimData[3])
        screen.refresh()
        sleep(0.50)

while True:
    Screen.wrapper(analogScreen)
