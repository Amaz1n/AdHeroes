#AdHeroes
from pygame import *
from math import *
from random import *
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
    running = True
    #background image
    screen.fill((30,30,24))
    selectbox=[Rect(x*120+170,510,100,100) for x in range(6)]
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        for i in range(len(selectbox)):
            draw.rect(screen,(150,100,200),selectbox[i])
        draw.rect(screen,(200,200,120),(270,210,500,200))#showing map
        draw.rect(screen,(110,200,100),(120,260,50,100))
        draw.rect(screen,(110,200,100),(870,260,50,100))
        if key.get_pressed()[27]: running = False
        display.flip()
    return "menu"

def instructions():
    running = True
    
    
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
    if page == "story":
        page = story()    
    if page == "credits":
        page = credit()
    if page == "select":
        page = select()
quit()
