class Cell:
    def __init__(self, i, j, owner, picture):
        self.i = i
        self.j = j
        self.owner = owner
        self.picture = picture
        self.x = self.j * 200 + 1
        self.y = self.i * 200 + 4

    def draw(self, window):
        window.blit(self.picture, (self.x, self.y))
