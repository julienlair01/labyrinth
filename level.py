# coding: utf-8

import configparser, tile

class Level:
    
    def __init__(self):
        self.tilesList = []
        self.generateLevel("levelconfig.ini")
        self.startTile = self.getStartTile()
        self.exitTile = self.getExitTile()

    def generateLevel(self, levelConfigfilename = "levelconfig.ini"):
        """Creates map individual tiles in the tilesList table, based on the layout in the config file"""
        config = configparser.ConfigParser()
        config.read(levelConfigfilename)
        map = config.get("level", "layout").split("\n")
        self.calculateSize(map)
        for y in range(self.height):
            for x in range(self.width):
                block = config.getboolean(map[y][x], "block")
                tileType = config.get(map[y][x], "name")
                image = config.get(map[y][x], "bg_image")
                self.tilesList.append(tile.Tile(tileType, image, x, y, block))
        self.tilesList = [self.tilesList[x:x+self.width] for x in range(0, len(self.tilesList), self.width)]

    def calculateSize(self, map):
        """Measures the size of the map, according to the layout"""
        self.height = len(map)
        self.width = len(map[0])

    def getStartTile(self):  
        """Returns the position of the start tile in the tilesList table"""
        for y in range(self.height):
            for x in range(self.width):   
                if self.tilesList[y][x].tileType == "start":
                    print("Found start tile:", x, y)
                    return self.tilesList[y][x].x, self.tilesList[y][x].y
        return None 


    def getExitTile(self):
        """Returns the position of the exit tile in the tilesList table """
        for y in range(self.height):
            for x in range(self.width):
                if self.tilesList[y][x].tileType == "exit":
                    return self.tilesList[y][x].x, self.tilesList[y][x].y
        return None 


    def isExitTile(self, x, y):
        return (x, y) == self.exitTile


    def canMove(self, x, y):
        """Returns True if tile is free to move to, or to get an element added, False if it is blocked"""
        return self.tilesList[y][x].isBlocking == False


    def draw(self, displaysurf):
        """Draws the map by drawing each tile of the grid, and the element of the tile"""
        for y in range (0, self.height):
            for x in range (0, self.width):
                self.tilesList[y][x].draw(displaysurf)
                try:
                    if self.tilesList[y][x].element:
                        self.tilesList[y][x].element.draw(displaysurf)
                except AttributeError:
                    continue