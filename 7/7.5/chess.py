from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical) -> None:
        self.vertical = vertical
        self.horizontal = horizontal
        self.hor = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
        self.ver = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}

    @abstractmethod
    def can_move(self):
        pass


class Knight(ChessPiece):

    def can_move(self, hori, veri):
        hori = str(hori)
        veri = str(veri)
        if (
            (
                (self.hor[str(self.horizontal)] + 2 == self.hor[hori])
                or (self.hor[str(self.horizontal)] - 2 == self.hor[hori])
            )
            and (
                (self.ver[str(self.vertical)] + 1 == self.ver[veri])
                or (self.ver[str(self.vertical)] - 1 == self.ver[veri])
            )
        ) or (
            (
                (self.hor[str(self.horizontal)] + 1 == self.hor[hori])
                or (self.hor[str(self.horizontal)] - 1 == self.hor[hori])
            )
            and (
                (self.ver[str(self.vertical)] + 2 == self.ver[veri])
                or (self.ver[str(self.vertical)] - 2 == self.ver[veri])
            )
        ):
            return True
        return False


class King(ChessPiece):

    def can_move(self, hori, veri):
        hori = str(hori)
        veri = str(veri)
        if str(self.vertical) == veri and self.horizontal == hori:
            return False
        if (
            abs(self.hor[hori] - self.hor[self.horizontal]) <= 1
            and abs(self.ver[veri] - self.ver[str(self.vertical)]) <= 1
        ):
            return True
        return False


king = King("e", 3)

print(king.can_move("e", 3))
print(king.can_move("e", 4))
print(king.can_move("b", 1))
