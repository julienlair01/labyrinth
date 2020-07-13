# coding: utf-8
""" Module containing the Element class, 
representing the items (plastic tube, needle and ether)
and the guard. """

import os

from constants import TILESIZE


class Element:

    def __init__(self, pos_x, pos_y, content):
        """ Constructor of the class Element.
        Specify whether an element is pickable or not,
        and whether the element has already been picked or not.

        Keyword arguments:
        pos_x -- x position of the tile the element is located on
        pos_y -- y position of the tile the element is located on
        content -- what the element contains (guard or item)
        """
        self.content = content
        self.is_picked = False
        if self.content == "guard":
            self.is_pickable = False
        else:
            self.is_pickable = True
