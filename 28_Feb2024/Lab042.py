# hierarchical inheritance

class Vehicle:
    def info(self):
        return "This is vehicle method"


class Car(Vehicle):
    pass
         # def car_method(self):
        #     return "This is car method"


class Bycycle(Car):
    def info(self):
        return "This is bycycle method"


car = Car()
print(car.info())
