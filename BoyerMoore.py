def bad_character_heuristic(pattern):
    """Создаем таблицу плохих символов."""
    bad_char = {}
    for index, char in enumerate(pattern):
        bad_char[char] = index
    return bad_char


def boyer_moore_search(text, pattern):
    """Поиск шаблона в тексте с использованием алгоритма Бойера-Мура."""
    m = len(pattern)
    n = len(text)
    bad_char = bad_character_heuristic(pattern)

    positions = []  # Список для хранения позиций начала совпадений
    shift = 0

    while shift <= n - m:
        j = m - 1  # Начинаем сравнение с конца шаблона

        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            positions.append(shift)
            shift += (m - bad_char.get(text[shift + m], -1)) if shift + m < n else 1
        else:
            shift += max(1, j - bad_char.get(text[shift + j], -1))

    return positions


file_path = "/BoyerMoore/BoyerMooretext.txt"
pattern = input("Введите шаблон для поиска: ")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    positions = boyer_moore_search(text, pattern)
    if positions:
        print("Шаблон найден на позициях:", positions)
    else:
        print("Шаблон не найден.")
except FileNotFoundError:
    print("Файл не найден. Проверьте путь к файлу.")
