# coding: utf-8
""" This is the level module. It will handle all actions
    relative to the level: generating the grid, putting items on
    tiles, finding a tile with specific coordinates. """
import random
import os

import configparser

import tile
from gui import gui_tile


class Level:
    """ This is the class which represent the game level.
    It contains all methods needed to initialize,
    generate and manipulate elements on the grid.
    """

    def __init__(self, game_mode):
        """ This is the Level clas constructor. It creates an empty
        list of tiles, which will be used to reprensent the grid.
        """
        self.tiles_list = []
        self.generate_level(game_mode)

    def generate_level(self, game_mode):
        """ Creates map individual tiles in the tiles_list table,
        based on the layout in the config file.
        """
        config = configparser.ConfigParser()
        absolute_path = os.path.join(os.path.dirname(__file__), "level_config.ini")
        config.read(absolute_path)
        map_layout = config.get("level", "layout").split("\n")
        self.width = len(map_layout[0])
        self.height = len(map_layout)
        for pos_y in range(self.height):
            for pos_x in range(self.width):
                is_blocking = config.getboolean(map_layout[pos_y][pos_x], "is_blocking")
                tile_type = config.get(map_layout[pos_y][pos_x], "name")
                image = config.get(map_layout[pos_y][pos_x], "image")
                if game_mode == "ui":
                    self.tiles_list.append(gui_tile.GUITile(tile_type, image, pos_x, pos_y, is_blocking))
                else:
                    self.tiles_list.append(tile.Tile(tile_type, image, pos_x, pos_y, is_blocking))
        self.tiles_list = [self.tiles_list[x:x+self.width] for x in range(0, len(self.tiles_list), self.width)]
        print("Level generation: OK")
        self.drop_items_on_grid()
        print("Items dropped on grid: OK")

    def get_start_tile(self):
        """ Returns the position of the start tile in the tiles_list table. """
        for pos_y in range(self.height):
            for pos_x in range(self.width):
                if self.tiles_list[pos_y][pos_x].tile_type == "start":
                    return pos_x, pos_y
        return None

    def get_exit_tile(self):
        """ Returns the position of the exit tile in the tiles_list table. """
        for pos_y in range(self.height):
            for pos_x in range(self.width):
                if self.tiles_list[pos_y][pos_x].tile_type == "exit":
                    return pos_x, pos_y
        return None

    def drop_items_on_grid(self):
        """ Position on the grid the 3 items Macgyver must pick to escape.
        It uses a temporary list of available tiles (no wall / character).
        """
        items_list = ["plastic_tube", "needle", "ether"]
        free_tiles_list = []
        for pos_y in range(self.height):
            for pos_x in range(self.width):
                if not self.tiles_list[pos_y][pos_x].is_blocking and self.tiles_list[pos_y][pos_x].tile_type != "exit" and self.tiles_list[pos_y][pos_x].tile_type != "start":
                    free_tiles_list.append(self.tiles_list[pos_y][pos_x])
        for item in items_list:
            index = random.randrange(0, len(free_tiles_list))
            free_tiles_list[index].add_element(item)

    def can_move(self, pos_x, pos_y):
        """ Returns True if tile is free to move to, False if it is blocked. 

        Keyword arguments:
        pos_x -- x position of the tile to check
        pos_y -- y position fo the tiel to check
        """
        return not self.tiles_list[pos_y][pos_x].is_blocking

    def is_exit_tile(self, pos_x, pos_y):
        """ Returns True if the tile is the exit tile, where the guard stands.
            It is used to position the guard at the game initilization and to
            know whether the player reached the exit of the maze or not.

            Keyword arguments:
            pos_x -- x position of the tile to check
            pos_y -- y position fo the tiel to check
        """
        return (pos_x, pos_y) == self.get_exit_tile()

    def pick_element(self, pos_x, pos_y):
        """ Returns the element present on the tile where the player stands.

            Keyword arguments:
            pos_x -- x position of the tile to check
            pos_y -- y position fo the tiel to check
            """
        if self.tiles_list[pos_y][pos_x].element and self.tiles_list[pos_y][pos_x].element.is_pickable:
            element = self.tiles_list[pos_y][pos_x].element
            self.tiles_list[pos_y][pos_x].element = None
            return element
        else:
            return None

