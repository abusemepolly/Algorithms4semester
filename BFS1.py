from collections import deque

def bfs(graph, start):
    visited = set()
    distance = {vertex: float('infinity') for vertex in range(len(graph))}
    queue = deque([start])

    distance[start] = 0
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        for neighbor in range(len(graph[vertex])):
            if graph[vertex][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distance[neighbor] = distance[vertex] + 1

    return distance

# Функция для чтения графа из файла с матрицей смежности
def create_graph_from_file(filename):
    with open(filename, 'r') as file:
        graph = [list(map(int, line.split())) for line in file.readlines()]
    return graph

filename = '/Users/adyl/PycharmProjects/BFS1/adjacency_matrix.txt'
user_graph = create_graph_from_file(filename)

# Выполнение BFS для начальной вершины 0
start_vertex = 0
distances = bfs(user_graph, start_vertex)

output_filename = 'output.txt'
with open(output_filename, 'w') as file:
    file.write("Кратчайшие расстояния от вершины " + str(start_vertex) + ":\n")
    for vertex, distance in distances.items():
        file.write(f'Вершина {vertex}: Расстояние {distance}\n')

print(f"Результаты записаны в файл '{output_filename}'")
