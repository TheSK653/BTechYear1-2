class Car:
    def __init__(self, make, model, year):
        self._make = make  # Encapsulated attribute
        self._model = model  # Encapsulated attribute
        self._year = year  # Encapsulated attribute
        self._is_running = False  # Encapsulated attribute

    def start_engine(self):
        if not self._is_running:
            print(f"The {self._year} {self._make} {self._model}'s engine is now running.")
            self._is_running = True
        else:
            print("The engine is already running.")

    def stop_engine(self):
        if self._is_running:
            print(f"The {self._year} {self._make} {self._model}'s engine is now stopped.")
            self._is_running = False
        else:
            print("The engine is already stopped.")

    def get_info(self):
        return f"{self._year} {self._make} {self._model}"

# Creating objects of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2021)

# Accessing and modifying encapsulated attributes
print(f"Car 1: {car1.get_info()}")
car1.start_engine()
car1.stop_engine()

print(f"\nCar 2: {car2.get_info()}")
car2.start_engine()
car2.start_engine()
car2.stop_engine()