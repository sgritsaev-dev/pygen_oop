from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args) -> None:
        self.sequence = []
        for el in args:
            if isinstance(el, int):
                self.sequence.append(el)
            else:
                self.sequence.extend(
                    range(int(el.split("-")[0]), int(el.split("-")[1]) + 1)
                )
        # super().__init__()

    def __getitem__(self, index):
        return self.sequence[index]

    def __len__(self):
        return len(self.sequence)


customrange = CustomRange("0-1000")

print(len(customrange))
print(*customrange)
