#AdHeroes
from pygame import *
from math import *
from random import *
init()
size=width,height=1000,600
screen=display.set_mode(size)
grav=4.4

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    display.flip()
quit()
