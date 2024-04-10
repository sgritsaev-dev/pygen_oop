class House:
    def __init__(self, color, rooms) -> None:
        self.color = color
        self.rooms = rooms

    def paint(self, new_color):
        self.color = new_color

    def add_rooms(self, amount):
        self.rooms+=amount

house = House('white', 4)

print(house.color)
print(house.rooms)