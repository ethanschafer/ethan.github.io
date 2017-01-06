import pygame, random
from Enemy import *

class Enemies:
    def __init__(self):
        self.myList = [Enemy(0,200,25),
                       Enemy(750,270,-25),
                       Enemy(150,340,25),
                       Enemy(550,410,-25)]
        
    def drawAndCollision(self, screen, guy):
        # Loop through the list of enemies
        for alien in self.myList:
            # if guy collides with any enemies,
                # return True - this will immediately end the method
            if guy.collide(alien):
                return True
        
            # Add the old position of the enemy to the
            alien.draw(screen)
            alien.move()
            # array of rectangles to be redrawn
            if alien.x < -50 or alien.x >  850:
                self.myList.remove(alien)

            
            # Move and draw the enemies
            
            
            # Add the old position of the enemy to the array of rectangles
            # to be redrawn
            
            
            # If the enemy has gone off the screen, remove it
            

    
        return False
          
          
    # Create a new enemy and add it to the list of enemies  
    def addEnemy(self, x, y, speed):
        badGuy = Enemy(x,y,speed)
        self.myList.append(badGuy)
    
    # Return the length of the list of enemies
    def numEnemies(self):
        return len(self.myList)
