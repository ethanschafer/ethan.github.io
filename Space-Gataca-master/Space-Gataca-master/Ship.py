import pygame
from pygame.locals import *

class Ship:
    def __init__ (self, newX, newY):
        self.x = newX
		
        self.y = newY
		
        self.img = pygame.image.load("Images/Ship.png")
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
        #pygame.draw.rect(window,Color(Red),300,10)
    def moveLeft(self):
        if self.x>0:
            self.x=self.x-5
    def moveRight(self):
        if self.x<720:
            self.x=self.x+5
    def moveUp(self):
        if self.y>0:
            self.y=self.y-5
    def moveDown(self):
        if self.y<520:
            self.y=self.y+5
    def collide(self, other):        
        otherRec = other.getRec()
        otherX = otherRec[0]
        otherY = otherRec[1]
        otherWidth = otherRec[2]
        otherHeight = otherRec[3]
        myRec = self.getRec()        
        width = myRec[0] + myRec[2] 
        height = myRec[1] + myRec[3]                
        if self.x > (otherX + otherWidth):
            return False               
        elif width < otherX:
            return False                         
        elif self.y > (otherY + otherHeight):
            return False                         
        elif height < otherY:
            return False 
        else:
            return True
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
