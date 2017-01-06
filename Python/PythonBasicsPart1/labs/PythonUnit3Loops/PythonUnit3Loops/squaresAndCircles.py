import pygame
from pygame.locals import *

def drawSquares(window):
    # Create variables to keep track of size and position
    x = 0
    y = 0
    width = 100
    height = 100
    
    # Use a loop to draw squares until the size is too small
    for num in range(10):
        pygame.draw.rect(window, (0,0,255), (x,y,width,height))

        width -= 10
        x += width + 20
        y += 10
        height -= 10
    
        
        
def drawCircles(window):
    # Create variables to keep track of size, position and color
    x = 300
    y = 300
    radius = 100
    green = 255
    
    # Use a loop to draw circles until the size is too small
    for num in range(10):
        pygame.draw.circle(window, (0,green,0), (x,y), radius)

        radius -= 10
        green -= 25

    pass
