class TypeChecked:
    def __init__(self, *args):
        self.types = tuple(args)

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError("Атрибут не найден")

    def __set__(self, obj, value):
        if isinstance(value, self.types):
            obj.__dict__[self._attr] = value
        else:
            raise TypeError("Некорректное значение")

    def __delete__(self, obj):
        del obj.__dict__[self._attr]


class Student:
    name = TypeChecked(str)


student = Student()
student.name = "Mary"

try:
    student.name = 99
except TypeError as e:
    print(e)

print(student.name)
