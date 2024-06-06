class AdvancedList(list):
    def join(self, delimeter=' '):
        return delimeter.join(str(item) for item in self[:])

    def map(self, func):
        for i in range(len(self)):
            self[i] = func(self[i])

    def filter(self, func):
        for el in self[:]:
            if func(el) is False:
                self.remove(el)


advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.map(lambda x: -x)

print(advancedlist)
