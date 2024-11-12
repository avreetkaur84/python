class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")

class EV(Car):
    def __init__(self, battery_size, brand, model):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def display(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Car Battery Size: {self.battery_size}")

my_car = Car("Toyota", "Corolla")
ev_car = EV("300", "Ferari", "Mustang")
ev_car.display()