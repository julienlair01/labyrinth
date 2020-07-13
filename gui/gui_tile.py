# coding: utf-8
""" This module contains the UITile class.
    It extends the Tile class with the pygame-related
    attributes, in order to play the game using a GUI. """

import os

import pygame

import tile
import element
from gui import gui_element
from constants import TILESIZE 


class GUITile(tile.Tile):

    def __init__(self, tile_type, image, pos_x, pos_y, is_blocking):
        super().__init__(tile_type, image, pos_x, pos_y, is_blocking)
        absolute_path = os.path.join(os.path.dirname(__file__), image)
        self.image = pygame.image.load(absolute_path)
        self.surf = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.surf.get_rect(topleft=(TILESIZE * self.pos_x, TILESIZE * self.pos_y))
    
    def add_element(self, element_type):
        """Adds an UI element on the tile (guard or item). 
        
        Keyword arguments:
        element_type -- guard or item
        """
        if element_type == "guard":
            self.element = gui_element.GUIElement(self.pos_x, self.pos_y, element_type, "assets/Gardien.png")
        elif element_type == "plastic_tube":
            self.element = gui_element.GUIElement(self.pos_x, self.pos_y, element_type, "assets/plastic_tube.png")
        elif element_type == "needle":
            self.element = gui_element.GUIElement(self.pos_x, self.pos_y, element_type, "assets/needle.png")
        elif element_type == "ether":
            self.element = gui_element.GUIElement(self.pos_x, self.pos_y, element_type, "assets/ether.png")

    def draw(self, surface):
        """Draws the single tile"""
        surface.blit(self.image, self.rect)
        