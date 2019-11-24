# main module

import pygame
import sys

from MainGame import Game
from GameWithBot import BotGame
from Home import Home


def __version__() -> str:
    return 'Version 1.0'


def start_game():
    """Start game from home page. Can be used by back button.

    Draws home page
    Make to make a choice which game will you play (with or without AI)
    Starting game which you chose
    """
    home_page = Home(win)
    home_page.draw()

    global game, start_timer, gameWithBot

    if home_page.start_choice() == 1:
        game = Game(win)
    else:
        if gameWithBot is None:
            gameWithBot = BotGame(win)
        game = gameWithBot

    game.start()
    start_timer = 0


def timer(n):
    for i in range(n):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.time.delay(30)


pygame.init()

# Global parameters, resolution of display
WIN_HEIGHT = 600
WIN_WIDTH = 600

# Makes new window and call it
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('TicToe')

gameWithBot = None
start_game()

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game.move() == 'back':
        start_game()
        continue

    if game.check_win() or game.check_draw():
        timer(100)
        game.start()

