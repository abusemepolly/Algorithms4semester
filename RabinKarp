# Определение функции алгоритма Рабина-Карпа
def rabin_karp(text, pattern):
    d = 256  # Количество символов в используемом алфавите
    q = 101  # Простое число для вычисления хеша
    m = len(pattern)
    n = len(text)
    h = 1
    p = 0  # хеш шаблона
    t = 0  # хеш текста
    results = []

    # Значение h = pow(d, m-1) % q
    for i in range(m-1):
        h = (h * d) % q

    # Вычисление хеша шаблона и первого окна текста
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Скользим по тексту
    for i in range(n - m + 1):
        # Если хеш шаблона совпадает с хешем текущего окна текста, проверяем на точное совпадение
        if p == t:
            if text[i:i+m] == pattern:
                results.append(i)

        # Вычисляем хеш для следующего окна текста
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q

    return results


file_path = "/RabinKarp/RabinKarptext.txt"
pattern = input("Введите шаблон для поиска: ")


try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    positions = rabin_karp(text, pattern)
    if positions:
        print(f"Шаблон найден на позициях: {positions}")
    else:
        print("Шаблон не найден.")
except FileNotFoundError:
    print("Файл не найден. Пожалуйста, проверьте путь к файлу.")
