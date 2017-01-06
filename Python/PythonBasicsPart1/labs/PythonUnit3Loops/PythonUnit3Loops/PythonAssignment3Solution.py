import pygame, sys
from pygame.locals import *
from Ground import *
from Person import *
from coin import *

pygame.init()
screen = pygame.display.set_mode((800,600))

background = pygame.Surface((800,600))

# Every 100 milliseconds check if a key is still pressed down
# Allows user to hold down the key to move
pygame.key.set_repeat(1,1)

# Create and draw the ground
grass = Ground()
grass.draw(background)

#Create guy & wall
guy = Person(400,300)
rewards = coin(200,200)

# create a variable that tracks if the game is over
gameEnd = False
gameWin = False
numSeconds = 10000
time = 10

# create a variable to keep track of how many walls you jumped over
score = 0

# display the background
screen.blit(background,(0,0))

pygame.display.update()


# Event loop that runs until you exit
while True:
    #grass.draw(background)
    screen.blit(background,(0,0))

    font = pygame.font.Font(None, 36)
    if gameEnd: 
        text = font.render("Game Over!", 1, (10, 10, 10))
    elif gameWin:
        text = font.render("You Win!", 1, (10, 10, 10))
    else:
        text = font.render("Score: " + str(score), 1, (10, 10, 10))
        

        if numSeconds > 0 and score < 10:
            numSeconds -= 1
            time = int(numSeconds/1000)
        if score == 10 and gameEnd == False:
            gameWin = True
        if numSeconds == 0:
            gameEnd = True
            

    if guy.collide(rewards):
        score += 1
        x = random.randint(0,750)
        y = random.randint(0,550)
        rewards.setPos(x,y)
        rewards.draw(screen)
    
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN:
            keys = pygame.key.get_pressed()

            if keys[K_LEFT]:
                guy.moveLeft()
                

            if keys[K_RIGHT]:
                guy.moveRight()
                

            
                

            if keys[K_UP]:
                guy.moveUp()
                

            if keys[K_DOWN]:
                guy.moveDown()
                

            if keys[K_w]:
                guy.moveUp()
                

            if keys[K_DOWN]:
                guy.moveDown()
                

            if keys[K_w]:
                bunny.moveUp()

            if keys[K_s]:
                bunny.moveDown()

            if keys[K_a]:
                bunny.moveLeft()

            if keys[K_d]:
                bunny.moveRight()

    # draw the text
    textpos = text.get_rect()
    textpos.centerx = 400
    screen.blit(text, textpos)

    timerText =  font.render("Time Remaining: " + str(time), 1, (10, 10, 10))
    timerTextpos = timerText.get_rect()
    timerTextpos.centerx = 150
    screen.blit(timerText, timerTextpos)

    guy.draw(screen)
    rewards.draw(screen)

    pygame.display.update()
