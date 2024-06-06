class ValueDict(dict):
    def key_of(self, val):
        for key, value in self.items():
            if value == val:
                return key

    def keys_of(self, val):
        for key, value in self.items():
            if value == val:
                yield key
