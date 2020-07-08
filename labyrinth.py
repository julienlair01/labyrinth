# coding: utf-8
""" This is the main file of the Escape MacGyver game.
    It initializes main game objects, calls the right method
    according to game mode (UI or text) and contains the main game loop. """

import level
import player
import ui
from constants import FPS

level = level.Level()
player = player.Player(level)
ui = ui.UI(level)
end_of_game = False
# game_mode = input("Do you want to play the text or the nice UI version (type text or ui to continue)\n")
game_mode = "ui"

while not end_of_game:
    if game_mode == "ui":
        ui.draw_ui(level, player)
        ui.pygame_event_get()
        ui.update_player(level, player)
        player.pick_item(level)
        ui.frame_per_sec.tick(FPS)
    elif game_mode == "text":
        # text.update.player(level, player)
        # player.pick_item(level)
        print("Not supported yet... coming soon...")
        end_of_game = True
    if player.has_found_exit(level):
        end_of_game = True
        if player.has_picked_all_items():
            print("Congratulationss, you escaped!")
        else:
            print("Ooops... You did not pick all required items... You lost! HAHAHAHA!!!")
