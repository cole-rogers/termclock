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

def drawHand(screen, rad, x_cen, y_cen, unit, chara):
    if(unit == "second"):
        ang =  math.radians(dt.now().second*6-90)
        angOld = math.radians((dt.now().second-1)*6-90)
    elif (unit == "minute"):
        ang = math.radians(dt.now().minute*6-90)
        angOld = math.radians((dt.now().minute-1)*6-90)
    else:
        ang = math.radians((dt.now().hour/24*360-90))
        angOld = math.radians((dt.now().hour-1)/24*360-90)
    x_pos = round(x_cen + rad*math.cos(ang)*2)
    y_pos = round(y_cen +rad*math.sin(ang))
    screen.move(x_cen,y_cen)
    screen.draw(x_pos, y_pos, chara,7, 0,True)
    x_pos_old = round(x_cen + rad*math.cos(angOld)*2)
    y_pos_old = round(y_cen + rad*math.sin(angOld))
    screen.move(x_cen,y_cen)
    screen.draw(x_pos_old, y_pos_old, ' ',7, 0,True)

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
        drawHand(screen, round(dimData[4])-1, dimData[2], dimData[3], "second",u'⬥')
        drawHand(screen, round(dimData[4])/1.5, dimData[2], dimData[3], "minute",'m')
        drawHand(screen, round(dimData[4])/2.5, dimData[2], dimData[3], "hour",'h')
        screen.print_at(u'◉',dimData[2],dimData[3])
        screen.refresh()
        sleep(0.1)

while True:
    Screen.wrapper(analogScreen)
