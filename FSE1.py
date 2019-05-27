#FSE
from pygame import *
from random import *
from math import *
size=widht,height=1024,800
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLACK=(0,0,0)
player1=[widht//2,630,0,True]
plats=[Rect(randint(300,3700),randint(280,430),60,10) for i in range(40)]
ONGROUND=3
def moveGuy1(player1):
    global move,frame
    newMove=-1
    keys=key.get_pressed()
    if keys[K_RIGHT]:
        newMove=0
        player1[0]+=2 
    elif keys[K_DOWN]:
        newMove=1
        player1[1]+=2   
    elif keys[K_UP] and player1[ONGROUND]:
        newMove=1
        player1[1]-=2
        player1[3]=-10
        player1[ONGROUND]=False
    elif keys[K_LEFT]:
        newMove=0
        player1[0]-=2
    else:
        frame=0
    if move==newMove:
        frame=frame+0.2
        if frame>=len(pics[move]):
            frame=1
    elif newMove!=-1:
        move=newMove
        frame=1
        print("start")
    player1[1]+=player1[2]
    
    player1[2]+=0.5#applying gravity
    if player1[1]>=450:
        player1[1]=450#set it on ground
        player1[2]=0#stop falling down
        player1[ONGROUND]=True

def checkCollision(player1,plats):
    rec=Rect(player1[0],player1[1],30,150)
    for p in plats:
        if rec.colliderect(p):
            if player1[2]>0 and rec.move(0,-player1[2]).colliderect(p)==False:#falling down
                guy[ONGROUND]=True
                guy[2]=0
                guy[1]=p.y-31
#def moveGuy2(player2):


def drawScene(screen,picList,player,plats):
    offset=250-player1[0]
    #background for fight
    screen.fill((200,222,244))
    pic=picList[move][int(frame)]
    screen.blit(pic,(player[0],player[1]))
    for p in plats:
        p=p.move(offset,0)#moving left/right
        draw.rect(screen,(0,255,0),p)
    display.flip()
#def checkHits():

#def moveskill():

def addPics(name,start,end):
    mypics=[]
    for i in range(start,end+1):
        mypics.append(image.load("%s%03d.png"%(name,i)))
    return mypics

pics=[]
pics.append(addPics("Kuwirama",1,12))
pics.append(addPics("Kuwirama",12,19))
pics.append(addPics("Kuwirama",20,24))
#def selectcharacter():
    #background for selecting
    #change select
    #
##def instructions():
##
##def menu():
##
##def game():


frame=0
move=0
    
myclock=time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    drawScene(screen,pics,player1,plats)
    moveGuy1(player1)
    checkCollision(player1,plats)
    myclock.tick(60)
quit()




        
