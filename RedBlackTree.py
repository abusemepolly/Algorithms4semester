class Node:
    RED = 1
    BLACK = 0

    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = Node.RED  # По умолчанию новые узлы красные


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)  # Создаем TNULL узел, который будет использоваться как листья
        self.TNULL.color = Node.BLACK
        self.TNULL.left = self.TNULL.right = None
        self.root = self.TNULL  # Инициализация корня как TNULL

    def pre_order_helper(self, node):
        """Обход дерева в прямом порядке."""
        if node != self.TNULL:
            print(f"{node.item} ", end='')
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    def in_order_helper(self, node):
        """Обход дерева в симметричном порядке."""
        if node != self.TNULL:
            self.in_order_helper(node.left)
            print(f"{node.item} ", end='')
            self.in_order_helper(node.right)

    def post_order_helper(self, node):
        """Обход дерева в обратном порядке."""
        if node != self.TNULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            print(f"{node.item} ", end='')

    def search_tree_helper(self, node, key):
        """Поиск узла с заданным ключом."""
        if node == self.TNULL or key == node.item:
            return node
        if key < node.item:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)


def insert(self, key):
    # Создаем новый узел с заданным ключом и инициализируем его свойства
    node = Node(key)
    node.parent = None
    node.item = key
    node.left = node.right = self.TNULL
    node.color = Node.RED  # Новые узлы всегда красные

    # Начинаем поиск места для вставки нового узла
    y = None
    x = self.root

    while x != self.TNULL:
        y = x
        if node.item < x.item:
            x = x.left
        else:
            x = x.right

    # y теперь ссылается на родителя для нового узла
    node.parent = y
    if y is None:  # Дерево было пустым
        self.root = node
    elif node.item < y.item:
        y.left = node
    else:
        y.right = node

    # Если новый узел — корень, просто перекрашиваем его в чёрный и завершаем
    if node.parent is None:
        node.color = Node.BLACK
        return

    # Если у нового узла нет дедушки, дерево остается валидным
    if node.parent.parent is None:
        return

    # Балансировка дерева с новым узлом
    self.fix_insert(node)
