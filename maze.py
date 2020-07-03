# coding: utf-8
""" This is the main file of the Escape MacGyver game.
    It initializes main game objects,
    and contains the main game loop """
import sys

import pygame
from pygame.locals import QUIT

import level
import player
import ui
from ui import *
from constants import FPS, TILESIZE

ui = ui.UI()
level = level.Level()
player = player.Player(level)
end_of_game = False

while not end_of_game:

    ui.draw_level(level)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    ui.update_player(player, level)
    ui.draw_player(player)
    player.pick_item(level)
    ui.draw_text()
    if player.has_found_exit(level):
        end_of_game = True
        if player.has_picked_all_items():
            print("Congratulationss, you escaped!")
        else:
            print("Ooops... you lost!")
    ui.frame_per_sec.tick(FPS)
