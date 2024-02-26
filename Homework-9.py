class Wagon:

    def __init__(self, number):
        self.number = number
        self.__passengers = []

    def add_passenger(self, *passengers):
        """Додає пасажирів до вагона."""
        for passenger in passengers:
            if len(self.__passengers) < 10:
                self.__passengers.append(passenger)
            else:
                print("The wagon is full, cannot add more passengers.")

    def get_passenger_count(self):
        """Повертає кількість пасажирів у вагоні."""
        return len(self.__passengers)

    def __str__(self):
        return f"Wagon {self.number}: {self.get_passenger_count()} passengers"


class Train:
    def __init__(self):
        self.wagons = [Wagon(0)]  # Локомотив має номер 0
        self.head = self.wagons[0]

    def add_wagon(self):
        wagon_number = len(self.wagons)  # Номер нового вагона
        new_wagon = Wagon(wagon_number)
        self.wagons.append(new_wagon)

    def __len__(self):
        return len(self.wagons) - 1  # Повертаємо кількість вагонів без локомотива

    def __str__(self):
        wagon_numbers = "-".join([str(f"[{wagon.number + 1}]") for wagon in self.wagons]) #<=[HEAD]-[0]-[1]-[2]
        return f"<=[HEAD]-{wagon_numbers if wagon_numbers else '...'}"


train = Train()
train.add_wagon()
train.add_wagon()
train.wagons[1].add_passenger("Passenger 1")
train.wagons[1].add_passenger("Passenger 2")
train.wagons[2].add_passenger("Passenger 3")

print(len(train))  # Поверне кількість вагонів у потязі (без локомотива)
print(train)  # Виведе потяг у форматі <=[HEAD]-[0]-[1]-[2]
