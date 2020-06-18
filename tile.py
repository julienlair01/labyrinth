# coding: utf-8

class Tile():
    def __init__(self, tileType, image, x, y, block):
        self.tileType = tileType
        self.image = ""
        self.x = x
        self.y = y
        self.block = block
        self.object = None
        
    def getInfo(self, x, y):
        return self.block
