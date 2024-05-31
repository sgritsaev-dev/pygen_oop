class PermaDict:
    def __init__(self, data={}) -> None:
        for key, value in data.items():
            object.__setattr__(self, str(key), value)

    def keys(self):
        yield from self.__dict__.keys()

    def values(self):
        yield from self.__dict__.values()

    def items(self):
        yield from self.__dict__.items()

    def __iter__(self):
        yield from self.__dict__.keys()

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, key):
        return self.__dict__[str(key)]

    def __setitem__(self, key, value):
        if str(key) not in self.__dict__:
            object.__setattr__(self, str(key), value)
        else:
            raise KeyError('Изменение значения по ключу невозможно')

    def __delitem__(self, key):
        object.__delattr__(self, str(key))


d = dict.fromkeys(range(100), None)
attrdict = PermaDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)
