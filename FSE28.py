#AdHeroes
from pygame import *#importing pygame
from math import *#importing math
from random import *#importing random
font.init()#initialize fonts
courierFont=font.SysFont("Courier New",25)#Courier New
init()
size=width,height=1024,800#screen size
screen=display.set_mode(size)#set screen
X=0#list position of x
Y=1#list position of y
VY=2#list position of y velocity
GODOWN=3#boolean if going down
DOUBLE=4#boolean if double jump available
p1=[500,520,0,True,True]#player 1
p2=[300,520,0,True,True]#player 2

v=[10,0]#the horiz and vert speed of the bullet
myClock=time.Clock()
rangeDmg=[5,7,7,10,12,20] #damage values for basic ranged ability, pistol,
                          #space gun, throwing away gun, rifle, and sniper
meleeDmg=[7,8,10,13] #damage values for basic melee, stick, french fry, mcsword

realmap=[image.load("wcdonalds.png"),image.load("animeback.png"),image.load("roboYardBack.png")]# add real size map

def menu():#main menu
    running = True#game running
    myClock = time.Clock()#clock
    buttons=[Rect(430,250,200,60),Rect(430,350,200,60),
             Rect(430,450,200,60),Rect(430,550,200,60)]#button boxes
    mainBack=image.load("Start screen.png")#load main menu background
    vals=["select","credits","instructions","exit"]#button types
          #game
    while running:#game running
        for evnt in event.get():
            if evnt.type==QUIT:#window exit button
                return "exit"
        mx,my=mouse.get_pos()#mouse position
        mb=mouse.get_pressed()#mouse pressed
        screen.blit(mainBack,(0,0))#blit main menu background
        
        #button text
        gametext=courierFont.render("Game",True,(255,255,255))#button 1 text
        screen.blit(gametext,(495,268))#blit text
        credittext=courierFont.render("Credits",True,(255,255,255))#button 2 text
        screen.blit(credittext,(480,368))#blit text
        instructiontext=courierFont.render("Instructions",True,(255,255,255))#button 3 text
        screen.blit(instructiontext,(444,468))#blit text
        quittext=courierFont.render("Quit",True,(255,255,255))#button 4 text
        screen.blit(quittext,(500,568))#blit text
        
        for i in range(len(buttons)):#button interactions
            draw.rect(screen,(0,255,0),buttons[i],2)
            if buttons[i].collidepoint(mx,my):
                draw.rect(screen,(0,0,255),buttons[i],2)
                if mb[0]==1:
                    return vals[i]
            else:
                draw.rect(screen,(255,255,0),buttons[i],2)
        display.flip()
mapPos=0
player1="Robot"
player2="Robot"
chapos1=0
chapos2=0

