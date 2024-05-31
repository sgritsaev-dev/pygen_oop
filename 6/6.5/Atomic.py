from copy import deepcopy as dc, copy as c


class Atomic:
    def __init__(self, data, deep=False) -> None:
        self.data = data
        self.deep = deep
        if self.deep:
            self.cp = dc(self.data)
        else:
            self.cp = c(self.data)

    def __enter__(self):
        return self.cp

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type:
            return True
        if isinstance(self.data, list):
            self.data[:] = self.cp
        if isinstance(self.data, set):
            self.data.clear()
            for el in self.cp:
                self.data.add(el)
        if isinstance(self.data, dict):
            self.data.clear()
            for key, value in self.cp.items():
                self.data[key] = value
        return False
