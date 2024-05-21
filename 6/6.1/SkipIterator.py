class SkipIterator:
    def __init__(self, iterable, n) -> None:
        self.iterable = [el for el in iterable]
        self.res = []
        self.n = n + 1
        for i in range(len(self.iterable)):
            if i % self.n == 0:
                self.res.append(self.iterable[i])
        self.index = -1

    def __iter__(self):
        yield from self.res

    def __next__(self):
        try:
            self.index += 1
            res = self.res[self.index]
            return res
        except IndexError:
            raise StopIteration


skipiterator = SkipIterator(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2
)  # пропускаем по два элемента

print(*skipiterator)

skipiterator = SkipIterator(iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)

print(*skipiterator)
