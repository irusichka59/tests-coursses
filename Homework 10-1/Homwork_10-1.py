# 1 - Зробити адаптер from_csv_to_html
# Приклад(вважайте, що на вході завжди формат csv - перша строка це назва колонок відділених комою, всі інші строки
# це дані, відділені комою):
#
# name, last_name, age, salary
# Leo, Moracchioli, 50, 5000
# ...
# Lemmy, Kilmister, 83, 0
def from_csv_to_html(file_path):
    html_string = ""  # Ініціалізуємо рядок HTML

    # Відкриваємо файл для читання
    with open(file_path, 'r') as file:
        # Читаємо перший рядок (назви колонок)
        columns = file.readline().strip().split(',')

        # Проходимося по кожному рядку у файлі
        for line in file:
            # Розбиваємо рядок на окремі значення
            values = line.strip().split(',')

            # Додаємо відповідні теги HTML для кожного значення
            html_string += "\n".join(f"<{col}>{val}</{col}>" for col, val in zip(columns, values))
            html_string += "\n<br />............<br />\n"  # Додаємо роздільник між записами

    return html_string


# Приклад використання
csv_file_path = "./data.csv"  # Замініть на шлях до Вашого CSV файлу
html_result = from_csv_to_html(csv_file_path)
print(html_result)
