from math import sqrt 

class Vector:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"""Vector({self.x}, {self.y})"""
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __pos__(self):
        return Vector(self.x, self.y)
    
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)


vector = Vector(3, -4)

print(+vector)
print(-vector)
print(abs(vector))