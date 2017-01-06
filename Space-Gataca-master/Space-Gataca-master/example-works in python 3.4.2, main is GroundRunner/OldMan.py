import pygame
from pygame.locals import *
from tkinter import*
import random
class OldMan:
    def __init__ (self, newX, newY):
        self.x = newX
        self.y = newY
        self.img = pygame.image.load("images/OldMan/D.png")
        self.direction="d"
        myRec = self.getRec()
        self.width = myRec[2]
        self.height = myRec[3]
        self.quotes=["Two wrongs don't make a right.",
                     "The pen is mightier than the sword.",
                     "When in Rome, do as the Romans.",
                     "The squeaky wheel gets the grease.",
                     "When the going gets tough, the tough get going.",
                     "No man is an island.",
                     "Fortune favors the bold.",
                     "People who live in glass houses should not throw stones.",
                     "Life is really simple, but we insist on making it complicated.",
                     "The most important thing is to enjoy your life.",
                     "Life is a dream for the wise, a game for the fool, a comedy for the rich, a tragedy for the poor.",
                     "Don't cry because it's over, smile because it happened.",
                     "Be yourself; everyone else is already taken.",
                     "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
                     "You only live once, but if you do it right, once is enough.",
                     "THE END IS COMING!"]
        self.quote=1
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
    def face(self,dir):
        if dir=="l":
            self.img = pygame.image.load("images/OldMan/L.png")
        if dir=="r":
            self.img = pygame.image.load("images/OldMan/R.png")
        if dir=="u":
            self.img = pygame.image.load("images/OldMan/U.png")
        if dir=="d":
            self.img = pygame.image.load("images/OldMan/D.png")
        self.direction=dir
    def interact(self,guy,grass):
        self.quote=self.quotes[random.randint(0,len(self.quotes)-1)]
        messagebox.showinfo("Dialougue Box","Old man says:\n"+self.quote)
