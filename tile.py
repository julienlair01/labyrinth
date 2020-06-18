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
        print(image)
        self.image = pygame.image.load(image)
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft = (50 * self.x, 50 * self.y))
        
    def getInfo(self):
        return {"tileType": self.tileType, "block": self.block}

    def drawTile(self, surface):
        surface.blit(self.image, self.rect) 
