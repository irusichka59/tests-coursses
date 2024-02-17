# 1Створіть декоратор, який виводить в консоль назву викликаної функції.
# Наприклад, створіть пару функцій для арифметичних операцій підсумовування та множення.
# Під час виклику цих функцій має бути повернутий результат операції, а ім’я викликаної функції має відображатися
# на консолі разом із результатом. Використовуйте __name__
def log_function_name(func):
    def wrapper(*args, **kwargs):
        resul = func(*args, **kwargs)
        print(f"Function '{func.__name__}' was called with arguments {args} and keyword arguments {kwargs}.")
        return resul

    return wrapper


# Декоруємо функції для операцій підсумовування та множення
@log_function_name
def add(x, y):
    return x + y


@log_function_name
def multiply(x, y):
    return x * y


# При виклику функцій результат разом з ім'ям функції буде виведений у консоль
print(add(5, 24))
print(multiply(9, 6))



