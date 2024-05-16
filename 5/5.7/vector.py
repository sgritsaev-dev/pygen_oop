from math import sqrt


class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __bool__(self):
        return any((self.x != 0, self.y != 0))

    def __int__(self):
        return int(sqrt(self.x**2 + self.y**2))

    def __float__(self):
        return float(sqrt(self.x**2 + self.y**2))

    def __complex__(self):
        return complex(self.x, self.y)
