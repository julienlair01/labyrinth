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
# game_mode = input("Tapez text ou ui :")
game_mode = "ui"

while not end_of_game:
    if game_mode == "ui":
        ui.draw_ui(level, player)
        ui.update_player(level, player)
    elif game_mode == "text":
        # text.update.player(level, player)
        pass
    player.pick_item(level)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if player.has_found_exit(level):
        end_of_game = True
        if player.has_picked_all_items():
            print("Congratulationss, you escaped!")
        else:
            print("Ooops... you lost!")
    ui.frame_per_sec.tick(FPS)
