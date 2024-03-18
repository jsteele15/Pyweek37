import pygame
from ui import*
from event_and_inputs import*
from ents import*
from settings import*


def main():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.WIDTH, setting.HEIGHT))
    
    ####for lines###
    line_colour = (0,0,0)
    start_pos = (30, 30)
    end_pos = (120, 120)
    end_pos2 = (120, 500)

    ###second line###
    line_colour2 = (150, 200, 100)
    l2_start = (50, 50)
    l2_1 = (50, 400)
    l2_2 = (400, 400)
    l2_3 = (400, 50)
    line2_list = [l2_start, l2_1, l2_2, l2_3]

    test_train = Train(0, start_pos[0], start_pos[1], [start_pos, end_pos, end_pos2])
    test_train2 = Train(0, l2_start[0], l2_start[1], line2_list, True)

    while setting.RUNNING:
        screen.fill((255, 255, 255))
        actions(setting)

        ###also for lines###
        pygame.draw.line(screen, line_colour, start_pos, end_pos, 10)
        pygame.draw.line(screen, line_colour, end_pos, end_pos2, 10)
        
        for l in range(len(line2_list)):
            if l+1 < len(line2_list):    
                pygame.draw.line(screen, line_colour2, line2_list[l], line2_list[l+1], 10)
            else:
                pygame.draw.line(screen, line_colour2, line2_list[l], line2_list[0], 10)


        test_train.move(setting, screen)
        test_train2.move(setting, screen)

        pygame.display.update()
        setting.clock.tick(60)

if __name__ == "__main__":
    main()