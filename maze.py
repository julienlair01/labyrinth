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
    if player.has_found_exit(level):
        i = 0
        for value in player.dict_bag.values():
            i += 1
        if i == 3:
            print("Congrats, you escaped!")
            end_of_game = True
        else:
            print("Ooops... you lost!")
            end_of_game = True
    FramePerSec.tick(FPS)
