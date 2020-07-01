# coding: utf-8

import pygame
from pygame.locals import *


class GraphicsElement():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("assets/macgyver.png")
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft=(50 * self.x, 50 * self.y))
    
    def draw(self, surface):
        """Draws the element on the grid"""
        surface.blit(self.image, self.rect)

