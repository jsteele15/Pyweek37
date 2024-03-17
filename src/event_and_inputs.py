import pygame
import sys
from pygame.locals import*


def actions(setting):
    for event in pygame.event.get():
        if event.type == QUIT:
            setting.RUNNING = False
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                setting.RUNNING = False
                sys.exit()

