# coding: utf-8

import pygame
from pygame.locals import *

class Player:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("assets/macgyver.png")
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect()

    def drawPlayer(self, surface):
        surface.blit(self.image, self.rect)
