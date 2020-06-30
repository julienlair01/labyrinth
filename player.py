# coding: utf-8

import pygame, sys, level, graphelement
from pygame.locals import *

class Player(pygame.sprite.Sprite, graphelement.GraphElement):

    def __init__(self, level):
        super().__init__() 
        self.x, self.y = level.startTile
        self.image = pygame.image.load("assets/macgyver.png")
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft = (50 * self.x, 50 * self.y))

        
    def draw(self, surface):
        """Draws the player on the grid"""
        surface.blit(self.image, self.rect)


    def update(self, screenHeight, screenWidth, level): # TODO move instead of update : bof bcs update can do nothing
        """Updates the player position on the grid, according to the move the player applies.
        Move is not allowed if the target tile is blocked by something (e.g. a wall)"""
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0 and  pressed_keys[K_UP] and level.canMove(self.x, self.y - 1):
            self.rect.move_ip(0, -50)
            self.y -= 1
        if self.rect.bottom < screenHeight and pressed_keys[K_DOWN] and level.canMove(self.x, self.y + 1):
            self.rect.move_ip(0, 50)
            self.y += 1
        if self.rect.left > 0 and pressed_keys[K_LEFT] and level.canMove(self.x - 1, self.y):
            self.rect.move_ip(-50, 0)
            self.x -= 1                
        if self.rect.right < screenWidth and pressed_keys[K_RIGHT] and level.canMove(self.x + 1, self.y):
            self.rect.move_ip(50, 0)
            self.x += 1
    

    def hasFoundExit(self, level):
        """Returns True if the player reached the exit tile"""
        return level.isExitTile(self.x, self.y)
