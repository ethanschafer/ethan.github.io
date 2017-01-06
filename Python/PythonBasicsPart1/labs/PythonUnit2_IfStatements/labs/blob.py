import pygame
from pygame.locals import *




class blob:
    # set all class variables in the constructor
    def __init__(self, newX, newY):
        self.img = pygame.image.load("blob.gif")
        self.x = newX
        self.y = newY
        
    # draw your image
    def draw(self, window):
        window.blit( self.img, (self.x ,self.y) )
        
    def moveLeft(self):
        # Change x so that the object can move left
        self.x = self.x - 1
        #self.x -= 1
    
    




    def moveRight(self):
        # Change x so that the object can move right
        if self.x > 0:
            self.x = self.x + 1
    
       




    def moveUp(self):
        # Change y so that the object can move up
        if self.y > 0:
            self.y = self.y - 1




    
    def moveDown(self):
        # Change y so that the object can move down
        if self.y < 550:
            self.y = self.y + 1
    
    
   # This will be filled out in the collide lab. 
    # It will return True if your person has 
    # collided with another object
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
        elif(self.x + (myWidth-3)) < otherX:
            return False 
        
        # elif person is above the object
            # person and object do not intersect
        elif(self.y + myHeight) < otherY:
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



