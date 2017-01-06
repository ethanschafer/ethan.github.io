import pygame
from pygame.locals import *
from tkinter import*
import random

class Clerk:
    def __init__ (self, newX, newY):
        self.x = newX
        self.y = newY
        self.img = pygame.image.load("images/Clerk/D.png")
        self.direction="d"
        myRec = self.getRec()
        self.width = myRec[2]
        self.height = myRec[3]
        self.bgtbp=["Green-Blue","Orange","Purple"]
        self.stbp=["Girl","Agent","Aristocrat"]
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
    def face(self,dir):
        if dir=="l":
            self.img = pygame.image.load("images/Clerk/L.png")
        if dir=="r":
            self.img = pygame.image.load("images/Clerk/R.png")
        if dir=="u":
            self.img = pygame.image.load("images/Clerk/U.png")
        if dir=="d":
            self.img = pygame.image.load("images/Clerk/D.png")
        self.direction=dir
    def interact(self,guy,grass):
        ask=[]
        reply=simpledialog.askinteger("Shop","1-Items\n2-Backgrounds\n3-Skins")
        if reply==1:
         if len(guy.inventory)<20:
            reply=simpledialog.askinteger("Items","1-Bush(5 coins)\n2-Random Pokemon(10 coins)\n3-Pokemart(15 coins)")
            if reply==1:
                if guy.cs<5:
                    messagebox.showinfo("Error","You need 5 coins to buy a bush.")
                    self.interact(guy,grass)
                else:
                    guy.cs-=5
                    guy.inventory.append("Bush")
                    messagebox.showinfo("Purhcase","You bought a bush.")
                    self.interact(guy,grass)
            if reply==2:
                if guy.cs<10:
                    messagebox.showinfo("Error","You need 10 coins to buy a Pokemon.")
                    self.interact(guy,grass)
                else:
                    guy.cs-=10
                    pkls=["Piplup","Torchic","Chikorita"]
                    newpoke=pkls[random.randint(0,(len(pkls)-1))]
                    guy.inventory.append(newpoke)
                    messagebox.showinfo("Purhcase","You bought a random Pokemon.\nIt turned out to be a "+newpoke+"!")
                    self.interact(guy,grass)
            if reply==3:
                if guy.cs<15:
                    messagebox.showinfo("Error","You need 15 coins to buy a Pokemart.")
                    self.interact(guy,grass)
                else:
                    guy.cs-=15
                    guy.inventory.append("Pokemart")
                    messagebox.showinfo("Purhcase","You bought a Pokemart.")
                    self.interact(guy,grass)
         else:
             messagebox.showinfo("Error","Your inventory is full. (20 items max)")
             self.interact(guy,grass)
        elif reply==2:
            if len(self.bgtbp)==0:
                messagebox.showinfo("Sold Out","You have already purchased all the backgrounds.")
                self.interact(guy,grass)
            elif guy.cs<10:
                messagebox.showinfo("Error","Backgrounds cost 10 coins each. You need to have at least 10 coins"
                                    + " to pucrchase one.")
                self.interact(guy,grass)

            else:
                ask=[]
                for i in range(len(self.bgtbp)):
                    ask.append(str(i+1)+"-"+self.bgtbp[i]+"\n")
                reply=""
                for i in range(len(ask)):
                    reply+=ask[i]
                reply=simpledialog.askinteger("Backgrounds",reply)
                bg=0
                nums=[]
                if reply==None:
                    self.interact(guy,grass)
                for i in range(len(ask)+1):
                    nums.append(i)
                if reply not in nums:
                    messagebox.showinfo("Error","Invalid Input.")
                    self.interact(guy,grass)
                bought=False
                while bg<=len(ask) and bought==False:
                    if reply==bg+1:
                        grass.grasses.append("images/ground/"+self.bgtbp[bg].lower()+".png")
                        messagebox.showinfo("Purchase","Purchased "+self.bgtbp[bg].lower()+" background.")
                        grass.grsls.append(self.bgtbp[bg])
                        self.bgtbp.pop(bg)
                        guy.cs-=10
                        bought=True
                        print(self.bgtbp)
                    bg+=1
                self.interact(guy,grass)

        elif reply==3:
            if len(self.stbp)==0:
                messagebox.showinfo("Sold Out","You have already purchased all the skins.")
                self.interact(guy,grass)
            elif guy.cs<15:
                messagebox.showinfo("Error","Skins cost 10 coins each. You need to have at least 15 coins"
                                    + " to pucrchase one.")
                self.interact(guy,grass)

            else:
                ask=[]
                for i in range(len(self.stbp)):
                    ask.append(str(i+1)+"-"+self.stbp[i]+"\n")
                reply=""
                for i in range(len(ask)):
                    reply+=ask[i]
                reply=simpledialog.askinteger("Skins",reply)
                bg=0
                nums=[]
                if reply==None:
                    self.interact(guy,grass)
                for i in range(len(ask)+1):
                    nums.append(i)
                if reply not in nums:
                    messagebox.showinfo("Error","Invalid Input.")
                    self.interact(guy,grass)
                bought=False
                while bg<=len(ask) and bought==False:
                    if reply==bg+1:
                        guy.skins.append(self.stbp[bg])
                        messagebox.showinfo("Purchase","Purchased "+self.stbp[bg].lower()+" skin.")
                        self.stbp.pop(bg)
                        guy.cs-=10
                        bought=True
                    bg+=1
                self.interact(guy,grass)
        elif reply==None:
            pass
        else:
            messagebox.showinfo("Error","Invalid Input.")
            self.interact(guy,grass)
        return False
