# coding: utf-8

import os
import sys

import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT

from constants import TILESIZE


class UI():

    def __init__(self, level):
        """ Constructor of the class UI. It initializes pygame. """
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Escape MacGyver")
        self.font = pygame.font.Font(None, 28)
        self.text = self.font.render("Your bag: ", True, (0, 128, 0))
        self.frame_per_sec = pygame.time.Clock()

    def draw_ui(self, level, player):
        """ Draws the entire game UI by calling the respective method
        for each element of the ui """
        self.draw_level(level)
        self.draw_player(player)
        self.draw_text()

    def draw_level(self, level):
        """ Draws the map by drawing each tile of the grid,
        and the element located on the tile """
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
        can be one of the unpicked items or the guard """
        if not element.is_picked:
            self.displaysurf.blit(element.image, element.rect)

    def draw_player(self, player):
        """ Draws the player on the grid, according to its position.
        Draws also the player's bag, containing the items picked
        by the player. """
        self.displaysurf.blit(player.image, player.rect)
        if player.bag:
            for index, value in enumerate(player.bag):
                surf = pygame.Surface((TILESIZE, TILESIZE))
                rect = surf.get_rect(topleft=(3 * TILESIZE + TILESIZE * index, 750))
                img_filename = value.content + ".png"
                absolute_path = os.path.join(os.path.dirname(__file__), "assets", img_filename)
                image = pygame.image.load(absolute_path)
                self.displaysurf.blit(image, rect)

    def draw_text(self):
        """ Draws the text representing the plyaer's bag
        at the bottom of the screen. """
        self.displaysurf.blit(self.text, (45, 765))

    def update_player(self, level, player):
        """ Converts the user input into a moving direction
        for the player. It only updates the sprite of the player
        and calls the player method move, which manages
        the coordinates update. """
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
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
