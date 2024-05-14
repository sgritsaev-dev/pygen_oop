import copy


class Matrix:
    def __init__(self, rows, cols, value=0) -> None:
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[value for _ in range(cols)] for _ in range(rows)]

    def __repr__(self) -> str:
        return f'Matrix({self.rows}, {self.cols})'

    def __str__(self) -> str:
        res = ''
        for row in self.matrix:
            res += (' '.join(list(map(str, row))))+'\n'
        return res.strip('\n')

    def __pos__(self):
        res = self.__class__(self.rows, self.cols, self.value)
        m_copy = copy.deepcopy(self.matrix)
        res.matrix = m_copy
        return res

    def __neg__(self):
        res = self.__class__(self.rows, self.cols, self.value)
        m_copy = copy.deepcopy(self.matrix)
        res.matrix = [[-el for el in row] for row in m_copy]
        return res

    def __invert__(self):
        res = self.__class__(self.cols, self.rows)
        m_copy = copy.deepcopy(self.matrix)
        for i in range(self.rows):
            for j in range(self.cols):
                res.set_value(j, i, m_copy[i][j])
        return res

    def __round__(self, number=None):
        res = self.__class__(self.rows, self.cols, self.value)
        m_copy = copy.deepcopy(self.matrix)
        res.matrix = m_copy
        for i in range(self.rows):
            for j in range(self.cols):
                res.set_value(i, j, round(m_copy[i][j], number))
        return res

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

matrix = Matrix(5, 10)

floats = [[7125.900408, 633.354471, -9237.8575119, 2865.3825158, 5509.2609336, 8712.260779, 8317.523947, 2512.4736075,
           -3087.5496014, 3861.68814],
          [-7852.451832, 376.465911, -8142.7867326, -6921.8371407, 3735.7516227, -3322.8019034, 7115.79968,
           -8949.9313078, -7032.4347679, -5217.8236385],
          [-7817.9657992, -4319.716346, -1038.6294521, -2959.8970273, -9263.5713405, 9358.607686, 1429.6576196,
           -9484.68116, 639.6343972, 3444.9938213],
          [-2844.2405153, -2078.2441427, 6812.1367017, 112.3910618, -1116.8662449, 5042.7026276, -5981.6930342,
           4370.9173164, -8851.7648474, 8990.6896422],
          [90.8102435, 5256.6137481, -9743.8477321, -131.5501688, -5920.5976176, 4963.8336619, -4907.3622526,
           8531.2015615, -244.3630074, 3421.8817151]]

for r in range(5):
    for c in range(10):
        matrix.set_value(r, c, floats[r][c])

print(matrix)
print()
print(~matrix)
print()
print(round(matrix, 2))
print()
print(-matrix)