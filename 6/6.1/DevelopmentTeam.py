class DevelopmentTeam:
    def __init__(self) -> None:
        self.juniors = []
        self.seniors = []

    def add_junior(self, *names):
        for name in names:
            self.juniors.append((name, "junior"))

    def add_senior(self, *names):
        for name in names:
            self.seniors.append((name, "senior"))

    def __iter__(self):
        yield from self.juniors + self.seniors


beegeek = DevelopmentTeam()

beegeek.add_junior("Timur")
beegeek.add_junior("Arthur", "Valery")
beegeek.add_senior("Gvido")
print(*beegeek, sep="\n")
