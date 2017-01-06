import pygame, sys, math
from pygame.locals import *
from Ground import *
from Person import *
import random
from Coins import *
from tkinter import*
from OldMan import *
from Clerk import*
from Pyramid import*
from Item import*
from Runner import*
from Collector import*
pygame.init()
pygame.key.set_repeat(1,1)
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((800,600))
background = pygame.Surface((800,600))
points=0
timeleft=60
maxcoins=5
ctime=0
defeat=False
victory=False
grass = Ground()
grass.draw(background)
money=Coins()
changedrecs = []
guy = Person(50,50)
guy.cinterval=5000
guy.cs=0
guy.maxcs=5
pyramid=Pyramid(650,30)
pbase=Base(650,88)
#oldman= OldMan(random.randint(0,783),random.randint(0,577))
oldman = OldMan(100,200)
clerk = Clerk(200,100)
collector= Collector(200,200)
runner= Runner(400,400)
font = pygame.font.Font(None, 36)
text = font.render("Money: "+str(guy.cs), 1, (10, 10, 10))
peoplelist=[oldman,clerk,collector,runner]
blist=[pbase]
while True:
    grass.draw(background)
    screen.blit(background,(0,0))
    guy.draw(screen)
    runner.move()
    money.drawAndCollision(screen, guy, changedrecs)
    if len(money.cs)<guy.maxcs:
        curtime=pygame.time.get_ticks()
        if ctime==0:
            ctime=pygame.time.get_ticks()
        elif ctime!=0 and curtime-ctime>=guy.cinterval:
            money.addCoin(random.randint(0,769),random.randint(100,579))
            ctime=0
    font = pygame.font.Font(None, 36)
    for i in range(len(blist)):
        blist[i].draw(screen)
        if guy.collide(blist[i]):
            guy.back()
    pyramid.draw(screen)
    for i in range(len(peoplelist)):
        peoplelist[i].draw(screen)
        if guy.collide(peoplelist[i]):
            guy.back()
    for i in range(len(guy.placed)):
        guy.placed[i].draw(screen)
        if guy.collide(guy.placed[i]):
            guy.back()
    text=font.render("Money: "+str(guy.cs), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = 400
    screen.blit(text, textpos)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN:
            if event.key==K_UP:
                guy.moveUp()
            elif event.key==K_DOWN:
                guy.moveDown()
            elif event.key==K_LEFT:
                guy.moveLeft()
            elif event.key==K_m:
                guy.cs+=15
            elif event.key==K_RIGHT:
                guy.moveRight()
            elif event.key==K_s:
                guy.showskins()
            elif event.key==K_g:
                guy.showbgs(grass)
            elif event.key==K_p:
                guy.tryplace()
            elif event.key==K_o:
                guy.changespeed()
            elif event.key==K_SPACE:
                for i in range(len(peoplelist)):
                    #print(math.sqrt(math.pow(guy.x-peoplelist[i].x,2)+math.pow(guy.y-peoplelist[i].y,2)))
                    if math.sqrt(math.pow(guy.x-peoplelist[i].x,2)+math.pow(guy.y-peoplelist[i].y,2))<=35:
                        guy.dirchange(peoplelist[i])
                        peoplelist[i].draw(screen)
                        pygame.display.update()
                        peoplelist[i].interact(guy,grass)
                for i in range(len(blist)):
                    if math.sqrt(math.pow(guy.x-blist[i].x,2)+math.pow(guy.y-blist[i].y,2))<=35:
                        blist[i].interact(guy,grass)
                for i in range(len(guy.placed)):
                    if math.sqrt(math.pow(guy.x-guy.placed[i].x,2)+math.pow(guy.y-guy.placed[i].y,2))<=35:
                        guy.placed[i].interact(guy)
    
    pygame.time.wait(int(round(guy.gamespeed,0)))
