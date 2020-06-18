# coding: utf-8

import configparser, tile

class Level:
    def __init__(self):
        self.tilesList = []
        self.generateLevel("levelconfig.ini")

    def generateLevel(self, levelConfigfilename = "levelconfig.ini"):
        config = configparser.ConfigParser()
        config.read(levelConfigfilename)
        self.map = config.get("level", "layout").split("\n")
        self.height = len(self.map)
        self.width = len(self.map[0])
        for y in range(self.height):
            for x in range(self.width):
                block = config.getboolean(self.map[y][x], "block")
                tileType = config.get(self.map[y][x], "name")
                image = config.get(self.map[y][x], "image")
                self.tilesList.append(tile.Tile(tileType, image, x, y, block))
        self.tilesList = [self.tilesList[x:x+5] for x in range(0, len(self.tilesList), 5)]