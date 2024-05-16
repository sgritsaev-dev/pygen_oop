class Vector:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"""Vector({self.x}, {self.y})"""

    def __add__(self, other):
        if isinstance(other, (self.__class__)):
            return self.__class__(
                self.x+other.x,
                self.y+other.y,
                )
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, (self.__class__)):
            return self.__class__(
                self.x-other.x,
                self.y-other.y,
                )
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(
                self.x*other,
                self.y*other,
                )
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(
                self.x/other,
                self.y/other,
                )
        else:
            return NotImplemented
