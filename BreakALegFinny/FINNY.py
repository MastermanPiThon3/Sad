#class page for finny fell

import random
import pygame
from pygame.locals import *

Y = 1

class FinnyFell:
    def __init__(self, startPosition):
        self.Position = startPosition

    def Move(self, speed):
        self.Position[Y]+= speed

class FinniesFell:
    def __init__(self, spawnDelay):
        self.Finny = pygame.image.load("badguy0.png")
        self.SpawnDelay = spawnDelay
        self.TimeToSpawn = 10
        self.Active = []
        self.Speed = 5
        self.Width = self.Finny.get_width()
        self.Height = self.Finny.get_height()
        self.Center = [self.Width/2, self.Height/2]

    def Move(self, height, width):
        if (0 >= self.TimeToSpawn):
            self.Spawn(width)
            self.TimeToSpawn = self.SpawnDelay

        #print "Move", len(self.Active)
        for b in self.Active:
            b.Move(self.Speed)

        self.Active = filter(lambda bg: bg.Position[Y] < height, self.Active)

        self.TimeToSpawn -= 1

    def Spawn(self, width):
        spawnPosition = [random.randint(20, width - 20), 0]
        #print "Spawn ", spawnPosition
        self.Active.append(FinnyFell(spawnPosition))

    def Draw(self, screen):
        for FF in self.Active:
            screen.blit(self.Finny, FF.Position)
#Nous avons fini. Merci beaucoup.

    
