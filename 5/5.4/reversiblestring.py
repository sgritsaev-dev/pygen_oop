class ReversibleString:
    def __init__(self, string) -> None:
        self.string=string
        
    def __repr__(self) -> str:
        return f'{self.string}'
    
    def __neg__(self):
        return ReversibleString(self.string[::-1])









string = ReversibleString('python')

print(string)
print(-string)