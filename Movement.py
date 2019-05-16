from pygame import *
from math import *
from random import *
screen=display.set_mode((1050,800))
WHITE=(255,255,255)
RED=(255,0,0)

p1Rect=Rect(200,700,64,64)
p1=[200,700,0,True]

X1=0
Y1=1
VY1=2
jump1=3



def drawScene(screen,pr):
    screen.fill(WHITE)
    hitbox1=draw.rect(screen,RED,p1Rect)
    display.flip()

def moveP1(pr):
    keys=key.get_pressed()
    if keys[K_LEFT] and p1[X1]>=0:
        p1[X1]-=3
    if keys[K_RIGHT] and p1[X1]<=986:
        p1[X1]+=3
    if keys[K_UP] and p1[jump1]:
        p1[VY1]=-4
        p1[jump1]=False

    p1[Y1]+=p1[VY1]
    if p1[Y1]>=700:
        p1[Y1]=700
        p1[VY1]=0
    p1[VY1]+=0.2
    print(p1)  
    
    
    



myclock=time.Clock()       
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
            
            
            
    
  
    drawScene(screen,p1)
    moveP1(p1)

quit()

