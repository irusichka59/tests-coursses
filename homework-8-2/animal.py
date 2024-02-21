from abc import ABC  # абстракція


class Animal(ABC):  # наслідування, абстракція
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass  # Поліморфізм: буде перевизначено у підкласах

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")
