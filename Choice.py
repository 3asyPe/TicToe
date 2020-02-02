# Tree for BOT could make decisions

import pickle


class Node:
    """Makes new objects which consist of some helpful information.
    Value is a number, not a two-dimensional array, cause it would
    take too much memory.
    """
    def __init__(self, value: int, motion):
        self.value = value
        self.motion = motion
        self.parent = None
        self.children = []
        self.crossWIN = 0
        self.zeroWIN = 0
        self.draw = 0


class Tree:
    def __init__(self):
        self.root = Node(1000000000, None)
        self.cross = '2'
        self.zero = '1'
        self.queue = []
        self.count = 0

    def build(self):
        """Starts building Tree"""
        self.sub_built(self.root)

    def sub_built(self, node):
        """Building Tree with recursion. Adds new sub tree to every
        objects which value isn't ends with win or draw.
        """
        if self.is_win(node) or self.is_draw(node):
            node.parent.crossWIN += node.crossWIN
            node.parent.zeroWIN += node.zeroWIN
            node.parent.draw += node.draw
            return

        if node is self.root or node.motion is self.zero:
            motion = self.cross
        else:
            motion = self.zero

        for i in range(1, 10):
            if str(node.value)[i] == '0':
                new_value = list(str(node.value))
                new_value[i] = motion
                new_node = Node(int(''.join(new_value)), motion)

                node.children.append(new_node)
                new_node.parent = node

                self.sub_built(new_node)

                node.crossWIN += new_node.crossWIN
                node.zeroWIN += new_node.zeroWIN
                node.draw += new_node.draw

    def is_win(self, node):
        """Checks game field on win situation"""
        temp_value = str(node.value)
        for n1, n2, n3 in (1, 2, 3), (4, 5, 6), (7, 8, 9):
            if temp_value[n1] == temp_value[n2] == temp_value[n3] != '0':
                if node.motion == self.cross:
                    node.crossWIN = 1
                else:
                    node.zeroWIN = 1
                return True

        for n1, n2, n3 in (1, 4, 7), (2, 5, 8), (3, 6, 9):
            if temp_value[n1] == temp_value[n2] == temp_value[n3] != '0':
                if node.motion == self.cross:
                    node.crossWIN = 1
                else:
                    node.zeroWIN = 1
                return True

        if (temp_value[1] == temp_value[5] == temp_value[9] != '0')\
                or (temp_value[3] == temp_value[5] == temp_value[7] != '0'):
            if node.motion == self.cross:
                node.crossWIN = 1
            else:
                node.zeroWIN = 1
            return True

        return False

    def is_draw(self, node):
        """Checks game field on draw situation"""
        for i in range(1, 10):
            if str(node.value)[i] == '0':
                return False
        node.draw = 1
        return True


def built_tree():
    try:
        with open('data.pickle', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        with open('data.pickle', 'wb') as f:
            MyTree = Tree()
            MyTree.build()
            pickle.dump(MyTree, f)
            return MyTree


# Test
if __name__ == '__main__':
    import time
    start_time = time.time()
    MyTree = Tree()
    MyTree.build()
    for child in MyTree.root.children:
        print(child.value)
    print('\n')
    for child in MyTree.root.children[0].children:
        print(child.value)
    print('\n')
    for child in MyTree.root.children[2].children:
        print(child.value)
    print('\n')
    for child in MyTree.root.children[4].children:
        print(child.value)
    print(MyTree.root.children[4].crossWIN)
    print(MyTree.root.children[4].zeroWIN)
    print(MyTree.root.children[4].draw)
    print('\n')
    print(MyTree.root.crossWIN)
    print(MyTree.root.zeroWIN)
    print(MyTree.root.draw)
    print('\n')
    print(MyTree.count)
    print('{:.2f}'.format(time.time()-start_time))

    with open('data.pickle', 'wb') as f:
        pickle.dump(MyTree, f)

    with open('data.pickle', 'rb') as f:
        print(pickle.load(f).root.children)
