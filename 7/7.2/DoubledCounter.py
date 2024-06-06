class Counter:
    def __init__(self, start=0) -> None:
        self.start = start
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        if self.value <= n:
            self.value = 0
        else:
            self.value -= n


class DoubledCounter(Counter):
    def inc(self, n=1):
        super().inc(n)
        super().inc(n)

    def dec(self, n=1):
        super().dec(n)
        super().dec(n)
