# Define a class representing a car and create instances of car objects.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"Driving {self.year} {self.make} {self.model}")

car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)

car1.drive()
car2.drive()
