import pygame
from pathlib import Path

class Buttons:
    pass

class Bars:
    def __init__(self, x_pos, y_pos, width, colour = (255, 255, 255)):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.colour = colour

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.x_pos, self.y_pos, self.width, 40))


class LevelText:
    def __init__(self, size, x_pos, y_pos, colour = (0, 37, 144)):
    
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size
        self.colour = colour
        self.font = pygame.font.Font(Path(r'../res/LondonTube-MABx.ttf'), self.size)

    def draw(self, screen, txt):
        text_surface = self.font.render(txt, True, self.colour)

        screen.blit(text_surface, (self.x_pos, self.y_pos))
  
#def month_timer(timer, setting):
   # #tim = timer
    #days = (pygame.time.get_ticks() - tim) // 1000

    #if days > 3:
       # #print(setting.months[setting.month])
        #setting.month += 1
        #tim = pygame.time.get_ticks()