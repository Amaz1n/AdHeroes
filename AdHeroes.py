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
    vals=["game","credits","instructions"]
    while running:
        for evnt in event.get():
            if evnt.type==QUIT:
                return "exit"
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        #background image (screen.blit(..))
        for i in range(len(buttons)):
            draw.rect(screen,(0,255,0),buttons[i],2)
            if buttons[i].collidepoint(mx,my):
                draw.rect(screen,(0,0,255),buttons[i],2)
                if mb[0]==1:
                    return vals[i]
            else:
                draw.rect(screen,(255,255,0),buttons[i],2)
                          
        display.flip()
                          
                          
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




quit()
