import pygame
from pygame.locals import *
from Enemy import *
from Blast import *
from Boss import *

class Enemies:
    def __init__ (self):
        self.enemies=[]
        self.blasts=[]
    def draw(self, window):
        i=0
        while i<len(self.enemies):
            self.enemies[i].draw(window)
            i+=1
        i=0
        while i<len(self.blasts):
            self.blasts[i].draw(window)
            i+=1
    def addNew(self,x,y):
        self.enemies.append(Enemy(x,y))
    def addBoss(self,x,y):
        self.enemies.append(Boss(x,y))
    def addBlast(self,x,y):
        self.blasts.append(Blast(x,y))
    def tick(self):
        i=0
        while i<len(self.enemies):
            self.enemies[i].tick()
            if self.enemies[i].y<0:
                self.enemies.pop(i)
            i+=1
        i=0
        while i<len(self.blasts):
            self.blasts[i].tick()
            if self.blasts[i].y>600:
                self.blasts.pop(i)
            i+=1
    
