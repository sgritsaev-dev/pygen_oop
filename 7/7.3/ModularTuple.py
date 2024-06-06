class ModularTuple(tuple):
    def __new__(cls, iterable=(), num=100):
        iterable = (el % num for el in iterable)
        return super().__new__(cls, iterable)


modulartuple = ModularTuple([101, 102, 103, 104, 105])

print(modulartuple)
print(type(modulartuple))
