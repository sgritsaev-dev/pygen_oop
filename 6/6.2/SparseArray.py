class SparseArray:
    def __init__(self, default) -> None:
        self.default = default
        self.dic = {}

    def __getitem__(self, key):
        return self.dic.setdefault(key, self.default)

    def __setitem__(self, key, value):
        self.dic[key] = value
