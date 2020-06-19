# coding: utf-8

import level, tile, pprint, pygame, sys, player
from pygame.locals import *

# Initialize program
pygame.init()
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TILE_SIZE = 50

level = level.Level()
player = player.Player()

while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF = pygame.display.set_mode((level.width * TILE_SIZE, level.height * TILE_SIZE))
    DISPLAYSURF.fill(WHITE)
    
    # Draw grid
    for y in range (0, level.height):
        for x in range (0, level.width):
            try:
                tileInfo = level.tilesList[y][x].getInfo()
            except IndexError:
                print("Index error for coord: ", x, y)
            level.tilesList[y][x].drawTile(DISPLAYSURF)
    
    player.drawPlayer(DISPLAYSURF)

    pygame.display.set_caption("Escape MacGyver")
    FramePerSec.tick(FPS)





