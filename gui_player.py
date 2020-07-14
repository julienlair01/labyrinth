# coding: utf-8
""" This module contains the GUIPlayer class.
    It extends the Player class with the pygame-related
    attributes, in order to play the game using a GUI. """

import os

import pygame

import player
from constants import TILESIZE


class GUIPlayer(player.Player, pygame.sprite.Sprite):

    def __init__(self, level):
        super().__init__(level)
        absolute_path = os.path.join(os.path.dirname(__file__), "assets", "MacGyver.png")
        self.image = pygame.image.load(absolute_path)
        self.surf = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.surf.get_rect(topleft=(TILESIZE * self.pos_x, TILESIZE * self.pos_y))
