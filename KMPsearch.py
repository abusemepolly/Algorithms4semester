"""

Основная идея заключается в том, что когда происходит несовпадение,
алгоритм использует уже проверенную информацию о шаблоне для того,
чтобы не совершать лишние проверки в тексте.
Это достигается за счет использования таблицы префиксов,
которая для каждой позиции в шаблоне указывает длину наибольшего собственного префикса,
совпадающего с суффиксом для подстроки, заканчивающейся на этой позиции.

"""


def kmp_search(text, pattern):
    """Выполнение поиска KMP в тексте."""
    m, n = len(pattern), len(text)
    lps = compute_lps_array(pattern)
    positions = []  # Список для хранения позиций начала совпадений

    i = j = 0  # i - индекс для text, j - индекс для pattern
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            positions.append(i - j)  # Совпадение найдено
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return positions


def compute_lps_array(pattern):
    """Вычисление префикс-функции для шаблона."""
    length = 0  # Длина предыдущего наибольшего префикса
    lps = [0] * len(pattern)  # LPS-массив
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


file_path = "/KMPsearch/KMPtext.txt"
pattern = input("Введите шаблон для поиска: ")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    positions = kmp_search(text, pattern)
    if positions:
        print("Шаблон найден на позициях:", positions)
    else:
        print("Шаблон не найден.")
except FileNotFoundError:
    print("Файл не найден. Проверьте путь к файлу.")
