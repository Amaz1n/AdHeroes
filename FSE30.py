#AdHeroes
from pygame import *#importing pygame
from math import *#importing math
from random import *#importing random
font.init()#initialize fonts
courierFont=font.SysFont("Courier New",25)#Courier New
smallFont=font.SysFont("Courier New",14)#size 14 font
largeFont=font.SysFont("Courier New",100)#size 100 font
init()
size=width,height=1024,800#screen size
screen=display.set_mode(size)#set screen
X=0#list position of x
Y=1#list position of y
VY=2#list position of y velocity
GODOWN=3#boolean if going down
DOUBLE=4#boolean if double jump available
p1=[600,520,0,True,True,True]#player 1
p2=[300,520,0,True,True,True]#player 2
musiclist=["menusong.mp3","select.mp3","creditsong.mp3","winnersong.mp3"]
mapmusic=["firstmap.mp3","secondmap.mp3","thirdmap.mp3"]
volume=0.3
v=[10,0]#the horiz and vert speed of the bullet
myClock=time.Clock()
rangeDmg=[5,7,7,10,12,20] #damage values for basic ranged ability, pistol,
                          #space gun, throwing away gun, rifle, and sniper
meleeDmg=[7,8,10,13] #damage values for basic melee, stick, french fry, mcsword
realmap=[image.load("wcdonalds.png"),image.load("animeback.png"),image.load("roboYardBack.png")]# add real size map

def menu():#main menu
    mixer.music.load(musiclist[0])#loading music from list
    mixer.music.play(-1)#play music
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
        keys=key.get_pressed()
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
        
        for i in range(len(buttons)):#button drawing and interactions
            draw.rect(screen,(0,255,0),buttons[i],2)#draw button
            if buttons[i].collidepoint(mx,my):#hover
                draw.rect(screen,(0,0,255),buttons[i],2)#highlight
                if mb[0]==1:#click
                    return vals[i]#value of the button (change page)
            else:#not hovering over
                draw.rect(screen,(255,255,0),buttons[i],2)#original button
        display.flip()
        if keys[K_m]:#M pauses music
            mixer.music.pause()
        if keys[K_SPACE]:#SPACE unpauses music
            mixer.music.unpause()
mapPos=0#position of map
player1="Robot"#default character
player2="Robot"
chapos1=0#character 1 position
chapos2=0#character 2 position

def select():#select function
    mixer.music.load(musiclist[1])#load track 1 (select screen song)
    mixer.music.play(-1)#play song
    global player1,player2,chapos1,chapos2,mapPos#global variables
    right=image.load("rightarrow.png")#load right arrow image >
    left=image.load("leftarrow.png")#load left arrow image <
    right2=image.load("rightarrow2.png")#load right arrow highlighted -
    left2=image.load("leftarrow2.png")#load left arrow highlighted -
    running = True
    
    back3=image.load("back3.png")#load back3 (icon-sized background), default map
    mapList=[image.load("back1.png"),image.load("back2.png"),transform.scale(back3,(500,200))]#map icon list
    screen.fill((30,30,24))#solid background colour
    chaList=["Robot","Mcman","Recycle bin","Slime"]#character names
    selectbox=[Rect(x*120+290,510,100,100) for x in range(4)]#boxes for character selection
    for i in range(len(selectbox)):#draw the boxes
        draw.rect(screen,(150,100,200),selectbox[i])
    startRect=Rect(350,620,350,150)#start game button
    mapRect=Rect(270,210,500,200)#box behind the map icon (not really needed)
    rightRect=Rect(870,260,63,81)#right button hitbox
    leftRect=Rect(124,260,63,81)#left button hitbox
    draw.rect(screen,(200,200,120),mapRect)#draw map icon box
    draw.rect(screen,(30,30,150),startRect)#draw start game button
    #####text
    selecttext=largeFont.render("SELECT",True,(255,255,255))#select screen title
    screen.blit(selecttext,(335,30))#blit text
    readytext=largeFont.render("READY",True,(255,255,255))#text in ready button
    screen.blit(readytext,(375,635))#blit text
    bottext=smallFont.render("ROBOT",True,(255,255,255))#robot text
    screen.blit(bottext,(318,480))#blit text
    mctext=smallFont.render("FRIES",True,(255,255,255))#fries text
    screen.blit(mctext,(440,480))#biit text
    bintext=smallFont.render("RECYCLE BIN",True,(255,255,255))#bin text
    screen.blit(bintext,(534,480))#blit text
    slimetext=smallFont.render("SLIME",True,(255,255,255))#slime text
    screen.blit(slimetext,(678,480))#blit text

    draw.rect(screen,(0,0,0),(10,125,390,30))#rectangle for p1 character selection
    p1text=courierFont.render("P1 Arrow keys: "+str(player1),True,(255,255,255))#text for p1 character
    screen.blit(p1text,(10,125))#blit text
    draw.rect(screen,(0,0,0),(10,165,390,30))#rectangle for p2 character selection
    p2text=courierFont.render("P2 WASD keys : "+str(player2),True,(255,255,255))#text for p2 character
    screen.blit(p2text,(10,165))#blit text
    #####character images
    robotimage=image.load("robotIdle000.png")
    screen.blit(robotimage,(307,520))
    mcdsimage=image.load("mcdsIdle000.png")
    screen.blit(mcdsimage,(428,520))
    recycleimage=image.load("binIdleF000.png")
    screen.blit(recycleimage,(550,520))
    slimeimage=image.load("slimeIdleF000.png")
    screen.blit(slimeimage,(670,520))
    
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
        keys=key.get_pressed()
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos() 
        if key.get_pressed()[27]: running = False
        draw.rect(screen,(30,30,24),leftRect)#left rect for chose map
        draw.rect(screen,(30,30,24),rightRect)#right rect for chose map
        screen.blit(right,(870,270))
        screen.blit(left,(120,270))
        
        #hovering over arrow buttons
        if rightRect.collidepoint(mx,my):
            draw.rect(screen,(30,30,24),rightRect)
            screen.blit(right2,(874,270))
            if mb[0]==1 and click:
                mapPos=(mapPos+1)%len(mapList)#select map
        if leftRect.collidepoint(mx,my):
            draw.rect(screen,(30,30,24),leftRect)
            screen.blit(left2,(122,270))
            if mb[0]==1 and click:
                mapPos=(mapPos-1)%len(mapList)#select map
        if startRect.collidepoint(mx,my):
            draw.rect(screen,(0,0,255),startRect,2)
        else:
            draw.rect(screen,(255,255,0),startRect,2)
        screen.blit(mapList[mapPos],(270,210))#showing the map which is selected
        #selecting character
        for i in range(len(selectbox)):
            if selectbox[i].collidepoint(mx,my) and mb[0]==1 and click:#select p1 character
                draw.rect(screen,(0,0,0),(10,125,390,30))
                player1=chaList[i]#chose character
                p1text=courierFont.render("P1 Arrow keys: "+str(chaList[i]),True,(255,255,255))#text for p1 character
                screen.blit(p1text,(10,125))#blit text
                if player1=="Robot":
                    chapos1=0#pos for character list
                elif player1=="Mcman":
                    chapos1=1#pos for character list
                elif player1=="Recycle bin":
                    chapos1=2#pos for character list
                elif player1=="Slime":
                    chapos1=3#pos for character list

            if selectbox[i].collidepoint(mx,my) and mb[2]==1 and click:#select p2 character
                draw.rect(screen,(0,0,0),(10,165,390,30))
                player2=chaList[i]#chose character
                p2text=courierFont.render("P2 WASD keys : "+str(chaList[i]),True,(255,255,255))#text for p2 character
                screen.blit(p2text,(10,165))#blit text
                if player2=="Robot":
                    chapos2=0#pos for character list
                elif player2=="Mcman":
                    chapos2=1#pos for character list
                elif player2=="Recycle bin":
                    chapos2=2#pos for character list
                elif player2=="Slime":
                    chapos2=3#pos for character list 
        if mb[0]==1 and startRect.collidepoint(mx,my) and click:
            return "game" #start game
        if keys[K_m]:
            mixer.music.pause()#pause music
        if keys[K_SPACE]:
            mixer.music.unpause()#pause music
        display.flip()
    return "menu" #go back to menu page

