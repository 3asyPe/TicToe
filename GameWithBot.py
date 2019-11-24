import pygame
import sys

from MainGame import Game
from Bot import Bot


class BotGame(Game):
    def __init__(self, window):
        super().__init__(window)
        self.bot = Bot()
        self.zeroPlayer = self.bot
        self.gameDesk.draw_loading()
        self.bot.start()

    def start(self):
        """Reset all parameters and start game with bot reset"""
        super().start()
        self.bot.reset()

    def move(self):
        """Tracking events by player and bot in game with AI"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.motion == self.crossPlayer and event.type == pygame.MOUSEBUTTONDOWN\
                        and event.button == 1:
                    click = self.click_event()
                    if click is False:
                        continue
                    return click

            if self.motion == self.zeroPlayer:
                return self.bot_click_event()

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
            # Sending information about event to bot
            self.bot.new_motion(i, j, self.motion)
            self.motion = self.zeroPlayer if self.motion == self.crossPlayer \
                else self.crossPlayer
            self.gameDesk.draw()
            self.gameDesk.draw_score(self.crossPlayer, self.zeroPlayer)
            return True
        return False

    def bot_click_event(self):
        """Handles click events by bot"""
        pygame.time.delay(1000)
        i, j = self.bot.do_move()
        self.gameDesk.button_is_pressed(self.motion, i=i, j=j)
        self.field[i][j] = self.motion.value
        self.motion = self.zeroPlayer if self.motion == self.crossPlayer \
            else self.crossPlayer
        self.gameDesk.draw()
        self.gameDesk.draw_score(self.crossPlayer, self.zeroPlayer)
        return True
