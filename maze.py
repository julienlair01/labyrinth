# coding: utf-8

import sys
import pygame
from pygame.locals import *
import level
import tile
import player
import element

FPS = 30
TILESIZE = 50

pygame.init()
FramePerSec = pygame.time.Clock()
level = level.Level()
player = player.Player(level)
pygame.display.set_caption("Escape MacGyver")
end_of_game = False

while not end_of_game:
    DISPLAYSURF = pygame.display.set_mode((50 * level.width, 50 * level.height))
    level.draw(DISPLAYSURF)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    player.update(level, 50 * level.width, 50 * level.height)
    player.draw(DISPLAYSURF)
    if player.has_found_exit(level) and player.has_picked_items():
            print("Congrats, you escaped!")
            end_of_game = True
    elif player.has_found_exit(level) and not player.has_picked_items():
            print("Ooops... you lost!")
            end_of_game = True


    FramePerSec.tick(FPS)
