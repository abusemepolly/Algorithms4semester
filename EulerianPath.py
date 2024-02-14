def is_eulerian_cycle(matrix):
    n = len(matrix)  # Количество вершин в графе
    for i in range(n):
        degree = sum(matrix[i][j] != 0 for j in range(n))
        if degree % 2 != 0:
            return False  # Найдена вершина с нечетной степенью

    # Проверка на связность графа
    visited = [False] * n
    dfs(matrix, 0, visited)
    if not all(visited):
        return False  # Граф несвязен

    return True  # Граф Эйлеров


def dfs(matrix, vertex, visited):
    visited[vertex] = True
    for i in range(len(matrix)):
        if matrix[vertex][i] != 0 and not visited[i]:
            dfs(matrix, i, visited)


def remove_edge(matrix, u, v):
    matrix[u][v] -= 1
    matrix[v][u] -= 1


def find_eulerian_cycle(matrix):
    if not is_eulerian_cycle(matrix):
        return None

    n = len(matrix)
    cycle = []
    stack = [0]
    while stack:
        u = stack[-1]
        has_edge = False
        for v in range(n):
            if matrix[u][v] > 0:
                stack.append(v)
                remove_edge(matrix, u, v)
                has_edge = True
                break
        if not has_edge:
            cycle.append(stack.pop())

    return cycle


def count_components(matrix):
    n = len(matrix)
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(matrix, i, visited)
            count += 1
    return count


def is_bridge(matrix, u, v):
    initial_components = count_components(matrix)

    matrix[u][v] -= 1
    matrix[v][u] -= 1

    new_components = count_components(matrix)

    matrix[u][v] += 1
    matrix[v][u] += 1

    return new_components > initial_components


def create_graph_from_adjacency_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = [[int(num) for num in line.split()] for line in lines]
    return matrix


def write_eulerian_cycle_to_file(cycle, filename):
    with open(filename, 'w') as file:
        cycle_str = '->'.join(map(str, cycle))
        file.write("Эйлеров цикл:\n" + cycle_str + "\n")


input_filename = '/Users/adyl/PycharmProjects/EulerianPath/EulerCorrect.txt'
output_filename = '/Users/adyl/PycharmProjects/EulerianPath/EulerCycleOutput.txt'


matrix = create_graph_from_adjacency_matrix(input_filename)


eulerian_cycle = find_eulerian_cycle(matrix)


if eulerian_cycle is not None:
    print("Найден Эйлеров цикл:", eulerian_cycle)

    write_eulerian_cycle_to_file(eulerian_cycle, output_filename)
    print(f"Эйлеров цикл был записан в файл {output_filename}")
else:
    print("В данном графе Эйлеров цикл не найден.")
