from mammal import Mammal  # інкапсуляція


class Feline(Mammal):  # наслідування
    def __init__(self, name, age, fur_color, breed):
        super().__init__(name, age, fur_color)
        self.breed = breed

    def give_birth(self):
        print(f"{self.name} gives birth to live young cat.")  # поліморфізм

    def speak(self):
        print(f"{self.name} meows.")
