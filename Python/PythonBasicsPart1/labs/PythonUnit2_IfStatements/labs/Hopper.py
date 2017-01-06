import pygame
from pygame.locals import *

class Hopper:
    # initialize all variables
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        self.up = False
        self.upCounter = 0
        self.img = pygame.image.load("dudeR.gif")
    
    # draw hopper
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
        
        
    # move left unless you hit the edge
    def moveLeft(self):
        if self.x > 0:
            self.x = self.x - 10
        
    # move left unless you hit the edge 
    def moveRight(self):
        if self.x < 755:
            self.x = self.x + 10
    
    # set the up variable to True
    def moveUp(self):
        if self.y > 200:
            self.up = True
        
    # updates to upCounter and sets the up variable to
    # false if upCounter has reached it's limit
    # moves hopper up or down
    def update(self):
        # if up is true
        if self.up == True:
            # move hopper up
            self.y = self.y - 15
            # increase upCounter
            self.upCounter += 1
            #self.upCounter  = self.upCounter  + 1
            
            # if hopper has moved up a number of times
            if self.upCounter > 7:
                # set up to false
                self.up = False

        # else if upCounter is greater than 0
        elif self.upCounter > 0:
            # move hopper down
            self.y = self.y + 15
            # decrease upCounter
            self.upCounter -= 1 
        
    
    
    # determine if hopper has collided with an object 
    def collide(self, other):
        # Get other's x, y, width and height
        otherRec = other.getRec()
        otherX = otherRec[0]
        otherY = otherRec[1]
        otherWidth = otherRec[2]
        otherHeight = otherRec[3]

        # Get person's width and height
        myRec = self.getRec()
        myWidth = myRec[2]
        myHeight = myRec[3]

        
        # if person is right of the object - self.x greater than (otherX + otherWidth)
            # person and object do not intersect
        if self.x > (otherX + otherWidth):
            return False
        
        # elif person is left of the object - (self.x + width) less than otherX
            # person and object do not intersect
        elif (self.x + (myWidth-3)) < otherX:
            return False
        
        # elif person is above the object
            # person and object do not intersect
        elif (self.y + myHeight) < otherY:
            return False
        
        # elif person is below the object
            # person and object do not intersect
        elif self.y > (otherY + otherHeight):
            return False
        
        # else
            # person and object do intersect
        else:
            return True
        
        return False

    
    # DO NOT CHANGE THIS
    # This method returns a rectangle - (x, y, width, height) - that represents
    # the object
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
