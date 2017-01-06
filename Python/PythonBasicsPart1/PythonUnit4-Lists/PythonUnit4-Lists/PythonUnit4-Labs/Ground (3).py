import pygame, random
from pygame.locals import *

def drawGround(window):
    # load all images into a list 
    bgImages = [ "grass.gif", "road.gif", "gtoroad.gif", "rtograss.gif"]
    
    # Create variables to keep track of where to
    # draw the grass
    bg = 0
    x = 0
    y = 0
    
    # Outer loop runs as long as x is 
    # not past the right edge of the screen
    while x < 800:  
        
        # Inner loop runs as long as y is 
        # not past the bottom edge of the screen
        while y < 600:
            # Use the y position to determine which tile to draw
            # Increase the y
            if y == 150:
                bg = 2
            elif y > 150 and y < 450:
                bg = 1
            elif y == 450:
                bg = 3
            else:
                bg = 0

            #draw bg
            window.blit( pygame.image.load( bgImages[ bg ] ),
                         (x,y) )
            y += 50
            
        # Increase the x and reset the y
        x += 50
        y = 0

    
