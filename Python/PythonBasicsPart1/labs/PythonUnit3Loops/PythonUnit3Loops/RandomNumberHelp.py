import pygame, sys, random
from pygame.locals import *

pygame.init()

answer = input("Enter q to quit")

while answer != "q":
    x = random.randint(0,10)
    y = random.randint(0,10)
    print("x = " + str(x) + " y = " + str(y) )
    answer = input("Enter q to quit")
    
