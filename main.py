from random import randint
from asciimatics.screen import Screen

def drawCircle():
    FontHW = 2;
    while True:

    ##    	y=sin(r*PI/180*6)*hand_max+sYcen;
##	draw_point(x,y,c);
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()
def defineParams():
   dimTup = screen.dimensions
   screen.print_at(dimTup,0,0) 

def main(screen):
    drawCircle()
    defineParams()
Screen.wrapper(screen)
