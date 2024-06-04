class NonNegativeInteger:
    def __init__(self, attr, default=None):
        self._attr = attr
        self.default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        elif self.default is not None:
            return self.default
        else:
            raise AttributeError("Атрибут не найден")

    def __set__(self, obj, value):
        if isinstance(value, int) and value >= 0:
            obj.__dict__[self._attr] = value
        else:
            raise ValueError("Некорректное значение")

    def __delete__(self, obj):
        del obj.__dict__[self._attr]


class Student:
    score = NonNegativeInteger("score", 0)


student = Student()

print(student.score)
student.score = 0
print(student.score)