def select():
    global player1,player2,chapos1,chapos2
    right=image.load("rightarrow.png")
    left=image.load("leftarrow.png")
    right2=image.load("rightarrow2.png")
    left2=image.load("leftarrow2.png")
    running = True
    global mapPos
    #resize "back3 picture" as mapRect"
    back3=image.load("back3.png")                               #resize "back3 picture" as mapRect"
    mapList=[image.load("back1.png"),image.load("back2.png"),transform.scale(back3,(500,200))]#we need to add map
    #background image
    screen.fill((30,30,24))
    chaList=["Robot","Mcman","Recycle bin","Slime"]#character name
    selectbox=[Rect(x*120+290,510,100,100) for x in range(4)]
    for i in range(len(selectbox)):
        draw.rect(screen,(150,100,200),selectbox[i])
    startRect=Rect(350,620,350,150)#start game button
    mapRect=Rect(270,210,500,200)
    rightRect=Rect(870,260,63,81)
    leftRect=Rect(124,260,63,81)
    draw.rect(screen,(200,200,120),mapRect)#showing map
    draw.rect(screen,(30,30,150),startRect)#start game button
    #####text
    largeFont=font.SysFont("Courier New",100)
    selecttext=largeFont.render("SELECT",True,(255,255,255))
    screen.blit(selecttext,(335,30))
    readytext=largeFont.render("READY",True,(255,255,255))
    screen.blit(readytext,(375,635))
    smallFont=font.SysFont("Courier New",20)
    Atext=smallFont.render("ROBOT",True,(255,255,255))
    screen.blit(Atext,(310,480))
    mctext=smallFont.render("MCMAN",True,(255,255,255))
    screen.blit(mctext,(430,480))
    bintext=smallFont.render("RECYCLE BIN",True,(255,255,255))
    screen.blit(bintext,(515,480))
    slimetext=smallFont.render("SLIME",True,(255,255,255))
    screen.blit(slimetext,(668,480))

    draw.rect(screen,(0,0,0),(30,100,313,30))
    p1text=courierFont.render("Player 1: "+str(player1),True,(255,255,255))
    screen.blit(p1text,(29,100))
    draw.rect(screen,(0,0,0),(30,140,313,30))
    p2text=courierFont.render("Player 2: "+str(player2),True,(255,255,255))
    screen.blit(p2text,(29,140))
    #####character images
    robotimage=image.load("robotIdle000.png")
    screen.blit(robotimage,(307,520))
    recycleimage=image.load("binIdleF000.png")
    screen.blit(recycleimage,(550,520))
    #####
    while running:
        click=False
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
            if evnt.type == MOUSEBUTTONDOWN:
                click = True
            if evnt.type == MOUSEBUTTONUP:
                click = False
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos() 
        if key.get_pressed()[27]: running = False
        draw.rect(screen,(30,30,24),leftRect)
        draw.rect(screen,(30,30,24),rightRect)
        screen.blit(right,(870,270))
        screen.blit(left,(120,270))
        
        #hovering over arrow buttons
        if rightRect.collidepoint(mx,my):
            draw.rect(screen,(30,30,24),rightRect)
            screen.blit(right2,(874,270))
            if mb[0]==1 and click:
                mapPos=(mapPos+1)%len(mapList)
        if leftRect.collidepoint(mx,my):
            draw.rect(screen,(30,30,24),leftRect)
            screen.blit(left2,(122,270))
            if mb[0]==1 and click:
                mapPos=(mapPos-1)%len(mapList)
        if startRect.collidepoint(mx,my):
            draw.rect(screen,(0,0,255),startRect,2)
        else:
            draw.rect(screen,(255,255,0),startRect,2)
        #resize the map as mapRect size
        screen.blit(mapList[mapPos],(270,210))
        #selecting character
        for i in range(len(selectbox)):
            if selectbox[i].collidepoint(mx,my) and mb[0]==1 and click:
                draw.rect(screen,(0,0,0),(30,100,313,30))
                player1=chaList[i]#chose character
                p1text=courierFont.render("Player 1: "+str(chaList[i]),True,(255,255,255))
                screen.blit(p1text,(29,100))
                if player1=="Robot":
                    chapos1=0
                elif player1=="Mcman":
                    chapos1=1
                elif player1=="Recycle bin":
                    chapos1=2
                elif player1=="Slime":
                    chapos1=3

            if selectbox[i].collidepoint(mx,my) and mb[2]==1 and click:
                draw.rect(screen,(0,0,0),(30,140,313,30))
                player2=chaList[i]#chose character
                p2text=courierFont.render("Player 2: "+str(chaList[i]),True,(255,255,255))
                screen.blit(p2text,(29,140))
                if player2=="Robot":
                    chapos2=0
                elif player2=="Mcman":
                    chapos2=1
                elif player2=="Recycle bin":
                    chapos2=2
                elif player2=="Slime":
                    chapos2=3   
        if mb[0]==1 and startRect.collidepoint(mx,my) and click:
            return "game"            
        display.flip()
    return "menu"

def instructions():
    running = True
    instruction=image.load("instructions.png") #load picture
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        screen.blit(instruction,(0,0))#blit the instruction picture
        if key.get_pressed()[27]: running = False
        display.flip()
    return "menu"

