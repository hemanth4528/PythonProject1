class Car:
    wheels = 4
    def __init__(self, mileage):
        self.mileage = mileage
    def display_specs(self):
        print(self.mileage)
        print(self.wheels)
    @classmethod
    def change_wheels(cls, wheels):
        cls.wheels = wheels

obj = Car(100)
obj.display_specs()
Car.change_wheels(3)
obj.display_specs()