def instructions():#Instruction page
    mixer.music.load(musiclist[2])#load music for instruction page
    mixer.music.play(-1)#play music
    running = True
    instruction=image.load("instructions.png") #load the instruction picture
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        keys=key.get_pressed()
        screen.blit(instruction,(0,0))#blit the instruction picture
        if key.get_pressed()[27]: running = False
        if keys[K_m]:
            mixer.music.pause()#pause music
        if keys[K_SPACE]:
            mixer.music.unpause()#unpause music
        display.flip()
    return "menu" #go back to menu page

def credit():#Credit page
    mixer.music.load(musiclist[2])#load music for credit page
    mixer.music.play(-1)#play music
    creditPic=image.load("credits.png")#load the credit picture
    running = True
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        keys=key.get_pressed()
        screen.blit(creditPic,(0,0))#blit the credit picture
        if key.get_pressed()[27]: running = False
        if keys[K_m]:
            mixer.music.pause()#pause music
        if keys[K_SPACE]:
            mixer.music.unpause()#unpause music
        display.flip()
    return "menu" #go back to menu page

def end(winner):#end page (winner page)
    courierFont=font.SysFont("Courier New",100)#large font
    courierFont1=font.SysFont("Courier New",30)#small font
    winnerimage=image.load("champion.png")#load winner image
    backimage=image.load("cool screen.png")#load background
    mixer.music.load(musiclist[3])#load ending page music
    mixer.music.play(-1)#play music
    running = True
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        keys=key.get_pressed()
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
        screen.blit(backimage,(0,0))#blit the background
        screen.blit(winnerimage,(300,150))#blit the winner image
        restartrect=Rect(400,500,250,100)
        draw.rect(screen,(0,230,110),restartrect)
        if winner=="player1":
            winnertext=courierFont.render("Player 1",True,(0,0,0))#player 1 is winner
        elif winner=="player2":
            winnertext=courierFont.render("Player 2",True,(0,0,0))#player 2 is winner
        screen.blit(winnertext,(300,180))#blit the winner text
        returntext=courierFont1.render("Play Again",True,(255,255,255))#play again text
        screen.blit(returntext,(440,532))#blit text
        if restartrect.collidepoint(mx,my):#hovering over
            draw.rect(screen,(100,159,180),restartrect,3)
        else:#not hovering over
            draw.rect(screen,(0,0,0),restartrect,3)
        if key.get_pressed()[27]: running = False
        if mb[0]==1 and restartrect.collidepoint(mx,my):#click play again button
            return "select" #back to select page
        if keys[K_m]:
            mixer.music.pause()#pause music
        if keys[K_SPACE]:
            mixer.music.unpause()#pause music
        display.flip()
    return "menu" #back to menu page

bulletimage=[image.load("robotBullet.png"),image.load("mcBullet.png"),image.load("recycleBullet.png"),image.load("slimeBullet.png")]#characters' bullet image
def drawScene(screen,picList1,picList2,health1,health2,bull1,bull2):#draw the scene
    global mapPos,chapos1,chapos2,p1
    screen.blit(realmap[mapPos],(0,0))#blit the map image
    p1text=courierFont.render("Player 1",True,(0,0,0))#player 1 text
    p2text=courierFont.render("Player 2",True,(0,0,0))#player 2 text
    screen.blit(p2text,(50,10))#blit text
    screen.blit(p1text,(850,10))#blit text
    draw.rect(screen,(255,0,0),(30,50,400,30))#red  
    draw.rect(screen,(0,255,0),(30,50,health2/100*400,30))#green
    draw.rect(screen,(255,0,0),(590,50,400,30))#red
    draw.rect(screen,(0,255,0),(590,50,health1/100*400,30))#green
    for b in bull1:
        screen.blit(bulletimage[chapos1],(int(b[0]),int(b[1])))#blit bullet image for player 1
    for b in bull2:
        screen.blit(bulletimage[chapos2],(int(b[0]),int(b[1])))#blit bullet image for player 2
    pic1=picList1[move1][int(frame1)]#bring player 1 character
    pic2=picList2[move2][int(frame2)]#bring player 2 characer
    
    screen.blit(pic1,(p1[X],p1[Y]))#blit player 1
    screen.blit(pic2,(p2[X],p2[Y]))#blit player 2
    
    myClock.tick(60)
    display.flip()

