# 3 Створіть декоратор, який повертає результат функції. а також друкує час за який вона виконана.
# Підсказка (для фіксації часу імпортуйте модуль time: import time)

import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} executed in {execution_time:.6f} seconds")
        return result

    return wrapper


# Приклад використання декоратора
@timer_decorator
def example_function():
    # Ваша функція або код тут
    time.sleep(1)  # Приклад штучної затримки


# Викликаємо функцію
example_function()


def print_table(number, operation):
    for i in range(1, 11):
        resul = number * i
        print(f"{number} {operation} {i} = {resul}")
