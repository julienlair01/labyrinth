# coding: utf-8

import level, tile, pprint, pygame, sys, player, element
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
TILESIZE = 50

level = level.Level()
player = player.Player(level)
exitX, exitY = level.getExitTile()

pygame.display.set_caption("Escape MacGyver") 
foundExit = False

while not foundExit:
    
    DISPLAYSURF = pygame.display.set_mode((level.width * TILESIZE, level.height * TILESIZE))
    level.draw(DISPLAYSURF)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
      
    player.update(level.height * TILESIZE, level.width * TILESIZE, level)
    player.draw(DISPLAYSURF)
    
    if (player.x, player.y) == (exitX, exitY):
        print("Congrats, you found the exit!")
        foundExit = True

    FramePerSec.tick(FPS)