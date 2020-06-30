# coding: utf-8

import level, tile, pprint, pygame, sys, player, element
from pygame.locals import *

# Initialize program
pygame.init()
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
TILESIZE = 50

level = level.Level()
player = player.Player(level)

pygame.display.set_caption("Escape MacGyver") 
foundExit = False

while not player.hasFoundExit(level):
    
    DISPLAYSURF = pygame.display.set_mode((50 * level.width, 50 * level.height))
    level.draw(DISPLAYSURF)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
      
    player.update(50 * level.height, 50 * level.width, level)
    player.draw(DISPLAYSURF)

    if player.hasFoundExit(level):
        print("Congrats, you escaped!")

    FramePerSec.tick(FPS)