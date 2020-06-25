# coding: utf-8

import configparser, tile

class Level:
    
    def __init__(self):
        self.tilesList = []
        self.generateLevel("levelconfig.ini")
        # init exit and start tiles

    def generateLevel(self, levelConfigfilename = "levelconfig.ini"):
        """Creates map individual tiles in the tilesList table, based on the layout in the config file"""
        config = configparser.ConfigParser()
        config.read(levelConfigfilename)
        self.map = config.get("level", "layout").split("\n") # map only, only used in that case
        self.getSize()
        for y in range(self.height):
            for x in range(self.width):
                block = config.getboolean(self.map[y][x], "block")
                tileType = config.get(self.map[y][x], "name")
                image = config.get(self.map[y][x], "bg_image")
                self.tilesList.append(tile.Tile(tileType, image, x, y, block))
        self.tilesList = [self.tilesList[x:x+self.width] for x in range(0, len(self.tilesList), self.width)]

    def getSize(self): # calculate / generate size better
        """Measure the size of the map, according to the layout"""
        self.height = len(self.map)
        self.width = len(self.map[0])

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


    def canMove(self, x, y):
        """Returns True if tile is free to move to, or to get an element added, False if it is blocked"""
        return self.tilesList[y][x].block == False # is blocking


    def draw(self, displaysurf):
        """Draws the map by drawing each tile of the grid, and the element of the tile"""
        for y in range (0, self.height):
            for x in range (0, self.width):
                self.tilesList[y][x].draw(displaysurf)
                if self.tilesList[y][x].elements:
                    for i in range (0, len(self.tilesList[y][x].elements)):
                        self.tilesList[y][x].elements[i].draw(displaysurf)