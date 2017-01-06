import pygame
from pygame.locals import *

class Enemy:
    def __init__ (self, newX, newY):
        self.x = newX
        self.y = newY
        self.direction=1
        self.img = pygame.image.load("Images/Enemy.png")
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
    def moveLeft(self):
        self.x=self.x-5
    def moveRight(self):
        self.x=self.x+5
    def moveUp(self):
        self.y=self.y-5
    def moveDown(self):
        self.y=self.y+5
    def tick(self):
        self.x+=3*self.direction
        if self.x<0:
            self.direction=1
        if self.x>800-52:
            self.direction=-1
