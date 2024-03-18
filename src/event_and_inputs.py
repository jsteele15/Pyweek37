import pygame
import sys
from pygame.locals import*

def play_func(setting):
    setting.state = "game"

def skip_func(setting):
    print("skip")

def exit_func(setting):
    sys.exit()

def next_func(setting):
    pass


def actions(setting, train_list, button_list):

    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            setting.RUNNING = False
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                setting.RUNNING = False
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                ###if the left mouse button is clicked on the train the train freezes
                for t in range(len(train_list)):
                    if train_list[t].col_rect.collidepoint(pygame.mouse.get_pos()):
                        train_list[t].frozen = True

                for b in button_list:
                    if b.rect.collidepoint(pos):
                        b.clicked = True
                        
            if event.button == 3:
                for t in range(len(train_list)):
                    if train_list[t].col_rect.collidepoint(pygame.mouse.get_pos()):
                        train_list[t].speedy = True

