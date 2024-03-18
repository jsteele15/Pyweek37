import pygame

class Settings():
    #colours
    UI_COLOUR = (255, 255, 255)


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
    month = 0
    months = ["Nov", "Dec", "Jan", "Feb", "Mar", "April","May"]
    passengers = 0

    clock = pygame.time.Clock()
