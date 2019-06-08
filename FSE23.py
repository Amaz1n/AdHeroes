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
p1=[500,700,0,True,True]#player 1
p2=[300,700,0,True,True]#player 2
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
player1="robot"
player2="robot"
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
    chaList=["Robot","Boomber","Mcman","Recycle bin","Slime","F"]#character name
    selectbox=[Rect(x*120+170,510,100,100) for x in range(6)]
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
    screen.blit(Atext,(190,480))
    boomtext=smallFont.render("BOOMBER",True,(255,255,255))
    screen.blit(boomtext,(300,480))
    mctext=smallFont.render("MCMAN",True,(255,255,255))
    screen.blit(mctext,(430,480))
    bintext=smallFont.render("RECYCLE BIN",True,(255,255,255))
    screen.blit(bintext,(515,480))
    slimetext=smallFont.render("SLIME",True,(255,255,255))
    screen.blit(slimetext,(668,480))
    Ftext=smallFont.render("F",True,(255,255,255))
    screen.blit(Ftext,(800,480))
    draw.rect(screen,(0,0,0),(30,100,313,30))
    p1text=courierFont.render("Player 1: Robot",True,(255,255,255))
    screen.blit(p1text,(29,100))
    draw.rect(screen,(0,0,0),(30,140,313,30))
    p1text=courierFont.render("Player 2: Robot",True,(255,255,255))
    screen.blit(p1text,(29,140))
    #####character images
    robotimage=image.load("robotIdle000.png")
    screen.blit(robotimage,(187,520))
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
                elif player1=="Boomber":
                    chapos1=1
                elif player1=="Mcman":
                    chapos1=2
                elif player1=="Recycle bin":
                    chapos1=3
                elif player1=="Slime":
                    chapos1=4
                elif player1=="F":
                    chapos1=5
            
            if selectbox[i].collidepoint(mx,my) and mb[2]==1 and click:
                draw.rect(screen,(0,0,0),(30,140,313,30))
                player2=chaList[i]#chose character
                p2text=courierFont.render("Player 2: "+str(chaList[i]),True,(255,255,255))
                screen.blit(p2text,(29,140))
                if player2=="Robot":
                    chapos2=0
                elif player2=="Boomber":
                    chapos2=1
                elif player2=="Mcman":
                    chapos2=2
                elif player2=="Recycle bin":
                    chapos2=3
                elif player2=="Slime":
                    chapos2=4
                elif player2=="F":
                    chapos2=5      
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
def drawScene(screen,picList1,picList2,health1,health2):
    global mapPos
    screen.blit(realmap[mapPos],(0,0))
    draw.rect(screen,(255,0,0),(30,50,400,30))#red
                        # left health  health1=50,health2=90    
    draw.rect(screen,(0,255,0),(30,50,health1/100*400,30))#green
    draw.rect(screen,(255,0,0),(590,50,400,30))#red
    draw.rect(screen,(0,255,0),(590,50,health2/100*400,30))#green
    pic1=picList1[move1][int(frame1)]
    pic2=picList2[move2][int(frame2)]
    screen.blit(pic1,(p1[X],p1[Y]))
    screen.blit(pic2,(p2[X],p2[Y]))
    
    myClock.tick(60)
    display.flip()

move1=0 #move for player1
frame1=0 #frame for player1
def moveGuy1(pr):
    global move1,frame1
    newMove=-1
    keys=key.get_pressed()
    
    if keys[K_UP] and pr[GODOWN] and pr[DOUBLE]:
        print("jump")
        newMove=3
        pr[VY]=-8
        if pr[Y]<700:
            pr[DOUBLE]=False
    if keys[K_DOWN]:
        newMove=1
        pr[Y]+=4
    if keys[K_LEFT] and pr[X]>=0:
        if pr[Y]<700:
            newMove=4
        else:
            newMove=1
        pr[X]-=6
        if keys[K_DOWN]:
            pr[Y]+=4
    elif keys[K_RIGHT] and pr[X]<=986:
        if pr[Y]<700:
            newMove=5
        else:
            newMove=2
        pr[X]+=6
        if keys[K_DOWN]:
            pr[Y]+=4

    else:
        frame1=0 #0 is the "idle" frame (standing pose)
    
    if keys[K_RSHIFT]:
        newMove=6
    if keys[K_RCTRL]:
        newMove=7
           
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
    
    if move1==newMove:
        frame1=frame1+0.4
        if frame1>=len(pics1[chapos1][move1]):
            frame1=1#restarting at frame 1 (0 - standing 1-5 is walking)
    elif newMove!=-1:#this is the MOMENT we START WALKING
        move1=newMove
        frame1=1
        print("start")

move2=0   #move for player2        
frame2=0  #frame for player2

def moveGuy2(pr):
    global move2,frame2
    newMove=-1
    keys=key.get_pressed()
    if keys[K_w] and pr[GODOWN] and pr[DOUBLE]:#just jump
        print("jump")
        newMove=3
        pr[VY]=-8
        if pr[Y]<700:
            pr[DOUBLE]=False
    if keys[K_s]:
        newMove=0
        pr[Y]+=4
    if keys[K_a] and pr[X]>=0:#go left
        if pr[Y]<700:
            newMove=4
        else:
            newMove=1
        pr[X]-=6
        if keys[K_s]:
            pr[Y]+=4
    elif keys[K_d] and pr[X]<=986:#go right
        if pr[Y]<700:
            newMove=5
        else:
            newMove=2
        pr[X]+=6
        if keys[K_s]:
            pr[Y]+=4
    else:
        frame2=0 #0 is the "idle" frame (standing pose)

    if keys[K_c]:
        newMove=6
    if keys[K_v]:
        newMove=7

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

    if move2==newMove:
        frame2=frame2+0.7
        if frame2>=len(pics2[chapos2][move2]):
            frame2=1#restarting at frame 1 (0 - standing 1-5 is walking)
    elif newMove!=-1:#this is the MOMENT we START WALKING
        move2=newMove
        frame2=1
#def checkHit():  
   
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
mcman=[]
boomber=[]
recyclebin=[]
recyclebin.append(addPics("binIdleF",0,0))
recyclebin.append(addPics("binWalkL",0,12))#left
recyclebin.append(addPics("binWalkR",0,12))#right
slime=[]
pics1=[robotpics,mcman,boomber,recyclebin,slime]#pics list for player1
pics2=[robotpics,mcman,boomber,recyclebin,slime]#pics list for player2

def game():
    running = True
    
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False
        global chapos1,chapos2
        moveGuy1(p1)########
        moveGuy2(p2)########
        #               player1 piclist  player2 piclist health1, health2
        drawScene(screen,pics1[chapos1],pics2[chapos2],50,90)
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
