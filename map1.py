from pygame import *
from math import *
from random import *
font.init()
courierFont=font.SysFont("Courier New",25)
init()
size=width,height=1024,800
screen=display.set_mode(size)

back1=image.load("wcdonalds.png")

running=True
while running:
    for evnt in event.get():
        if evnt.type==QUIT:
            running=False
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    screen.blit(back1,(0,0))
    draw.rect(screen,(30,30,250),(0,560,1024,40))#bottom
    draw.rect(screen,(30,30,250),(300,430,300,40))
    draw.rect(screen,(30,30,250),(500,300,200,40))
    draw.rect(screen,(30,30,250),(120,170,300,40))
    draw.rect(screen,(30,30,250),(640,170,330,40))
    
    
    display.flip()
quit()