def credit():
    creditPic=image.load("credits.png")
    running = True
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        screen.blit(creditPic,(0,0))#blit the credit picture
        if key.get_pressed()[27]: running = False
        display.flip()
    return "menu"

def end(winner):
    running = True
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
        if winner=="player1":
            print("p1 win")
        elif winner=="player2":
            print("p2 win")
        restartrect=Rect(400,500,250,100)
        draw.rect(screen,(0,230,110),restartrect)
        if restartrect.collidepoint(mx,my):
            draw.rect(screen,(100,159,180),restartrect,3)
        else:
            draw.rect(screen,(0,0,0),restartrect,3)
        if key.get_pressed()[27]: running = False
        if mb[0]==1 and restartrect.collidepoint(mx,my):
            return "select"
        
        display.flip()
    return "menu"

def drawScene(screen,picList1,picList2,health1,health2,bull1,bull2):
    global mapPos
    screen.blit(realmap[mapPos],(0,0))
    draw.rect(screen,(255,0,0),(30,50,400,30))#red
                        # left health  health1=50,health2=90    
    draw.rect(screen,(0,255,0),(30,50,health1/100*400,30))#green
    draw.rect(screen,(255,0,0),(590,50,400,30))#red
    draw.rect(screen,(0,255,0),(590,50,health2/100*400,30))#green
    for b in bull1:
        draw.circle(screen,(255,0,0),(b[0],b[1]),4)
    for b in bull2:
        draw.circle(screen,(255,0,0),(int(b[0]),int(b[1])),4)
    pic1=picList1[move1][int(frame1)]
    pic2=picList2[move2][int(frame2)]
    screen.blit(pic1,(p1[X],p1[Y]))
    screen.blit(pic2,(p2[X],p2[Y]))
    
    myClock.tick(60)
    display.flip()

move1=0 #move for player1
frame1=0 #frame for player1
bullets1=[]
MAXRAPID1=13
rapid1=MAXRAPID1
def moveGuy1(pr,cha):
    global move1,frame1
    newMove=-1
    keys=key.get_pressed()
    
    if keys[K_UP] and pr[GODOWN] and pr[DOUBLE]:
        newMove=3
        pr[VY]=-8
        if pr[Y]<520:
            pr[DOUBLE]=False
    if keys[K_DOWN]:
        newMove=0
        pr[Y]+=4
    if keys[K_LEFT] and pr[X]>=0:
        if pr[Y]<520:
            newMove=4
        else:
            newMove=1
        pr[X]-=6
        if keys[K_DOWN]:
            pr[Y]+=4
    elif keys[K_RIGHT] and pr[X]<=986:
        if pr[Y]<520:
            newMove=5
        else:
            newMove=2
        pr[X]+=6
        if keys[K_DOWN]:
            pr[Y]+=4
    else:
        frame1=0 #0 is the "idle" frame (standing pose)
    
    if keys[K_RSHIFT]:#ranged
        newMove=6
    if keys[K_RCTRL]:#melee
        newMove=7
           
    if pr[VY]<=0:#going up
        pr[GODOWN]=False
    elif pr[VY]>=0:#going down
        pr[GODOWN]=True
    pr[Y]+=pr[VY]
    if pr[Y]>=520:
        pr[Y]=520
        pr[VY]=0
        pr[GODOWN]=True
        pr[DOUBLE]=True
    pr[VY]+=0.2    
    
    if move1==newMove:
        frame1=frame1+0.4
        if frame1>=len(pics1[chapos1][move1]):
            frame1=1#restarting at frame 1 (0 - standing 1-5 is walking)
    elif newMove!=-1:#this is the MOMENT we START WALKING
        move1=newMove
        frame1=1

