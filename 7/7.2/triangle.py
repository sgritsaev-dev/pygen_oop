class Triangle:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, side) -> None:
        super().__init__(side, side, side)
