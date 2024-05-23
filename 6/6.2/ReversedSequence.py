class ReversedSequence:
    def __init__(self, sequence) -> None:
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.__class__(self.sequence[~key])
        return self.sequence[~key]

    def __iter__(self):
        return reversed(self.sequence)
