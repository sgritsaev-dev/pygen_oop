class Dice:
    def __init__(self, sides) -> None:
        self.sides = sides

    def __call__(self):
        import random

        return random.choice(range(1, self.sides))
