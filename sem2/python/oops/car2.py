class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return f"{super().display_info()}, {self.num_doors}-door car"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def display_info(self):
        return f"{super().display_info()}, {self.num_wheels}-wheeler motorcycle"

class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        return f"{super().display_info()}, {self.cargo_capacity}-cargo capacity"

# Creating object
car = Car("Toyota", "Camry", 2022, 4)
motorcycle = Motorcycle("Harley-Davidson", "Street Glide", 2022, 2)
truck = Truck("Ford", "F-150", 2022, 5000)

print(car.display_info())
print(motorcycle.display_info())
print(truck.display_info())