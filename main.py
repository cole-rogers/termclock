from random import randint
from asciimatics.screen import Screen
import math
from time import sleep
#def drawCircle():
#    font_ratio = 2;
#    while True:

        #yplotpoint=sin(r*math.pi/180*6)*circleWide+YMax;
        #print_at(,x,y);
 #       ev = screen.get_key()
  #      if ev in (ord('Q'), ord('q')):
          #  return
     #   screen.refresh()
def defineParams(screen):
   dimTup = screen.dimensions
   screen.print_at(str(dimTup),0,0) 
   screen.refresh()
   sleep(20)

Screen.wrapper(defineParams)
