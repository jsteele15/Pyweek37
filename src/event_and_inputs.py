import pygame
import sys
from pygame.locals import*

def play_func(setting):
    setting.state = "cut_scene"

def skip_func(setting):
    setting.passengers = 0
    setting.state = "game"

def exit_func(setting):
    sys.exit()

def next_func(setting):
    setting.passengers = 0
    setting.txt_state += 1

def pause_func(setting):
    setting.game_speed_ind = 0
    setting.SPEED = setting.speeds[setting.game_speed_ind]
    setting.game_speed = setting.speeds[setting.game_speed_ind]

def norm_func(setting):
    setting.game_speed_ind = 1
    setting.SPEED = setting.speeds[setting.game_speed_ind]
    setting.game_speed = setting.speeds[setting.game_speed_ind]

def double_func(setting):
    setting.game_speed_ind = 2
    setting.SPEED = setting.speeds[setting.game_speed_ind]
    setting.game_speed = setting.speeds[setting.game_speed_ind]

def restart_func(setting):
    setting.month = 0
    setting.passengers = 0
    setting.crashes = 0
    setting.freezes = 0
    setting.speedys = 0
    setting.elections_won = 0
    for t in setting.train_list:
        t.refresh()

    setting.route_list = [setting.starter_r_1, setting.starter_r_2]
    setting.train_list = [setting.starter_t_1, setting.starter_t_2]
    setting.day_counter = setting.stored_counter

    for f in setting.fired_list:
        f = False

    for i in setting.part:
        i.refresh()

    setting.state = "game"


    

def actions(setting, train_list, button_list, tutorial_list, cross_list, tutorial_cross):

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

            if event.key == K_SPACE:
                if setting.game_speed_ind == 0:
                    setting.game_speed_ind = 1
                    setting.SPEED = setting.speeds[setting.game_speed_ind]
                    setting.game_speed = setting.speeds[setting.game_speed_ind]

                if setting.game_speed_ind >= 1:
                    setting.game_speed_ind = 0
                    setting.SPEED = setting.speeds[setting.game_speed_ind]
                    setting.game_speed = setting.speeds[setting.game_speed_ind]



        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                ###if the left mouse button is clicked on the train the train freezes
                for t in range(len(train_list)):
                    if train_list[t].col_rect.collidepoint(pos):
                        train_list[t].frozen = True

                for c in cross_list:
                    if c.hitbox.collidepoint(pos):
                        c.vertical = not c.vertical

                for t in range(len(tutorial_list)):
                    if tutorial_list[t].col_rect.collidepoint(pos):
                        tutorial_list[t].frozen = True

                for b in button_list:
                    if b.rect.collidepoint(pos):
                        b.clicked = True

                if tutorial_cross.hitbox.collidepoint(pos):
                    tutorial_cross.vertical = not tutorial_cross.vertical
                
                        
            if event.button == 3:
                for t in range(len(train_list)):
                    if train_list[t].col_rect.collidepoint(pos):
                        train_list[t].speedy = True

                for t in range(len(tutorial_list)):
                    if tutorial_list[t].col_rect.collidepoint(pos):
                        tutorial_list[t].speedy = True
"""
                        if train_list[t].x_pos % 2:
                            train_list[t].x_pos += 1

                        elif train_list[t].y_pos % 2:
                            train_list[t].y_pos += 1"""