move1=0 #move for player1
frame1=0 #frame for player1
bullets1=[]#bullet list for player1
maxrapid11=7#melee maxrapid for player1
rapid11=maxrapid11#melee rapid for player1
MAXRAPID1=0#shoot maxrapid for player 1
rapid1=MAXRAPID1#shoot rapid for player 1
keyboard1=["right"]#character's facing way
def moveGuy1(pr,cha):
    global move1,frame1,rapid1,MAXRAPID1,keyboard1,rapid11,maxrapid11
    newMove=-1
    keys=key.get_pressed()
    maxrapid11=7#maxrapid for melee
    if keys[K_UP] and pr[GODOWN] and pr[DOUBLE]:#jump straight
        newMove=3
        pr[VY]=-12
        if pr[Y]<520:
            pr[DOUBLE]=False
    if keys[K_DOWN]:
        newMove=0
        pr[Y]+=10
    if keys[K_LEFT] and pr[X]>=0:
        if pr[Y]<520:
            newMove=4
        else:
            newMove=1
        pr[X]-=6
        keyboard1.append("left")#facing left
        if keys[K_DOWN]:
            pr[Y]+=6
        if keys[K_LEFTBRACKET] and rapid11==maxrapid11:
            newMove=6
            rapid11=0#make melee rapid 0
    elif keys[K_RIGHT] and pr[X]<=986:
        if pr[Y]<520:
            newMove=5
        else:
            newMove=2
        keyboard1.append("right")#facing right
        pr[X]+=6
        if keys[K_DOWN]:
            pr[Y]+=6
        if keys[K_LEFTBRACKET] and rapid11==maxrapid11:
            newMove=7
            rapid11=0#make melee rapid 0
    elif keys[K_LEFTBRACKET] and rapid11==maxrapid11:#melee
        if keyboard1[-1]=="left":
            newMove=6
        elif keyboard1[-1]=="right":
            newMove=7
        rapid11=0#make melee rapid 0
    else:
        frame1=0 #0 is the "idle" frame (standing pose)


    if keys[K_RIGHTBRACKET]:#shooting
        if cha=="robot":
            MAXRAPID1=24#maxrapid for robot
            if rapid1==MAXRAPID1:#player can shoot
                rapid1=0#make shooting rapid 0
                if keyboard1[-1]=="left":#facing left
                    bullets1.append([pr[X]+5,pr[Y]+25,v[0],v[1],keyboard1[-1]])#append bullet to bullets list
                if keyboard1[-1]=="right":#facing right
                    bullets1.append([pr[X]+50,pr[Y]+25,v[0],v[1],keyboard1[-1]])#append bullet to bullets list
        if cha=="mcman":
            MAXRAPID1=12#maxrapid for mcman
            if rapid1==MAXRAPID1:#player can shoot
                rapid1=0#make shooting rapid 0
                if keyboard1[-1]=="left":#facing left
                    bullets1.append([pr[X]-15,pr[Y]+32,v[0],v[1],keyboard1[-1]])#append bullet to bullets list
                if keyboard1[-1]=="right":#facing right
                    bullets1.append([pr[X]+60,pr[Y]+32,v[0],v[1],keyboard1[-1]])#append bullet to bullets list
        if cha=="recyclebin":
            MAXRAPID1=8#maxrapid for recyclebin
            if rapid1==MAXRAPID1:#player can shoot
                rapid1=0#make shooting rapid 0
                if keyboard1[-1]=="left":#facing left
                    bullets1.append([pr[X]+10,pr[Y]+5,v[0],v[1],keyboard1[-1]])#append bullet to bullets list
                if keyboard1[-1]=="right":#facing right
                    bullets1.append([pr[X]+55,pr[Y]+5,v[0],v[1],keyboard1[-1]]) #append bullet to bullets list      
        if cha=="slime":
            MAXRAPID1=3#maxrapid for slime
            if rapid1==MAXRAPID1:#player can shoot
                rapid1=0#make shooting rapid 0
                if keyboard1[-1]=="left":#facing left
                    bullets1.append([pr[0]+10,pr[1]+35,v[0],v[1],keyboard1[-1]])#append bullet to bullets list
                if keyboard1[-1]=="right":#facing right
                    bullets1.append([pr[0]+60,pr[1]+35,v[0],v[1],keyboard1[-1]])#append bullet to bullets list
        if keyboard1[-1]=="left":
            newMove=8#shooting sprite list for left side
        if keyboard1[-1]=="right":
            newMove=9#shooting sprite list for right side
    if rapid1<MAXRAPID1:
        rapid1+=1#increase rapid for shoothing
    else:
        rapid1-=1#if rapid is bigger than maxrapid decrease rapid
        
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
    pr[VY]+=0.35    
    
    if move1==newMove:
        frame1=frame1+0.4
        if newMove==6 or newMove==7:# if player is using melee
            frame1+=0.6 #add 0.6 frame so that it can be frame1= 1
        if frame1>=len(pics1[chapos1][move1]):
            frame1=1#restarting at frame 1 (0 - standing 1-5 is walking)
    elif newMove!=-1:#this is the MOMENT we START WALKING
        move1=newMove
        frame1=1
    if rapid11<maxrapid11:
        rapid11+=0.5#increase rapid for melee
        
