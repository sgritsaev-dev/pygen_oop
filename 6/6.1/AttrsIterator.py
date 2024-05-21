class AttrsIterator:
    def __init__(self, obj) -> None:
        self.obj = obj
        self.index = 0

    def __iter__(self):
        yield from self.obj.__dict__.items()

    def __next__(self):
        try:
            res = list(self.obj.__dict__.items())[self.index]
            self.index += 1
            return res
        except IndexError:
            raise StopIteration


class Kemal:
    def __init__(self):
        self.family = "cats"
        self.breed = "british"
        self.master = "Kemal"


kemal = Kemal()
attrs_iterator = AttrsIterator(kemal)

print(next(attrs_iterator))
print(next(attrs_iterator))
print(next(attrs_iterator))
