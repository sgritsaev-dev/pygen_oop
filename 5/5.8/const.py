class Const:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
    
    def __setattr__(self, name: str, value):
        if name in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        object.__setattr__(self, name, value)
    
    def __delattr__(self, name: str) -> None:
        raise AttributeError('Удаление атрибута невозможно')