from copy import deepcopy as dc


class HistoryDict:
    def __init__(self, data={}) -> None:
        self.data = dc(data)
        self.data_history: dict = {}
        for key, value in self.data.items():
            self.data_history.setdefault(key, [])
            self.data_history[key].append(value)

    def keys(self):
        yield from self.data.keys()

    def values(self):
        yield from self.data.values()

    def items(self):
        yield from self.data.items()

    def history(self, key):
        if key in self.data_history:
            return self.data_history[key]
        return []

    def all_history(self):
        return self.data_history

    def __iter__(self):
        yield from self.data.keys()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
        if key in self.data_history:
            self.data_history[key].append(value)
        else:
            self.data_history[key] = [value]

    def __delitem__(self, key):
        del self.data[key]
        del self.data_history[key]


# TEST_9:
d = dict.fromkeys(range(100), None)
attrdict = HistoryDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)
