import pygame
import sys
from pygame.locals import*

def play_func(setting):
    setting.state = "cut_scene"

def skip_func(setting):
    setting.state = "game"

def exit_func(setting):
    sys.exit()

def next_func(setting):
    setting.txt_state += 1



def actions(setting, train_list, button_list, tutorial_list):

    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            setting.RUNNING = False
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                setting.RUNNING = False
                sys.exit()

            if event.key == K_d:
                if setting.game_speed_ind < 2:
                    setting.game_speed_ind += 1
                    setting.SPEED = setting.speeds[setting.game_speed_ind]
                    setting.game_speed = setting.speeds[setting.game_speed_ind]
            
            if event.key == K_a:
                if setting.game_speed_ind > 0:
                    setting.game_speed_ind -= 1
                    setting.SPEED = setting.speeds[setting.game_speed_ind]
                    setting.game_speed = setting.speeds[setting.game_speed_ind]


        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                ###if the left mouse button is clicked on the train the train freezes
                for t in range(len(train_list)):
                    if train_list[t].col_rect.collidepoint(pygame.mouse.get_pos()):
                        train_list[t].frozen = True

                for t in range(len(tutorial_list)):
                    if tutorial_list[t].col_rect.collidepoint(pygame.mouse.get_pos()):
                        tutorial_list[t].frozen = True

                for b in button_list:
                    if b.rect.collidepoint(pos):
                        b.clicked = True
                        
            if event.button == 3:
                for t in range(len(train_list)):
                    if train_list[t].col_rect.collidepoint(pygame.mouse.get_pos()):
                        train_list[t].speedy = True

                for t in range(len(tutorial_list)):
                    if tutorial_list[t].col_rect.collidepoint(pygame.mouse.get_pos()):
                        tutorial_list[t].speedy = True
"""
                        if train_list[t].x_pos % 2:
                            train_list[t].x_pos += 1

                        elif train_list[t].y_pos % 2:
                            train_list[t].y_pos += 1"""
