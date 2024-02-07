class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # Инициализация предка каждого элемента самим собой
        self.rank = [0] * n  # Инициализация ранга каждого элемента

    def find(self, v):
        # Нахождение корня множества, к которому принадлежит элемент v
        if v != self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, x, y):
        # Объединение двух множеств, к которым принадлежат элементы x и y
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
            return True
        return False

def kruskal(edges, n):
    tree_edges = []  # Список рёбер в минимальном покрывающем дереве
    dsu = DisjointSet(n)  # Инициализация DSU
    edges.sort()  # Сортировка рёбер по весу
    cost = 0  # Общий вес минимального покрывающего дерева
    for edge in edges:
        weight, u, v = edge
        if dsu.union(u, v):
            tree_edges.append((u, v))
            cost += weight
    return tree_edges, cost

def read_graph_from_file(file_name):
    # Чтение графа из файла в виде матрицы смежности и преобразование в список рёбер
    with open(file_name, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    edges = []
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] > 0:  # Если ребро существует
                edges.append((matrix[i][j], i, j))
    return edges, n

def write_result_to_file(tree_edges, cost, file_name):
    with open(file_name, 'w') as file:
        file.write(f"Общий вес минимального покрывающего дерева: {cost}\n")
        file.write("Рёбра в минимальном покрывающем дереве:\n")
        for edge in tree_edges:
            file.write(f"Вершина {edge[0]} связана с вершиной {edge[1]}\n")


input_file = 'graph_adjacency_matrix.txt'
output_file = 'mst_result.txt'

edges, n = read_graph_from_file(input_file)
tree_edges, cost = kruskal(edges, n)
write_result_to_file(tree_edges, cost, output_file)
