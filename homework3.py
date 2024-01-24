# 1) Запропонувати юзеру створити список(введіть продукти через пробіл)

input_product = (input("Введіть продукти через пробіл: "))

# 2) Строку яку ввів юзер перевести в список
product_list = input_product.split()

# 4) Якщо юзер нічогоне ввів(або ввів лише пробіли) то написати список продуктів порожній і закінчити програму

if not input_product or input_product.isspace():
    print("Список продуктів порожній")
else:
    # 3) Надрукувати список який ввів юзер
    print("Створений список продуктів:", product_list)
    while True:  # 8) Продовжувати поки список не стане порожнім
        # 5)Запропонувати юзеру ввести продукт та ознаку чи варто його видаляти чи додавати(якщо видаляти, то продукт
        # починаеться з -
        second_input = input("Введіть продукт та дію (+ для додавання, - для видалення): ")

        if not second_input:
            break

        list_action = second_input[0]
        # 6) Додати/видалити продукт
        if list_action == "+":

            product = second_input[1:].strip()
            product_list.append(product)
            print(f"Продукт '{product}' додано до списку.")
            # 7) Надрукувати оновлений список продуктів
            print("Поточний список продуктів:", product_list)
        elif list_action == "-":

            product = second_input[1:].strip()
            if product in product_list:
                product_list.remove(product)
                print(f"Продукт '{product}' видалено зі списку.")
                # 7) Надрукувати оновлений список продуктів
                print("Поточний список продуктів:", product_list)
            else:
                print(f"Продукт '{product}' не знайдено у списку.")
        else:
            print("Невідома дія. Введіть + для додавання або - для видалення.")
    if len(product_list):
        print("Остаточний список продуктів:", product_list)
    else:
        print("Остаточний список продуктів порожній.")
