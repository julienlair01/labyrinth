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
        self.getLevelSize()
        for y in range(self.height):
            for x in range(self.width):
                block = config.getboolean(self.map[y][x], "block")
                tileType = config.get(self.map[y][x], "name")
                image = config.get(self.map[y][x], "image")
                self.tilesList.append(tile.Tile(tileType, image, x, y, block))
        self.tilesList = [self.tilesList[x:x+self.width] for x in range(0, len(self.tilesList), self.width)]

    def getLevelSize(self):
        self.height = len(self.map)
        self.width = len(self.map[0])

    def getStartTile(self):  
        for y in range(self.height):
            for x in range(self.width):   
                if self.tilesList[y][x].tileType == "start":
                    print("Found start tile:", x, y)
                    return self.tilesList[y][x].x, self.tilesList[y][x].y
        return None 

    def getExitTile(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.tilesList[y][x].tileType == "exit":
                    return self.tilesList[y][x].x, self.tilesList[y][x].y
        return None 

    def canMove(self, x, y):
        if self.tilesList[y][x].block == False:
            return True
        elif self.tilesList[y][x].block:
            return False
        else:
            return False

    def draw(self, displaysurf):
        for y in range (0, self.height):
            for x in range (0, self.width):
                try:
                    tileInfo = self.tilesList[y][x].getInfo()
                except IndexError:
                    print("Index error for coord: ", x, y)
                self.tilesList[y][x].draw(displaysurf)
                if self.tilesList[y][x].elements:
                    for i in range (0, len(self.tilesList[y][x].elements)):
                        self.tilesList[y][x].elements[i].draw(displaysurf)