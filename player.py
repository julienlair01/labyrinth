# coding: utf-8

import pygame, level
from pygame.locals import *

class Player:

    def __init__(self, level):
        self.x, self.y = level.getStartTile()
        # self.x = 0
        # self.y = 0
        self.image = pygame.image.load("assets/macgyver.png")
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft = (50 * self.x, 50 * self.y))

    def drawPlayer(self, surface):
        surface.blit(self.image, self.rect)
