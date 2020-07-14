# coding: utf-8

import element


class Tile():

    def __init__(self, tile_type, pos_x, pos_y, is_blocking):
        """ Constructor of the class Tile.
        Initializes attribute of a single tile, according to layout.

        Keyword arguments:
        tile_type -- wall, floor, start or exit
        image -- image representing the tile
        pos_x -- x position of the tile
        pos_y -- y position of the tile
        is_blocking -- whether the tile blocks (wall) or not
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tile_type = tile_type
        self.is_blocking = is_blocking
        self.element = []
        if self.tile_type == "exit":
            self.add_element("guard")

    def add_element(self, element_type):
        """Adds an element on the tile (guard or item).

        Keyword arguments:
        element_type -- guard or item
        """
        if element_type == "guard":
            self.element = element.Element(self.pos_x, self.pos_y,
                                           element_type)
        # elif element_type == "plastic_tube":
        #     self.element = element.Element(self.pos_x, self.pos_y,
        #                                    element_type)
        # elif element_type == "needle":
        #     self.element = element.Element(self.pos_x, self.pos_y,
        #                                    element_type)
        # elif element_type == "ether":
        #     self.element = element.Element(self.pos_x, self.pos_y,
        #                                    element_type)
