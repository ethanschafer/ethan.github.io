import pygame, random
from pygame.locals import *

class Ground:
    # Load grass.gif and rock.gif into variables
    def __init__(self):
        self.grass = pygame.image.load("grass.gif")
        self.rock = pygame.image.load("rock.gif")
    
    # draw the grass and rocks
    def draw(self, window):
        # Create variables to keep track of where to
        # draw the grass
        xPos = 0
        yPos = 0
        # Outer loop runs as long as x is 
        # not past the right edge of the screen
        while  xPos < 800:
            
            # Inner loop runs as long as y is 
            # not past the bottom edge of the screen
            while  yPos < 600:
                # Draw the grass and increase the y
                window.blit(self.grass, (xPos,yPos))
                yPos += 50
             
            # Increase the x and reset the y
            xPos += 50
            yPos = 0
        
        # Draw 30 rocks in random x and y positions
        for numRocks in range( 30 ):
            x = random.randint( 0,790 )
            y = random.randint(0,590)
            window.blit(self.rock, ( x,y ) )



