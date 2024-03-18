import pygame
from ui import*
from event_and_inputs import*
from ents import*
from settings import*


def main():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.WIDTH, setting.HEIGHT))
    bar = Bars( setting.WIDTH - setting.WIDTH, setting.HEIGHT - setting.HEIGHT , setting.WIDTH *2)
    score = LevelText( 30, 0, 0)
    date_txt = LevelText( 30, setting.WIDTH/2 - 75, setting.HEIGHT/setting.HEIGHT)
    end_txt = LevelText( 50, setting.WIDTH/2 - 250, setting.HEIGHT/2)

    ###to control the time of day
    start_time = pygame.time.get_ticks()
    

    ###second line###
    l2_start = Stations(None, 50, 50)
    l2_1 = Stations(None, 100, 350)
    l2_2 = Stations(None, 400, 400)
    l2_3 = Stations(None, 400, 50)
    r2 = Route([l2_start, l2_1, l2_2, l2_3], (0, 255, 0), loop = True)

    #3rd line
    s1 = Stations(None, 170, 520)
    s2 = Stations(None, 300, 210)
    s3 = Stations(None, 360, 100)

    r3 = Route([s1, s2, s3, l2_3])

    #4th line
    l4_1 = Stations(None, 600, 500)
    l4_2 = Stations(None, 600, 200)
    l4_3 = Stations(None, 400, 50)

    r4 = Route([l4_1, l4_2, l4_3], (100, 200, 200))

    train2 = Train(None, r2)
    train3 = Train(None, r3)
    train4 = Train(None, r4)

    #list, for months to add to the comlexity
    dec_list = [[r4, train4]]

    route_list = [r2, r3]
    train_list = [train2, train3]

    
    while setting.RUNNING:
        screen.fill((232, 222, 214))
        

        actions(setting)
        
        for r in range(len(route_list)):
            route_list[r].draw(screen)

        for t in range(len(train_list)):
            train_list[t].move(setting, screen)
        

        


        ###this code iterates over the list of trains and works out if theyve collided. And sets their alive property to false. A little animation can be played then 
        for i in range(len(train_list)):
            for j in range(i + 1, len(train_list)):
                if train_list[i].col_rect.colliderect(train_list[j].col_rect) and train_list[i].alive and train_list[j].alive:
                    train_list[i].alive = False
                    train_list[j].alive = False

        #timer for the progression of the months, i have a rudementary function in the ui
        #.py. but its not working as intended, will come back to
        days = (pygame.time.get_ticks() - start_time) // setting.game_speed

        ###this 3 represents the number of seconds, we can change that 
        if days > 3:
            if setting.months[setting.month] != "May":
                if setting.months[setting.month] == "Nov":
                    for i in range(len(dec_list)):
                        route_list.append(dec_list[i][0])
                        train_list.append(dec_list[i][1])
                    
                    setting.month += 1
                    start_time = pygame.time.get_ticks()
                else:
                    setting.month += 1
                    start_time = pygame.time.get_ticks()
            else:
                screen.fill((255, 255, 255))
                end_txt.draw(screen, f"YOUR WIFE LEFT YOU =D")


        #draw the ui
        bar.draw(screen, setting)
        score.draw(screen, f"PASSENGERS: {setting.passengers}")
        date_txt.draw(screen, f"DATE: {setting.months[setting.month]}")

        pygame.display.update()
        setting.clock.tick(60)

if __name__ == "__main__":
    main()