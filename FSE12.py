#AdHeroes
from pygame import *
from math import *
from random import *
font.init()
courierFont=font.SysFont("Courier New",25)
init()
size=width,height=1024,800
screen=display.set_mode(size)
grav=4.4
X=0
Y=1
VY=2
GODOWN=3
DOUBLE=4
p1=[500,700,0,True,True]
p2=[300,700,0,True,True]
myclock=time.Clock()
def menu():
    running = True
    myClock = time.Clock()
    buttons=[Rect(430,250,200,60),Rect(430,350,200,60),
             Rect(430,450,200,60),Rect(430,550,200,60)]
    mainBack=image.load("Start screen.png")
    vals=["select","credits","instructions","exit"]
          #game
    while running:
        for evnt in event.get():
            if evnt.type==QUIT:
                return "exit"
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        #background image (screen.blit(..))
        screen.blit(mainBack,(0,0))
        
        #button text
        gametext=courierFont.render("Game",True,(255,255,255))
        screen.blit(gametext,(495,268))
        credittext=courierFont.render("Credits",True,(255,255,255))
        screen.blit(credittext,(480,368))
        instructiontext=courierFont.render("Instructions",True,(255,255,255))
        screen.blit(instructiontext,(444,468))
        quittext=courierFont.render("Quit",True,(255,255,255))
        screen.blit(quittext,(500,568))
        
        for i in range(len(buttons)):
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
def select():
    global player1,player2
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
    chaList=["Robot","B","C","D","E","F"]#character name
    selectbox=[Rect(x*120+170,510,100,100) for x in range(6)]
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
    Atext=smallFont.render("robot",True,(255,255,255))
    screen.blit(Atext,(160,480))
    draw.rect(screen,(0,0,0),(40,100,250,30))
    p1text=courierFont.render("Player 1: Robot",True,(255,255,255))
    screen.blit(p1text,(40,100))
    draw.rect(screen,(0,0,0),(40,140,250,30))
    p1text=courierFont.render("Player 2: Robot",True,(255,255,255))
    screen.blit(p1text,(40,140))
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
        
        for i in range(len(selectbox)):
            draw.rect(screen,(150,100,200),selectbox[i])
        if key.get_pressed()[27]: running = False

        draw.rect(screen,(30,30,24),leftRect)
        draw.rect(screen,(30,30,24),rightRect)
        screen.blit(right,(870,270))#DO NOT DELETE THIS PLS
        screen.blit(left,(120,270))
        
        #hovering over buttons
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
        
        if mb[0]==1 and startRect.collidepoint(mx,my) and click:
            return "game"
        if startRect.collidepoint(mx,my):
            draw.rect(screen,(0,0,255),startRect,2)
        else:
            draw.rect(screen,(255,255,0),startRect,2)
        #resize the map as mapRect size
        screen.blit(mapList[mapPos],(270,210))
        #selecting character
        for i in range(len(selectbox)):
            if selectbox[i].collidepoint(mx,my) and mb[0]==1 and click:
                draw.rect(screen,(0,0,0),(40,100,250,30))
                player1=chaList[i]#chose character
                p1text=courierFont.render("Player 1: "+str(chaList[i]),True,(255,255,255))
                screen.blit(p1text,(40,100))
            if selectbox[i].collidepoint(mx,my) and mb[2]==1 and click:
                draw.rect(screen,(0,0,0),(40,140,250,30))
                player2=chaList[i]#chose character
                p2text=courierFont.render("Player 2: "+str(chaList[i]),True,(255,255,255))
                screen.blit(p2text,(40,140))
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


def drawScene(screen,picList1):
    global mapPos
    realmap=[image.load("wcdonalds.png"),image.load("animeback.png"),image.load("roboYardBack.png")]# add real size map
    screen.blit(realmap[mapPos],(0,0))
    print(picList1)
    pic1=picList1[move][int(frame)]
    #pic2=picList2[move][int(frame)]
    screen.blit(pic1,(p1[X],p1[Y]))
    #screen.blit(pic2,(player2[X],player[Y]))
    display.flip()
'''
We need to have moveGuy for player 1 and player 2
move and frame also should have one for each player
'''
def moveGuy1(pr):
    global move,frame
    newMove=-1
    keys=key.get_pressed()
    if keys[K_LEFT] and pr[X]>=0:
        newMove=1
        pr[X]-=3
    if keys[K_RIGHT] and pr[X]<=986:
        newMove=2
        pr[X]+=3
    
    if keys[K_DOWN]:
        newMove=1
        pr[Y]+=2
    
    if keys[K_RIGHT] and pr[X]>=0 and keys[K_UP] and pr[GODOWN] and pr[DOUBLE]:
        newMove=5
        pr[VY]=-4
        if pr[Y]<700:
            pr[DOUBLE]=False
    elif keys[K_LEFT] and pr[X]>=0 and keys[K_UP] and pr[GODOWN] and pr[DOUBLE]:
        newMove=4
        pr[VY]=-4
        if pr[Y]<700:
            pr[DOUBLE]=False
    elif keys[K_UP] and pr[GODOWN] and pr[DOUBLE]:
        print("jump")
        newMove=3
        pr[VY]=-4
        if pr[Y]<700:
            pr[DOUBLE]=False
        
    else:
        frame=0 #0 is the "idle" frame (standing pose)

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
    
##    elif keys[K_SHIFT]
##    elif keys[K_CTRL]
    

    if move==newMove:
        frame=frame+0.2
        if frame>=len(pics[move]):
            frame=1#restarting at frame 1 (0 - standing 1-5 is walking)
    elif newMove!=-1:#this is the MOMENT we START WALKING
        move=newMove
        frame=1
        print("start")

move=0            
frame=0

def moveGuy2(pr):
    global move,frame
    newMove=-1
    keys=key.get_pressed()
    if keys[K_a] and pr[X]>=0:
        newMove=3
        pr[X]-=3
    elif keys[K_d] and pr[X]<986:
        newMove=0
        pr[X]+=3
    elif keys[K_w]:
        newMove=2
        pr[Y]-=4
    elif keys[K_s]:
        newMove=1
        pr[Y]+=2
    
        
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
    
    
##    elif keys[K_SHIFT]
##    elif keys[K_CTRL]
    

    if move==newMove:
        frame=frame+0.2
        if frame>=len(pics[move]):
            frame=1#restarting at frame 1 (0 - standing 1-5 is walking)
    elif newMove!=-1:#this is the MOMENT we START WALKING
        move=newMove
        frame=1
    else:
        frame=0 #0 is the "idle" frame (standing pose)
def addPics(name,start,end):
    mypic=[]
    for i in range(start,end+1):
        mypic.append(image.load("%s%03d.png"%(name,i)))
    return mypic         
robotpics=[]
robotpics.append(addPics("robotIdle",0,0))
robotpics.append(addPics("robotIdle",1,2))
robotpics.append(addPics("robotIdle",3,4))
robotpics.append(addPics("robotIdle",5,6))
robotpics.append(addPics("robotIdle",7,8))#jump left
robotpics.append(addPics("robotIdle",9,10))#jump right
mcman=[]
boomber=[]

pics=[robotpics,mcman,boomber]
def game():
    running = True
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False
        moveGuy1(p1)########
        #moveGuy2(p2)########
        cha1=player1
        drawScene(screen,robotpics)
        myclock.tick(60)
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
