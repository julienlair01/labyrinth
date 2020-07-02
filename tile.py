# coding: utf-8

import os

import pygame

import element


class Tile():

    def __init__(self, tile_type, image, x, y, is_blocking):
        self.tile_type = tile_type
        self.x = x
        self.y = y
        self.is_blocking = is_blocking
        absolute_path = os.path.join(os.path.dirname(__file__), image)
        self.image = pygame.image.load(absolute_path)
        if self.tile_type == "exit":
            self.add_element("guard")
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft=(50 * self.x, 50 * self.y))

    def add_element(self, element_type):
        """Adds an element on the tile (guard or item)"""
        if element_type == "guard":
            self.element = element.Element(self.x, self.y, element_type, "assets/Gardien.png")
        elif element_type == "tube":
            self.element = element.Element(self.x, self.y, element_type, "assets/plastic_tube.png")
        elif element_type == "needle":
            self.element = element.Element(self.x, self.y, element_type, "assets/syringe.png")
        elif element_type == "ether":
            self.element = element.Element(self.x, self.y, element_type, "assets/ether.png")

    def get_info(self):
        return {"tile_type": self.tile_type, "is_blocking": self.is_blocking}

    def draw(self, surface):
        """Draws the single tile"""
        surface.blit(self.image, self.rect)
