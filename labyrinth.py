# coding: utf-8
""" This is the main file of the Escape MacGyver game.
    It contains the Labyrinth class, initializing the main game objects,
    and manages the main game loop. """

from os import system

import level
import player
import ui
from constants import FPS


class Labyrinth:

    def __init__(self):
        self.level = level.Level()
        self.player = player.Player(self.level)
        self.ui = ui.UI(self.level)
        system("clear")
        print("Welcome to Escape MacGyver!\nPick the 3 items and find the exit. Enjoy !")

    def main_loop(self):
        end_of_game = False
        while not end_of_game:
            self.ui.display_game(self.level, self.player)
            self.player.pick_item(self.level)
            if self.player.has_found_exit(self.level):
                end_of_game = True
                if self.player.has_picked_all_items():
                    print("Congratulationss, you escaped!")
                    self.ui.draw_text("green", "Congratulations!", (415, 765))
                else:
                    print("Ooops... You did not pick all required items... You lost! HAHAHAHA!!!")
                    self.ui.draw_text("red", "You lost! HAHAHAHA!", (415, 765))

game = Labyrinth()
game.main_loop()
