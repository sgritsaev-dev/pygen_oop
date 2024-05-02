from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, v_string) -> None:
        self.first = int(v_string.split('.')[0])
        if len(v_string.split('.'))>=2:
            self.second = int(v_string.split('.')[1])
        else:
            self.second = 0
            self.third = 0
        if len(v_string.split('.'))>=3:
            self.third = int(v_string.split('.')[2])
        else:
            self.third = 0
        
    def __repr__(self) -> str:
        return f'''Version('{self.first}.{self.second}.{self.third}')'''
    
    def __str__(self) -> str:
        return f'{self.first}.{self.second}.{self.third}'
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Version):
            return self.first==value.first and self.second==value.second and self.third==value.third
        return NotImplemented
    
    def __lt__(self, value):
        if isinstance(value, Version):
            if self.first!=value.first: 
                return self.first<value.first
            elif self.second!=value.second:
                return self.second<value.second
            else:
                return self.third<value.third      
        return NotImplemented