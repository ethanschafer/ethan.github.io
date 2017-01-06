import pygame, random
from pygame.locals import *
class Ground:
    def __init__(self):
        self.grasses=["images/ground/grass.png"]
        self.rx=[]
        self.ry=[]
        self.drawn=0
        self.grassy=0
        self.grsls=["Default"]
        self.grass = pygame.image.load(self.grasses[self.grassy])
        self.rock = pygame.image.load("images/ground/rock.gif")
    def draw(self, window):
        grassX = 0
        grassY = 0
        self.grass = pygame.image.load(self.grasses[self.grassy])
        for col in range(40):
            for row in range(30):
                window.blit(self.grass, (grassX, grassY))
                grassY += 50
            grassX += 50
            grassY = 0
        if self.drawn==0:
            for numRocks in range(30):
                rockX = random.randint(0,777)
                self.rx.append(rockX)
                rockY = random.randint(0,587)
                self.ry.append(rockY)
                window.blit(self.rock, (rockX, rockY))
                self.drawn=1
        else:
            for numRocks in range(30):
                window.blit(self.rock, (self.rx[numRocks],self.ry[numRocks]))
    def changeB(self):
        self.grassy=(self.grassy+1)%len(self.grasses)
        #print (self.grassy)
    #def moveCam(guy):
            #this will be for later, too complicated for now







        
