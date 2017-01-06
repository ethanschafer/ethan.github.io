import pygame, random
from pygame.locals import *
from tkinter import*
class Runner:
    def __init__ (self, newX, newY):
        self.x = newX
        self.y = newY
        self.img = pygame.image.load("images/Runner/D-B.png")
        myRec = self.getRec()
        self.width = myRec[2]
        self.height = myRec[3]
        self.skins=["Runner"]
        self.skin=0
        self.skindlib=[pygame.image.load("images/Runner/D-B.png"),pygame.image.load("images/Runner/D-L.png"),pygame.image.load("images/Runner/D-B.png"),pygame.image.load("images/Runner/D-R.png")]
        self.skinulib=[pygame.image.load("images/Runner/U-B.png"),pygame.image.load("images/Runner/U-L.png"),pygame.image.load("images/Runner/U-B.png"),pygame.image.load("images/Runner/U-R.png")]
        self.skinllib=[pygame.image.load("images/Runner/L-B.png"),pygame.image.load("images/Runner/L-L.png"),pygame.image.load("images/Runner/L-B.png"),pygame.image.load("images/Runner/L-R.png")]
        self.skinrlib=[pygame.image.load("images/Runner/R-B.png"),pygame.image.load("images/Runner/R-L.png"),pygame.image.load("images/Runner/R-B.png"),pygame.image.load("images/Runner/R-R.png")]
        self.dirnum=0
        self.direction="d"
        self.way=0
        self.ways=["d","l","u","r"]
        self.moves=0
        self.placed=[]
        self.quotes=["What a good day to be excersising!",
                     "You should try running some time!",
                     "What a pleasant day!",
                     "Good day to you, sir.",
                     "Salutations.",
                     "Greetings.",
                     "Hello.",
                     "I feel great!"]
        self.quote=1
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
    def moveLeft(self):
        if self.direction=="l":
            self.dirnum+=1
            if self.x > 0:
                self.x = self.x - 5
        else:
            self.dirnum=0
        self.direction="l"
        self.img = self.skinllib[self.dirnum%4]
    def moveRight(self):
        if self.direction=="r":
            self.dirnum+=1
            if self.x < 780:
                self.x = self.x + 5
        else:
            self.dirnum=0
        self.direction="r"
        self.img = self.skinrlib[self.dirnum%4]
    def move(self):
        if self.moves==20:
            self.way+=1
            self.moves=0
        if self.way%4==0:
            self.moveDown()
        elif self.way%4==1:
            self.moveLeft()
        elif self.way%4==2:
            self.moveUp()
        elif self.way%4==3:
            self.moveRight()
        self.moves+=1
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
    def face(self,dir):
        if dir=="l":
            self.img = pygame.image.load("images/Runner/L-B.png")
        if dir=="r":
            self.img = pygame.image.load("images/Runner/R-B.png")
        if dir=="u":
            self.img = pygame.image.load("images/Runner/U-B.png")
        if dir=="d":
            self.img = pygame.image.load("images/Runner/D-B.png")
        self.direction=dir
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
    def interact(self,other,grass):
        self.quote=self.quotes[random.randint(0,len(self.quotes)-1)]
        messagebox.showinfo("Dialougue Box",self.quote)
    
