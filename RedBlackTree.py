class Node:
    def __init__(self, value, color='B'):  # По умолчанию цвет узла чёрный
        self.value = value
        self.color = color
        self.left = None
        self.right = None

def build_tree_from_string(s):
    stack = []
    root = None
    i = 0

    while i < len(s):
        if s[i].isdigit() or s[i] in ['R', 'B']:  # Распознавание цвета
            start = i
            color = 'B'  # Цвет по умолчанию

            if s[i] in ['R', 'B']:
                color = s[i]
                i += 1

            while i < len(s) and s[i].isdigit():
                i += 1
            value = int(s[start:i]) if s[start].isdigit() else None

            new_node = Node(value, color)

            if not stack:
                root = new_node
            else:
                parent = stack[-1]
                if not parent.left:
                    parent.left = new_node
                else:
                    parent.right = new_node

            stack.append(new_node)
            continue
        elif s[i] == ')':
            stack.pop()
        i += 1

    return root
