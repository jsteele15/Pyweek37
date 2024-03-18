import pygame
from pathlib import Path
from spritesheet import*


class CutScene:
    def __init__(self):
        self.minister = pygame.image.load("../res/tory.png").convert_alpha()

    def play(self, screen, setting):
        screen.blit(self.minister, (0, 0))

