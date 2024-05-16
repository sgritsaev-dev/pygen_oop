class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates) -> None:
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self) -> str:
        return f'FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})'

    def __add__(self, other):
        if isinstance(other, (self.__class__)):
            return self.__class__(
                self.proteins+other.proteins,
                self.fats+other.fats,
                self.carbohydrates+other.carbohydrates
                )
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(
                self.proteins*other,
                self.fats*other,
                self.carbohydrates*other
                )
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(
                self.proteins/other,
                self.fats/other,
                self.carbohydrates/other
                )
        else:
            return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(
                self.proteins//other,
                self.fats//other,
                self.carbohydrates//other
                )
        else:
            return NotImplemented
