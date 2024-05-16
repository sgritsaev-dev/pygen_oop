class SuperString:
    def __init__(self, string) -> None:
        self.string = string

    def __repr__(self) -> str:
        return f'{self.string}'

    def __add__(self, other):
        if isinstance(other, (self.__class__)):
            return self.__class__(
                self.string + other.string
                )
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int)):
            return self.__class__(
                self.string*other,
                )
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int)):
            return self.__class__(
                self.string[:len(self.string)//other],
                )
        else:
            return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, (int)):
            if other == 0:
                return self.__class__(self.string[:])
            elif other < len(self.string):
                return self.__class__(
                    self.string[:(-other)],
                    )
            return ''
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, (int)):
            if other < len(self.string):
                return self.__class__(
                    self.string[other:],
                    )
            return ''
        return NotImplemented
