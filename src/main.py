import pygame
from event_and_inputs import*
from ents import*
from settings import*


def main():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.WIDTH, setting.HEIGHT))

    while setting.RUNNING:
        screen.fill((255, 255, 255))
        actions(setting)
        
        pygame.display.update()
        setting.clock.tick(60)

if __name__ == "__main__":
    main()