# coding: utf-8
""" This module contains the Player class and related methods.
    It is used by the main game loop, to generate the player character. """
import os

import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

from constants import TILESIZE


class Player(pygame.sprite.Sprite):
    """ Player class docstring"""
    def __init__(self, level):
        super().__init__()
        self.pos_x, self.pos_y = level.get_start_tile()
        self.bag = []
        absolute_path = os.path.join(os.path.dirname(__file__), "assets", "MacGyver.png")
        self.image = pygame.image.load(absolute_path)
        self.surf = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.surf.get_rect(topleft=(TILESIZE * self.pos_x, TILESIZE * self.pos_y))

    def get_position(self):
        return self.pos_x, self.pos_y

    def move(self, direction):
        if direction == "up":
            self.pos_y -= 1
        elif direction == "down":
            self.pos_y += 1
        elif direction == "left":
            self.pos_x -= 1
        elif direction == "right":
            self.pos_x += 1
        else:
            raise
        print("Moving", direction)


    def draw(self, surface):
        """Draws the player on the grid"""
        surface.blit(self.image, self.rect)
        if self.bag:
            for index, value in enumerate(self.bag):
                surf = pygame.Surface((TILESIZE, TILESIZE))
                rect = surf.get_rect(topleft=(3 * TILESIZE + TILESIZE * index, 750))
                img_filename = value.content + ".png"
                absolute_path = os.path.join(os.path.dirname(__file__), "assets", img_filename)
                image = pygame.image.load(absolute_path)
                surface.blit(image, rect)

    # def update(self, level, screen_width, screen_height):
    #     """Updates MacGyver's position on the grid,
    #     according to the direction given by the player.
    #     Move is not allowed if the target tile is blocked by something
    #     (wall or map boundary)"""
    #     pressed_keys = pygame.key.get_pressed()
    #     if self.rect.top > 0 and pressed_keys[K_UP] and level.can_move(self.pos_x, self.pos_y - 1):
    #         self.rect.move_ip(0, -TILESIZE)
    #         self.pos_y -= 1
    #     if self.rect.bottom < screen_height and pressed_keys[K_DOWN] and level.can_move(self.pos_x, self.pos_y + 1):
    #         self.rect.move_ip(0, TILESIZE)
    #         self.pos_y += 1
    #     if self.rect.left > 0 and pressed_keys[K_LEFT] and level.can_move(self.pos_x - 1, self.pos_y):
    #         self.rect.move_ip(-TILESIZE, 0)
    #         self.pos_x -= 1
    #     if self.rect.right < screen_width and pressed_keys[K_RIGHT] and level.can_move(self.pos_x + 1, self.pos_y):
    #         self.rect.move_ip(TILESIZE, 0)
    #         self.pos_x += 1
    #     self.pick_item(level)

    def has_found_exit(self, level):
        """Returns True if the player reached the exit tile"""
        return level.is_exit_tile(self.pos_x, self.pos_y)

    def pick_item(self, level):
        """ If there is an item on the tile,
            picks it and put in MacGyver's bag """
        element = level.pick_element(self.pos_x, self.pos_y)
        if element:
            self.bag.append(element)

    def has_picked_all_items(self):
        """Checks if Player has picked all 3 items"""
        return len(self.bag) == 3
