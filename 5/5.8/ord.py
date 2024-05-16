class Ord:
    def __getattribute__(self, name):
        return ord(name)
