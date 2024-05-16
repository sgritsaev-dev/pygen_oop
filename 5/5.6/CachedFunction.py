class CachedFunction:
    def __init__(self, func) -> None:
        self.cache = {}
        self.func = func

    def __call__(self, *args):
        if tuple(args) in self.cache:
            return self.cache[tuple(args)]
        res = self.func(*args)
        self.cache[tuple(args)] = res
        return res
