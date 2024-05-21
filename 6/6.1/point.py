class Point:
    def __init__(self, x, y, z) -> None:
        self.coordinates = (x, y, z)
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"""Point({self.x}, {self.y}, {self.z})"""

    def __iter__(self):
        yield from self.coordinates
