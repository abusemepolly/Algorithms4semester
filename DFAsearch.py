def build_dfa(pattern):
    """Построение детерминированного конечного автомата для заданного шаблона."""
    alphabet = set(pattern)  # Уникальные символы в шаблоне
    m = len(pattern)
    dfa = [{ch: 0 for ch in alphabet} for _ in range(m + 1)]
    dfa[0][pattern[0]] = 1

    x = 0
    for j in range(1, m):
        for ch in alphabet:
            dfa[j][ch] = dfa[x][ch]
        dfa[j][pattern[j]] = j + 1
        x = dfa[x][pattern[j]]
    dfa[m] = {ch: dfa[x][ch] for ch in alphabet}  # Завершающее состояние

    return dfa


def search_pattern(text, pattern):
    """Поиск шаблона в тексте с использованием ДКА."""
    dfa = build_dfa(pattern)
    n = len(text)
    m = len(pattern)
    state = 0
    positions = []

    for i in range(n):
        state = dfa[state].get(text[i], 0)
        if state == m:
            position = i - m + 1
            positions.append(position)

    return positions


file_path = "/Users/adyl/PycharmProjects/DFAsearch/DFAtext.txt"
pattern = input("Введите шаблон для поиска: ")

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

positions = search_pattern(text, pattern)

if positions:
    print("Шаблон найден на позициях:", positions)
else:
    print("Шаблон не найден.")
