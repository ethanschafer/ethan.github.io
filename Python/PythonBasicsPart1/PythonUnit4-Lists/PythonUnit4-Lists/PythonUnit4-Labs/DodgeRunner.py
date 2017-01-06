import pygame, sys
from pygame.locals import *
from Ground import *
from Person import *
from Enemies import *

# Making writing text in the center of the screen easier
def writeText(window, written, cenX, cenY):
    font = pygame.font.Font(None, 48)
    text = font.render(written, 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = cenX
    textpos.centery = cenY
    window.blit(text, textpos)
    return (textpos)


# Initialize pygames and set the screen size to 800 by 600
pygame.init()
screen = pygame.display.set_mode((800,600))

# Check if a key is still pressed down every 100 milliseconds
# allows user to hold down the key to move
pygame.key.set_repeat(1, 1)

# Draw the background
background = pygame.Surface((800,600))
drawGround(background)
screen.blit(background, (0,0))


# Set variable to keep track of if the game is over
# and if the user won
gameEnd = False
win = False


# Create a person at position (400, 50)
guy = Person(400, 50)


# Create an Enemies object to keep track of Enemy objects and
# a counter to know when to add an Enemy
foes = Enemies()
counter = 10

# Draw the entire background
pygame.display.update()

while True:
    screen.blit(background, (0,0))
    
    # Check to see if more enemies need to be added
    if foes.numEnemies() < 4 and not gameEnd:
        # Check if it has been enough time since the last enemy was added
        # and add a new enemy to the list of enemies
        if counter > 5:
            y = random.randint(100, 450)
            if random.randint(0,1) > 0:
                foes.addEnemy(0,y,25)
            else:
                foes.addEnemy(800,y,-25)
            counter = 0
        counter +=1
    

    # Checks if the game has ended and determines if the user has won
    if gameEnd:
        if win:
            writeText(screen, "Win!", 400,300)
        else:
            writeText(screen, "Game Over!", 400,300)
    else:
        gameEnd = foes.drawAndCollision(screen, guy)
        

    # draw guy's new position and update only the rectangles that have been changed
    guy.draw(screen)
   
    pygame.display.update()
    
    # Check for events
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
            
        elif event.type==KEYDOWN:
            # Move guy based on key's pressed
          
            
            if event.key==K_UP:     
                guy.moveUp()

            elif event.key==K_DOWN:
                guy.moveDown()
                # Determine if guy has reached the bottom of the screen without hitting an enemy
                if guy.getRec()[1] > 500 and not gameEnd:
                    gameEnd = True
                    win = True

            elif event.key==K_LEFT:
                guy.moveLeft()

            elif event.key==K_RIGHT:
                guy.moveRight()

                    
    pygame.time.wait(1)
