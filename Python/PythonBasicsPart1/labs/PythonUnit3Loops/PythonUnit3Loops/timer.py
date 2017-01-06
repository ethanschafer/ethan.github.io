import pygame

# Ask user for number of seconds
numSeconds = input("Enter the number of Seconds for your timer")
numSeconds = int(numSeconds)

# Loop while seconds are less or equal to 0
while (numSeconds >= 0):
    # Part 1 - Print the time left as seconds
    print("Time Remaining in Seconds: " + str(numSeconds) + "\n")
    
    # Part 2 - Print the time left as minutes and seconds
    print("Time Remaining in Minutes and Seconds: " +
          str(int(numSeconds/60)) +" : " + str(numSeconds%60))
    numSeconds = numSeconds - 1
    
    pygame.time.wait(1000)
