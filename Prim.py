import sys


def prim_algorithm(matrix):
    n = len(matrix)
    selected = [False] * n  # Массив для отслеживания добавленных в MST вершин
    num_edges = 0
    selected[0] = True
    result_edges = []

    while num_edges < n - 1:
        minimum = sys.maxsize
        x = 0
        y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and matrix[i][j] != sys.maxsize:
                        if minimum > matrix[i][j]:
                            minimum = matrix[i][j]
                            x = i
                            y = j
        result_edges.append((x, y, matrix[x][y]))
        selected[y] = True
        num_edges += 1

    return result_edges


def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        matrix = [[int(num) if num != "0" else sys.maxsize for num in line.split()] for line in file]
    return matrix


def write_result_to_file(edges, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("Результат работы алгоритма Прима:\n")
        total_weight = sum([edge[2] for edge in edges])
        file.write(f"Общий вес минимального покрывающего дерева: {total_weight}\n")
        for edge in edges:
            file.write(f"{chr(65 + edge[0])} - {chr(65 + edge[1])}, Вес: {edge[2]}\n")


input_file_path = 'prim_matrix.txt'
output_file_path = 'prim_result.txt'


matrix = read_matrix_from_file(input_file_path)
result_edges = prim_algorithm(matrix)
write_result_to_file(result_edges, output_file_path)
