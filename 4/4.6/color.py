class Color:
    def __init__(self, hexcode) -> None:
        self.r=int(hexcode[:2], base=16)
        self.g=int(hexcode[2:4], base=16)
        self.b=int(hexcode[4:], base=16)
    
    @property
    def hexcode(self):
        res=''
        for el in [self.r, self.g, self.b]:
            res+=('%X' % el if el!=0 else ('%X' % el)*2)
        return res
    @hexcode.setter
    def hexcode(self, new_code):
        self.r=int(new_code[:2], base=16)
        self.g=int(new_code[2:4], base=16)
        self.b=int(new_code[4:], base=16)

color = Color('0000FF')

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)