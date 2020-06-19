# coding: utf-8
import pygame
from pygame.locals import *

class Tile():
    def __init__(self, tileType, image, x, y, block):
        self.tileType = tileType
        self.x = x
        self.y = y
        self.block = block
        self.object = None
        if self.tileType == "wall": # problem with loading image through image variable (pygame can't load the image)
            self.image = pygame.image.load("assets/wall.png")
        elif self.tileType == "floor":
            self.image = pygame.image.load("assets/floor.png")
        else:
            self.image = pygame.image.load("assets/floor.png")
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft = (50 * self.x, 50 * self.y))
        
    def getInfo(self):
        return {"tileType": self.tileType, "block": self.block}

    def drawTile(self, surface):
        surface.blit(self.image, self.rect) 