move2=0   #move for player2        
frame2=0  #frame for player2
bullets2=[]#bullet list for player2
maxrapid=7#melee maxrapid for player2
rapid=maxrapid#melee rapid for player2
MAXRAPID2=6#shooting maxrapid for player2
rapid2=MAXRAPID2#shooting rapid for player2
keyboard2=["left"]#facing way
def moveGuy2(pr,cha):
    global move2,frame2,rapid2,MAXRAPID2,keyboard2,rapid,maxrapid
    newMove=-1
    keys=key.get_pressed()
    maxrapid=7#maxrapid for melee
    if keys[K_w] and pr[GODOWN] and pr[DOUBLE]:#jump straight
        newMove=3
        pr[VY]=-12
        if pr[Y]<520:
            pr[DOUBLE]=False
    if keys[K_s]:
        newMove=0
        pr[Y]+=10
    if keys[K_a] and pr[X]>=0:#go left
        if pr[Y]<520:
            newMove=4
        else:
            newMove=1
        pr[X]-=6
        keyboard2.append("left")#facing left
        if keys[K_s]:
            pr[Y]+=6
        if keys[K_c] and rapid==maxrapid:
            newMove=6
            rapid=0#make melee rapid 0
    elif keys[K_d] and pr[X]<=986:#go right
        if pr[Y]<520:
            newMove=5
        else:
            newMove=2
        pr[X]+=6
        keyboard2.append("right")#facing right
        if keys[K_s]:
            pr[Y]+=6
        if keys[K_c] and rapid==maxrapid:
            newMove=7
            rapid=0#make melee rapid 0
    elif keys[K_c] and rapid==maxrapid:   
        if keyboard2[-1]=="left":
            newMove=6
        elif keyboard2[-1]=="right":
            newMove=7
        rapid=0#make melee rapid 0
    else:
        frame2=0 #0 is the "idle" frame (standing pose)
        
    if keys[K_v]:#ranged
        if cha=="robot":
            MAXRAPID2=24#maxrapid for robot
            if rapid2==MAXRAPID2:#player can shoot
                rapid2=0#make shooting rapid 0
                if keyboard2[-1]=="left":#facing left
                    bullets2.append([pr[X]+5,pr[Y]+25,v[0],v[1],keyboard2[-1]])#append bullet to bullets list
                if keyboard2[-1]=="right":#facing right
                    bullets2.append([pr[X]+50,pr[Y]+25,v[0],v[1],keyboard2[-1]])#append bullet to bullets list
        if cha=="mcman":
            MAXRAPID2=12#maxrapid for mcman
            if rapid2==MAXRAPID2:#player can shoot
                rapid2=0#make shooting rapid 0
                if keyboard2[-1]=="left":#facing left
                    bullets2.append([pr[X]-15,pr[Y]+32,v[0],v[1],keyboard2[-1]])#append bullet to bullets list
                if keyboard2[-1]=="right":#facing right
                    bullets2.append([pr[X]+60,pr[Y]+32,v[0],v[1],keyboard2[-1]])#append bullet to bullets list
        if cha=="recyclebin":
            MAXRAPID2=8#maxrapid for recyclebin
            if rapid2==MAXRAPID2:#player can shoot
                rapid2=0#make shooting rapid 0
                if keyboard2[-1]=="left":#facing left
                    bullets2.append([pr[X]+10,pr[Y]+5,v[0],v[1],keyboard2[-1]])#append bullet to bullets list
                if keyboard2[-1]=="right":#facing right
                    bullets2.append([pr[X]+55,pr[Y]+5,v[0],v[1],keyboard2[-1]])#append bullet to bullets list
        
        if cha=="slime":
            MAXRAPID2=3#maxrapid for slime
            if rapid2==MAXRAPID2:#player can shoot
                rapid2=0#make shooting rapid 0
                if keyboard2[-1]=="left":#facing left
                    bullets2.append([pr[X]+10,pr[Y]+35,v[0],v[1],keyboard2[-1]])#append bullet to bullets list
                if keyboard2[-1]=="right":#facing right
                    bullets2.append([pr[X]+60,pr[Y]+35,v[0],v[1],keyboard2[-1]])#append bullet to bullets list
        
        if keyboard2[-1]=="left":
            newMove=8#shooting sprite list for left side
        if keyboard2[-1]=="right":
            newMove=9#shooting sprite list for right side
    if rapid2<MAXRAPID2:
        rapid2+=1#increase rapid for shoothing
    else:
        rapid2-=1#if rapid is bigger than maxrapid decrease rapid


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
    pr[VY]+=0.35
    if move2==newMove:
        frame2=frame2+0.4
        if newMove==6 or newMove==7:# if player is using melee
            frame2+=0.6 #add 0.6 frame so that it can be frame2= 1
        if frame2>=len(pics2[chapos2][move2]):
            frame2=1#restarting at frame 1 (0 - standing 1-5 is walking)
    elif newMove!=-1:#this is the MOMENT we START WALKING
        move2=newMove
        frame2=1
    if rapid<maxrapid:
        rapid+=0.5#increase rapid for melee

