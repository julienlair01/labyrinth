# coding: utf-8
""" This module contains the Player class and related methods.
    It is used by the main game loop, to generate the player character. """
import os

from constants import TILESIZE


class Player:
    """ Player class docstring"""
    def __init__(self, level):
        self.pos_x, self.pos_y = level.get_start_tile()
        self.bag = []

    def move(self, direction):
        """ Updates MacGyver coordinates according to movement applied by player. """
        if direction == "up":
            self.pos_y -= 1
        elif direction == "down":
            self.pos_y += 1
        elif direction == "left":
            self.pos_x -= 1
        elif direction == "right":
            self.pos_x += 1

    def has_found_exit(self, level):
        """Returns True if the player reached the exit tile"""
        return level.is_exit_tile(self.pos_x, self.pos_y)

    def pick_item(self, level):
        """ If there is an item on the tile,
            picks it and put in MacGyver's bag """
        element = level.pick_element(self.pos_x, self.pos_y)
        if element:
            self.bag.append(element)
            print("You picked an item:", element.content)

    def has_picked_all_items(self):
        """ Checks if Player has picked all 3 items. 
            Returns True or False. """
        return len(self.bag) == 3
