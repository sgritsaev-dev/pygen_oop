from math import sqrt 

class ColoredPoint:
    
    def __init__(self, x, y, color=(0,0,0)) -> None:
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self) -> str:
        return f"""ColoredPoint({self.x}, {self.y}, {self.color})"""
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)
    
    def __neg__(self):
        return ColoredPoint(-self.x, -self.y, self.color)
    
    def __invert__(self):
        return self.__class__(self.y, self.x, tuple(255-el for el in self.color))
    
    
    
point = ColoredPoint(2, -3)

print(+point)
print(-point)
print(~point)

point1 = ColoredPoint(2, -3)
point2 = ColoredPoint(10, 20, (34, 45, 67))
point2= ~point2

print(point1.color)
print(point2.color)