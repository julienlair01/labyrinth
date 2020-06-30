# coding: utf-8

import pygame
from pygame.locals import *
import element


class Tile():

    def __init__(self, tile_type, image, x, y, is_blocking):
        self.tile_type = tile_type
        self.x = x
        self.y = y
        self.is_blocking = is_blocking
        if self.tile_type == "wall":
            self.image = pygame.image.load("assets/wall.png")
        else:
            self.image = pygame.image.load("assets/floor.png")
        if self.tile_type == "exit":
            self.add_element("guard")
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft=(50 * self.x, 50 * self.y))

    def add_element(self, element_type):
        """Adds an element on the tile (guard or item)"""
        if element_type == "guard":
            self.element = element.Element(self.x, self.y, element_type, "assets/Gardien.png")

    def get_info(self):
        return {"tile_type": self.tile_type, "is_blocking": self.is_blocking}

    def draw(self, surface):
        """Draws the single tile"""
        surface.blit(self.image, self.rect)
