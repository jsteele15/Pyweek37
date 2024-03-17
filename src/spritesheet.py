import pygame
from pathlib import Path

class SpriteSheet:
    def __init__(self, image, animation_steps, x_pos, y_pos, x_cut, y_cut, ind = 0):
        self.shett = image
        self.animation_list = []
        self.animation_steps = animation_steps

        self.ind = ind

        self.x_cut = x_cut
        self.y_cut = y_cut

        BLACK_GRE = (11, 158, 3)

        for x in range(self.animation_steps):
            self.animation_list.append(self.get_image(x, self.cut, self.y_cut, BLACK_GRE))
        
    def get_image(self, frame, width, height, colour):
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image.set_colorkey(colour)
        return image