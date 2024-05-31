from time import perf_counter


class AdvancedTimer:
    def __init__(self) -> None:
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = perf_counter() - self.start
        if self.last_run is None:
            self.min = self.elapsed
            self.max = self.elapsed
        self.last_run = self.elapsed
        self.runs.append(self.elapsed)
        if self.elapsed > self.max:
            self.max = self.elapsed
        if self.elapsed < self.min:
            self.min = self.elapsed
