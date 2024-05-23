class CyclicList:
    def __init__(self, iterable=list()) -> None:
        self.cyclist = iterable[:]
        self.index = -1

    def append(self, value):
        self.cyclist.append(value)

    def pop(self, index=-1):
        return self.cyclist.pop(index)

    def __len__(self):
        return len(self.cyclist)

    def __next__(self):
        self.index += 1
        try:
            return self.cyclist[self.index]
        except IndexError:
            self.index = 0
            return self.cyclist[self.index]

    def __getitem__(self, key):
        return self.cyclist[key % len(self.cyclist)]
