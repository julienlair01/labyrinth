# coding: utf-8
""" This module contains the GUILevel class.
    It extends the Player class with the pygame-related
    attributes, in order to play the game using a GUI. """

import level
import gui_tile


class GUILevel(level.Level):

    def __init__(self):
        super().__init__()

    def generate_level(self):
        """ Creates map individual tiles in the tiles_list table,
        based on the layout in the config file.
        """
        map_layout, config = self.load_config()
        for pos_y in range(self.height):
            for pos_x in range(self.width):
                is_blocking = config.getboolean(map_layout[pos_y][pos_x], "is_blocking")
                tile_type = config.get(map_layout[pos_y][pos_x], "name")
                image = config.get(map_layout[pos_y][pos_x], "image")
                self.tiles_list.append(gui_tile.GUITile(tile_type, image, pos_x, pos_y, is_blocking))
        self.tiles_list = [self.tiles_list[x:x+self.width] for x in range(0, len(self.tiles_list), self.width)]
        print("Level generation: OK")
        self.drop_items_on_grid()
        print("Items dropped on grid: OK")