move2=0   #move for player2        
frame2=0  #frame for player2
bullets2=[]
MAXRAPID2=8
rapid2=MAXRAPID2
keyboard2=[]
def moveGuy2(pr,cha):
    global move2,frame2,rapid2,MAXRAPID2,keyboard2
    newMove=-1
    keys=key.get_pressed()
    if keys[K_w] and pr[GODOWN] and pr[DOUBLE]:#just jump
        newMove=3
        pr[VY]=-8
        if pr[Y]<520:
            pr[DOUBLE]=False
    if keys[K_s]:
        newMove=0
        pr[Y]+=4
    if keys[K_a] and pr[X]>=0:#go left
        if pr[Y]<520:
            newMove=4
        else:
            newMove=1
        pr[X]-=6
        keyboard2.append("left")
        if keys[K_s]:
            pr[Y]+=4
    elif keys[K_d] and pr[X]<=986:#go right
        if pr[Y]<520:
            newMove=5
        else:
            newMove=2
        pr[X]+=6
        keyboard2.append("right")
        if keys[K_s]:
            pr[Y]+=4
    else:
        frame2=0 #0 is the "idle" frame (standing pose)

    if keys[K_c]:#melee
        if keyboard2[-1]=="left":
            newMove=6
        elif keyboard2[-1]=="right":
            newMove=7
        
    if keys[K_v]:#ranged
        if cha=="robot" and rapid2==MAXRAPID2:
            rapid2=0
            bullets2.append([pr[X]+50,pr[Y]+32,v[0],v[1],keyboard2[-1]])
        if cha=="mcman" and rapid2==MAXRAPID2:
            rapid2=0
            bullets2.append([pr[0]+50,pr[1]+32,v[0],v[1],keyboard2[-1]])
        if cha=="recyclebin" and rapid2==MAXRAPID2:
            rapid2=0
            bullets2.append([pr[0]+50,pr[1]+10,v[0],v[1],keyboard2[-1]])
        if cha=="slime" and rapid2==MAXRAPID2:
            rapid2=0
            bullets2.append([pr[0]+50,pr[1]+48,v[0],v[1],keyboard2[-1]])
        if keyboard2[-1]=="left":
            newMove=8
        if keyboard2[-1]=="right":
            newMove=9
    if rapid2<MAXRAPID2:
        rapid2+=1
        

    if pr[VY]<=0:#going up
        pr[GODOWN]=False
    elif pr[VY]>=0:#going down
        pr[GODOWN]=True
    pr[Y]+=pr[VY]
    if pr[Y]>=520:
        pr[Y]=520
        pr[VY]=0
        pr[GODOWN]=True
        pr[DOUBLE]=True
    pr[VY]+=0.2

    if move2==newMove:
        frame2=frame2+0.4
        if frame2>=len(pics2[chapos2][move2]):
            frame2=1#restarting at frame 1 (0 - standing 1-5 is walking)
    elif newMove!=-1:#this is the MOMENT we START WALKING
        move2=newMove
        frame2=1
def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)
def checkHit(bull1,bull2,pr1,pr2):
    global health1,health2
    for b in bull1:
        if distance(b[0],b[1],pr2[0],pr2[1])<10:
            print("J")
            bull1.remove(b)
            health2-=6
    for b in bull2:
        if distance(b[0],b[1],pr1[0],pr1[1])<33:
           
            bull2.remove(b)
            health1-=6
    return health1,health2         
def moveBullets(p1,p2,bull1,bull2,keyboard2):
    for b in bull1:
        if b[4]=="right":
            b[0]+=b[2]*2
            b[1]+=b[3]*2
        if b[4]=="left":
            b[0]-=b[2]*2
            b[1]-=b[3]*2
        
        if b[0]<0 or b[0]>1024:
            bull1.remove(b)
    for b in bull2:
        if b[4]=="right":
            b[0]+=b[2]*2
            b[1]+=b[3]*2
        if b[4]=="left":
            b[0]-=b[2]*2
            b[1]-=b[3]*2
            
        if b[0]<0 or b[0]>1024:
            bull2.remove(b)
          
