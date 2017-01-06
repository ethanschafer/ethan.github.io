import pygame
from pygame.locals import *
from Bullet import *

class Bullets:
    def __init__ (self):
        self.bullets=[]
    def draw(self, window):
        i=0
        while i<len(self.bullets):
            self.bullets[i].draw(window)
            i+=1
    def addNew(self,x,y):
        self.bullets.append(Bullet(x,y))
    def tick(self):
        i=0
        while i<len(self.bullets):
            self.bullets[i].tick()
            if self.bullets[i].y<0:
                self.bullets.pop(i)
            i+=1
    
