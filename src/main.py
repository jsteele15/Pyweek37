import pygame
from pathlib import Path
from ui import*
from event_and_inputs import*
from ents import*
from settings import*


def main():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.WIDTH, setting.HEIGHT))

    ###ui stuff
    bar = Bars( setting.WIDTH - setting.WIDTH, setting.HEIGHT - setting.HEIGHT , setting.WIDTH *2, )
    behind_sign = Bars(14, setting.HEIGHT - 100, 169, colour = (0, 37, 144))
    bar = Bars( setting.WIDTH - setting.WIDTH, setting.HEIGHT - setting.HEIGHT , setting.WIDTH *2)

    score = LevelText( 30, 10, 0)
    date_txt = LevelText( 30, setting.WIDTH/2 - 75, setting.HEIGHT/setting.HEIGHT)
    end_txt = LevelText( 50, setting.WIDTH/2 - 250, setting.HEIGHT/2)
    under_txt = LevelText( 20, 20, setting.HEIGHT - 90, colour=(255, 255, 255))

    ###to control the time of day
    start_time = pygame.time.get_ticks()
    

    ###second line###
    l2_start = Stations(None, 50, 50)
    l2_1 = Stations(None, 100, 350)
    l2_2 = Stations(None, 400, 400)
    l2_3 = Stations(None, 400, 50)
    r2 = Route([l2_start, l2_1, l2_2, l2_3], (0, 255, 0), loop = True)

    #3rd line
    s1 = Stations(None, 200, 520)
    s2 = Stations(None, 300, 210)
    s3 = Stations(None, 360, 100)

    r3 = Route([s1, s2, s3, l2_3])

    #4th line
    l4_1 = Stations(None, 600, 400)
    l4_2 = Stations(None, 600, 200)
    l4_3 = Stations(None, 400, 50)

    r4 = Route([l4_1, l4_2, l4_3], (100, 200, 200))

    #5th line
    l5_1 = Stations(None, 600, 250)
    l5_2 = Stations(None, 200, 250)

    r5 = Route([l5_1, l5_2], (248, 153, 177))
    
    #6th line
    l6_1 = Stations(None, 750, 550)
    l6_2 = Stations(None, 750, 150)
    l6_3 = Stations(None, 406, 150)
    l6_4 = Stations(None, 406, 550)

    r6 = Route([l6_1, l6_2, l6_3, l6_4, l6_1], (175, 27, 105), loop = True)
    r62 = Route([l6_3, l6_4, l6_1, l6_2, l6_3], (175, 27, 105), loop = True)

    #7th line
    l7_1 = Stations(None, 500, 500)
    l7_2 = Stations(None, 250, 150)
    l7_3 = Stations(None, 100, 150)
    
    r7 = Route([l7_1, l7_2, l7_3], (190, 116, 19))
    #8th line
    l8_1 = Stations(None, 600, 50)
    l8_2 = Stations(None, 600, 280)
    l8_3 = Stations(None, 200, 280)
    l8_4 = Stations(None, 50, 400)

    r8 = Route([l8_1, l8_2, l8_3, l8_4], (255, 215, 0))

    #9th line
    l9_1 = Stations(None, 56, 56)
    l9_2 = Stations(None, 766, 56)
    l9_3 = Stations(None, 766, 546)
    l9_4 = Stations(None, 200, 546)
    l9_5 = Stations(None, 56, 206)

    r9 = Route([l9_1, l9_2, l9_3, l9_4, l9_5, l9_1], (0, 176, 223))

    #trains
    train2 = Train(None, r2)
    train3 = Train(None, r3)
    train4 = Train(None, r4)
    train5 = Train(None, r5)
    train6 = Train(None, r6)
    train62 = Train(None, r62)
    train7 = Train(None, r7)
    train8 = Train(None, r8)
    train9 = Train(None, r9)

    #list, for months to add to the comlexity
    nov_list = [[r4, train4]]
    dec_list = [[r5, train5]]
    jan_list = [[r6, train6], [r62, train62]]
    feb_list = [[r7, train7]]
    mar_list = [[r8, train8]]
    apr_list = [[r9, train9]]

    nov_fired = False
    dec_fired = False
    jan_fired = False
    feb_fired = False
    mar_fired = False
    apr_fired = False

    route_list = [r2, r3]
    train_list = [train2, train3]

    ###to scale the image
    ###could use three scaled images to change based on the zoom if we get to that
    back_map = pygame.image.load("../res/map.png").convert_alpha()
    scaled_im = pygame.transform.scale(back_map,(1000,1000)) #2000, 2000
    
    while setting.RUNNING:
        screen.fill((255, 255, 251))
        ###blitting the background
        screen.blit(scaled_im, (0, -250))
        actions(setting, train_list)
        
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
            
            if setting.months[setting.month] == "Nov" and nov_fired == False:
                for i in range(len(nov_list)):
                    route_list.append(nov_list[i][0])
                    train_list.append(nov_list[i][1])
                    nov_fired = True
                #setting.month += 1
                #start_time = pygame.time.get_ticks()

            if setting.months[setting.month] == "Dec" and dec_fired == False:
                for i in range(len(dec_list)):
                    route_list.append(dec_list[i][0])
                    train_list.append(dec_list[i][1])
                    dec_fired = True

            if setting.months[setting.month] == "Jan" and jan_fired == False:
                for i in range(len(jan_list)):
                    route_list.append(jan_list[i][0])
                    train_list.append(jan_list[i][1])
                    dec_fired = True

            if setting.months[setting.month] == "Feb" and feb_fired == False:
                for i in range(len(feb_list)):
                    route_list.append(feb_list[i][0])
                    train_list.append(feb_list[i][1])
                    dec_fired = True
       
            if setting.months[setting.month] == "Mar" and mar_fired == False:
                for i in range(len(mar_list)):
                    route_list.append(mar_list[i][0])
                    train_list.append(mar_list[i][1])
                    dec_fired = True

            if setting.months[setting.month] == "April" and apr_fired == False:
                for i in range(len(apr_list)):
                    route_list.append(apr_list[i][0])
                    train_list.append(apr_list[i][1])
                    dec_fired = True
                
                #setting.month += 1
                #start_time = pygame.time.get_ticks()
            


            if setting.months[setting.month] == "May":
                for i in range(len(train_list)):
                    train_list[i].alive = False

                screen.fill((255, 255, 255))
                end_txt.draw(screen, f"YOUR WIFE LEFT YOU =D")

            if setting.months[setting.month] != "May":
                
                setting.month += 1
                start_time = pygame.time.get_ticks()



        #draw the ui
        pygame.draw.circle(screen, (255, 0, 0), (100, setting.HEIGHT - 85), 70)        
        pygame.draw.circle(screen, (255, 255, 255), (100, setting.HEIGHT - 85), 50)        
        bar.draw(screen)
        behind_sign.draw(screen)
        score.draw(screen, f"PASSENGERS: {setting.passengers}")
        date_txt.draw(screen, f"DATE: {setting.months[setting.month]}")
        under_txt.draw(screen, f"UNDERGROUND")
        
        pygame.display.update()
        setting.clock.tick(60)

if __name__ == "__main__":
    main()