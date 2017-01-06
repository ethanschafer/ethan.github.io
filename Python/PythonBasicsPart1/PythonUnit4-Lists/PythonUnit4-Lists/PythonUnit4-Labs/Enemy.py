import pygame
from pygame.locals import *

class Enemy:
    # Creates a enemy at (newX, newY) that moves speed steps at a time
    def __init__(self, newX, newY, speed):
        self.x = newX
        self.y = newY
        self.steps = speed
        self.img = pygame.image.load("enemy.gif").convert()
        
    # Draw the enemy on window
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
        
    # Move the enemy
    def move(self):
        self.x += self.steps

    # Get a rectangle that represents the enemy
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
