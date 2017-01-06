import pygame, sys
from pygame.locals import *
from Ground import *
from Person import *

# Initialize the screen
pygame.init()
screen = pygame.display.set_mode((800,600))


# draw the ground
background = pygame.Surface((800,600))

drawGround(background)
screen.blit(background, (0,0))

# Check if a key is still pressed down every 100 milliseconds
# allows user to hold down the key to move
pygame.key.set_repeat(1, 1)


# create a person at position (400, 50)
guy = Person(400, 50)



#draw the starting screen
pygame.display.update()

while True:
    # draw the scene
    screen.blit(background, (0,0))
    
    guy.draw(screen)
    
    
    #update only the changed areas of the screen
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

            elif event.key==K_RIGHT:
                guy.moveRight()

                    
    pygame.time.wait(1)
