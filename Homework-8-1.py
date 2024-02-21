# Клас вашого рахунку банківського рахунку.
# Обов'язкові методи: покласти на рахунок, зняти з рахунку, подивитись баланс.
# Баланс напряму міняти не можна(підказка: тут краще за все робити через атрибут __balance ),
# використовуйте методи  ядл поповнення та зняття коштів з рахунку
# Зняти гроші можна при умові що їх достатньо на рахунку
# Використати як мінімум по 1 разу елементи: public, protected, privat атрибути, гетери, сетери,
# staticmethod та classmethod
# Приклад ініціації класу. не обов'язково саме такий, це концепт my_user_account = UserAccount(name, card_number,
# cvv, date, balance)
#
class UserAccount:
    def __init__(self, name, card_number, cvv, date, balance):
        self._name = name  # protected атрибут
        self.__card_number = card_number  # private атрибут
        self.__cvv = cvv  # private атрибут
        self.__date = date  # private атрибут
        self.__balance = balance  # private атрибут

    # гетер для отримання балансу
    def get_balance(self):
        return self.__balance

    # setter для поповнення рахунку
    def deposit(self, amount):
        self.__balance += amount

    # setter для зняття коштів з рахунку
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            print("Insufficient funds.") #Зняти гроші можна при умові що їх достатньо на рахунку
            return False

    # staticmethod для вітання користувача
    @staticmethod
    def greet_user(name):
        print(f"Hello, {name}!")

    # classmethod для створення об'єкту з рядка даних
    @classmethod
    def create_from_string(cls, data_string):
        name, card_number, cvv, date, balance = data_string.split(',')
        return cls(name, card_number, cvv, date, float(balance))


# Приклад використання класу
my_user_account = UserAccount("John Doe", "1234567890", "123", "12/25", 1000.0)
my_user_account.greet_user(my_user_account._name)
print("Balance:", my_user_account.get_balance())
my_user_account.deposit(500.0)
print("Balance after deposit:", my_user_account.get_balance())
my_user_account.withdraw(500.0)
print("Balance after withdrawal:", my_user_account.get_balance())

# Створення об'єкту з рядка даних
data_string = "Jane Doe,0987654321,456,11/24,2000.0"
user_account_from_string = UserAccount.create_from_string(data_string)
print("User account created from string:", user_account_from_string.__dict__)

2

