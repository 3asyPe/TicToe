from Choice import built_tree
from ZeroPlayer import ZeroPlayer


class Bot(ZeroPlayer):
    def __init__(self):
        super().__init__()
        self.current_motion = None
        self.choices = None

    def reset(self):
        """Resets whole settings"""
        self.current_motion = self.choices.root

    def start(self):
        """Building Choices Tree and start settings reset"""
        self.choices = built_tree()
        self.reset()

    def new_motion(self, i, j, motion):
        """Finds motion in sub tree of current motion value of Choices Tree
        and set new current motion value of Choices Tree
        """
        value = self.converting_location_to_number(i, j, motion)
        for child in self.current_motion.children:
            if child.value == value:
                self.current_motion = child

    def converting_location_to_number(self, i, j, motion):
        """Converts location in (i, j) format to number format
        for Choices Tree
        """
        value = list(str(self.current_motion.value))
        value[i * 3 + j + 1] = motion.bot_value
        value = int(''.join(value))
        return value

    def do_move(self):
        """Makes a motion basing on Choice Tree with the choose algorithm"""
        winner = self.choose()
        return self.search_difference(self.current_motion, winner)

    def search_difference(self, person1, person2):
        """Static method which is searching a difference between two values.
        Returns location of difference in (i, j) format.
        Changes current motion
        """
        for pos in range(1, 10):
            if str(person1.value)[pos] != str(person2.value)[pos]:
                i, j = divmod(pos, 3)
                if j - 1 < 0:
                    i, j = i - 1, 2
                else:
                    i, j = i, j - 1
                self.current_motion = person2
                return i, j

    def choose(self):
        """Basing on algorithm makes a choice"""
        win_lose = 0
        win_draw_lose = 0
        winner = None
        draw = False
        for child in self.current_motion.children:
            new_win_lose = child.zeroWIN - child.crossWIN
            new_win_draw_lose = child.zeroWIN + child.draw - child.crossWIN
            coefficient = new_win_lose - win_lose + new_win_draw_lose - win_draw_lose
            if child.zeroWIN == 1 and child.crossWIN == 0 and child.draw == 0:
                return child
            if not winner:
                win_lose = new_win_lose
                win_draw_lose = new_win_draw_lose
                winner = child
                continue
            elif child.zeroWIN == 0 and child.crossWIN == 1 and child.draw == 0:
                continue
            elif child.draw == 1 and child.crossWIN == 0 and child.zeroWIN == 0:
                win_lose = new_win_lose
                win_draw_lose = new_win_draw_lose
                winner = child
                draw = True
            for child1 in child.children:
                if self.choices.is_win(child1):
                    break
            else:
                if draw is False and coefficient > -coefficient:
                    win_lose = new_win_lose
                    win_draw_lose = new_win_draw_lose
                    winner = child
        return winner

    def __version__(self):
        return 'Bot version 1.1'
