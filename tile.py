# coding: utf-8

import os

import pygame

import element
from constants import TILESIZE


class Tile():

    def __init__(self, tile_type, image, pos_x, pos_y, is_blocking):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tile_type = tile_type
        self.is_blocking = is_blocking
        self.element = []
        absolute_path = os.path.join(os.path.dirname(__file__), image)
        self.image = pygame.image.load(absolute_path)
        if self.tile_type == "exit":
            self.add_element("guard")
        self.surf = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.surf.get_rect(topleft=(TILESIZE * self.pos_x, TILESIZE * self.pos_y))

    def add_element(self, element_type):
        """Adds an element on the tile (guard or item)"""
        if element_type == "guard":
            self.element = element.Element(self.pos_x, self.pos_y, element_type, "assets/Gardien.png")
        elif element_type == "plastic_tube":
            self.element = element.Element(self.pos_x, self.pos_y, element_type, "assets/plastic_tube.png")
        elif element_type == "needle":
            self.element = element.Element(self.pos_x, self.pos_y, element_type, "assets/needle.png")
        elif element_type == "ether":
            self.element = element.Element(self.pos_x, self.pos_y, element_type, "assets/ether.png")

    def get_info(self):
        return {"tile_type": self.tile_type, "is_blocking": self.is_blocking}

    def draw(self, surface):
        """Draws the single tile"""
        surface.blit(self.image, self.rect)
