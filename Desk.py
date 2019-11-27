import pygame
import os.path

from Cell import Cell

# Loading all images
bg = pygame.image.load(os.path.join('Pictures', 'BG.jpg'))
cross = pygame.image.load(os.path.join('Pictures', 'Cross.png'))
zero = pygame.image.load(os.path.join('Pictures', 'Zero.png'))
draw = pygame.image.load(os.path.join('Pictures', 'Draw.png'))

right_diagonal = pygame.image.load(os.path.join('Pictures', 'Right diagonal.png'))
left_diagonal = pygame.image.load(os.path.join('Pictures', 'Left diagonal.png'))
vertical_line = pygame.image.load(os.path.join('Pictures', 'Vertical line.png'))
horizontal_line = pygame.image.load(os.path.join('Pictures', 'Horizontal line.png'))

back_picture = pygame.image.load(os.path.join('Pictures', 'Back.png'))
loading_picture = pygame.image.load(os.path.join('Pictures', 'KiraLoading.jpg'))


class GameField:
    def __init__(self, window):
        self.window = window
        self.cells = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]
        self.score1 = pygame.font.SysFont('comicsans', 30)
        self.score2 = pygame.font.SysFont('comicsans', 30)
        self.back = back_picture
        self.loading = loading_picture

    def draw(self):
        """Draws/redraws game field and back button"""
        self.window.blit(bg, (0, 0))
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.cells[i][j] != '.':
                    self.cells[i][j].draw(self.window)
        self.draw_back()
        pygame.display.update()

    def start(self):
        """Reset all settings"""
        self.window.blit(bg, (0, 0))
        self.draw_back()
        self.cells = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]

    def game_draw(self):
        """Handles draw situation. Draws background and title 'Draw'"""
        pygame.time.delay(300)
        self.window.blit(bg, (0, 0))
        self.window.blit(draw, (0, 0))

    def button_is_pressed(self, owner, x=None, y=None, i=None, j=None):
        """Makes new cell and returns location of it
        if received information from which_button method
        about location of cell.

        If received (None, None) returns it.
        It means that back button was pressed.
        """
        if i is None or j is None:
            i, j = self.which_button(x, y)
            if i is None:
                return None, None
        if self.cells[i][j] == '.':
            self.cells[i][j] = Cell(i, j, owner, owner.picture)
            return i, j
        return False

    @staticmethod
    def which_button(x, y):
        """Static method for determining which button was pressed.
        Return location of button which was pressed
        or (None, None) if Back button was pressed
        """
        if 20 <= x <= 67 and 30 <= y <= 77:
            return None, None
        if 0 <= x < 200:
            j = 0
        elif 200 <= x <= 400:
            j = 1
        else:
            j = 2

        if 0 <= y < 200:
            i = 0
        elif 200 <= y <= 400:
            i = 1
        else:
            i = 2

        return i, j

    def draw_line(self, i, j, name, winner):
        """Draws win line"""
        winner.score += 1
        if name == 'horizontal_line':
            self.window.blit(horizontal_line, (0, 200 * i - 200))
        elif name == 'vertical_line':
            self.window.blit(vertical_line, (200 * j - 203, 0))
        elif name == 'left_diagonal':
            self.window.blit(left_diagonal, (0, 0))
        else:
            self.window.blit(right_diagonal, (0, 0))
        pygame.display.update()

    def draw_score(self, person1, person2):
        """Makes and draws score of both players"""
        text1 = self.score1.render('Cross score: ' + str(person1.score), 1, (0, 0, 0))
        text2 = self.score2.render('Oval score: ' + str(person2.score), 1, (0, 0, 0))
        self.window.blit(text1, (20, 10))
        self.window.blit(text2, (450, 10))
        pygame.display.update()

    def draw_back(self):
        """Draws the back button"""
        self.window.blit(self.back, (20, 30))
        pygame.display.update()

    def draw_loading(self):
        """Draws the loading picture"""
        print('loading...')
        self.window.blit(self.loading, (0, 0))
        pygame.display.update()
