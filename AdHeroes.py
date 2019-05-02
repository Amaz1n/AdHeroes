#AdHeroes
from pygame import *
from math import *
from random import *
init()
size=width,height=600,850
screen=display.set_mode(size)

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

quit()
