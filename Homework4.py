# homework 3
# 1 - Є 3 группи людей(sets) australia_blacklist, poker_blacklist, alcohol_blacklist.
# В кожній групі вказані імена. Вивести тих хто виграв джекпот(є одразу в 3х списках)

australia_blacklist = {"Max", "Alya", "Natalia"}
poker_blacklist = {"Nadia", "Sergey", "Max"}
alcohol_blacklist = {"Max", "Olia", "Evgen", "Maria"}

jackpot = australia_blacklist.intersection(poker_blacklist, alcohol_blacklist)

print("Виграв джекпот:", jackpot)


# 2 - Словник має наступні дані: {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Appartments', 'Oleh': 'Trench'}

# Використвоючі f-string вивести: "User_name is living in place_name" для кожного юзера. Використовувати цикл

dictionary = {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Appartments', 'Oleh': 'Trench'}

for user_name, place_name in dictionary.items():
    print(f"{user_name} is living in {place_name}")


# # 3 Є список ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
# # Вивести ТІЛЬКИ коректні імена(тобто стрінги). Використовувати Continue.

list_name = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

for name in list_name:
    if not isinstance(name, str):
        continue
    print(name)


# 4 - Порахувати та вивести(print) кількість букв в строці.
# Юзер щось вводить(input)
# Ваша задача надрукувати кількість кожного символу того що він ввів.

users_input = input("Заповніть рядок: ")
my_dict = {}

for index in users_input:
    my_dict[index] = my_dict.get(index, 0) + 1

for char, count in my_dict.items():
    print(f"{char} -> {count}")

