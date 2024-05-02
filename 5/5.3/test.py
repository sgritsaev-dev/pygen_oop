class Fruit:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    # def __eq__(self, other):
    #     if isinstance(other, Fruit):
    #         return self.mass == other.mass
    #     return NotImplemented

    def __le__(self, other):
        if isinstance(other, Fruit):
            return self.mass <= other.mass
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Fruit):
            return self.mass >= other.mass
        return NotImplemented


fruit1 = Fruit('банан', 150)
fruit2 = Fruit('яблоко', 180)
fruit3 = Fruit('груша', 150)

print(fruit1 <= fruit2)
print(fruit1 >= fruit2)
print(fruit1 <= fruit3)
print(fruit1 >= fruit3)