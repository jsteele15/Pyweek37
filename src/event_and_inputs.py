import pygame
import sys
from pygame.locals import*


def actions(setting, train_list):

    ###this allows you to pause trains by hovering over them
    for t in range(len(train_list)):
        if train_list[t].col_rect.collidepoint(pygame.mouse.get_pos()):
            train_list[t].multi = 0
            #train_list[t].fired = True
        else:
            train_list[t].multi = 1

    for event in pygame.event.get():
        if event.type == QUIT:
            setting.RUNNING = False
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                setting.RUNNING = False
                sys.exit()

