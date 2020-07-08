# coding: utf-8
""" This is the main file of the Escape MacGyver game.
    It initializes main game objects, calls the right method
    according to game mode (UI or text) and contains the main game loop. """

import level
import player
import ui
from constants import FPS


class Labyrinth:

    def __init__(self):
        self.level = level.Level()
        self.player = player.Player(self.level)
        self.ui = ui.UI(self.level)

    def main_loop(self):
        end_of_game = False
        while not end_of_game:
            self.ui.display_game(self.level, self.player, FPS)
            self.player.pick_item(self.level)
            if self.player.has_found_exit(self.level):
                end_of_game = True
                if self.player.has_picked_all_items():
                    print("Congratulationss, you escaped!")
                else:
                    print("Ooops... You did not pick all required items... You lost! HAHAHAHA!!!")

game = Labyrinth()
game.main_loop()