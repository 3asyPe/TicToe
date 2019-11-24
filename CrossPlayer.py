import pygame
import os.path

from Player import Player


class CrossPlayer(Player):
    def __init__(self):
        super().__init__()
        self.value = 'x'
        self.bot_value = '2'
        self.picture = pygame.image.load(os.path.join('Pictures', 'Cross.png'))