def checkHit(bull1,bull2,pr1,pr2,cha1,cha2):
    global health1,health2
    for b in bull1:#player 1's bullets
        if cha1=="robot":#robot
            bulletrect=Rect(b[X],b[Y],16,16)#rect for bullet
            if cha2=="robot":
                inplayer2=Rect(p2[X]+18,p2[Y]+12,27,54)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=16#damage to player2
            if cha2=="mcman":
                inplayer2=Rect(p2[X]+10,p2[Y]+10,50,55)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=16#damage to player2
            if cha2=="recyclebin":
                inplayer2=Rect(p2[X]+5,p2[Y]+10,60,55)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=16#damage to player2
            if cha2=="slime":
                inplayer2=Rect(p2[X],p2[Y]+14,60,53)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=16#damage to player2
        if cha1=="mcman":#mcman
            bulletrect=Rect(b[X],b[Y],16,16)#rect for bullet
            if cha2=="robot":
                inplayer2=Rect(p2[X]+18,p2[Y]+12,27,54)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=8#damage to player2
            if cha2=="mcman":
                inplayer2=Rect(p2[X]+10,p2[Y]+10,50,55)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=8#damage to player2
            if cha2=="recyclebin":
                inplayer2=Rect(p2[X]+5,p2[Y]+10,60,55)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=8#damage to player2
            if cha2=="slime":
                inplayer2=Rect(p2[X],p2[Y]+14,60,53)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=8#damage to player2
        if cha1=="recyclebin":#recyclebin
            bulletrect=Rect(b[X],b[Y]+3,16,10)#rect for bullet
            if cha2=="robot":
                inplayer2=Rect(p2[X]+18,p2[Y]+12,27,54)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=5#damage to player2
            if cha2=="mcman":
                inplayer2=Rect(p2[X]+10,p2[Y]+10,50,55)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=5#damage to player2
            if cha2=="recyclebin":
                inplayer2=Rect(p2[X]+5,p2[Y]+10,60,55)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=5#damage to player2
            if cha2=="slime":
                inplayer2=Rect(p2[X],p2[Y]+14,60,53)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=5#damage to player2
        if cha1=="slime":#slime
            bulletrect=Rect(b[X],b[Y],16,16)#rect for bullet
            if cha2=="robot":
                inplayer2=Rect(p2[X]+18,p2[Y]+12,27,54)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=2#damage to player2
            if cha2=="mcman":
                inplayer2=Rect(p2[X]+10,p2[Y]+10,50,55)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=2#damage to player2
            if cha2=="recyclebin":
                inplayer2=Rect(p2[X]+5,p2[Y]+10,60,55)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=2#damage to player2
            if cha2=="slime":
                inplayer2=Rect(p2[X],p2[Y]+14,60,53)#enemy rect
                if bulletrect.colliderect(inplayer2):#check the bullet hits the enemy
                    bull1.remove(b)#remove the bullet that hit the enemy
                    health2-=2#damage to player2
    for b in bull2:#player 2's bullets
        if cha2=="robot":#robot
            bulletrect=Rect(b[X],b[Y],16,16)#rect for bullet
            if cha1=="robot":
                inplayer1=Rect(p1[X]+18,p1[Y]+12,27,54)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=16#damage to player1
            if cha1=="mcman":
                inplayer1=Rect(p1[X]+10,p1[Y]+10,50,55)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=16#damage to player1
            if cha1=="recyclebin":
                inplayer1=Rect(p1[X]+5,p1[Y]+10,60,55)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=16#damage to player1
            if cha1=="slime":
                inplayer1=Rect(p1[X],p1[Y]+14,60,53)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=16#damage to player1
        if cha2=="mcman":#mcman
            bulletrect=Rect(b[X],b[Y],16,16)#rect for bullet
            if cha1=="robot":
                inplayer1=Rect(p1[X]+18,p1[Y]+12,27,54)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=8#damage to player1
            if cha1=="mcman":
                inplayer1=Rect(p1[X]+10,p1[Y]+10,50,55)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=8#damage to player1
            if cha1=="recyclebin":
                inplayer1=Rect(p1[X]+5,p1[Y]+10,60,55)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=8#damage to player1
            if cha1=="slime":
                inplayer1=Rect(p1[X],p1[Y]+14,60,53)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=8#damage to player1
        if cha2=="recyclebin":#recyclebin
            bulletrect=Rect(b[X],b[Y],16,16)#rect for bullet
            if cha1=="robot":
                inplayer1=Rect(p1[X]+18,p1[Y]+12,27,54)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=5#damage to player1
            if cha1=="mcman":
                inplayer1=Rect(p1[X]+10,p1[Y]+10,50,55)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=5#damage to player1
            if cha1=="recyclebin":
                inplayer1=Rect(p1[X]+5,p1[Y]+10,60,55)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=5#damage to player1
            if cha1=="slime":
                inplayer1=Rect(p1[X],p1[Y]+14,60,53)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=5#damage to player1
        if cha2=="slime":#slime
            bulletrect=Rect(b[X],b[Y],16,16)#rect for bullet
            if cha1=="robot":
                inplayer1=Rect(p1[X]+18,p1[Y]+12,27,54)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=2#damage to player1
            if cha1=="mcman":
                inplayer1=Rect(p1[X]+10,p1[Y]+10,50,55)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=2#damage to player1
            if cha1=="recyclebin":
                inplayer1=Rect(p1[X]+5,p1[Y]+10,60,55)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=2#damage to player1
            if cha1=="slime":
                inplayer1=Rect(p1[X],p1[Y]+14,60,53)#enemy rect
                if bulletrect.colliderect(inplayer1):#check the bullet hits the enemy
                    bull2.remove(b)#remove the bullet that hit the enemy
                    health1-=2#damage to player1
    return health1,health2 #return health1 and health2

