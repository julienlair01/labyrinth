# coding: utf-8

import pygame
from pygame.locals import *

class Element:

    def __init__(self, x, y, content, image):
        self.content = content
        
        if self.content == "exit":
            self.image = pygame.image.load(str(image))
        elif self.content == "needle":
            self.image = pygame.image.load("assets/seringue.png")

        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft = (50 * x, 50 * y))

    def drawElement(self, surface):
        surface.blit(self.image, self.rect)

    