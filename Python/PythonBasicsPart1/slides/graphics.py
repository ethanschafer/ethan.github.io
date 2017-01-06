import pygame, random

def drawScene(window):
    # Loads an image
    img = pygame.image.load("dude.gif")
    
    # Draws the image on the screen that is passed to it
    window.blit(img, (100,100))
    

    # This will draw a circle a random spot
    pygame.draw.circle(window, (255,0,0),(random.randint(0,800),random.randint(0,600)), 50)

    # This will draw a rectangle a random spot
    pygame.draw.rect(window, (0,255,0),(random.randint(0,800),random.randint(0,600), 150, 150))