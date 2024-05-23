from copy import deepcopy as dc


class OrderedSet:
    def __init__(self, iterable=None) -> None:
        if iterable:
            self.dig = dict.fromkeys(dc(iterable), None)
        else:
            self.dig = {}

    def add(self, value):
        if value not in self.dig.keys():
            self.dig[value] = None

    def discard(self, value):
        if value in self.dig.keys():
            del self.dig[value]

    def __len__(self):
        return len(self.dig.keys())

    def __iter__(self):
        yield from self.dig.keys()

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return list(self.dig.keys()) == list(value.dig.keys())
        elif isinstance(value, set):
            return set(self.dig.keys()) == value
        return NotImplemented
