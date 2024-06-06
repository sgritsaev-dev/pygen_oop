from typing import Any


class FieldTracker:
    cache_dict = {}

    def __setattr__(self, name: str, value: Any) -> None:
        object.__setattr__(self, name, value)
        self.cache_dict.setdefault(name, []).append(value)

    def base(self, name):
        return self.cache_dict[name][0]

    def has_changed(self, name):
        return len(self.cache_dict[name]) > 1

    def changed(self):
        res = {}
        for key, value in self.cache_dict.items():
            if len(value) > 1:
                res[key] = value[0]
        return res

    def save(self):
        for key in self.cache_dict:
            self.cache_dict[key] = [self.cache_dict[key][-1]]


class Point(FieldTracker):
    fields = ("x", "y", "z")

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.z = 5


print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())
