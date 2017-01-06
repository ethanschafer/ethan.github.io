import pygame
from pygame.locals import *
from tkinter import*
import random

class Pyramid:
    def __init__ (self, newX, newY):
        self.x = newX
        self.y = newY
        self.img = pygame.image.load("images/Pyramid.png")
        myRec = self.getRec()
        self.width = myRec[2]
        self.height = myRec[3]
        
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
    def interact(self):
        pass
class Base:
    def __init__ (self, newX, newY):
        self.x = newX
        self.y = newY
        self.img = pygame.image.load("images/PyramidBase.png")
        myRec = self.getRec()
        self.width = myRec[2]
        self.height = myRec[3]
        
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
    def interact(self,guy,grass):
        reply=simpledialog.askfloat("Pyramid of Wealth","1-Increase Coin Drop Rate (1 per "+str(round(guy.cinterval/1000,3))+" seconds -> 1 per "+str(round(guy.cinterval*0.9/1000,3))+
                                    " seconds)\nPrice: 10 coins\n2-Increase maximum coins ("+str(guy.maxcs)+" coins ->"+str(guy.maxcs+1)+" coins)\nPrice: 5 coins")
        if reply==1:
            if guy.cs>=10:
                guy.cs-=10
                guy.cinterval=guy.cinterval*0.9
            else:
                messagebox.showinfo("Dialougue Box","You can't afford that.")
            self.interact(guy,grass)
        elif reply==2:
            if guy.cs>=5:
                guy.cs-=5
                guy.maxcs+=1
            else:
                messagebox.showinfo("Dialougue Box","You can't afford that.")
            self.interact(guy,grass)
        elif reply==None:
            pass
        else:
            messagebox.showinfo("Dialougue Box","Invalid Reply.")
            self.interact(guy,grass)
        
