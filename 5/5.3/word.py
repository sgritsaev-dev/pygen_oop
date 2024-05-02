from functools import total_ordering

@total_ordering
class Word:
    def __init__(self, word) -> None:
        self.word = word
        
    def __str__(self) -> str:
        res = self.word.capitalize()
        return res
    
    def __repr__(self) -> str:
        return f'''Word('{self.word}')'''
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Word):
            return len(self.word)==len(value.word)
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word)<len(other.word)
        return NotImplemented 