#AdHeroes
from pygame import *
from math import *
from random import *
font.init()
courierFont=font.SysFont("Courier New",26)
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
        
        #doing text
        gametext=courierFont.render("Game",True,(255,255,255))
        screen.blit(gametext,(495,218))
        credittext=courierFont.render("Credit",True,(255,255,255))
        screen.blit(credittext,(485,318))
        instructiontext=courierFont.render("Instruction",True,(255,255,255))
        screen.blit(instructiontext,(445,418))
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
    right=image.load("rightarrow.png")
    left=image.load("leftarrow.png")
    running = True
    mapPos=0
    mapList=[image.load("back1.png"),image.load("back2.png"),image.load("back3.png")]#we need to add map
    #background image
    screen.fill((30,30,24))
    #####text
    comicFont=font.SysFont("Comic Sans MS",100)
    selecttext=comicFont.render("SELECT",True,(255,255,255))
    screen.blit(selecttext,(335,30))
    #####
    selectbox=[Rect(x*120+170,510,100,100) for x in range(6)]
    startRect=Rect(350,620,350,150)#start game button
    mapRect=Rect(270,210,500,200)
    rightRect=Rect(870,260,61,81)
    leftRect=Rect(120,260,61,81)
    draw.rect(screen,(200,200,120),mapRect)#showing map
    draw.rect(screen,(110,200,100),leftRect)
    draw.rect(screen,(110,200,100),rightRect)
    draw.rect(screen,(30,30,150),startRect)#start game button
    screen.blit(right,(870,260))
    screen.blit(left,(120,260))
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
        if mb[0]==1 and rightRect.collidepoint(mx,my) and click:
            mapPos=(mapPos+1)%len(mapList)
        if mb[0]==1 and leftRect.collidepoint(mx,my) and click:
            mapPos=(mapPos-1)%len(mapList)
        if mb[0]==1 and startRect.collidepoint(mx,my) and click:
            return "game"
        #resize the map as mapRect size
        screen.blit(mapList[mapPos],(270,210))
        display.flip()
    return "menu"

def instructions():
    running = True
    #screen.load() load picture
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        #screen.blit()#blit the instruction picture
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
running=True                          
x,y=0,0        
page = "menu"
while page != "exit":
    if page == "menu":
        page = menu()
    if page == "game":
        page = simpleGame()    
    if page == "instructions":
        page = instructions()       
    if page == "credits":
        page = credit()
    if page == "select":
        page = select()
quit()
