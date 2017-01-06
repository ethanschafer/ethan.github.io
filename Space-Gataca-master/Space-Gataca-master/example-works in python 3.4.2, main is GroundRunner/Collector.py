import pygame
from pygame.locals import *
from tkinter import*
import random
class Collector:
    def __init__ (self, newX, newY):
        self.x = newX
        self.y = newY
        self.img = pygame.image.load("images/Collector/D.png")
        self.direction="d"
        myRec = self.getRec()
        self.width = myRec[2]
        self.height = myRec[3]
        self.price=0
        self.buying=""
        self.offered=False
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
    def face(self,dir):
        if dir=="l":
            self.img = pygame.image.load("images/Collector/L.png")
        if dir=="r":
            self.img = pygame.image.load("images/Collector/R.png")
        if dir=="u":
            self.img = pygame.image.load("images/Collector/U.png")
        if dir=="d":
            self.img = pygame.image.load("images/Collector/D.png")
        self.direction=dir
    def interact(self,guy,grass):
     blist=["Piplup","Chikorita","Torchic","Bush","Pokémart"]
     if self.offered==False:
        self.buying=blist[random.randint(0,len(blist)-1)]
        self.price=random.randint(10,30)
        self.offered=True
     reply=simpledialog.askinteger("Dialougue Box","If you can get me a "
                                      +self.buying+", then I will give you "+
                                      str(self.price)+" coins.\n1-Ok, sure\n2-So"+
                                      "rry, I can't do that right now.")
     if reply==1:
                if self.buying in guy.inventory:
                    guy.cs+=self.price
                    guy.inventory.remove(self.buying)
                    messagebox.showinfo("Item Sold","Thanks! Here is the money.")
                    self.offered=False
                else:
                    messagebox.showinfo("A Problem has Occured","You lied! You don't have the "
                                        +self.buying+" I wanted!")
                    if self.price>5:
                        self.price-=1
                    else:
                        self.offered=False
     elif reply==2:
                pass
     elif reply==None:
                pass
