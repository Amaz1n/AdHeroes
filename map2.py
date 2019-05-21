from pygame import *
from math import *
from random import *
font.init()
courierFont=font.SysFont("Courier New",25)
init()
size=width,height=1024,800
screen=display.set_mode(size)

back2=image.load("animeback.png")

running=True
while running:
    for evnt in event.get():
        if evnt.type==QUIT:
            running=False
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    screen.blit(back2,(0,0))
    draw.rect(screen,(0,0,255),(270,60,500,40))
    draw.rect(screen,(0,0,255),(150,190,200,40))
    draw.rect(screen,(0,0,255),(700,190,200,40))
    draw.rect(screen,(0,0,255),(35,320,400,40))
    draw.rect(screen,(0,0,255),(600,320,400,40))
    draw.rect(screen,(0,0,255),(360,450,310,40))
    draw.rect(screen,(0,0,255),(0,580,1024,40))
    display.flip()
quit()
