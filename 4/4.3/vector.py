import math
class Vector:
    def __init__(self, x=0, y=0) -> None:
        self.x=x
        self.y=y
    def abs(self):
        return math.sqrt(self.x**2+self.y**2)