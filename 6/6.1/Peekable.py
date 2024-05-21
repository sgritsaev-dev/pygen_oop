class Peekable:
    def __init__(self, iterable) -> None:
        self.iterable = list(el for el in iterable)
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            res = next(self.iterator)
            self.iterable.remove(res)
            return res
        except IndexError:
            raise StopIteration

    def peek(self, default='something'):
        try:
            return self.iterable[0]
        except IndexError:
            if default!='something':
                return default
            raise StopIteration


iterator = Peekable("beegeek")

print(next(iterator))
print(next(iterator))
print(*iterator)

iterator = Peekable("Python")

print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print(next(iterator))
print(iterator.peek())
print(iterator.peek())
