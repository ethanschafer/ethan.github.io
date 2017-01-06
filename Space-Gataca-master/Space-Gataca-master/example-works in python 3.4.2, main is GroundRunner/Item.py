import pygame
from pygame.locals import *
from tkinter import*
import random
class Item:
    def __init__ (self, newX, newY,img):
        self.x = newX
        self.y = newY
        self.name=img[:-4]
        self.img = pygame.image.load("images/items/"+img)
        myRec = self.getRec()
        self.width = myRec[2]
        self.height = myRec[3]
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
    def interact(self, guy):
        guy.inventory.append(self.name)
        messagebox.showinfo("Item Pickup","You picked up a "+self.name+" and "
                            +"added it to your inventory.")
        guy.placed.remove(self)
