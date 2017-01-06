import pygame, sys
from pygame.locals import *
from Person import *

# Creates the screen to draw on
pygame.init()
screen = pygame.display.set_mode((800,600))

# Allows a key that is held down to count as multiple presses
pygame.key.set_repeat(1,1)

# Creates a Person object named guy
guy = Person(50,50)

# Event Loop
while True:
    # Colors the screen white
    screen.fill((255,255,255))
    
    # Draw your person on the screen
    guy.draw(screen)
    
    # Update the screen
    pygame.display.update()


    # Check for key presses and mouse clicks
    for event in pygame.event.get():
        # Determine if the user has closed the window or pressed escape
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            # Quit the program
            pygame.quit()
            sys.exit()
        
        # Check if an arrow key is pressed and 
        # move guy in the correct direction
        elif event.type==KEYDOWN:

            if event.key==K_UP: 
                guy.moveUp()

            elif event.key==K_DOWN:
                guy.moveDown()

            elif event.key==K_LEFT:
                guy.moveLeft()

            elif event.key==K_RIGHT:
                guy.moveRight()
