import pygame
import os.path

from Player import Player


class ZeroPlayer(Player):
    def __init__(self):
        super().__init__()
        self.value = '0'
        self.bot_value = '1'
        self.picture = pygame.image.load(os.path.join('Pictures', 'Zero.png'))


