class AnyClass:
    str_of_kwargs = ''
    def __init__(self, **kwargs) -> None:
        for key,value in kwargs.items():
            if isinstance(value, str):
                self.str_of_kwargs+= f"{key}='{value}', "
            else:
                self.str_of_kwargs+= f"{key}={value}, "
                
    def __repr__(self) -> str:
        return f"AnyClass({self.str_of_kwargs.rstrip(', ')})"
    
    def __str__(self) -> str:
        return f"AnyClass: {self.str_of_kwargs.rstrip(', ')}"
     
obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))