# Start menu

import pygame
import os.path
import sys

# Loading images
home_picture = pygame.image.load(os.path.join('Pictures', 'HomePage.jpg'))

play1x1 = pygame.image.load(os.path.join('Pictures', '1x1.png'))
play1x1FOCUS = pygame.image.load(os.path.join('Pictures', '1x1RED.png'))
playAI = pygame.image.load(os.path.join('Pictures', 'vsBOT.png'))
playAIFOCUS = pygame.image.load(os.path.join('Pictures', 'vsBOTRED.png'))
play = pygame.image.load(os.path.join('Pictures', 'Play.png'))


class Home:
    def __init__(self, win):
        self.window = win

        self.home_pic = home_picture

        # 1x1 button is turned on, vsBOT button is turned off at default
        # State 1 - on. State 0 - off
        self.button1 = play1x1FOCUS
        self.button1_state = 1

        self.button2 = playAI
        self.button2_state = 0

        self.playButton = play

    def draw(self):
        """Draws whole interface"""
        self.window.blit(self.home_pic, (0, 0))

        self.window.blit(self.button1, (95, 405))
        self.window.blit(self.button2, (401, 405))
        self.window.blit(self.playButton, (248, 405))

        pygame.display.update()

    def start(self):
        """Resets settings and starts drawing function"""
        self.button1 = play1x1FOCUS
        self.button1_state = 1

        self.button2 = playAI
        self.button2_state = 0

        self.draw()

    def in_focus(self, button):
        """Checks which button in focus and change state with picture of button.
        Returns which button in focus right now
        """
        if button == 1:
            self.button1 = play1x1FOCUS
            self.button1_state = 1

            self.button2 = playAI
            self.button2_state = 0
        elif button == 3:
            self.button1 = play1x1
            self.button1_state = 0

            self.button2 = playAIFOCUS
            self.button2_state = 1

        self.draw()
        return button

    def start_choice(self):
        """Home page mainloop. Waiting when player choose the mode of the game.
        Return which button was in focus when PLAY button was pressed
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.which_button(*pos) == 2:
                        return self.button1_state

    def which_button(self, x, y):
        """Determines which button was pressed.
        Starts method which changing focus on buttons if button was pressed.
        Also returns which button was that.
        Returns False if button wasn't pressed.
        """
        if 95 <= x <= 203 and 405 <= y <= 459:
            return self.in_focus(1)
        if 401 <= x <= 509 and 405 <= y <= 459:
            return self.in_focus(3)
        if 248 <= x <= 363 and 405 <= y <= 470:
            return 2
        return False


