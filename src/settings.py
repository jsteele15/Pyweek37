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
    month = 0
    months = ["Nov", "Dec", "Jan", "Feb", "Mar", "April","May"]
    
    day_counter = 0
    stored_counter = 0

    ###stats for the end
    passengers = 0
    crashes = 0
    freezes = 0
    speedys = 0
    elections_won = 0
    end_txts = [
                "In the most train focused election in British history, \nwe ended up losing. You must now retire to a six figure job \nin the private sector, we're so sorry!",
                "In the most train focused election in British history, \nwe came out victorious. You now get to do this for the next \nfive years, we're so sorry!"]
    ###a state to control whats playing
    #[main_menu, cut_scene, game, end]
    state = "main_menu"
    #1 or 2
    txt_state = 1
    
    ##routes and train lists
    starter_r_1 = 0
    starter_r_2 = 0
    starter_t_1 = 0
    starter_t_2 = 0
    route_list = []
    train_list = []
    clock = pygame.time.Clock()

    ##to reset the particle affects
    part = []

    ##to reset the months firing
    fired_list = []


