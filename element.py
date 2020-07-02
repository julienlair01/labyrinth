# coding: utf-8

import os

import pygame

from constants import TILESIZE


class Element:

    def __init__(self, pos_x, pos_y, content, image):
        self.content = content
        absolute_path = os.path.join(os.path.dirname(__file__), image)
        self.image = pygame.image.load(absolute_path)
        self.is_picked = False
        if self.content == "guard":
            self.is_pickable = False
        else:
            self.is_pickable = True
        self.surf = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.surf.get_rect(topleft=(TILESIZE * pos_x, TILESIZE * pos_y))

    def draw(self, surface):
        if not self.is_picked:
            surface.blit(self.image, self.rect)
