class ColoredPoint:
    def __init__(self, x, y, color) -> None:
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    def __repr__(self) -> str:
        return f'''ColoredPoint({self.x}, {self.y}, '{self.color}')'''

    def __eq__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return all((self.x == value.x, self.y == value.y,
                        self.color == value.color))
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.color))


point = ColoredPoint(71, 42, 'Indigo')

not_supported = [6952, 208621309.925047,
                 'Крестик на моей груди, на него ты погляди', False,
                 {'whom': True, 'administration': 1862,
                     'collection': 56102.956722026},
                 (-326.5668977995, True,
                  'Темный, мрачный коридор, Я на цыпочках, как вор',
                  975006604.874278),
                 [3599, 26637.9272286489, 'JeGfEEwKXxCoxlTBTYnL',
                  -25690105773711.2],
                 {'izPmPJcBqaYBUfrSHpin', -850300479586.218, 22.2224616976328}]

for item in not_supported:
    print(item == point)

# TEST_7:
coloredpoint = ColoredPoint(85, 100, 'PeachPuff')
print(coloredpoint.__eq__(1))
print(coloredpoint.__ne__(1.1))