def addPics(name,start,end):
    mypic=[]
    for i in range(start,end+1):
        mypic.append(image.load("%s%03d.png"%(name,i)))
    return mypic
#making picture list for each character movement
robotpics=[]
robotpics.append(addPics("robotIdle",0,1))
robotpics.append(addPics("robotWalkL",0,12))#left
robotpics.append(addPics("robotWalkR",0,12))#right (needs fixing, how do i add numbers)
robotpics.append(addPics("robotIdle",5,6))#jump
robotpics.append(addPics("robotIdle",7,8))#jump left
robotpics.append(addPics("robotIdle",9,10))#jump right
robotpics.append(addPics("robotIdle",9,10))
robotpics.append(addPics("robotIdle",9,10))
robotpics.append(addPics("robotIdle",9,10))
robotpics.append(addPics("robotIdle",9,10))

mcman=[]
mcman.append(addPics("mcdsIdle",0,1))
mcman.append(addPics("mcdsWalkL",0,11))#left
mcman.append(addPics("mcdsWalkR",0,11))#right
mcman.append(addPics("mcdsJumpL",0,5))#jump (needs fixing proper jump)
mcman.append(addPics("mcdsJumpL",0,5))#jump left
mcman.append(addPics("mcdsJumpR",0,5))#jump right
mcman.append(addPics("mcdsMeleeL",0,1))#hit left
mcman.append(addPics("mcdsMeleeR",0,1))#hit right
mcman.append(addPics("mcdsShootL",0,1))#shoot left
mcman.append(addPics("mcdsShootR",0,1))#shoot right

recyclebin=[]
recyclebin.append(addPics("binIdleF",0,1))
recyclebin.append(addPics("binWalkL",0,12))#left
recyclebin.append(addPics("binWalkR",0,12))#right
recyclebin.append(addPics("binJumpR",0,5))#jump
recyclebin.append(addPics("binJumpL",2,3))#jump left
recyclebin.append(addPics("binJumpR",2,3))#jump right
recyclebin.append(addPics("binMeleeL",0,1))#hit left
recyclebin.append(addPics("binMeleeR",0,1))#hit right
recyclebin.append(addPics("binShootL",0,1))#shoot left
recyclebin.append(addPics("binShootR",0,1))#shoot right

slime=[]
slime.append(addPics("slimeMoveL",1,2))
slime.append(addPics("slimeMoveL",1,5))#left
slime.append(addPics("slimeMoveR",1,5))#right
slime.append(addPics("slimeJumpR",0,2))#jump
slime.append(addPics("slimeJumpL",1,2))#jump left
slime.append(addPics("slimeJumpR",1,2))#jump left
slime.append(addPics("slimeJumpR",1,2))
slime.append(addPics("slimeJumpR",1,2))
slime.append(addPics("slimeJumpR",1,2))
slime.append(addPics("slimeJumpR",1,2))
pics1=[robotpics,mcman,recyclebin,slime]#pics list for player1
pics2=[robotpics,mcman,recyclebin,slime]#pics list for player2

charlist=["robot","mcman","recyclebin","slime"]

def game():
    running = True
    health1=100
    health2=100
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False
        global chapos1,chapos2,health1,health2
        moveGuy1(p1,charlist[chapos1])########
        moveGuy2(p2,charlist[chapos2])########
        
        #               player1 piclist  player2 piclist health1, health2
        drawScene(screen,pics1[chapos1],pics2[chapos2],health1,health2,bullets1,bullets2)
        moveBullets(p1,p2,bullets1,bullets2,keyboard2)
        checkHit(bullets1,bullets2,p1,p2,health1,health2)
        if health1<=0:
            return end(health2)
        if health2<=0:
            return end(health1)
        myClock.tick(60)

    return "select"


running=True                          
x,y=0,0        
page = "menu"
while page != "exit":
    if page == "menu":
        page = menu()
    if page == "game":
        page = game()    
    if page == "instructions":
        page = instructions()       
    if page == "credits":
        page = credit()
    if page == "select":
        page = select()

quit()
