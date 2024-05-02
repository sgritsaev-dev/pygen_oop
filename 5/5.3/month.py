from functools import total_ordering

@total_ordering
class Month:
    def __init__(self, year, month) -> None:
        self.year = year
        self.month = month
        
    def __repr__(self) -> str:
        return f'''Month({self.year}, {self.month})'''
    
    def __str__(self) -> str:
        return f'{self.year}-{self.month}'
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Month):
            return self.year==value.year and self.month==value.month
        elif isinstance(value, tuple) and len(value)==2:
            return self.year==value[0] and self.month==value[1]
        return NotImplemented
    
    def __lt__(self, value):
        if isinstance(value, Month):
            if not self.year==value.year: 
                return self.year<value.year
            else:
                return self.month<value.month
        elif isinstance(value, tuple):
            if not self.year==value[0]: 
                return self.year<value[0]
            else:
                return self.month<value[1]
        return NotImplemented
