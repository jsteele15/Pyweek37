import pygame

class Settings():


    #for the screen size
    HEIGHT = 600
    WIDTH = 800

    #for the program to run
    RUNNING = True

    

    #game speed, for how fast the days go by
    #0.01 is paused, 1 is normal, 2 is double speed
    speeds = [0, 1, 2]
    game_speed_ind = 1
    game_speed = speeds[game_speed_ind]
    
    #for train speed
    SPEED = speeds[game_speed_ind]

    ##for the day
    month = 1
    months = ["Nov", "Dec", "Jan", "Feb", "Mar", "April","May"]
    
    day_counter = 24
    stored_counter = 0

    ###stats for the end
    passengers = 0
    crashes = 0
    freezes = 0
    speedys = 0
    elections_won = 0
    end_txts = ["In the most train focused election in British history, we came out victorious. You now get to do this for the next five years, we're so sorry!",
                "In the most train focused election in British history, we ended up losing. You must now retire to a six figure job in the private sector, we're so sorry!"]
    ###a state to control whats playing
    #[main_menu, cut_scene, game, end_scene]
    state = "main_menu"
    #1 or 2
    txt_state = 1
    
    clock = pygame.time.Clock()

