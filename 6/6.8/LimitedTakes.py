class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __init__(self, times):
        self.times = times

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            self.times -= 1
            if self.times < 0:
                raise MaxCallsException("Превышено количество доступных обращений")
            return obj.__dict__[self._attr]
        else:
            raise AttributeError("Атрибут не найден")

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value

    def __delete__(self, obj):
        del obj.__dict__[self._attr]


class Student:
    name = LimitedTakes(3)


student = Student()
student.name = "Gwen"

print(student.name)
print(student.name)
print(student.name)

try:
    print(student.name)
except MaxCallsException as e:
    print(e)