maxrapid1=7#melee maxrapid for player 1
rapidmelee1=maxrapid1#melee rapid for player 1
maxrapid2=7#melee maxrapid for player 2
rapidmelee2=maxrapid2#melee rapid for player 2 
def checkHitmelee(pr1,pr2,cha1,cha2):
    global health1,health2,rapidmelee1,rapidmelee2,maxrapid1,maxrapid2
    if cha1=="robot" and frame1!=0:
        if move1==6 :#facing left
            meleerect=Rect(p1[X],p1[Y]+27,20,10)#melee area for robot
            if cha2=="robot":
                inplayer2=Rect(p2[X]+18,p2[Y]+12,27,54)#rect player 2
            elif cha2=="mcman":
                inplayer2=Rect(p2[X]+10,p2[Y]+10,50,55)#rect player 2
            elif cha2=="recyclebin":
                inplayer2=Rect(p2[X]+5,p2[Y]+10,60,55)#rect player 2
            elif cha2=="slime":
                inplayer2=Rect(p2[X]+3,p2[Y]+14,58,53)#rect player 2
            if meleerect.colliderect(inplayer2) and rapidmelee1==maxrapid1:#check the melee hits the player2
                rapidmelee1=0#make melee rapid 0
                health2=health2-5#damage to player2
        if move1==7:#facing right
            meleerect=Rect(p1[X]+44,p1[Y]+27,20,10)#melee area for robot
            if cha2=="robot":
                inplayer2=Rect(p2[X]+18,p2[Y]+12,27,54)#rect player 2
            elif cha2=="mcman":
                inplayer2=Rect(p2[X]+10,p2[Y]+10,50,55)#rect player 2
            elif cha2=="recyclebin":
                inplayer2=Rect(p2[X]+5,p2[Y]+10,60,55)#rect player 2
            elif cha2=="slime":
                inplayer2=Rect(p2[X]+3,p2[Y]+14,58,53) #rect player 2
            if meleerect.colliderect(inplayer2) and rapidmelee1==maxrapid1:#check the melee hits the player2
                rapidmelee1=0#make melee rapid 0
                health2=health2-5#damage to player2
    elif cha1=="mcman" and frame1!=0:
        if move1==6:#facing left
            meleerect=Rect(p1[X]-2,p1[Y]+37,18,10)#melee area for mcman
            if cha2=="robot":
                inplayer2=Rect(p2[X]+18,p2[Y]+12,27,54)#rect player 2
            elif cha2=="mcman":
                inplayer2=Rect(p2[X]+10,p2[Y]+10,50,55)#rect player 2
            elif cha2=="recyclebin":
                inplayer2=Rect(p2[X]+5,p2[Y]+10,60,55)#rect player 2
            elif cha2=="slime":
                inplayer2=Rect(p2[X]+3,p2[Y]+14,58,53)#rect player 2 
            if meleerect.colliderect(inplayer2) and rapidmelee1==maxrapid1:#check the melee hits the player2
                rapidmelee1=0#make melee rapid 0
                health2=health2-5#damage to player2
        if move1==7:#facing right
            meleerect=Rect(p1[X]+49,p1[Y]+37,16,10)#melee area for mcman
            if cha2=="robot":
                inplayer2=Rect(p2[X]+18,p2[Y]+12,27,54)#rect player 2
            elif cha2=="mcman":
                inplayer2=Rect(p2[X]+10,p2[Y]+10,50,55)#rect player 2
            elif cha2=="recyclebin":
                inplayer2=Rect(p2[X]+5,p2[Y]+10,60,55)#rect player 2
            elif cha2=="slime":
                inplayer2=Rect(p2[X]+3,p2[Y]+14,58,53)#rect player 2
            if meleerect.colliderect(inplayer2) and rapidmelee1==maxrapid1:#check the melee hits the player2
                rapidmelee1=0#make melee rapid 0
                health2=health2-5#damage to player2
    elif cha1=="recyclebin" and frame1!=0:
        if move1==6:#facing left
            meleerect=Rect(p1[X],p1[Y]+27,20,10)#melee area for recyclebin
            if cha2=="robot":
                inplayer2=Rect(p2[X]+18,p2[Y]+12,27,54)#rect player 2
            elif cha2=="mcman":
                inplayer2=Rect(p2[X]+10,p2[Y]+10,50,55)#rect player 2
            elif cha2=="recyclebin":
                inplayer2=Rect(p2[X]+5,p2[Y]+10,60,55)#rect player 2
            elif cha2=="slime":
                inplayer2=Rect(p2[X]+3,p2[Y]+14,58,53)#rect player 2  
            if meleerect.colliderect(inplayer2) and rapidmelee1==maxrapid1:#check the melee hits the player2
                rapidmelee1=0#make melee rapid 0
                health2=health2-5#damage to player2
        if move1==7:#facing right
            meleerect=Rect(p1[X]+44,p1[Y]+27,20,10)#melee area for recyclebin
            if cha2=="robot":
                inplayer2=Rect(p2[X]+18,p2[Y]+12,27,54)#rect player 2
            elif cha2=="mcman":
                inplayer2=Rect(p2[X]+10,p2[Y]+10,50,55)#rect player 2
            elif cha2=="recyclebin":
                inplayer2=Rect(p2[X]+5,p2[Y]+10,60,55)#rect player 2
            elif cha2=="slime":
                inplayer2=Rect(p2[X]+3,p2[Y]+14,58,53)#rect player 2 
            if meleerect.colliderect(inplayer2) and rapidmelee1==maxrapid1:#check the melee hits the player2
                rapidmelee1=0#make melee rapid 0
                health2=health2-5#damage to player2
    elif cha1=="slime" and frame1!=0:
        if move1==6:#facing left
            meleerect=Rect(p1[X],p1[Y]+20,20,20)#melee area for slime
            if cha2=="robot":
                inplayer2=Rect(p2[X]+18,p2[Y]+12,27,54)#rect player 2
            elif cha2=="mcman":
                inplayer2=Rect(p2[X]+10,p2[Y]+10,50,55)#rect player 2
            elif cha2=="recyclebin":
                inplayer2=Rect(p2[X]+5,p2[Y]+10,60,55)#rect player 2
            elif cha2=="slime":
                inplayer2=Rect(p2[X]+3,p2[Y]+14,58,53)#rect player 2    
            if meleerect.colliderect(inplayer2) and rapidmelee1==maxrapid1:#check the melee hits the player2
                rapidmelee1=0#make melee rapid 0
                health2=health2-5#damage to player2
        if move1==7:#facing right
            meleerect=Rect(p2[X]+44,p2[Y]+27,18,20)#melee area for slime
            if cha2=="robot":
                inplayer2=Rect(p2[X]+18,p2[Y]+12,27,54)#rect player 2
            elif cha2=="mcman":
                inplayer2=Rect(p2[X]+10,p2[Y]+10,50,55)#rect player 2
            elif cha2=="recyclebin":
                inplayer2=Rect(p2[X]+5,p2[Y]+10,60,55)#rect player 2
            elif cha2=="slime":
                inplayer2=Rect(p2[X]+3,p2[Y]+14,58,53)#rect player 2
            if meleerect.colliderect(inplayer2) and rapidmelee1==maxrapid1:#check the melee hits the player2
                rapidmelee1=0#make melee rapid 0
                health2=health2-5#damage to player2

    if cha2=="robot" and frame2!=0:#robot
        if move2==6 :#facing left
            meleerect=Rect(p2[X],p2[Y]+27,20,10)#melee area for robot
            if cha1=="robot":
                inplayer1=Rect(p1[X]+18,p1[Y]+12,27,54)#rect player 1
            elif cha1=="mcman":
                inplayer1=Rect(p1[X]+10,p1[Y]+10,50,55)#rect player 1
            elif cha1=="recyclebin":
                inplayer1=Rect(p1[X]+5,p1[Y]+10,60,55)#rect player 1
            elif cha1=="slime":
                inplayer1=Rect(p1[X]+3,p1[Y]+14,58,53) #rect player 1
            if meleerect.colliderect(inplayer1) and rapidmelee2==maxrapid2:#check the melee hits the player1
                rapidmelee2=0#make melee rapid 0
                health1=health1-5#damage to player1
        if move2==7 :#facing right
            meleerect=Rect(p2[X]+44,p2[Y]+27,20,10)#melee area for robot
            if cha1=="robot":
                inplayer1=Rect(p1[X]+18,p1[Y]+12,27,54)#rect player 1
            elif cha1=="mcman":
                inplayer1=Rect(p1[X]+10,p1[Y]+10,50,55)#rect player 1
            elif cha1=="recyclebin":
                inplayer1=Rect(p1[X]+5,p1[Y]+10,60,55)#rect player 1
            elif cha1=="slime":
                inplayer1=Rect(p1[X]+3,p1[Y]+14,58,53)#rect player 1
            if meleerect.colliderect(inplayer1) and rapidmelee2==maxrapid2:#check the melee hits the player1
                rapidmelee2=0#make melee rapid 0
                health1=health1-5#damage to player1
    if cha2=="mcman" and frame2!=0:#mcman
        if move2==6:#facing left
            meleerect=Rect(p2[X]-2,p2[Y]+37,18,10)#melee area for mcman
            if cha1=="robot":
                inplayer1=Rect(p1[X]+18,p1[Y]+12,27,54)#rect player 1
            elif cha1=="mcman":
                inplayer1=Rect(p1[X]+10,p1[Y]+10,50,55)#rect player 1
            elif cha1=="recyclebin":
                inplayer1=Rect(p1[X]+5,p1[Y]+10,60,55)#rect player 1
            elif cha1=="slime":
                inplayer1=Rect(p1[X]+3,p1[Y]+14,58,53) #rect player 1 
            if meleerect.colliderect(inplayer1) and rapidmelee2==maxrapid2:#check the melee hits the player1
                rapidmelee2=0#make melee rapid 0
                health1=health1-5#damage to player1
        if move2==7:#facing right
            meleerect=Rect(p2[X]+49,p2[Y]+37,16,10)#melee area for mcman
            if cha1=="robot":
                inplayer1=Rect(p1[X]+18,p1[Y]+12,27,54)#rect player 1
            elif cha1=="mcman":
                inplayer1=Rect(p1[X]+10,p1[Y]+10,50,55)#rect player 1
            elif cha1=="recyclebin":
                inplayer1=Rect(p1[X]+5,p1[Y]+10,60,55)#rect player 1
            elif cha1=="slime":
                inplayer1=Rect(p1[X]+3,p1[Y]+14,58,53)#rect player 1
            if meleerect.colliderect(inplayer1) and rapidmelee2==maxrapid2:#check the melee hits the player1
                rapidmelee2=0#make melee rapid 0
                health1=health1-5#damage to player1
    if cha2=="recyclebin" and frame2!=0:#recyclebin
        if move2==6:#facing left
            meleerect=Rect(p2[X],p2[Y]+27,20,10)#melee area for recyclebin
            if cha1=="robot":
                inplayer1=Rect(p1[X]+18,p1[Y]+12,27,54)#rect player 1
            elif cha1=="mcman":
                inplayer1=Rect(p1[X]+10,p1[Y]+10,50,55)#rect player 1
            elif cha1=="recyclebin":
                inplayer1=Rect(p1[X]+5,p1[Y]+10,60,55)#rect player 1
            elif cha1=="slime":
                inplayer1=Rect(p1[X]+3,p1[Y]+14,58,53) #rect player 1   
            if meleerect.colliderect(inplayer1) and rapidmelee2==maxrapid2:#check the melee hits the player1
                rapidmelee2=0#make melee rapid 0
                health1=health1-5#damage to player1
        if move2==7:#facing right
            meleerect=Rect(p2[X]+44,p2[Y]+27,18,20)#melee area for recyclebin
            if cha1=="robot":
                inplayer1=Rect(p1[X]+18,p1[Y]+12,27,54)#rect player 1
            elif cha1=="mcman":
                inplayer1=Rect(p1[X]+10,p1[Y]+10,50,55)#rect player 1
            elif cha1=="recyclebin":
                inplayer1=Rect(p1[X]+5,p1[Y]+10,60,55)#rect player 1
            elif cha1=="slime":
                inplayer1=Rect(p1[X]+3,p1[Y]+14,58,53)#rect player 1
            if meleerect.colliderect(inplayer1) and rapidmelee2==maxrapid2:#check the melee hits the player1
                rapidmelee2=0#make melee rapid 0
                health1=health1-5#damage to player1
    if cha2=="slime" and frame2!=0:#slime
        if move2==6:#facing left
            meleerect=Rect(p2[X],p2[Y]+20,20,20)#melee area for slime
            if cha1=="robot":
                inplayer1=Rect(p1[X]+18,p1[Y]+12,27,54)#rect player 1
            elif cha1=="mcman":
                inplayer1=Rect(p1[X]+10,p1[Y]+10,50,55)#rect player 1
            elif cha1=="recyclebin":
                inplayer1=Rect(p1[X]+5,p1[Y]+10,60,55)#rect player 1
            elif cha1=="slime":
                inplayer1=Rect(p1[X]+3,p1[Y]+14,58,53)#rect player 1   
            if meleerect.colliderect(inplayer1) and rapidmelee2==maxrapid2:#check the melee hits the player1
                rapidmelee2=0#make melee rapid 0
                health1=health1-5#damage to player1
        if move2==7:#facing right
            meleerect=Rect(p2[X]+44,p2[Y]+27,20,10)#melee area for slime
            if cha1=="robot":
                inplayer1=Rect(p1[X]+18,p1[Y]+12,27,54)#rect player 1
            elif cha1=="mcman":
                inplayer1=Rect(p1[X]+10,p1[Y]+10,50,55)#rect player 1
            elif cha1=="recyclebin":
                inplayer1=Rect(p1[X]+5,p1[Y]+10,60,55)#rect player 1
            elif cha1=="slime":
                inplayer1=Rect(p1[X]+3,p1[Y]+14,58,53)#rect player 1
            if meleerect.colliderect(inplayer1) and rapidmelee2==maxrapid2:#check the melee hits the player1
                rapidmelee2=0#make melee rapid 0
                health1=health1-5#damage to player1
    if rapidmelee1<maxrapid1:
        rapidmelee1+=0.5#increase player 1's melee rapid
    if rapidmelee2<maxrapid2:
        rapidmelee2+=0.5#increase player 2's melee rapid
    
