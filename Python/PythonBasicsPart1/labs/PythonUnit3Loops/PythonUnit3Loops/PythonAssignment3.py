import pygame, sys
from pygame.locals import *
from ground import *
from Person import * 

# Create a screen that is 800 by 600 pixels
pygame.init()
screen = pygame.display.set_mode((800,600))
guy = Person(200,200)
background = pygame.Surface((800,600))

# Create and draw the ground
grass = Ground()
grass.draw(background)

score = 0
gameEnd = False
gameWin = False

#display the background
screen.blit(background,(0,0))
guy.draw(screen)
pygame.display.update()


# Event loop that runs until you exit
while True:
    font = pygame.font.Font(None,30)
    if gameEnd == True:
        text = font.render("Game Over!", 1,(10,10,10))
    elif gameWin == True:
        text = font.render("You Win!", 1,(10,10,10))
    else:
        text = font.render("Score:"+str(score),1(10,10,10))

    textpos = text.get_rect()
    textpos.centerx = 400
    screen.blit(text,textpos)


    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
