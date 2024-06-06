from collections import UserList
from copy import deepcopy


class NumberList(UserList):
    def __init__(self, iterable=()) -> None:
        for el in iterable:
            self.check(el)
            return super().__init__(deepcopy(iterable))

    @staticmethod
    def check(val):
        if isinstance(val, (int, float)):
            return True
        raise TypeError(
            'Элементами экземпляра класса NumberList должны быть числа')

    def __setitem__(self, index, item):
        self.check(item)
        self.data[index] = item

    def insert(self, index, item):
        self.check(item)
        self.data.insert(index, item)

    def append(self, item):
        self.check(item)
        self.data.append(item)

    def extend(self, other):
        for el in other:
            self.check(el)
        self.data.extend(item for item in other)

    def __add__(self, other):
        for el in other:
            self.check(el)
        return self.__class__(self.data+other)

    def __radd__(self, other):
        for el in other:
            self.check(el)
        return self.__class__(other+self.data)

    def __iadd__(self, other):
        for el in other:
            self.check(el)
        self.data.extend(item for item in other)
        return self


numberlist = NumberList([0, 1.0])

numberlist[1] = 1
numberlist = numberlist + NumberList([2, 3])
numberlist += NumberList([4, 5])
print(numberlist)
