import sys
import os


def read_matrix_from_file(file_path):
    """
    Читает матрицу смежности из файла.
    Заменяет все "0" на sys.maxsize для обозначения отсутствия прямого пути.
    """
    with open(file_path, 'r') as file:
        matrix = [
            [int(num) if num != "0" else sys.maxsize for num in line.split()]
            for line in file
        ]
    return matrix


def dijkstra(matrix, start):
    """
    Реализация алгоритма Дейкстры для нахождения кратчайших путей.
    Принимает матрицу смежности и индекс начальной вершины.
    """
    n = len(matrix)
    dist = [sys.maxsize] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        # Находим не посещённую вершину с минимальным расстоянием
        u = min((dist[i], i) for i in range(n) if not visited[i])[1]
        visited[u] = True

        for v in range(n):
            if matrix[u][v] != sys.maxsize and not visited[v]:
                if dist[u] + matrix[u][v] < dist[v]:
                    dist[v] = dist[u] + matrix[u][v]

    return dist


def ensure_directory_exists(file_path):
    """
    Проверяет, существует ли директория для файла, и создает ее при необходимости.
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_distances_to_file(file_path, distances):
    ensure_directory_exists(file_path)
    with open(file_path, 'w') as file:
        for index, distance in enumerate(distances):
            if distance == sys.maxsize:
                file.write(f"Вершина {index}: недостижима\n")
            else:
                file.write(f"Вершина {index}: кратчайшее расстояние = {distance}\n")


if __name__ == '__main__':

    input_matrix_path = '/Users/adyl/PycharmProjects/Djikstra/Djikstra_matrix.txt'
    output_distances_path = '/Users/adyl/PycharmProjects/Djikstra/Djikstra_result.txt'

    matrix = read_matrix_from_file(input_matrix_path)
    distances = dijkstra(matrix, 0)

    write_distances_to_file(output_distances_path, distances)
