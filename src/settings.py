import pygame

class Settings():


    #for the screen size
    HEIGHT = 600
    WIDTH = 800

    #for the program to run
    RUNNING = True

    #for train speed
    SPEED = 1

    #game speed, for how fast the days go by
    #1000 is the standard speed
    #if you wanted to double the speed you could change it to 500
    game_speed = 1000

    ##for the day
    month = 1
    months = ["Nov", "Dec", "Jan", "Feb", "Mar", "April","May"]
    passengers = 0

    ###a state to control whats playing
    #[main_menu, cut_scene, game, end_scene]
    state = "main_menu"
    #1 or 2
    txt_state = 1

    clock = pygame.time.Clock()
