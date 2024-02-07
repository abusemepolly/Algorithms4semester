def dfs(graph, vertex, visited, stack=None, component=None):
    visited.add(vertex)
    if component is not None:
        component.add(vertex)
    for neighbor in range(len(graph)):
        if graph[vertex][neighbor] == 1 and neighbor not in visited:
            dfs(graph, neighbor, visited, stack, component)
    if stack is not None:
        stack.append(vertex)

def transpose_graph(graph):
    return [[graph[j][i] for j in range(len(graph))] for i in range(len(graph))]

def kosaraju(graph):
    visited = set()
    stack = []
    components = []

    # Первый проход DFS для определения порядка вершин
    for vertex in range(len(graph)):
        if vertex not in visited:
            dfs(graph, vertex, visited, stack)

    # Транспонирование графа
    transposed_graph = transpose_graph(graph)

    # Второй проход DFS для нахождения сильно связных компонент
    visited.clear()
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            component = set()
            dfs(transposed_graph, vertex, visited, component=component)
            components.append(component)

    return components

def create_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        graph = [[int(val) for val in line.split()] for line in lines]
    return graph

def write_components_to_file(components, filename):
    with open(filename, 'w') as file:
        file.write(f"Количество сильно связных компонент: {len(components)}\n")
        for i, component in enumerate(components, start=1):
            file.write(f"Компонента {i}: {', '.join(map(str, component))}\n")


filename = '/Users/adyl/PycharmProjects/DFS2/adjacency_matrixDFS2.txt'
output_filename = 'components_output.txt'

graph = create_graph_from_file(filename)
components = kosaraju(graph)
write_components_to_file(components, output_filename)

print(f"Результаты записаны в файл '{output_filename}'")
