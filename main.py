from random import randint
from asciimatics.screen import Screen
import math
from time import sleep
def drawCircle(screen, max_circle):
#    font_ratio = 2;
    for i in range(1,max_circle):
        y =math.sin(i*math.pi/180*6)*max_circle+10
        x =math.sin(i*math.pi/180*6)*max_circle+10
        
        screen.print_at("*",round(x),round(y))
 #       ev = screen.get_key()
  #      if ev in (ord('Q'), ord('q')):
          #  return
    screen.refresh()

def defineParams(screen):
   dimTup = screen.dimensions
   return dimTup
def mainScreen(screen):
    dimTup = defineParams(screen)
    while True:
        drawCircle(screen,10)

Screen.wrapper(mainScreen)
