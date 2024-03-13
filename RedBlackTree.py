class Node:
    RED = 1
    BLACK = 0

    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = Node.RED  # По умолчанию новые узлы красные
