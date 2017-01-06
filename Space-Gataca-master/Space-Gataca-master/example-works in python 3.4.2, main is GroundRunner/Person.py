import pygame
from pygame.locals import *
from tkinter import*
from Item import*
root = Tk()
w = Label(root, text="Customization")
w.pack()
class Person:
    def __init__ (self, newX, newY):
        self.x = newX
        self.y = newY
        self.img = pygame.image.load("images/Calem/D-B.png")
        myRec = self.getRec()
        self.width = myRec[2]
        self.height = myRec[3]
        self.skins=["Calem"]
        self.skin=0
        self.namespeed=1
        self.gamespeed=100
        self.skindlib=[pygame.image.load("images/Calem/D-B.png"),pygame.image.load("images/Calem/D-L.png"),pygame.image.load("images/Calem/D-B.png"),pygame.image.load("images/Calem/D-R.png")]
        self.skinulib=[pygame.image.load("images/Calem/U-B.png"),pygame.image.load("images/Calem/U-L.png"),pygame.image.load("images/Calem/U-B.png"),pygame.image.load("images/Calem/U-R.png")]
        self.skinllib=[pygame.image.load("images/Calem/L-B.png"),pygame.image.load("images/Calem/L-L.png"),pygame.image.load("images/Calem/L-B.png"),pygame.image.load("images/Calem/L-R.png")]
        self.skinrlib=[pygame.image.load("images/Calem/R-B.png"),pygame.image.load("images/Calem/R-L.png"),pygame.image.load("images/Calem/R-B.png"),pygame.image.load("images/Calem/R-R.png")]
        self.skin=0
        self.cs=0
        self.dirnum=0
        self.direction="d"
        self.maxcs=5
        self.cinterval=5000
        self.inventory=[]
        self.lastplace=""
        self.placed=[]
    def changeskin(self):
        self.skin=(self.skin+1)%len(self.skins)
        self.skindlib=[pygame.image.load("images/"+self.skins[self.skin]+"/D-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/D-L.png"),pygame.image.load("images/"+self.skins[self.skin]+"/D-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/D-R.png")]
        self.skinulib=[pygame.image.load("images/"+self.skins[self.skin]+"/U-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/U-L.png"),pygame.image.load("images/"+self.skins[self.skin]+"/U-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/U-R.png")]
        self.skinllib=[pygame.image.load("images/"+self.skins[self.skin]+"/L-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/L-L.png"),pygame.image.load("images/"+self.skins[self.skin]+"/L-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/L-R.png")]
        self.skinrlib=[pygame.image.load("images/"+self.skins[self.skin]+"/R-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/R-L.png"),pygame.image.load("images/"+self.skins[self.skin]+"/R-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/R-R.png")]
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
    def tryplace(self):
     if len(self.inventory)==0:
            messagebox.showinfo("Place Item","Your inventory is empty.")
            return False
     else:
        items=""
        for i in range (len(self.inventory)):
            items+=str(i+1)+"-"+self.inventory[i]+"\n"
        reply=simpledialog.askinteger("Place Item","Inventory:\n"+items)
        if reply<=len(self.inventory) and reply>0:           
            self.placed.append(Item(self.x+20,self.y+20,self.inventory[reply-1]+".gif"))
            messagebox.showinfo("Item Placed","Placed "+self.inventory[reply-1]+" at ("+str(self.x+20)+","+str(self.y+20)+").")
            self.inventory.pop(i)
        elif reply==None:
            return False
        else:
            messagebox.showinfo("Error","Invalid Input.")
            self.tryplace()
            return "ok?"
        return True
    def moveLeft(self):
        if self.direction=="l":
            self.dirnum+=1
            if self.x > 0:
                self.x = self.x - 5
        else:
            self.dirnum=0
        self.direction="l"
        self.img = self.skinllib[self.dirnum%4]
    def showskins(self):
        skins=""
        for i in range (len(self.skins)):
            skins+=str(i+1)+"-"+self.skins[i]+"\n"
        reply=simpledialog.askinteger("Skin Selector","Skins:\n"+skins)
        if reply==None:
            return False
        elif reply<=len(self.skins) and reply>0:
            self.skin=reply-1
            self.skindlib=[pygame.image.load("images/"+self.skins[self.skin]+"/D-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/D-L.png"),pygame.image.load("images/"+self.skins[self.skin]+"/D-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/D-R.png")]
            self.skinulib=[pygame.image.load("images/"+self.skins[self.skin]+"/U-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/U-L.png"),pygame.image.load("images/"+self.skins[self.skin]+"/U-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/U-R.png")]
            self.skinllib=[pygame.image.load("images/"+self.skins[self.skin]+"/L-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/L-L.png"),pygame.image.load("images/"+self.skins[self.skin]+"/L-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/L-R.png")]
            self.skinrlib=[pygame.image.load("images/"+self.skins[self.skin]+"/R-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/R-L.png"),pygame.image.load("images/"+self.skins[self.skin]+"/R-B.png"),pygame.image.load("images/"+self.skins[self.skin]+"/R-R.png")]
            messagebox.showinfo("Skin Select","Selected the '"+self.skins[self.skin]+"' skin.")
        
        else:
            messagebox.showinfo("Error","Invalid Input.")
            self.showskins()
    def showbgs(self,grass):
        bgs=""
        
        for i in range (len(grass.grsls)):
            bgs+=str(i+1)+"-"+grass.grsls[i]+"\n"
        reply=simpledialog.askinteger("Background Selector","Backgrounds:\n"+bgs)
        if reply==None:
            return False
        elif reply<=len(grass.grsls) and reply>0:
            grass.grassy=reply-1
            messagebox.showinfo("Background Select","Selected the '"+grass.grsls[reply-1]+"' background.")
        
        else:
            messagebox.showinfo("Error","Invalid Input.")
            self.showbgs(grass)
    def moveRight(self):
        if self.direction=="r":
            self.dirnum+=1
            if self.x < 780:
                self.x = self.x + 5
        else:
            self.dirnum=0
        self.direction="r"
        self.img = self.skinrlib[self.dirnum%4]
        
        
    def moveUp(self):
        if self.direction=="u":
            self.dirnum+=1
            if self.y > 0:
                self.y = self.y - 5
        else:
            self.dirnum=0
        self.direction="u"
        self.img = self.skinulib[self.dirnum%4]
        
    def moveDown(self):
        if self.direction=="d":
            self.dirnum+=1
            if self.y < 573:
                self.y = self.y + 5
        else:
            self.dirnum=0
        self.direction="d"
        self.img = self.skindlib[self.dirnum%4]
    def collide(self, other):        
        otherRec = other.getRec()
        otherX = otherRec[0]
        otherY = otherRec[1]
        otherWidth = otherRec[2]
        otherHeight = otherRec[3]
        myRec = self.getRec()        
        width = myRec[0] + myRec[2] 
        height = myRec[1] + myRec[3]                
        if self.x > (otherX + otherWidth):
            return False               
        elif width < otherX:
            return False                         
        elif self.y > (otherY + otherHeight):
            return False                         
        elif height < otherY:
            return False 
        else:
            return True
    def dirchange(self,other):
        otherRec = other.getRec()
        otherX = otherRec[0]
        otherY = otherRec[1]
        otherWidth = otherRec[2]
        otherHeight = otherRec[3]
        myRec = self.getRec()
        width = myRec[0] + myRec[2] 
        height = myRec[1] + myRec[3]       
        rightEdge = myRec[0] + myRec[2] 
        bottomEdge = myRec[1] + myRec[3]
        dists=[((otherX-rightEdge)**2+(otherY-myRec[1])**2)**(1/2),
               ((otherX-myRec[0])**2+(otherY-height)**2)**(1/2),
               ((otherX+otherWidth-myRec[0])**2+(otherY-myRec[1])**2)**(1/2),
               ((otherX-rightEdge)**2+(otherHeight-myRec[1])**2)**(1/2)]
        smallst = 0
        for i in range(len(dists)):
            if dists[i]<dists[smallst]:
                smallst=i
        if smallst==0:
            other.face("l")
        elif smallst==1:
            other.face("u")
        elif smallst==2:
            other.face("r")
        elif smallst==3:
            other.face("d")
    def changespeed(self):
        reply=simpledialog.askfloat("Speed Settings","Set the speed(currently speed level "
                                    +str(round(self.namespeed,3))+"):")
        if reply==None:
            pass
        elif reply<=0:
            messagebox.showinfo("Error","You can't set the speed level to 0 or below.")
        else:
            self.namespeed=reply
            self.gamespeed=100/reply
    def back(self):
        if self.direction=="l":
            self.x+=5
        if self.direction=="r":
            self.x-=5
        if self.direction=="d":
            self.y-=5
        if self.direction=="u":
            self.y+=5
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
    def interact(self,other):
        other.interact()
    def changeSkin(self):
        self.skin+=1
        if self.direction=="l":
            self.img = self.skinllib[self.skin%4]
        elif self.direction=="r":
            self.img = self.skinrlib[self.skin%4]
        elif self.direction=="u":
            self.img = self.skinulib[self.skin%4]
        elif self.direction=="d":
            self.img = self.skindlib[self.skin%4]
