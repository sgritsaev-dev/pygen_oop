class Queue:
    def __init__(self, *args) -> None:
        self.que = list(args)

    def add(self, *args):
        for element in args:
            self.que.append(element)

    def pop(self):
        if len(self.que) > 0:
            return self.que.pop(0)
        return None

    def __str__(self) -> str:
        return " -> ".join(str(el) for el in self.que)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return self.que == value.que
        return NotImplemented

    def __neq__(self, value):
        return not self.__eq__(value)

    def __add__(self, value):
        if isinstance(value, self.__class__):
            return self.__class__(*(self.que + value.que))
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, self.__class__):
            self.que += value.que
            return self
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            if n < len(self.que):
                return self.__class__(*self.que[n:])
            return self.__class__("")
        return NotImplemented
