# coding: utf-8
""" This module contains the UITile class.
    It extends the Tile class with the pygame-related
    attributes, in order to play the game using a GUI. """

import os

import pygame

import element
from constants import TILESIZE 

class UIElement(element.Element):
    def __init__(self, pos_x, pos_y, content, image):
        super().__init__(pos_x, pos_y, content, image)
        absolute_path = os.path.join(os.path.dirname(__file__), image)
        self.image = pygame.image.load(absolute_path)
        self.surf = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.surf.get_rect(topleft=(TILESIZE * pos_x, TILESIZE * pos_y))