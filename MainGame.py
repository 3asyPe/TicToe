import pygame
import sys

from Desk import GameField
from CrossPlayer import CrossPlayer
from ZeroPlayer import ZeroPlayer


class Game:
    def __init__(self, window):
        self.window = window

        self.gameDesk = GameField(self.window)
        self.crossPlayer = CrossPlayer()
        self.zeroPlayer = ZeroPlayer()

        self.field = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]

        self.motion = self.crossPlayer

    def start(self):
        """Reset all parameters and start game"""
        self.gameDesk = GameField(self.window)
        self.gameDesk.start()
        self.gameDesk.draw_score(self.crossPlayer, self.zeroPlayer)
        self.field = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]
        self.motion = self.crossPlayer

    def move(self):
        """Tracking click events in game 1x1"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = self.click_event()
                    if click is False:
                        continue
                    return click

    def click_event(self):
        """Handles click events by player.
        Returns 'back' if back button was pressed,
        True if new cell was created,
        False if nothing happened.
        """
        pos = pygame.mouse.get_pos()
        coordinates = self.gameDesk.button_is_pressed(self.motion, *pos)
        if coordinates == (None, None):
            return 'back'
        if coordinates is not False:
            i, j = coordinates[0], coordinates[1]
            self.field[i][j] = self.motion.value
            self.motion = self.zeroPlayer if self.motion == self.crossPlayer \
                else self.crossPlayer
            self.gameDesk.draw()
            self.gameDesk.draw_score(self.crossPlayer, self.zeroPlayer)
            return True
        return False

    def check_win(self):
        """Checks field on win situation.
        Return True if there is a win else False
        """
        possible_winner = self.crossPlayer if self.motion == self.zeroPlayer\
            else self.zeroPlayer
        for i in range(3):
            if self.field[i][0] == self.field[i][1] == self.field[i][2] != '.':
                self.gameDesk.draw_line(i, 0, 'horizontal_line', possible_winner)
                return True

        for j in range(3):
            if self.field[0][j] == self.field[1][j] == self.field[2][j] != '.':
                self.gameDesk.draw_line(0, j, 'vertical_line', possible_winner)
                return True

        if self.field[0][0] == self.field[1][1] == self.field[2][2] != '.':
            self.gameDesk.draw_line(0, 0, 'left_diagonal', possible_winner)
            return True

        if self.field[0][2] == self.field[1][1] == self.field[2][0] != '.':
            self.gameDesk.draw_line(0, 0, 'right_diagonal', possible_winner)
            return True

        return False

    def check_draw(self):
        """Checks field on draw situation.
        Starting method handle draw situation.
        Return True if there is a win else False
        """
        for i in range(3):
            for j in range(3):
                if self.field[i][j] == '.':
                    return False
        self.gameDesk.game_draw()
        self.gameDesk.draw_score(self.crossPlayer, self.zeroPlayer)
        return True
