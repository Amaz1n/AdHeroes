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

def menu():
    running = True
    myClock = time.Clock()
    buttons=[Rect(430,200,200,60),Rect(430,300,200,60),
             Rect(430,400,200,60),Rect(430,500,200,60)]
    
    vals=["select","credits","instructions"]
          #game
    while running:
        for evnt in event.get():
            if evnt.type==QUIT:
                return "exit"
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        #background image (screen.blit(..))
        screen.fill((222,100,30))
        
        #button text
        gametext=courierFont.render("Game",True,(255,255,255))
        screen.blit(gametext,(495,218))
        credittext=courierFont.render("Credits",True,(255,255,255))
        screen.blit(credittext,(480,318))
        instructiontext=courierFont.render("Instructions",True,(255,255,255))
        screen.blit(instructiontext,(444,418))
        button4=courierFont.render("Button 4",True,(255,255,255))
        screen.blit(button4,(470,518))
        
        for i in range(len(buttons)):
            draw.rect(screen,(0,255,0),buttons[i],2)
            if buttons[i].collidepoint(mx,my):
                draw.rect(screen,(0,0,255),buttons[i],2)
                if mb[0]==1:
                    return vals[i]
            else:
                draw.rect(screen,(255,255,0),buttons[i],2)
        display.flip()
                          
def select():
    player1="A"
    player2="A"
    right2=image.load("rightarrow2.png")
    left2=image.load("leftarrow2.png")
    running = True
    mapPos=0
    mapList=[image.load("back1.png"),image.load("back2.png"),image.load("back3.png")]#we need to add map
    #background image
    screen.fill((30,30,24))
    chaList=["A","B","C","D","E","F"]#character name
    
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
                player1=chaList[i]#chose character
                print(player1)
            if selectbox[i].collidepoint(mx,my) and mb[2]==1 and click:
                player2=chaList[i]#chose character
                print(player2)
        display.flip()
    return "menu"

def instructions():
    running = True
    instruction=image.load("instruction.png") #load picture
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        screen.blit(instruction,(0,0))#blit the instruction picture
        if key.get_pressed()[27]: running = False
        display.flip()
    return "menu"

def credit():
    running = True
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        #screen.blit()#blit the credit picture
        if key.get_pressed()[27]: running = False
        display.flip()
    return "menu"
def game():
    X=0
    Y=1
    p1=[70,0]
    p2=[980,0]
    running = True
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False
        moveGuy(p1)########
        moveGuy(p2)########
        drawScene(screen,pics1,pics2,player1,player2)

def drawScene(screen,picList1,picList2,player1,player2):
    realmap=[]# add real size map
    screen.blit(realmap[mapPos])
    pic1=picList1[move][int(frame)]
    pic2=picList2[move][int(frame)]
    screen.blit(pic1,(player1[X],player[Y]))
    screen.blit(pic2,(player2[X],player[Y]))
    display.flip()
'''
We need to have moveGuy for player 1 and player 2
move and frame also should have one for each player
'''
def moveGuy1(player):
    global move,frame
    newMove=-1
    keys=key.get_pressed()
    if keys[K_RIGHT]:
        newMove=0
        player[0]+=2
    elif keys[K_DOWN]:
        newMove=1
        player[1]+=2
    elif keys[K_UP]:
        newMove=2
        player[1]-=2
    elif keys[K_LEFT]:
        newMove=3
        player[0]-=2
##    elif keys[K_c]
##    elif keys[K_v]
    else:
        frame=0 #0 is the "idle" frame (standing pose)

    if move==newMove:
        frame=frame+0.2
        if frame>=len(pics[move]):
            frame=1#restarting at frame 1 (0 - standing 1-5 is walking)
    elif newMove!=-1:#this is the MOMENT we START WALKING
        move=newMove
        frame=1 

move=0            
frame=0

def moveGuy2(player):
    global move,frame
    newMove=-1
    keys=key.get_pressed()
    if keys[K_RIGHT]:
        newMove=0
        player[0]+=2
    elif keys[K_DOWN]:
        newMove=1
        player[1]+=2
    elif keys[K_UP]:
        newMove=2
        player[1]-=2
    elif keys[K_LEFT]:
        newMove=3
        player[0]-=2
##    elif keys[K_SHIFT]
##    elif keys[K_CTRL]
    else:
        frame=0 #0 is the "idle" frame (standing pose)

    if move==newMove:
        frame=frame+0.2
        if frame>=len(pics[move]):
            frame=1#restarting at frame 1 (0 - standing 1-5 is walking)
    elif newMove!=-1:#this is the MOMENT we START WALKING
        move=newMove
        frame=1 

move=0            
frame=0 
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
