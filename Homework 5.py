# Homework 5

# Дано список str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Лише за допомогою функцій map, lambda, zip(необов'зково) створити та надрукувати словник квадратів цих чисел

new_dict = dict(map(lambda x: (int(x), int(x) ** 2), str_list))

# Очікуваний результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
print(new_dict)


# 2 Напишіть інтерактивний калькулятор.
class FormulaError(Exception):
    pass


class WrongOperatorError(FormulaError):
    pass


def calculate_formula(formula):
    try:
        elements = formula.split()
        if len(elements) != 3:
            raise FormulaError("Формула має складатися з трьох елементів (число, оператор, число).")

        num1_str, operator, num2_str = elements

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            raise ValueError("Введені дані повинні бути числовими значеннями.")

        if operator not in ('*', '/'):
            raise WrongOperatorError("Підтримуються тільки оператори '*' і '/'.")

        if operator == '/' and num2 == 0:
            raise FormulaError("Ділення на 0 неможливе.")

        inner_result = 0
        if operator == '*':
            inner_result = num1 * num2
        elif operator == '/':
            inner_result = num1 / num2

        formatted_result = round(inner_result, 2)
        print(f"Результат: {formatted_result}")
        return formatted_result

    except FormulaError as fe:
        print(f"Помилка: {fe}")
        return None
    except ValueError as ve:
        print(f"Помилка: {ve}")
        return None


# Три спроби використання калькулятора
attempt = 0
while attempt < 3:
    formula_input = input("Введіть формулу (число оператор число): ")
    result = calculate_formula(formula_input)

    if result is not None:
        break  # Вихід з циклу, якщо формула валідна та результат успішно обчислений

    attempt += 1

if attempt == 3:
    print("Спроби використання калькулятора закінчились.")
