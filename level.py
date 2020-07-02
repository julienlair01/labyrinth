# coding: utf-8
""" This is the level module. It will handle all actions
    relative to the level: generating the grid, putting items on
    tiles, finding a tile with specific coordinates. """
import random

import configparser

import tile


class Level:
    """ This is the class which represent the game level.
        It contains all methods needed to initialize,
        generate and manipulate elements on the grid. """

    def __init__(self):
        """ This is the Level clas constructor. It creates an empty
            list of tiles, which will be used to reprensent the grid. """
        self.tiles_list = []
        self.generate_level("level_config.ini")

    def generate_level(self, level_config_name="level_config.ini"):
        """ Creates map individual tiles in the tiles_list table,
        based on the layout in the config file. """
        config = configparser.ConfigParser()
        config.read(level_config_name)
        map_layout = config.get("level", "layout").split("\n")
        self.width = len(map_layout[0])
        self.height = len(map_layout)
        for y in range(self.height):
            for x in range(self.width):
                is_blocking = config.getboolean(map_layout[y][x], "is_blocking")
                tile_type = config.get(map_layout[y][x], "name")
                image = config.get(map_layout[y][x], "image")
                self.tiles_list.append(tile.Tile(tile_type, image, x, y, is_blocking))
        self.tiles_list = [self.tiles_list[x:x+self.width] for x in \
            range(0, len(self.tiles_list), self.width)]
        self.drop_items_on_grid()

    def get_start_tile(self):
        """ Returns the position of the start tile in the tiles_list table. """
        for y in range(self.height):
            for x in range(self.width):
                if self.tiles_list[y][x].tile_type == "start":
                    return self.tiles_list[y][x].x, self.tiles_list[y][x].y
        return None

    def get_exit_tile(self):
        """ Returns the position of the exit tile in the tiles_list table. """
        for y in range(self.height):
            for x in range(self.width):
                if self.tiles_list[y][x].tile_type == "exit":
                    return self.tiles_list[y][x].x, self.tiles_list[y][x].y
        return None

    def drop_items_on_grid(self):
        """ Position on the grid the 3 items Macgyver must pick to escape.
            It uses a temporary list of available tiles (no wall / character). """
        items_list = ["plastic_tube", "needle", "ether"]
        free_tiles_list = []
        for y in range(self.height):
            for x in range(self.width):
                if not self.tiles_list[y][x].is_blocking and \
                    self.tiles_list[y][x].tile_type != "exit" and \
                    self.tiles_list[y][x].tile_type != "start":
                    free_tiles_list.append(self.tiles_list[y][x])
        for item in items_list:
            index = random.randrange(0, len(free_tiles_list))
            free_tiles_list[index].add_element(item)

    def can_move(self, x, y):
        """ Returns True if tile is free to move to, False if it is blocked. """
        return not self.tiles_list[y][x].is_blocking

    def is_exit_tile(self, x, y):
        """ Returns True if the tile is the exit tile, where the guard stands.
            It is used to position the guard at the game initilization and to
            know whether the player reached the exit of the maze or not. """
        return (x, y) == self.get_exit_tile()

    def get_tile_element(self, x, y):
        """ Returns the element present on the tile where the player stands.
            This will be used to know if there is an item to be picked. """
        try:
            if self.tiles_list[y][x].element.is_pickable:
                return self.tiles_list[y][x].element
            else:
                return None
        except AttributeError:
            return None

    def draw(self, displaysurf):
        """Draws the map by drawing each tile of the grid,
        and the element located on the tile"""
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.tiles_list[y][x].draw(displaysurf)
                try:
                    if self.tiles_list[y][x].element:
                        self.tiles_list[y][x].element.draw(displaysurf)
                except AttributeError:
                    continue
