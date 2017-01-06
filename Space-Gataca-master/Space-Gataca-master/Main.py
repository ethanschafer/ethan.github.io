
import pygame,sys,math
from pygame.locals import *
from Ship import *
from Bullets import *
from Bullet import *
from Enemies import *
from Enemy import *

pygame.init()
pygame.key.set_repeat(1,1)
screen = pygame.display.set_mode((800,600))
background = pygame.Surface((800,600))
ground=pygame.image.load("Images/Background.png")

wait=False

ship = Ship(100,450)
bullets= Bullets()
lastShootTime=pygame.time.get_ticks()
lastEnemyShoot=500

def update():
    screen.blit(background,(0,0))
    screen.blit(ground,(0,0))
    ship.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)
    screen.fill((100,100,100),Rect(0,550,800,50))

level=0
waitTime=pygame.time.get_ticks()

enemies=Enemies()
pause=False
font = pygame.font.Font(None, 50)

while True:# Game loop
  if pause==False:
    update()
    if level==6:
            
            text=font.render("You Win!", 1, (255, 255, 0))
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
                ship.moveUp()
            elif event.key==K_DOWN:
                ship.moveDown()
            elif event.key==K_LEFT:
                ship.moveLeft()
            elif event.key==K_RIGHT:
                ship.moveRight()
            elif event.key==K_SPACE:
                #bullets.addNew(ship.x,ship.y)
                if pygame.time.get_ticks()>lastShootTime+500 and wait==False:
                    bullets.addNew(ship.x+34,ship.y-30)
                    lastShootTime=pygame.time.get_ticks()
            elif event.key==K_m and len(enemies.enemies)>0:
                
                enemies.enemies.pop(0)
                pygame.time.wait(100)
            elif event.key==K_p:
                text=font.render("Paused", 1, (255, 255, 0))
                textpos = text.get_rect()
                textpos.centerx = 400
                screen.blit(text, textpos)
                pygame.display.update()
                pause=True
                
    if pygame.time.get_ticks()>lastEnemyShoot+500:
            i=0
            while i<len(enemies.enemies):
                if enemies.enemies[i].__class__.__name__=="Boss":
                    enemies.addBlast(enemies.enemies[i].x+50,enemies.enemies[i].y+100)
                    enemies.addBlast(enemies.enemies[i].x+164,enemies.enemies[i].y+100)
                    enemies.addBlast(enemies.enemies[i].x+214,enemies.enemies[i].y+100)
                else:
                    enemies.addBlast(enemies.enemies[i].x,enemies.enemies[i].y)
                i+=1
                
                
            lastEnemyShoot=pygame.time.get_ticks()
    bullets.tick()
    enemies.tick()
    if len(enemies.enemies)==0:
        if wait==False:
            wait=True
            waitTime=pygame.time.get_ticks()
    if len(enemies.enemies)==0 and level<=5 and pygame.time.get_ticks()>=waitTime+3000:
        wait=False
        level+=1
        if level==1:
            enemies.addNew(100,100)
            enemies.addNew(200,100)
        elif level==2:
            enemies.addNew(0,100)
            enemies.addNew(375,100)
            enemies.addNew(740,100)
        elif level==3:
            enemies.addNew(200,100)
            enemies.addNew(600,100)
            enemies.addNew(300,200)
            enemies.addNew(700,200)
        elif level==4:
            enemies.addNew(200,100)
            enemies.addNew(600,100)
            enemies.addNew(300,200)
            enemies.addNew(700,200)
            enemies.addNew(400,150)
        elif level==5:
            enemies.addBoss(300,30)
        if level<6:
        
            update()
            text=font.render("Level "+str(level), 1, (255, 255, 0))
            textpos = text.get_rect()
            textpos.centerx = 400
            screen.blit(text, textpos)
            pygame.display.update()
            pygame.time.wait(3000)

    pygame.time.wait(10)
  else:
      for event in pygame.event.get():
        if event.type==KEYDOWN:
          if event.key==K_p:
                pause=False
