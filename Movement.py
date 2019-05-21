from pygame import *
from math import *
from random import *
screen=display.set_mode((1050,800))
WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)

p1Rect=Rect(200,700,64,64)
p1=[200,700,0,True,True]
p2Rect=Rect(300,700,64,64)
p2=[300,700,0,True,True]
X=0
Y=1
VY=2
GODOWN=3
DOUBLE=4

def drawScene(screen,pr):
    screen.fill(WHITE)
    hitbox1=draw.rect(screen,RED,(p1[X],p1[Y],64,64))
    hitbox2=draw.rect(screen,BLUE,(p2[X],p2[Y],64,64))
    display.flip()

def moveP1(pr):
    keys=key.get_pressed()
    if keys[K_LEFT] and pr[X]>=0:
        pr[X]-=3
    if keys[K_RIGHT] and pr[X]<=986:
        pr[X]+=3
    if keys[K_UP] and pr[GODOWN] and pr[DOUBLE]:
        pr[VY]=-4
        if pr[Y]<700:
            pr[DOUBLE]=False
    if pr[VY]<=0:#going up
        pr[GODOWN]=False
    elif pr[VY]>=0:#going down
        pr[GODOWN]=True
    pr[Y]+=pr[VY]
    if pr[Y]>=700:
        pr[Y]=700
        pr[VY]=0
        pr[GODOWN]=True
        pr[DOUBLE]=True
    pr[VY]+=0.2
    print(pr)

def moveP2(pr):
    keys=key.get_pressed()
    if keys[K_a] and pr[X]>=0:
        pr[X]-=3
    if keys[K_d] and pr[X]<=986:
        pr[X]+=3
    if keys[K_w] and pr[GODOWN] and pr[DOUBLE]:
        pr[VY]=-4
        if pr[Y]<700:
            pr[DOUBLE]=False
    if pr[VY]<=0:#going up
        pr[GODOWN]=False
    elif pr[VY]>=0:#going down
        pr[GODOWN]=True
    pr[Y]+=pr[VY]
    if pr[Y]>=700:
        pr[Y]=700
        pr[VY]=0
        pr[GODOWN]=True
        pr[DOUBLE]=True
    pr[VY]+=0.2
    print(pr)

myclock=time.Clock()       
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    drawScene(screen,p1)
    drawScene(screen,p2)
    moveP1(p1)
    moveP2(p2)
    myclock.tick(60)
quit()
