import sys
import os

def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        matrix = [
            [int(num) if num != "0" else sys.maxsize for num in line.split()]
            for line in file
        ]
    return matrix

def bellman_ford(matrix, start):
    n = len(matrix)
    dist = [sys.maxsize] * n
    dist[start] = 0

    for _ in range(n-1):
        for u in range(n):
            for v in range(n):
                if matrix[u][v] != sys.maxsize and dist[u] + matrix[u][v] < dist[v]:
                    dist[v] = dist[u] + matrix[u][v]

    # Проверка на наличие циклов отрицательного веса
    for u in range(n):
        for v in range(n):
            if matrix[u][v] != sys.maxsize and dist[u] + matrix[u][v] < dist[v]:
                print("Граф содержит цикл отрицательного веса")
                return None

    return dist

def ensure_directory_exists(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_distances_to_file(file_path, distances):
    ensure_directory_exists(file_path)
    with open(file_path, 'w') as file:
        if distances is None:
            file.write("Граф содержит циклы отрицательного веса, кратчайшие пути не могут быть найдены.\n")
        else:
            for index, distance in enumerate(distances):
                if distance == sys.maxsize:
                    file.write(f"Вершина {index}: недостижима\n")
                else:
                    file.write(f"Вершина {index}: кратчайшее расстояние = {distance}\n")

if __name__ == '__main__':

    input_matrix_path = '/Users/adyl/PycharmProjects/BellmanFord/BFcorrect.txt'
    output_distances_path = '/Users/adyl/PycharmProjects/BellmanFord/BF_result.txt'

    matrix = read_matrix_from_file(input_matrix_path)
    distances = bellman_ford(matrix, 0)

    write_distances_to_file(output_distances_path, distances)
