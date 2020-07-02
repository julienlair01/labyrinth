# coding: utf-8
""" This is the main file of the Escape MacGyver game.
    It initializes main game objects,
    and contains the main game loop """
import sys

import pygame
from pygame.locals import QUIT

import level
import player

FPS = 30
TILESIZE = 50

pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 28)
text = font.render("Your bag: ", True, (0, 128, 0))


FramePerSec = pygame.time.Clock()
level = level.Level()
player = player.Player(level)
pygame.display.set_caption("Escape MacGyver")
end_of_game = False

while not end_of_game:
    DISPLAYSURF = pygame.display.set_mode((50 * level.width, 50 * level.height + 50))
    level.draw(DISPLAYSURF)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    player.update(level, 50 * level.width, 50 * level.height)
    player.draw(DISPLAYSURF)
    player.draw_bag(DISPLAYSURF)
    DISPLAYSURF.blit(text, (45,765))
    if player.has_found_exit(level):
        end_of_game = True
        if player.has_picked_all_items():
            print("Congratulationss, you escaped!")
        else:
            print("Ooops... you lost!")

    FramePerSec.tick(FPS)
