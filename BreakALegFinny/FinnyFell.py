#WARNING- this game was created by two people who recently read A Separate Peace and can be a tad bit crazy. Proceed at your own risk
#Pippin beat Sauron
#Eowyn > Frodo
#Eowyn killed witch king unlike anyone else so yes she should be allowed to go and fight otherwise he would still be terrorizing many people of middle earth and they possibly wouldn't have won the war of the ring and sauron would rule and there would be complete and utter KAOS under Siegfried (this is KAOS not a lotr fan club!)
#Import pygame module
import math
import pygame
from pygame.locals import *

from FINNY import *

#Initialize the pygame
pygame.init()

gameOn = True

####game variables####
width = 640     # width of game screen
height = 480    # height of screen

#Create the screen
screen=pygame.display.set_mode((width, height))

#Holds current position of the c-c thing. Set the start position of the case.
X = 0
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

#To spawn FInny randomly
MrFell = FinniesFell(1000)

#Holds current direction the player is moving. Set no movement
#       right-a left-d
keys = {K_a:0, K_d:0}

#Main Game Loop. The game does not run forever. It gets tired.
while gameOn:
    #Fill screen with color-CHANGE TO BACKGROUND PICTURE
    screen.fill((0,0,200))
    MrFell.Move(height,width,playerPos,playerWidth,playerHeight)

    #Place image on screen
    screen.blit(Player,playerPos)
    MrFell.Draw(screen)
    #Loop over input to see if the keys a or d were pressed or released
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:    #une key was pressed
            keys[event.key] = PlayerSpeed
        elif event.type == pygame.KEYUP:    #une key a laisse
            keys[event.key] = 0
        elif event.type == pygame.QUIT:     #l'user a quitte
            pygame.quit()
            gameOn = False

    #Update the x position of the player
    xUpdated = playerPos[X] - keys[K_a] + keys[K_d]
    if xMinMargin <= xUpdated <= xMaxMargin:
        playerPos[X] = xUpdated
        

    #Dessiner l'ecran
    pygame.display.flip() 
            
    #Vous etes venu a le fin de ce logiciel. Felicitation a vous. Nous sont desolees si vous ne savez pas le francais.
    #Le seigneur des anneaux

