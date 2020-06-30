# coding: utf-8

import random
import configparser
import tile


class Level:

    def __init__(self):
        self.tiles_list = []
        self.generate_level("level_config.ini")

    def generate_level(self, level_config_name="level_config.ini"):
        """Creates map individual tiles in the tiles_list table,
        based on the layout in the config file"""
        config = configparser.ConfigParser()
        config.read(level_config_name)
        map = config.get("level", "layout").split("\n")
        self.width = self.get_width(map)
        self.height = self.get_height(map)
        for y in range(self.height):
            for x in range(self.width):
                is_blocking = config.getboolean(map[y][x], "block")
                tile_type = config.get(map[y][x], "name")
                image = config.get(map[y][x], "bg_image")
                self.tiles_list.append(tile.Tile(tile_type, image, x, y, is_blocking))
        self.tiles_list = [self.tiles_list[x:x+self.width]for x in range(0, len(self.tiles_list), self.width)]
        self.generate_items()


    def get_width(self, map):
        """Returns width of the level, in number of tiles"""
        return len(map[0])

    def get_height(self, map):
        """Returns height of the level, in number of tiles"""
        return len(map)

    def get_start_tile(self):
        """Returns the position of the start tile in the tiles_list table"""
        for y in range(self.height):
            for x in range(self.width):
                if self.tiles_list[y][x].tile_type == "start":
                    print("Found start tile:", x, y)
                    return self.tiles_list[y][x].x, self.tiles_list[y][x].y
        return None

    def get_exit_tile(self):
        """Returns the position of the exit tile in the tiles_list table """
        for y in range(self.height):
            for x in range(self.width):
                if self.tiles_list[y][x].tile_type == "exit":
                    return self.tiles_list[y][x].x, self.tiles_list[y][x].y
        return None

    def generate_items(self):
        """Position the 3 items Macgyved needs to pick on the grid"""
        items_list = ["tube", "needle", "ether"]
        tiles_list_free = []
        for y in range(self.height):
            for x in range(self.width):
                if not self.tiles_list[y][x].is_blocking and self.tiles_list[y][x].tile_type != "exit" and self.tiles_list[y][x].tile_type != "start":
                    tiles_list_free.append(self.tiles_list[y][x])
        for item in items_list:
            rand = random.randrange(0, len(tiles_list_free))
            tiles_list_free[rand].add_element(item)
            print(item, tiles_list_free[rand].x, tiles_list_free[rand].y)

    def can_move(self, x, y):
        """Returns True if tile is free to move to, or to get an element added,
        False if it is blocked"""
        return not self.tiles_list[y][x].is_blocking

    def is_exit_tile(self, x, y):
        return (x, y) == self.get_exit_tile()

    def draw(self, displaysurf):
        """Draws the map by drawing each tile of the grid,
        and the element of the tile"""
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.tiles_list[y][x].draw(displaysurf)
                try:
                    if self.tiles_list[y][x].element:
                        self.tiles_list[y][x].element.draw(displaysurf)
                except AttributeError:
                    continue
