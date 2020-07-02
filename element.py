# coding: utf-8

import os
import pygame
from pygame.locals import *


class Element:

    def __init__(self, x, y, content, image):
        self.content = content
        absolute_path = os.path.join(os.path.dirname(__file__), image)
        self.image = pygame.image.load(absolute_path)
        if self.content == "guard":
            self.is_pickable = False
        else:
            self.is_pickable = True
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft=(50 * x, 50 * y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
