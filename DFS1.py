def dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def find_components(graph):
    visited = set()
    components = []
    component_list = []  # Для хранения списков вершин каждой компоненты

    for vertex in graph:
        if vertex not in visited:
            prev_visited = set(visited)  # Сохраняем состояние посещенных вершин
            dfs(graph, vertex, visited)
            new_component = visited - prev_visited  # Определяем новую компоненту связности
            components.append(vertex)  # Сохраняем представителя компоненты
            component_list.append(new_component)  # Сохраняем список вершин новой компоненты

    return components, component_list


def create_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        graph = {i: [] for i in range(len(lines))}
        for i, line in enumerate(lines):
            for j, val in enumerate(map(int, line.split())):
                if val == 1:
                    graph[i].append(j)
    return graph


filename = '/Users/adyl/PycharmProjects/DFS1/adjacency_matrix.txt'
user_graph = create_graph_from_file(filename)

components, component_lists = find_components(user_graph)

with open('output.txt', 'w') as file:
    file.write("Количество компонент связности: " + str(len(components)) + "\n")
    for i, comp in enumerate(component_lists, start=1):
        file.write(f"Компонента {i}: " + ', '.join(map(str, comp)) + "\n")

print("Результаты записаны в файл 'output.txt'")


"""
В этом коде функция dfs рекурсивно посещает все вершины графа, доступные из начальной вершины, 
пока не будут исследованы все вершины в текущей компоненте связности. 
Функция find_components используется для определения всех компонент связности в графе. 
После чего, результаты записываются в файл, включая количество компонент связности и состав каждой компоненты.

"""
