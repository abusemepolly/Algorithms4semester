from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def find_components(graph):
    visited = set()
    components = []

    for vertex in graph:
        if vertex not in visited:
            bfs(graph, vertex, visited)
            components.append(vertex)

    return components

def create_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        graph = {i: [] for i in range(len(lines))}
        for i, line in enumerate(lines):
            for j, val in enumerate(map(int, line.split())):
                if val == 1:
                    graph[i].append(j)
    return graph

filename = '/Users/adyl/PycharmProjects/BFS2/adjacency_matrix.txt'
user_graph = create_graph_from_file(filename)

components = find_components(user_graph)

with open('output.txt', 'w') as file:
    file.write("Количество компонент связности: " + str(len(components)) + "\n")
    file.write("Компоненты связности: " + ', '.join(map(str, components)) + "\n")

print("Результаты записаны в файл 'output.txt'")
