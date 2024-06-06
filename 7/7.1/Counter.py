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


class NonDecCounter(Counter):
    def dec(self, n=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10) -> None:
        super().__init__(start)
        self.limit = limit

    def inc(self, n=1):
        if (self.value + n) >= self.limit:
            self.value = self.limit
        else:
            self.value += n
