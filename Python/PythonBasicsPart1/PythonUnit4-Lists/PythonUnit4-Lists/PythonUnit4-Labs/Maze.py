import pygame, sys
from pygame.locals import *
from wall import *

class Maze:
    def __init__(self):
       self.M = 10
       self.N = 8
       self.maze = [ 1,1,1,1,1,1,1,1,1,1,
                             1,0,0,0,0,0,0,0,0,1,
                             1,0,0,0,0,0,0,0,0,1,
                             1,0,1,1,1,1,1,1,0,1,
                             1,0,1,0,0,0,0,0,0,1,
                             1,0,1,0,1,1,1,1,0,1,
                             1,0,0,0,0,0,0,0,0,1,
                             1,1,1,1,1,1,1,1,1,1,]
       self.walls = []
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           if self.maze[ bx + (by*self.M) ] == 0:
               newWall = Wall( bx * 50 , by * 50)
               self.walls.append(newWall)
               
           bx = bx + 1
           if bx > self.M-1:
               bx = 0 
               by = by + 1
 
    def draw(self,window):
        for w in self.walls:
            w.draw(window)

        
    def collide(self, guy):
        for w in self.walls:
            if guy.collide(w):
                return True

        return False
