class Vector:

    def __repr__(self) -> str:
        return f"""Vector({self.x}, {self.y})"""

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, value: object) -> bool:
        try:
            if isinstance(value, Vector):
                return self.x == value.x and self.y == value.y
            elif isinstance(value, tuple) and len(value) == 2:
                return self.x == value[0] and self.y == value[1]
            return NotImplemented
        except:
            return NotImplemented


a = Vector(1, 2)
b = Vector(3, 4)
c = Vector(5, 6)

vectors = [a, b, c]
print(vectors)
