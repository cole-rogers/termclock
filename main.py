# -*- coding: utf-8 -*-
from random import randint
from asciimatics.screen import Screen
import math
from time import sleep
def drawCircle(screen, max_circle, x_cen, y_cen):
#    font_ratio = 2;
    for i in range(0,60):
        y =math.sin(i*math.pi/180*6)*max_circle+x_cen
        x =math.cos(i*math.pi/180*6)*2*max_circle+y_cen
        screen.print_at("*",round(x),round(y))
 #       ev = screen.get_key()
  #      if ev in (ord('Q'), ord('q')):
          #  return

def defineParams(screen):
   dimTup = screen.dimensions
   x_cen = round(dimTup[0]/2)
   y_cen = round(dimTup[1]/2)
   if(x_cen*2 > y_cen):
       max_radius = round(y_cen-1)
   else:
       max_radius = x_cen-1
   dimData = (dimTup[0],dimTup[1],x_cen, y_cen, max_radius)
   return dimData
def mainScreen(screen):
    v = 0
    while True:
        if (screen.has_resized() == True or v == 0):
            dimData = defineParams(screen)
            drawCircle(screen,dimData[4], dimData[2], dimData[3])
            screen.refresh()
        v = 1

Screen.wrapper(mainScreen)
