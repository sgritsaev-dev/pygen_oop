from collections import UserString


class MutableString(UserString):
    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=None, reverse=False):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse))

    def __setitem__(self, index, item):
        res = list(self.data)
        res[index] = item
        self.data = ''.join(res)

    def __delitem__(self, index):
        res = list(self.data)
        del res[index]
        self.data = ''.join(res)
