import pygame, random
from coin import *

class Coins:
    def __init__(self):
        self.cs = [Coin(random.randint(0,769),random.randint(200,579)),
                    Coin(random.randint(0,769),random.randint(200,579)),
                    Coin(random.randint(0,769),random.randint(200,579)),
                    Coin(random.randint(0,769),random.randint(200,579)),
                    Coin(random.randint(0,769),random.randint(200,579))]
        
    def drawAndCollision(self, screen, guy, changedrecs):
        # Loop through the list of enemies
        i=0
        while i<len(self.cs):
            if guy.collide(self.cs[i]):               
                self.cs.pop(i)
                guy.cs+=1
            else:
                changedrecs.append(self.cs[i].getRec())
                self.cs[i].draw(screen)
                changedrecs.append(self.cs[i].getRec())
                i+=1
        return False
          
    def numCoins(self):
        return len(self.cs)
    # Create a new enemy and add it to the list of enemies  
    def addCoin(self, x, y):
        self.cs.append(Coin(x,y))
        return True
    # Return the length of the list of enemies
    
