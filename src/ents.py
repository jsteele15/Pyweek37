import pygame
from spritesheet import*

class Train:
    def __init__(self, image, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos


        self.sprite = SpriteSheet(0, 0, 0, 0, 0, 0)