def moveBullets(p1,p2,bull1,bull2):
    for b in bull1:#player 1's bullets
        if b[4]=="right":#player 1bullet move right
            b[0]+=b[2]
            b[1]+=b[3]
        if b[4]=="left":#player 1 bullet move left
            b[0]-=b[2]
            b[1]-=b[3]
        
        if b[0]<0 or b[0]>1024:
            bull1.remove(b)
    for b in bull2:#player 2's bullets
        if b[4]=="right":#player 2 bullet move right
            b[0]+=b[2]
            b[1]+=b[3]
        if b[4]=="left":#player 2 bullet move left
            b[0]-=b[2]
            b[1]-=b[3]
            
        if b[0]<0 or b[0]>1024:
            bull2.remove(b)
          
def addPics(name,start,end):#for adding picture to the movement list
    mypic=[]
    for i in range(start,end+1):
        mypic.append(image.load("%s%03d.png"%(name,i)))
    return mypic
#making picture list for each character movement
#robot picture list
robotpics=[]
robotpics.append(addPics("robotIdle",0,1))#forward
robotpics.append(addPics("robotWalkL",0,11))#left
robotpics.append(addPics("robotWalkR",0,11))#right (needs fixing, how do i add numbers)
robotpics.append(addPics("robotIdle",5,6))#jump
robotpics.append(addPics("robotIdle",7,8))#jump left
robotpics.append(addPics("robotIdle",9,10))#jump right
robotpics.append(addPics("robotMeleeL",0,1))#hit left
robotpics.append(addPics("robotMeleeR",0,1))#hit right
robotpics.append(addPics("robotShootL",0,1))#shoot left
robotpics.append(addPics("robotShootR",0,1))#shoot right
#mcman picture list
mcman=[]
mcman.append(addPics("mcdsIdle",0,1))#forward
mcman.append(addPics("mcdsWalkL",0,11))#left
mcman.append(addPics("mcdsWalkR",0,11))#right
mcman.append(addPics("mcdsJumpF",3,4))#jump 
mcman.append(addPics("mcdsJumpL",0,5))#jump left
mcman.append(addPics("mcdsJumpR",0,5))#jump right
mcman.append(addPics("mcdsMeleeL",0,1))#hit left
mcman.append(addPics("mcdsMeleeR",0,1))#hit right
mcman.append(addPics("mcdsShootL",0,1))#shoot left
mcman.append(addPics("mcdsShootR",0,1))#shoot right
#recyclebin picture list
recyclebin=[]
recyclebin.append(addPics("binIdleF",0,1))#forward
recyclebin.append(addPics("binWalkL",0,11))#left
recyclebin.append(addPics("binWalkR",0,11))#right
recyclebin.append(addPics("binJumpF",2,3))#jump
recyclebin.append(addPics("binJumpL",2,3))#jump left
recyclebin.append(addPics("binJumpR",2,3))#jump right
recyclebin.append(addPics("binMeleeL",0,1))#hit left
recyclebin.append(addPics("binMeleeR",0,1))#hit right
recyclebin.append(addPics("binShootL",0,1))#shoot left
recyclebin.append(addPics("binShootR",0,1))#shoot right
#slime picture list
slime=[]
slime.append(addPics("slimeIdleF",0,1))#forward
slime.append(addPics("slimeWalkL",0,5))#left
slime.append(addPics("slimeWalkR",0,5))#right
slime.append(addPics("slimeJumpF",2,3))#jump
slime.append(addPics("slimeJumpL",0,5))#jump left
slime.append(addPics("slimeJumpR",0,5))#jump left
slime.append(addPics("slimeMeleeL",0,1))#hit left
slime.append(addPics("slimeMeleeR",0,1))#hit right
slime.append(addPics("slimeShootL",0,1))#shoot left
slime.append(addPics("slimeShootR",0,1))#shoot right
pics1=[robotpics,mcman,recyclebin,slime]#pics list for player1
pics2=[robotpics,mcman,recyclebin,slime]#pics list for player2

