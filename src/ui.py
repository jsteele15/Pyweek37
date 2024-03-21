import pygame
from pathlib import Path

class Bars:
    def __init__(self, x_pos, y_pos, width, colour = (255, 255, 255), height = 40):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.colour = colour
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.x_pos, self.y_pos, self.width, self.height))


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
  

class Buttons:
    def __init__(self, func, pos, size, sound, txt_size = 30, speed_butts = 0):
        self.func = func
        self.pos = pos
        self.txt_size = txt_size
        self.size = size
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.speed_butts = 0
        self.sound = sound


        self.clicked = False
        self.once = False
        self.hover = False

        

    def draw(self, screen, txto, change ):
        if self.speed_butts == 0:
            txt = LevelText(self.txt_size, self.pos[0], self.pos[1])
        if self.speed_butts == 1:
            txt = LevelText(self.txt_size, self.pos[0], self.pos[1], colour = (255, 210, 0))

        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        txt.draw(screen, txto)

        mpos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mpos):
            self.hover = True
        else:
            self.hover = False

        if self.clicked == False:
            self.once = False
        
        if self.hover == True:
            if self.clicked == True and self.once == False:
                self.sound.play()
                self.func(change)
                self.once = True

    def refresh(self):
        self.hover = False
        self.clicked = False
        self.once = False


def speed_buttons_change(setting, button_list):
    for b in range(len(button_list)):
        if b == setting.SPEED:
            button_list[b].speed_butts = 1
        else:
            button_list[b].speed_butts = 0
        
        button_list[b].refresh()
        
        
        





#def month_timer(timer, setting):
   # #tim = timer
    #days = (pygame.time.get_ticks() - tim) // 1000

    #if days > 3:
       # #print(setting.months[setting.month])
        #setting.month += 1
        #tim = pygame.time.get_ticks()
        