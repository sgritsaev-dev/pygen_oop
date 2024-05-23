from copy import deepcopy as dc


class AttrDict:
    def __init__(self, data=None) -> None:
        if data:
            self.dig = dc(data)
            for key, value in dc(data).items():
                object.__setattr__(self, str(key), value)
        else:
            self.dig = {}

    def __len__(self):
        return len(self.dig)

    def __iter__(self):
        yield from self.dig.keys()

    def __getitem__(self, key):
        return self.dig[key]

    def __setitem__(self, key, value):
        self.dig[key] = value
        object.__setattr__(self, key, value)


d = dict.fromkeys(range(100), None)
print(d)
attrdict = AttrDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)
