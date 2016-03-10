#WARNING- this game was created by two people who recently read A Separate Peace and can be a tad bit crazy. Proceed at your own risk

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

#Holds current position of the staircase thing. Set the start position of the case.
X = 0
Y = 1
playerPos = [400, 480]

#Number of pixles to move the cactus-catcher each loop
PlayerSpeed = 6

#The image for the cactus-catcher, it is loaded from the file '....png'
