class SuperInt(int):
    def repeat(self, n=2):
        if self >= 0:
            return self.__class__(int(str(self) * n))
        else:
            return self.__class__(-int(str(abs(self)) * n))

    def to_bin(self):
        if self >= 0:
            return bin(self)[2:]
        else:
            return "-" + bin(self)[3:]

    def next(self):
        return self.__class__(self + 1)

    def prev(self):
        return self.__class__(self - 1)

    def __iter__(self):
        for el in str(self).replace("-", ""):
            yield self.__class__(el)


superint1 = SuperInt(-1)
superint2 = SuperInt(-17)

print(*superint2)
print(superint2.repeat(3))
