class Knight:
    def __init__(self, vertical, horizontal, color) -> None:
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.verdic = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'h': 5,
            'g': 6,
            'h': 7}
        self.hordic = {
            '1': 7,
            '2': 6,
            '3': 5,
            '4': 4,
            '5': 3,
            '6': 2,
            '7': 1,
            '8': 0}

    def get_char(self):
        char = 'N'
        return char

    def can_move(self):
        pass

    def move_to(self):
        pass

    def draw_board(self):
        board = [['.' for el in self.hordic] for el in self.verdic]
        for i in range(8):
            for j in range(8):
                if i == self.hordic[str(self.horizontal)
                                    ] and j == self.verdic[self.vertical]:
                    board[i][j] = self.get_char()
                elif (i == (self.hordic[str(self.horizontal)] + 2) or i == (self.hordic[str(self.horizontal)] - 2)) and (j == (self.verdic[self.vertical] + 1) or j == (self.verdic[self.vertical] - 1)):
                    board[i][j] = '*'
                elif (i == (self.hordic[str(self.horizontal)] + 1) or i == (self.hordic[str(self.horizontal)] - 1)) and (j == (self.verdic[self.vertical] + 2) or j == (self.verdic[self.vertical] - 2)):
                    board[i][j] = '*'
        for el in board:
            print(*el)


knight = Knight('e', 5, 'white')

knight.draw_board()
