class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)
