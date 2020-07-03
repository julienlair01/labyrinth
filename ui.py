# coding: utf-8

import pygame
from pygame.locals import *

from constants import FPS, TILESIZE

import level


class UI():

    # init surface and font and display tick
    # draw and update objects and texts
    # manage user inputs

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Escape MacGyver")
        self.font = pygame.font.Font(None, 28)
        self.text = self.font.render("Your bag: ", True, (0, 128, 0))
        self.frame_per_sec = pygame.time.Clock()

    def draw_level(self, level):
        self.displaysurf = pygame.display.set_mode((TILESIZE * level.width, TILESIZE * level.height + TILESIZE))
        level.draw(self.displaysurf)

    def draw_player(self, player):
        player.draw(self.displaysurf)
    
    def draw_text(self):
        self.displaysurf.blit(self.text, (45, 765))

    def update_player(self, player, level):
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
