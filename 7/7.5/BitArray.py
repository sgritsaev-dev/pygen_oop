from _collections_abc import Sequence
from typing import Iterator
from copy import deepcopy as dc


class BitArray(Sequence):
    def __init__(self, sequence=[]) -> None:
        self.sequence = list(el for el in dc(list(sequence)))

    def __str__(self) -> str:
        return f"{[el for el in self.sequence]}"

    def __getitem__(self, index):
        return self.sequence[index]

    def __len__(self) -> int:
        return super().__len__()

    def __invert__(self):
        defa = [1, 0]
        return self.__class__(defa[el] for el in self.sequence)

    def __reversed__(self) -> Iterator:
        return self.sequence[::-1]

    def __and__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        if len(self.sequence) != len(other.sequence):
            raise TypeError
        return self.__class__(a & b for a, b in zip(self.sequence, other.sequence))

    def __or__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        if len(self.sequence) != len(other.sequence):
            raise TypeError
        return self.__class__(a | b for a, b in zip(self.sequence, other.sequence))


bitarray = BitArray([1, 0, 1, 1])

print(bitarray)
print(~bitarray)
print(bitarray[0])
print(bitarray[1])
print(bitarray[-1])
print(0 in bitarray)
print(1 not in bitarray)
