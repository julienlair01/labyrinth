# coding: utf-8

import pygame
from pygame.locals import *
import level


class Player(pygame.sprite.Sprite):

    def __init__(self, level):
        super().__init__()
        self.x, self.y = level.get_start_tile()
        self.image = pygame.image.load("assets/macgyver.png")
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft=(50 * self.x, 50 * self.y))

    def draw(self, surface):
        """Draws the player on the grid"""
        surface.blit(self.image, self.rect)

    def update(self, level, screen_width, screen_height):
        """Updates the player position on the grid,
        according to the move the player applies.
        Move is not allowed if the target tile
        is blocked by something (e.g. a wall)"""
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0 and pressed_keys[K_UP] and level.can_move(self.x, self.y - 1):
            self.rect.move_ip(0, -50)
            self.y -= 1
        if self.rect.bottom < screen_height and pressed_keys[K_DOWN] and level.can_move(self.x, self.y + 1):
            self.rect.move_ip(0, 50)
            self.y += 1
        if self.rect.left > 0 and pressed_keys[K_LEFT] and level.can_move(self.x - 1, self.y):
            self.rect.move_ip(-50, 0)
            self.x -= 1
        if self.rect.right < screen_width and pressed_keys[K_RIGHT] and level.can_move(self.x + 1, self.y):
            self.rect.move_ip(50, 0)
            self.x += 1

    def has_found_exit(self, level):
        """Returns True if the player reached the exit tile"""
        return level.is_exit_tile(self.x, self.y)
