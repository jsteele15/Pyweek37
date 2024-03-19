import pygame
from cutsene import*
from music_and_sound import*
from pathlib import Path
from ui import*
from event_and_inputs import*
from ents import*
from settings import*



def main():
    pygame.init()

    pygame.display.set_caption("Thomas the Minister of Transportation")
    
    ###adds an icon
    #icon = pygame.image.load("../res/icon.png")
    #pygame.display.set_icon(icon)   

    setting = Settings()
    screen = pygame.display.set_mode((setting.WIDTH, setting.HEIGHT))

    ###ui stuff
    bar = Bars( setting.WIDTH - setting.WIDTH, setting.HEIGHT - setting.HEIGHT , setting.WIDTH *2, )
    behind_sign = Bars(14, setting.HEIGHT - 100, 169, colour = (0, 37, 144))
    text_sign = Bars(setting.WIDTH + 60, setting.HEIGHT - 180, 760, colour = (0, 37, 144), height = 120)
    speach_sign = Bars( 530, 190, 150, colour = (0, 37, 144), height = 60)
    bar = Bars( setting.WIDTH - setting.WIDTH, setting.HEIGHT - setting.HEIGHT , setting.WIDTH *2)

    game_title1 = LevelText(60, setting.WIDTH + 100, 10)
    game_title2 = LevelText(60, setting.WIDTH, 70)
    game_title_tar = 50

    score = LevelText( 30, 10, 0)
    date_txt = LevelText( 30, setting.WIDTH/2 - 75, setting.HEIGHT/setting.HEIGHT)
    end_txt = LevelText( 50, setting.WIDTH/2 - 250, setting.HEIGHT/2)
    under_txt = LevelText( 20, 20, setting.HEIGHT - 90, colour=(255, 255, 255))
    
    lt_1 = LevelText( 30, setting.WIDTH +100, setting.HEIGHT - 175, (255, 255, 255))
    lt_2 = LevelText( 30, setting.WIDTH +100, setting.HEIGHT - 140, (255, 255, 255))
    lt_3 = LevelText( 30, setting.WIDTH +100, setting.HEIGHT - 105, (255, 255, 255))
    lt_5 = LevelText( 30, setting.WIDTH +100, setting.HEIGHT - 175, (255, 255, 255))
    lt_6 = LevelText( 30, setting.WIDTH +100, setting.HEIGHT - 140, (255, 255, 255))
    lt_7 = LevelText( 30, setting.WIDTH +100, setting.HEIGHT - 105, (255, 255, 255))

    lt_8 = LevelText( 25, 40, 105)
    lt_9 = LevelText( 25, 40, 50)
    lt_4 = LevelText( 30, setting.WIDTH - 250, setting.HEIGHT/2- 100,(255, 255, 255)) #
    #buttons
    play_but = Buttons(play_func,[setting.WIDTH + 50, setting.HEIGHT/2 - 100], (100, 100))
    play_target = 50
    skip_but = Buttons(skip_func,[setting.WIDTH /3 + setting.WIDTH /3-50, setting.HEIGHT -50], (100, 100))

    exit_but = Buttons(exit_func,[setting.WIDTH + 100, setting.HEIGHT/2 - 50], (100, 100))
    next_but = Buttons(next_func,[setting.WIDTH /3-50, setting.HEIGHT -50], (100, 100))

    button_list = [play_but, skip_but, exit_but, next_but]

    ###to control the time of day
    start_time = pygame.time.get_ticks()
    
    ###tutorial line###
    tutorial_line_p2_1 = Stations(None, 57, 200)
    tutorial_line_p2_2 = Stations(None, 290, 200)

    tutorial_line_p1_1 = Stations(None, 477, 200)
    tutorial_line_p1_2 = Stations(None, 710, 200)
    r_t_1 = Route([tutorial_line_p2_1, tutorial_line_p2_2], ((0, 255, 0)))
    r_t_2 = Route([tutorial_line_p1_1, tutorial_line_p1_2], ((100, 200, 200)))

    t_t_1 =  Train(None, r_t_1)
    t_t_2 =  Train(None, r_t_2)

    tutorial_list_lines = [r_t_1, r_t_2]
    tutorial_list_trains = [t_t_1, t_t_2]

    ###second line###
    l2_start = Stations(None, 50, 50)
    l2_1 = Stations(None, 50, 400)
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

    r8 = Route([l8_1, l8_2, l8_3, l8_4], (247, 146, 57))

    #9th line
    l9_1 = Stations(None, 56, 56)
    l9_2 = Stations(None, 766, 56)
    l9_3 = Stations(None, 766, 546)
    l9_4 = Stations(None, 200, 546)
    l9_5 = Stations(None, 56, 206)

    r9 = Route([l9_1, l9_2, l9_3, l9_4, l9_5, l9_1], (42, 38, 39))

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
    hp = pygame.image.load("../res/buildings2.png").convert_alpha()
    sp = pygame.image.load("../res/buildings1.png").convert_alpha()
    hp_current = setting.HEIGHT+200
    hp_target = setting.HEIGHT -150
    sp_current = setting.HEIGHT +200
    cutscene = CutScene()

    
    while setting.RUNNING:
        screen.fill((255, 255, 251))
        ###blitting the background        
        actions(setting, train_list, button_list, tutorial_list_trains)
        
        if setting.state == "main_menu":
            play_but.draw(screen, "PLAY", setting)
            game_title1.draw(screen, "Thomas the Minister")
            game_title2.draw(screen, "of Transportation")
            exit_but.draw(screen, "EXIT", setting)
            if game_title1.x_pos > game_title_tar:
                game_title1.x_pos -= 10

            if game_title2.x_pos > game_title_tar:
                game_title2.x_pos -= 10

            if play_but.pos[0] > play_target:
                play_but.pos[0] -= 10

            if exit_but.pos[0] > play_target:
                exit_but.pos[0] -= 10
            
            screen.blit(hp, (setting.WIDTH - 200,hp_current))
            screen.blit(sp, (setting.WIDTH/2 , sp_current+100))

            if hp_target < hp_current:
                hp_current -= 5
            if hp_target < sp_current +100:
                sp_current -= 5

            pygame.draw.circle(screen, (255, 0, 0), (100, setting.HEIGHT - 85), 70)        
            pygame.draw.circle(screen, (255, 255, 255), (100, setting.HEIGHT - 85), 50)        
            behind_sign.draw(screen)
            under_txt.draw(screen, f"UNDERGROUND")
            #this skip is to go into the cutscenes but thats for later
            #skip_but.draw(screen, "SKIP", setting)
        
        if setting.state == "cut_scene":
            cutscene.play(screen, setting, [skip_but, next_but], [lt_1, lt_2, lt_3, lt_4, lt_5, lt_6, lt_7, lt_8, lt_9], [text_sign, speach_sign])
            if setting.txt_state == 4:
                for r in range(len(tutorial_list_lines)):
                    tutorial_list_lines[r].draw(screen)

                for t in range(len(tutorial_list_trains)):
                    tutorial_list_trains[t].move(setting, screen)
            
        if setting.state == "game":
            screen.blit(scaled_im, (0, -250))
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