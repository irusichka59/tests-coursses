from abc import abstractmethod

from animal import Animal  # інкапсуляція


class Mammal(Animal):  # наслідування
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    @abstractmethod
    def give_birth(self):
        pass  # абстрактний метод

    def lactate(self):
        print(f"{self.name} is lactating.")  # поліморфізм
