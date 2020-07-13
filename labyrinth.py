# coding: utf-8
""" This is the main file of the Escape MacGyver game.
    It contains the Labyrinth class, initializing the main game objects,
    manages the main game loop and the end of game. """

from os import system

import level
import player
from gui import gui
from gui import gui_player
from gui import gui_level


class Game:

    def __init__(self, game_mode):
        if game_mode == "ui":
            self.level = gui_level.GUILevel()
            self.level.generate_level()
            self.player = gui_player.GUIPlayer(self.level)
            self.gui = gui.GUI(self.level)
        else:
            self.level = level.Level()
            self.level.generate_level()
            self.player = player.Player(self.level)         
        system("clear")
        print("Welcome to Escape MacGyver!\nPick the 3 items and find the exit. Enjoy !")

    def main_loop(self, game_mode):
        end_of_game = False
        while not end_of_game:
            if game_mode == "ui":
                self.gui.display_game(self.level, self.player)
                self.player.pick_item(self.level)
            else:
                print("This game mode is not yet supported.")
                end_of_game = True
            if self.player.has_found_exit(self.level):
                end_of_game = True
                if self.player.has_picked_all_items():
                    print("Congratulationss, you escaped!")
                    self.gui.draw_text("green", "Congratulations!", (415, 765))
                else:
                    print("Ooops... You did not pick all required items... You lost! HAHAHAHA!!!")
                    self.gui.draw_text("red", "You lost! HAHAHAHA!", (415, 765))

game_mode = "ui"
game = Game(game_mode)
game.main_loop(game_mode)
