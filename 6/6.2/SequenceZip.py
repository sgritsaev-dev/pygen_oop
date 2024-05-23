from copy import deepcopy as dc


class SequenceZip:
    def __init__(self, *args) -> None:
        self.zib = zip(*dc(args))

    def __iter__(self):
        yield from dc(self.zib)

    def __len__(self):
        count = 0
        for el in dc(self.zib):
            count += 1
        return count

    def __getitem__(self, key):
        index = -1
        for el in dc(self.zib):
            index += 1
            if index == key:
                return el


print(len(SequenceZip([1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 4], "data")))
