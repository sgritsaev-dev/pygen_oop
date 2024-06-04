from random import choice


class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.random = choice(range(self.start, self.end + 1))
        self.cache = cache
        if self.cache:
            self.cache_list = []
            self.cache_list.append(self.random)

    # def __set_name__(self, cls, attr):
    #     self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.cache:
            return self.cache_list[0]
        else:
            return self.random

    def __set__(self, obj, value):
        raise AttributeError("Изменение невозможно")

    def __delete__(self, obj):
        del obj.__dict__[self._attr]


# TEST_1:
class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)


magicpoint = MagicPoint()

print(magicpoint.x in [1, 2, 3, 4, 5])
print(magicpoint.y in [1, 2, 3, 4, 5])
print(magicpoint.z in [1, 2, 3, 4, 5])


# TEST_2:
class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)


magicpoint = MagicPoint()

print(magicpoint.x in [6, 7, 8, 9, 10])
print(magicpoint.y in [6, 7, 8, 9, 10])
print(magicpoint.z in [6, 7, 8, 9, 10])


# TEST_3:
class MagicPoint:
    x = RandomNumber(0, 5, True)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)


magicpoint = MagicPoint()
value = magicpoint.x

print(magicpoint.x in [0, 1, 2, 3, 4, 5])
print(magicpoint.x == value)
print(magicpoint.x == value)
print(magicpoint.x == value)


# TEST_4:
class MagicPoint:
    x = RandomNumber(0, 5)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)


magicpoint = MagicPoint()

try:
    magicpoint.x = 10
except AttributeError as e:
    print(e)
