class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def get_perimeter(self):
        return (self.length+self.width)*2
    def get_area(self):
        return self.length*self.width
    perimeter = property(get_perimeter)
    area = property(get_area)