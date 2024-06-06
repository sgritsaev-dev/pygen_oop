class AdvancedTuple(tuple):
    def __add__(self, other):
        return self.__class__(tuple(self) + tuple(other))

    def __radd__(self, other):
        return self.__class__(tuple(other) + tuple(self))


advancedtuple = AdvancedTuple([1, 2, 3])

print(advancedtuple + (4, 5))
print(advancedtuple + [4, 5])
print({"a": 1, "b": 2} + advancedtuple)

print(
    (1, 2, 3)
    + (
        4,
        5,
        6,
    )
)
