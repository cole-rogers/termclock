from asciimatics.screen import Screen
from asciimatics.effects import Effect
from time import sleep

def demo(screen):
    while True:
        screen.print_at('Hello world!', 0, 0)
        screen.refresh()
        if (screen.has_resized() == True): 
            break;
        sleep(0.20)


while True:
    Screen.wrapper(demo)
