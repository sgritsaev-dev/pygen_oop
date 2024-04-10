class Scales:
    def __init__(self) -> None:
        self.left = 0
        self.right = 0
    
    def add_right(self, n):
        self.right+=n
    def add_left(self, n):
        self.left+=n
    def get_result(self):
        if self.left==self.right:
            return 'Весы в равновесии'
        elif self.left>self.right:
            return 'Левая чаша тяжелее'
        else:
            return 'Правая чаша тяжелее'