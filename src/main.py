import pygame
from ui import*
from event_and_inputs import*
from ents import*
from settings import*


def main():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.WIDTH, setting.HEIGHT))

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

    test_train2 = Train(None, r2)
    test_train3 = Train(None, r3)

    while setting.RUNNING:
        screen.fill((255, 255, 255))
        actions(setting)

        r2.draw(screen)
        r3.draw(screen)

        test_train2.move(setting, screen)
        test_train3.move(setting, screen)

        pygame.display.update()
        setting.clock.tick(60)

if __name__ == "__main__":
    main()