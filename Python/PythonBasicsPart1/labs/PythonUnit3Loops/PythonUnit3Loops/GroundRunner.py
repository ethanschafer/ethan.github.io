import pygame, sys, random
from pygame.locals import *
from Ground import *
from Person import *
from coin import *




# Create a screen that is 800 by 600 pixels
pygame.init()
screen = pygame.display.set_mode((800,600))


background = pygame.Surface((800,600))


#create and assign variables
score = 0
time = 10
gameEnd = False
gameWin = False


#Allows user to hold down key
pygame.key.set_repeat(1,1)


# Create a person named guy at position (40,40)
guy = Person(40,40)
myCoin = Coin(250,250)


# a list that keeps track of the areas of screen that have changed
changedRecs=[]


# Create and draw the ground
grass = Ground()
grass.draw(background)


#display the background
screen.blit(background,(0,0))


pygame.display.update()

#colliding with coin
while True:


    # draw the scene
    screen.blit(background,(0,0))
    guy.draw(screen)
    myCoin.draw(screen)


    #position of guy  for places that changed
    changedRecs.append(guy.getRec())
    changedRecs.append(myCoin.getRec())




    #set fonrt and control for score,game over, and win
    font = pygame.font.Font(None,36)
    if gameEnd:
        text = font.render("Game Over!", 1,(10,10,10))
    elif gameWin: 
        text = font.render("You Win!", 1,(10,10,10))
    else:
        text = font.render("Score: " + str(score), 1,(10,10,10))


    #draw the text for score,game over, and win
        textpos = text.get_rect()
        textpos.centerx = 400
        screen.blit(text, textpos)


    if gameEnd:
        text = font.render("Game Over!", 1,(10,10,10))
    elif gameWin:
        text = font.render("You Win!", 1,(10,10,10))
    else:
        text = font.render("Time: " + str(time), 1,(10,10,10))


    #draw the text for score,game over, and win
        textpos = text.get_rect()
        textpos.centerx = 300
        screen.blit(text, textpos)
        
    if gameWin:
        text = font.render("You Win!", 1,(10,10,10))
        
    #draw the text for score,game over, and win
        textpos = text.get_rect()
        textpos.centerx = 350
        screen.blit(text, textpos)

    #If guy hits coin
    if guy.collide(myCoin):
        score += 1
        coinX = 1000
        myCoin.x = random.randint(0,769)
        myCoin.y = random.randint(0,579)
    elif score > 9:
        gameWin = True
    #timer 
    
    if (time >= 0):
        time -= 1
        pygame.time.wait(1000)
    #draw the text for score,game over, and win
        textpos = text.get_rect()
        textpos.centerx = 300
        screen.blit(text, textpos)
        
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()


        elif event.type==KEYDOWN:
            #add the old position of guy to the areas of guy that have been changed
            changedRecs.append(guy.getRec())
            
            
            # fill in code for the key presses
            # check for which key was pressed and
            # use the person object's methods to
            # move guy in the correct direction
            if event.key==K_UP: 
                guy.moveUp()


            elif event.key==K_DOWN:
                guy.moveDown()


            elif event.key==K_LEFT:
                guy.moveLeft()


            elif event.key==K_RIGHT:
                guy.moveRight()


    pygame.display.update()
