class CountCalls:
    def __init__(self, func) -> None:
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)
