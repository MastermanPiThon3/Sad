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
        self.TimeToSpawn = pygame.time.get_ticks()
        self.Active = []
        self.Speed = 5
        self.Width = self.Finny.get_width()
        self.Height = self.Finny.get_height()
        self.Center = [self.Width/2, self.Height/2]

    def Move(self, height, width, playerPos, playerWidth, playerHeight):
        CurrentTime = pygame.time.get_ticks()
        if CurrentTime - self.TimeToSpawn >= self.SpawnDelay:
            self.Spawn(width)
            self.TimeToSpawn = CurrentTime - random.randint(0, 333)

        #print "Move", len(self.Active)
        for b in self.Active:
            b.Move(self.Speed)

        self.Active = filter(lambda bg: bg.Position[Y] < height, self.Active)

        self.TimeToSpawn -= 1
        #HELP
        self.Active = filter(lambda ff: not self.Intersect(ff, playerPos, playerWidth, playerHeight), self.Active)

    def Spawn(self, width):
        spawnPosition = [random.randint(20, width - 20), 0]
        #print "Spawn ", spawnPosition
        self.Active.append(FinnyFell(spawnPosition))

    def Intersect(self, finnyfell, playerPos, playerWidth, playerHeight):
        Finnyrect = Rect(finnyfell.Position, [self.Width, self.Height])
        Playerrect = Rect(playerPos, [playerWidth, playerHeight])
        return Finnyrect.colliderect(Playerrect)

          
    def Draw(self, screen):
        for FF in self.Active:
            screen.blit(self.Finny, FF.Position)
#Nous avons fini. Merci beaucoup.

    
