class Numbers:
    def __init__(self) -> None:
        self.odds=list()
        self.evens=list()
    def add_number(self, n):
        if n%2==1:
            self.odds.append(n)
        else:
            self.evens.append(n)
    def get_even(self):
        return self.evens[:]
    def get_odd(self):
        return self.odds[:]