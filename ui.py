# coding: utf-8
""" This module contains the UI class.
    It manages everything that is needed to display
    the game on the screen, using pygame. """

import os
import sys

import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT

from constants import TILESIZE, FPS


class UI:

    def __init__(self, level):
        """ Constructor of the class UI.
        Initializes pygame.

        Keyword arguments:
        level -- an instance of the class Level
        """
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Escape MacGyver")
        self.font = pygame.font.Font(None, 28)
        self.displaysurf = pygame.display.set_mode((TILESIZE * level.width, TILESIZE * level.height + TILESIZE))
        self.displaysurf.fill("grey")
        self.frame_per_sec = pygame.time.Clock()

    def display_game(self, level, player):
        """ Displays and updates the game objects on the screen.

        Keyword arguments:
        level -- an instance of the class Level
        player -- an instance if the class Player
        """
        self.draw_ui(level, player)
        self.pygame_event_get()
        self.update_player(level, player)
        self.frame_per_sec.tick(FPS)

    def draw_ui(self, level, player):
        """ Draws the game UI.

        Keyword arguments:
        level -- an instance of the class Level
        player -- an instance if the class Player
        """
        self.draw_level(level)
        self.draw_player(player)
        self.draw_text("black", "Your bag: ", (45, 765))

    def draw_level(self, level):
        """ Draws the map by drawing each tile of the grid,
        and the element located on the tile.

        Keyword arguments:
        level -- an instance of the class Level
        """
        self.displaysurf = pygame.display.set_mode((TILESIZE * level.width, TILESIZE * level.height + TILESIZE))
        for pos_y in range(0, level.height):
            for pos_x in range(0, level.width):
                level.tiles_list[pos_y][pos_x].draw(self.displaysurf)
                try:
                    if level.tiles_list[pos_y][pos_x].element:
                        self.draw_element(level.tiles_list[pos_y][pos_x].element)
                except AttributeError:
                    continue

    def draw_element(self, element):
        """ Draws an element on a specific tile:
        can be one of the unpicked items or the guard

        Keyword arguments:
        element -- an instance of the class Element
        """
        if not element.is_picked:
            self.displaysurf.blit(element.image, element.rect)

    def draw_player(self, player):
        """ Draws the player on the grid, according to its position.
        Draws also the player's bag, containing the items picked
        by the player. 
        
        Keyword arguments:
        player -- an instance of the class Player
        """
        self.displaysurf.blit(player.image, player.rect)
        if player.bag:
            for index, value in enumerate(player.bag):
                surf = pygame.Surface((TILESIZE, TILESIZE))
                rect = surf.get_rect(topleft=(3 * TILESIZE + TILESIZE * index, 750))
                img_filename = value.content + ".png"
                absolute_path = os.path.join(os.path.dirname(__file__), "assets", img_filename)
                image = pygame.image.load(absolute_path)
                self.displaysurf.blit(image, rect)

    def draw_text(self, color, message, text_position):
        """ Draws the text representing the player's bag
        at the bottom of the screen.

        Keyword arguments:
        color -- the color of the text
        message -- the text to be displayed
        text_position -- position of the text on the screen
        """
        self.text = self.font.render(message, True, color)
        self.displaysurf.blit(self.text, text_position)

    def update_player(self, level, player):
        """ Converts the user input into a moving direction
        for the player and update the player's sprite.

        Keyword arguments:
        level -- an instance of the class Level
        player -- an instance if the class Player
        """
        pressed_keys = pygame.key.get_pressed()
        if player.rect.top > 0 and pressed_keys[K_UP] and level.can_move(player.pos_x, player.pos_y - 1):
            player.rect.move_ip(0, -TILESIZE)
            player.move("up")
        if player.rect.bottom < level.height * TILESIZE and pressed_keys[K_DOWN] and level.can_move(player.pos_x, player.pos_y + 1):
            player.rect.move_ip(0, TILESIZE)
            player.move("down")
        if player.rect.left > 0 and pressed_keys[K_LEFT] and level.can_move(player.pos_x - 1, player.pos_y):
            player.rect.move_ip(-TILESIZE, 0)
            player.move("left")
        if player.rect.right < level.width * TILESIZE and pressed_keys[K_RIGHT] and level.can_move(player.pos_x + 1, player.pos_y):
            player.rect.move_ip(TILESIZE, 0)
            player.move("right")

    def pygame_event_get(self):
        """ Captures event for pygame. """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
