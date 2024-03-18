import pygame
from spritesheet import*

class Train:
    def __init__(self, image, x_pos, y_pos, route, loop = False):
        self.x_pos = x_pos
        self.y_pos = y_pos

        ###to tell the train if its going
        self.going = True
        self.route = route
        self.prev_dest = 0
        self.dest = 1 # self = self, dest = destination
        self.forward = True
        self.loop = loop
        ###to test train rect
        self.RECT_COLOUR = (30, 30, 150)

        self.sprite = SpriteSheet(0, 0, 0, 0, 0, 0)
    
    def move(self, setting, screen):
        if self.route[self.dest][0] > self.route[self.prev_dest][0]:
            self.x_pos += setting.SPEED
        elif self.route[self.dest][0]< self.route[self.prev_dest][0]:
            self.x_pos -= setting.SPEED

        if self.route[self.dest][1] > self.route[self.prev_dest][1]:
            self.y_pos += setting.SPEED
        elif self.route[self.dest][1] < self.route[self.prev_dest][1]:
            self.y_pos -= setting.SPEED

        #print(f"x: {self.x_pos}, y: {self.y_pos}\n at dest: {self.x_pos == self.route[self.dest][0] and self.y_pos == self.route[self.dest][1]}")
        if self.loop == False:
            if self.x_pos == self.route[self.dest][0] and self.y_pos == self.route[self.dest][1]:
                if self.forward == True:
                    if self.dest < len(self.route)-1:
                        self.prev_dest = self.dest
                        self.dest += 1
                    else:
                        self.forward = False
                        self.prev_dest = self.dest
                        self.dest -= 1

                elif self.forward == False:
                    if self.dest > 0:
                        self.prev_dest = self.dest
                        self.dest -= 1
                    else:
                        self.forward = True
                        self.prev_dest = self.dest
                        self.dest += 1
                print(f"x: {self.x_pos}, y: {self.y_pos}\n dest: {self.dest}") 

        if self.loop == True:
            if self.x_pos == self.route[self.dest][0] and self.y_pos == self.route[self.dest][1]:
                if self.dest < len(self.route)-1:
                        self.prev_dest = self.dest
                        self.dest += 1
                else:
                    self.prev_dest = self.dest
                    self.dest = 0

        pygame.draw.rect(screen, self.RECT_COLOUR, pygame.Rect(self.x_pos, self.y_pos, 10, 10))

class Stations:
    def __init__(self, image, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos