import pygame
from pygame.locals import *

class Coin:

    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        self.img = pygame.image.load("images/money.png")
        

    def draw(self, window):
        window.blit(self.img, (self.x,self.y))

    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
