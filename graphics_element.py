# coding: utf-8

import pygame


class GraphicsElement():

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
    
    def draw(self, surface):
        """Draws the element on the grid"""
        surface.blit(self.image, self.rect)

