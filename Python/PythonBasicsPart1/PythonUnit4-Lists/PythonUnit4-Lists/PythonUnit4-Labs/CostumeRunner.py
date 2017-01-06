import pygame, sys
from pygame.locals import *
from Person import *
from Bob import *
from Maze import *

# Initialize the screen
pygame.init()
screen = pygame.display.set_mode((800,600))

# allows user to hold down the key to move
pygame.key.set_repeat(1, 1)


# create a person named guy
guy = Person(0,0)
bob = Bob(200,200)
room = Maze()

#draw the starting screen
WHITE = (255,255,255)
screen.fill(WHITE)
room.draw(screen)
pygame.display.update()


#Event Loop
while True:
    # draw the scene
    screen.fill((255,255,255))
    room.draw(screen)
    guy.draw(screen)
    #bob.draw(screen)
    
       
    
    #update only the changed areas of the screen
    pygame.display.update()

    # check for events
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
            
        elif event.type==KEYDOWN:
            
            if event.key==K_UP:
                guy.moveUp()
                if room.collide(guy):
                    guy.moveDown()
                

            elif event.key==K_DOWN:
                guy.moveDown()
                if room.collide(guy):
                    guy.moveUp()
                

            elif event.key==K_LEFT:
                guy.moveLeft()
                if room.collide(guy):
                    guy.moveRight()
                

            elif event.key==K_RIGHT:
                guy.moveRight()
                if room.collide(guy):
                    guy.moveLeft()
                

##            if event.key==K_w: 
##                bob.moveUp()
##
##            elif event.key==K_s:
##                bob.moveDown()
##
##            elif event.key==K_a:
##                bob.moveLeft()
##
##            elif event.key==K_d:
##                bob.moveRight()

            
