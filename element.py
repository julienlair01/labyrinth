# coding: utf-8

import pygame
from pygame.locals import *


class Element:

    def __init__(self, x, y, content, image):
        self.content = content
        if self.content == "guard":
            self.image = pygame.image.load("assets/Gardien.png")
        elif self.content == "syringe":
            self.image = pygame.image.load("assets/syringe.png")
        elif self.content == "needle":
            self.image = pygame.image.load("assets/needle.png")
        elif self.content == "ether":
            self.image = pygame.image.load("assets/ether.png")
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft=(50 * x, 50 * y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
