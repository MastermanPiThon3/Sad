#WARNING- this game was created by two people who recently read A Separate Peace and can be a tad bit crazy. Proceed at your own risk
#Pippin beat Sauron
#Import pygame module
import math
import pygame
from pygame.locals import *

#Initialize the pygame
pygame.init()

####game variables####
width = 640     # width of game screen
height = 480    # height of screen

#Create the screen
screen=pygame.display.set_mode((width, height))

#Holds current position of the c-c thing. Set the start position of the case.
X = 0
Y = 1
playerPos = [320, 400]

#Number of pixles to move the cactus-catcher each loop
PlayerSpeed = 10

#The image for the cactus-catcher, it is loaded from the file 'dude.png'-CHANGE TO PICTURE
Player = pygame.image.load("dude.png")
playerWidth = Player.get_width()
playerHeight = Player.get_height()

xMinMargin = 10
xMaxMargin = width - playerWidth
yMinMargin = 10
yMaxMargin = height - playerHeight

#Finny image loaded from le fichier-CHANGE TO PICTURE
Finny = pygame.image.load("badguy0.png")
finnyWidth = Finny.get_width()
finnyHeight = Finny.get_height()

xMinMargin = 10
xMaxMargin = width - finnyWidth
yMinMargin = 10
yMaxMargin = height - finnyHeight

#To spawn FInny randomly
#from game 4 badguys class- spawndelay, timetospawn, active,speed, def spawn change to random width

#Holds current direction the player is moving. Set no movement
#       right-a left-d
keys = {K_a:0, K_d:0}

#Main Game Loop. The game does not run forever. It gets tired.
while True:
    #Fill screen with color-CHANGE TO BACKGROUND PICTURE
    screen.fill((0,0,200))

    #Place image on screen
    screen.blit(Player,playerPos)
    #Loop over input to see if the keys a or d were pressed or released
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:    #une key was pressed
            keys[event.key] = PlayerSpeed
        elif event.type == pygame.KEYUP:    #une key a laisse
            keys[event.key] = 0
        elif event.type == pygame.QUIT:     #l'user a quitte
            pygame.quit()

    #Update the x position of the player
    xUpdated = playerPos[X] - keys[K_a] + keys[K_d]
    if xMinMargin <= xUpdated <= xMaxMargin:
        playerPos[X] = xUpdated
        

    #Dessiner l'ecran
    pygame.display.flip() 
            
    #Vous etes venu a le fin de ce logiciel. Felicitation a vous. Nous sont desolees si vous ne savez pas le francais.


