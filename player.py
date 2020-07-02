# coding: utf-8

import os
import pygame
from pygame.locals import *
import level


class Player(pygame.sprite.Sprite):

    def __init__(self, level):
        super().__init__()
        self.x, self.y = level.get_start_tile()
        self.bag = []
        absolute_path = os.path.join(os.path.dirname(__file__), "assets", "MacGyver.png")
        self.image = pygame.image.load(absolute_path)
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(topleft=(50 * self.x, 50 * self.y))

    def draw(self, surface):
        """Draws the player on the grid"""
        surface.blit(self.image, self.rect)

    def update(self, level, screen_width, screen_height):
        """Updates the player position on the grid, according to the move the player applies.
        Move is not allowed if the target tile is blocked by something (a wall or the map boundaries)"""
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0 and pressed_keys[pygame.K_UP] and level.can_move(self.x, self.y - 1):
            self.rect.move_ip(0, -50)
            self.y -= 1
        if self.rect.bottom < screen_height and pressed_keys[pygame.K_DOWN] and level.can_move(self.x, self.y + 1):
            self.rect.move_ip(0, 50)
            self.y += 1 
        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT] and level.can_move(self.x - 1, self.y):
            self.rect.move_ip(-50, 0)
            self.x -= 1
        if self.rect.right < screen_width and pressed_keys[pygame.K_RIGHT] and level.can_move(self.x + 1, self.y):
            self.rect.move_ip(50, 0)
            self.x += 1
        self.pick_item(level)

    def has_found_exit(self, level):
        """Returns True if the player reached the exit tile"""
        return level.is_exit_tile(self.x, self.y)

    def pick_item(self, level):
        """Checks if there is an item on the tile and picks it if so"""
        try: 
            if level.tile_has_element(self.x, self.y) not in self.bag:
                element = level.get_tile_element(self.x, self.y)
                self.bag.append(element)
                print("Picked", element.content)
        except AttributeError:
            pass
    
    def has_picked_all_items(self):
        """Checks if Player has picked all 3 items"""
        return len(self.bag) == 3
