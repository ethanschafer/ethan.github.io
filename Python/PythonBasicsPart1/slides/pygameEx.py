# all imports go at the top
import pygame, sys
from pygame.locals import *
from graphics import *

# create the screen
pygame.init()
screen = pygame.display.set_mode((800,600))


# Colors the screen white
screen.fill((255,255,255))


# Calls the method draw scene and sends it the screen to draw on
drawScene(screen)

# Updates the display
pygame.display.update()

while True:
    
    for event in pygame.event.get():
        # Check the if the user closed the window or pressed escape
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            # End the program
            pygame.quit()
            sys.exit()
            
