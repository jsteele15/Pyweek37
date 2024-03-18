import pygame
from pathlib import Path
from spritesheet import*


class CutScene:
    def __init__(self):
        self.minister = pygame.image.load("../res/tory.png").convert_alpha()
        self.phone = pygame.image.load("../res/phone.png").convert_alpha()
        self.rece = pygame.image.load("../res/rec.png").convert_alpha()

        self.sheet_phone = SpriteSheet(self.phone, 1, 200, 200, 100, 100)
        self.sheet_recev = SpriteSheet(self.rece, 1, 200, 200,93, 33)
        self.angle = 0
        self.target_angle = -90

        self.recev_start = [500, 312]
        self.recev_target = [550, 150]
        self.recev_loc = [500, 312]

        ##states call, end and info
        self.state = "call"
    def play(self, screen, setting, button_list):
        screen.blit(self.minister, (0, 0))
        #screen.blit(self.rece, (200, 300))
        screen.blit(self.sheet_phone.animation_list[self.sheet_phone.ind], (500, 300))
        rotated_image = pygame.transform.rotate(self.sheet_recev.animation_list[self.sheet_recev.ind], self.angle)
        screen.blit(rotated_image, self.recev_loc)
        
        if self.state == "call":
            if self.recev_loc[1] > self.recev_target[1]:
                self.recev_loc[1] -= 2

            if self.recev_loc[0] < self.recev_target[0]:
                self.recev_loc[0] += 1
            
            if self.angle > self.target_angle:
                self.angle-=1

            button_list[0].draw(screen, "SKIP", setting)
            button_list[1].draw(screen, "NEXT", setting)
        

