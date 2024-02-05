# 1)
#
# Є json файл
#
# В ньому є департамент(departments)
#
# У кожного departments є витрати(expenses) та прибуток(incomes)
#
# Задача:
#
# Написати скріпт де
#
# 1) будуть вичитані дані з файлу
#
# 2) всім робітникам в департаментах де витрати менші за приубуток буде збільшено зп(salary) на 10%
#
# 3) потім ці дані(оновлені) запише в файл з назвою new_costs.json

import json


def update_salaries(departments_data):
    for department in departments_data:
        expenses = department.get('expenses', 0)
        income = department.get('income', 0)

        if expenses < income:
            employees = department.get('employees', [])
            for employee in employees:
                salary = employee.get('salary', 0)
                new_salary = salary * 1.1  # Збільшення зарплати на 10%
                employee['salary'] = round(new_salary, 2)


def main():
    input_filename = 'departments.json'
    output_filename = 'new_costs.json'

    try:
        # Відкриття та зчитування даних з файлу
        with open(input_filename, 'r') as file:
            data = json.load(file)

        # Оновлення зарплат за умовою
        update_salaries(data['departments'])

        # Запис оновлених даних у новий файл
        with open(output_filename, 'w') as new_file:
            json.dump(data, new_file, indent=2)

        print(f"New costs have been written to {output_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")


main()


# 2) Створіть 2 функції
#
# get_sum та print_table(імена можете вказувати на ваш розсуд)
#
# 1) get_sum викликає print_table всередині себе
#
# 2) get_sum приймає 2 значення: число та операцію +,*(тобто get_sum(num: int, operation:str) ) та повертає результат додавання числа та наступнийх 9ти після нього(тобто результат додавання 10 цифр)
#
# 3) print_table друкує таблицю з числом та операцєю які було передано в get_sum від 1 до 10
#
# вважайте, що юзер завжди вводить правильно операцію та число

def print_table(number, operation):
    for i in range(1, 11):
        result = number * i
        print(f"{number} {operation} {i} = {result}")


def get_sum(num, operation):
    print_table(num, operation)
    # Сума чисел від 6 до 15 (5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14)
    result_summ = sum(range(num + 5, num + 15))
    print(f"sum is {num}+6+7+8+9+10+11+12+13+14 = {result_summ}")
    return result_summ


if __name__ == '__main__':
    result_sum = get_sum(5, '*')
