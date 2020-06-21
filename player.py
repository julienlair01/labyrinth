# coding: utf-8

import pygame, sys, level
from pygame.locals import *

class Player(pygame.sprite.Sprite):

    def __init__(self, level):
        super().__init__() 
        self.x, self.y = level.getStartTile()
        self.image = pygame.image.load("assets/macgyver.png")
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft = (self.x, self.y))
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, screenHeight, screenWidth, level):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                if level.canMove(self.x, self.y - 1):
                    self.rect.move_ip(0, -50)
                    self.y -= 1

        if self.rect.bottom < screenHeight: 
            if pressed_keys[K_DOWN]:
                if level.canMove(self.x, self.y + 1):
                    self.rect.move_ip(0, 50)
                    self.y += 1

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                if level.canMove(self.x - 1, self.y):
                    self.rect.move_ip(-50, 0)
                    self.x -= 1
                    
        if self.rect.right < screenWidth:
            if pressed_keys[K_RIGHT]:
                if level.canMove(self.x + 1, self.y):
                    self.rect.move_ip(50, 0)
                    self.x += 1
