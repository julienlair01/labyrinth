# coding: utf-8

import level, tile, pprint, pygame, sys
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
SCREEN_WIDTH = 250
SCREEN_HEIGHT = 250
TILE_SIZE = 50

level = level.Level()
print(level.tilesList[1][1].getInfo())

while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    DISPLAYSURF.fill(WHITE)
    
    # Draw grid
    for y in range (0, 5):
        for x in range (0, 5):
            tileInfo = level.tilesList[y][x].getInfo()
            level.tilesList[y][x].drawTile(DISPLAYSURF)

    pygame.display.set_caption("Escape MacGyver")
    FramePerSec.tick(FPS)