charlist=["robot","mcman","recyclebin","slime"]#characters list


def game():
    running = True
    global chapos1,chapos2,health1,health2,frame1,move1,frame2,move2,bullets1,bullets2,keyboard1,keyboard2,p1,p2,pos
    #######make all the values to the beginning
    frame1=0
    move1=0
    frame2=0
    move2=0
    health1=100
    health2=100
    bullets1=[]
    bullets2=[]
    keyboard1=["left"]
    keyboard2=["right"]
    p1=[600,520,0,True,True,True]
    p2=[300,520,0,True,True,True]
    #######
    mixer.music.load(mapmusic[mapPos])#load music for the map
    mixer.music.play(-1)#play music
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False
        keys=key.get_pressed()
        moveGuy1(p1,charlist[chapos1])########
        moveGuy2(p2,charlist[chapos2])########
        
        #               player1 piclist  player2 piclist health1, health2
        drawScene(screen,pics1[chapos1],pics2[chapos2],health1,health2,bullets1,bullets2)#draw the scene
        moveBullets(p1,p2,bullets1,bullets2)#move bullets
        checkHit(bullets1,bullets2,p1,p2,charlist[chapos1],charlist[chapos2])#check bullets hit
        checkHitmelee(p1,p2,charlist[chapos1],charlist[chapos2])#check melee hit
        if health1<=0:
            return end("player2")#player 2 win
        if health2<=0:
            return end("player1")#player 1 win
        myClock.tick(60)
        if keys[K_m]:
            mixer.music.pause()#pause music
        if keys[K_SPACE]:
            mixer.music.unpause()#unpause music
    return "select"#go back to select page


running=True                                 
page = "menu"
while page != "exit":
    if page == "menu":
        page = menu()#menu page
    if page == "game":
        page = game()#game page
    if page == "instructions":
        page = instructions()#instruction page     
    if page == "credits":
        page = credit()#credit page
    if page == "select":
        page = select()#select page

quit()
