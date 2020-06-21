# coding: utf-8
import pygame, element
from pygame.locals import *

class Tile():
    def __init__(self, tileType, image, x, y, block):
        self.tileType = tileType
        self.x = x
        self.y = y
        self.block = block
        self.elements = []

        if self.tileType == "wall": # problem with pygame when loading image through image variable (pygame can't load the image), now using hardcoded values
            self.image = pygame.image.load("assets/wall.png")
        elif self.tileType == "floor":
            self.image = pygame.image.load("assets/floor.png")
        elif self.tileType == "exit":
            self.image = pygame.image.load("assets/floor.png")
            self.elements.append(element.Element(self.x, self.y, tileType, "assets/Gardien.png"))
        elif self.tileType == "needle":
            self.image = pygame.image.load("assets/floor.png")
            self.elements.append(element.Element(self.x, self.y, tileType, "assets/seringue.png"))
        else:
            self.image = pygame.image.load("assets/floor.png")

        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft = (50 * self.x, 50 * self.y))
        
    def getInfo(self):
        return {"tileType": self.tileType, "block": self.block}

    def drawTile(self, surface):
        surface.blit(self.image, self.rect)
