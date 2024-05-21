class RandomLooper:
    def __init__(self, *iterables) -> None:
        self.iterable = []
        for el in iterables:
            self.iterable.extend(el)
        self.iterator = iter(self.iterable)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except IndexError:
            raise StopIteration


randomlooper = RandomLooper(["red", "blue", "green", "purple"])

print(list(randomlooper))
print(list(randomlooper))
