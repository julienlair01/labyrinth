# coding: utf-8

import sys
import pygame
from pygame.locals import *
import level
import tile
import player
import element

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

while not player.has_found_exit(level):
    
    DISPLAYSURF = pygame.display.set_mode((50 * level.width, 50 * level.height))
    level.draw(DISPLAYSURF)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
      
    player.update(level, 50 * level.width, 50 * level.height)
    player.draw(DISPLAYSURF)

    if player.has_found_exit(level):
        print("Congrats, you escaped!")

    FramePerSec.tick(FPS)