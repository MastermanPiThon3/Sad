#class page for finny fell

import random
import pygame
from pygame.locals import *

class FinnyFell:
    def __init__(self, player, startPosition):
        self.Position = startPosition

    def Move(self, position, speed):
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

    def Move(self, height, width, player):
        if (0 >= self.TimeToSpawn):
            self.Spawn(width, player)
            self.TimeToSpawn = self.SpawnDelay

        #print "Move ", len(self.Active)
        for b in self.Active:
            b.Move(player.Position, self.Speed)

        self.Active = filter(lambda bg: bg.Position[Y] < height, self.Active)

        self.TimeToSpawn -= 1

    def Spawn(self, width, player):
        spawnPosition = [random.randint(20, width - 20), 0]
        #print "Spawn ", spawnPosition
        self.Active.append(FinnyFell(player, spawnPosition))
#Nous avons fini. Merci beaucoup.

    
