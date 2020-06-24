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
        else:
            self.image = pygame.image.load("assets/floor.png")
        
        if self.tileType == "exit":
            self.addElement("guard")
 
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft = (50 * self.x, 50 * self.y))
        
    def addElement(self, elementType):
        if elementType == "guard":
            self.elements.append(element.Element(self.x, self.y, self.tileType, "assets/Gardien.png"))
    
    def getInfo(self):
        return {"tileType": self.tileType, "block": self.block}

    def draw(self, surface):
        surface.blit(self.image, self.rect)
