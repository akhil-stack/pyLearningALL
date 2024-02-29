# Multiple inheritance

class Father:
    def money(self):
        return "5"

    def home(self):
        return "This is fathers home"


class Mother:
    def money(self):
        return "2"

    def home(self):
        return "This is Mother home"


class Son(Mother, Father):
    pass


son = Son()
print(Son.mro())
print(son.home())
#MRO - Method Resolution Order
